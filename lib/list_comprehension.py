#!/usr/bin/env python3

def return_evens(num_list):
    even_elm = [num for num in num_list if num % 2 == 0] 
    return even_elm


def make_exclamation(sentence_list):
    new_list = [sentence + "!" for sentence in sentence_list]
    return new_list
