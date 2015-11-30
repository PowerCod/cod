#! /usr/bin/env python
#coding=utf-8


def rstr(str):
    return str[::-1]

def is_vowel(s):
    if s.isalpha() and s in 'aeiouAEIOU':
        return True

def ay(str):
    for i in str:
        if not is_vowel(i):
            return ''.join([str,'-',i,'ay'])
    
def cal_vowel(str):
    d = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in str:
        if is_vowel(i):
            d[i] = d[i]+1
    return d

def palindrome(str):
    return str == rstr(str)
       
    
if __name__ == '__main__':
    s='banana'
    print palindrome(s)
    