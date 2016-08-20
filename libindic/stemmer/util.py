#! /use/bin/env python


def rreplace(string, old, new, count=None):
    string_reverse = string[::-1]
    old_reverse = old[::-1]
    new_reverse = new[::-1]
    if count:
        final_reverse = string_reverse.replace(old_reverse, new_reverse, count)
    else:
        final_reverse = string_reverse.replace(old_reverse, new_reverse)
    result = final_reverse[::-1]
    return result
