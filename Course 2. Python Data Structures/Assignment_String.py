#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 11:17:50 2017

@author: jiexue
"""

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
text_temp=text[pos+1:len(text)].strip()
print text_temp