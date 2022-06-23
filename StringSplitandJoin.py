#!/usr/bin/env python3.7

#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

#Complete the split_and_join function in the editor below.

def split_and_join(line):

#Here is the solution.

    var = line
    split_var = var.split(" ")
    joined_var = '-'.join(split_var)
    return joined_var
