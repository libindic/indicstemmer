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

import os


class Malayalam:
    """
    Instantiate class to get the methods
    """

    def __init__(self):
        self.rules_file = os.path.join(
            os.path.dirname(__file__), 'data/ml.rules')
        self.rulesDict = None
        self.dictionary_file = open(os.path.join(
            os.path.dirname(__file__), 'data/rootwords.txt'))
        self.dictionary = self.dictionary_file.readlines()
        self.dictionary_file.close()
        try:
            self.dictionary = [x.strip().decode('utf-8')
                               for x in self.dictionary]
        except:
            self.dictionary = [x.strip() for x in self.dictionary]

    def singleencode(self, word):
        '''
        Normalize word to single encoding.
        '''
        replace = {'\\u0d15\\u0d4d\\u200d': '\\u0d7f',
                   '\\u0d23\\u0d4d\\u200d': '\\u0d7a',
                   '\\u0d28\\u0d4d\\u200d': '\\u0d7b',
                   '\\u0d30\\u0d4d\\u200d': '\\u0d7c',
                   '\\u0d32\\u0d4d\\u200d': '\\u0d7d',
                   '\\u0d33\\u0d4d\\u200d': '\\u0d7e'}
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
            original_word = words[word_iter]
            word = self.trim(word)
            word = word.strip('!,.?:')
            try:
                result = self.trim(word).decode('utf-8')
            except:
                result = word
            result = self.singleencode(result)
            word = result
            if result in self.dictionary:
                result_dict[original_word] = result
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
                if result in self.dictionary:
                    result_dict[original_word] = result
                    break
                while counter < len(result):
                    suffix = result[counter:]  # Right to left suffix stripping
                    if suffix in self.rulesDict:
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
            result_dict[original_word] = result
        return result_dict

    def LoadRules(self):
        rules_dict = dict()
        rules_file_object = open(self.rules_file)
        rules_text = rules_file_object.readlines()
        rules_file_object.close()
        rules_dict = {}
        for line in rules_text:
            if line == '' or line[0] == '#':
                continue
            items = line.strip().split('=')
            try:
                try:
                    lhs = items[0].strip().strip(
                        '"').strip("'").decode('utf-8')
                    rhs = items[1].strip().strip(
                        '"').strip("'").decode('utf-8')
                except:
                    lhs = items[0].strip().strip('"').strip("'")
                    rhs = items[1].strip().strip('"').strip("'")
                lhs = self.singleencode(lhs)
                rhs = self.singleencode(rhs)
                rules_dict[lhs] = rhs
            except:
                continue
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
