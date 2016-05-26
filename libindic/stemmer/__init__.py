#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email:
# santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in

import codecs
import os
import normalizer


class Malayalam:
    """
    Instantiate class to get the methods
    """

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.rules_file = os.path.join(os.path.dirname(__file__), 'data/ml.rules')
        self.rulesDict = None
        self.normalizer = normalizer.getInstance()
        self.dictionary_file = open(os.path.join(
            os.path.dirname(__file__), 'data/rootwords.txt'))
        self.dictionary = self.dictionary_file.readlines()
        self.dictionary_file.close()
        self.dictionary = [x.strip().decode('utf-8')
                           for x in self.dictionary]

    def singleencode(self, word):
        '''
        Normalize word to single encoding.
        '''
        replace = {u'\u0d15\u0d4d\u200d': u'\u0d7f',
                   u'\u0d23\u0d4d\u200d': u'\u0d7a',
                   u'\u0d28\u0d4d\u200d': u'\u0d7b',
                   u'\u0d30\u0d4d\u200d': u'\u0d7c',
                   u'\u0d32\u0d4d\u200d': u'\u0d7d',
                   u'\u0d33\u0d4d\u200d': u'\u0d7e'}
        for character in replace:
            word = word.replace(character, replace[character])
        return word

    def stem(self, text):
        """
        :param text: unicode encoded malayalam string
        :returns: dictionary with words as the key and the stemmer result
        as the values. stems all the words in the given text and
        returns a dictionary
        """
        if self.rulesDict is None:
            self.rulesDict = self.LoadRules()
        words = text.split(" ")
        word_count = len(words)
        result_dict = dict()
        word_iter = 0
        word = ""
        while word_iter < word_count:
            word = words[word_iter]
            word = self.trim(word)
            word = word.strip('!,.?:')
            word_length = len(word)
            suffix_pos_itr = 2
            try:
                result = self.trim(word).decode('utf-8')
            except:
                result = word
            result = self.singleencode(result)
            word = result
            if result in self.dictionary:
                result_dict[word] = result
                word_iter += 1
                continue
            completed = False
            while not completed:
                # For multilevel inflection handling.
                # Repeats stemming until
                # (i) a mis-hit in rules or
                # (ii) a rootword is found
                # 'found' variable is used to detect mis-hit, for
                # each intermediate form of word
                found = False
                counter = 1
                if self.verbose:
                    print(result)
                if result in self.dictionary:
                    result_dict[word] = result
                    break
                while counter < len(result):
                    suffix = result[counter:]  # Right to left suffix stripping
                    if suffix in self.rulesDict:
                        if self.verbose:
                            print("\t Satisfying rule found : ", suffix, " = ", self.rulesDict[suffix])
                        result = result[:counter] + self.rulesDict[suffix]
                        # A satisfying rule found, continue stemming.
                        found = True
                        break
                    counter = counter + 1
                # Stop stemming, no matching rules found - probably a root
                # word.
                if not found:
                    completed = True
            word_iter += 1
            result_dict[word] = result
        return result_dict

    def LoadRules(self):
        rules_dict = dict()
        line = []
        line_number = 0
        rule_number = 0
        rules_file = codecs.open(self.rules_file, encoding='utf-8',
                                 errors='ignore')
        while 1:
            line_number = line_number + 1
            try:
                text = unicode(rules_file.readline())
            except:
                text = rules_file.readline()
            if text == "":
                break
            if text[0] == '#':
                continue  # this is a comment - ignore
            text = text.split("#")[0]  # remove the comment part of the line
            line_number = line_number + 1
            line = text.strip()  # remove unwanted space
            if(line == ""):
                continue
            if(len(line.split("=")) != 2):
                print("[Error] Syntax Error in the Rules. Line number: ", line_number)
                print("Line: " + text)
                continue
            lhs = line.split("=")[0].strip()
            rhs = line.split("=")[1].strip()
            if(len(rhs) > 0):
                if(lhs[0] == '"'):
                    lhs = lhs[1:len(lhs)]  # if the string is "quoted"
                if(lhs[len(lhs) - 1] == '"'):
                    lhs = lhs[0:len(lhs) - 1]  # if the string is "quoted"
            if(len(rhs) > 0):
                if(rhs[0] == '"'):
                    rhs = rhs[1:len(rhs)]  # if the string is "quoted"
                if(rhs[len(rhs) - 1] == '"'):
                    rhs = rhs[0:len(rhs) - 1]     # if the string is "quoted"
            rule_number = rule_number + 1
            rules_dict[lhs] = rhs
        return rules_dict

    def trim(self, word):
        punctuations = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                        '-', '+', '_', '=', '{', '}', '|', ':', ';', '<', '>',
                        '\,', '.', '?']
        word = word.strip()
        index = len(word) - 1
        while index > 0:
            if word[index] in punctuations:
                word = word[0:index]
            else:
                break
            index = index - 1
        return word

    def get_module_name(self):
        """
        returns the module name.
        """
        return "Stemmer"

    def get_info(self):
        """
        returns info on the module
        """
        return "Malayalam Stemmer(Experimental)"


def getInstance():
    return Malayalam()
