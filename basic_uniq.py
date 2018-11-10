#! /usr/bin/python3


import sys
import re
from collections import Counter

def analyse():
	text_input = sys.stdin.read()
	words = re.split('\s+', text_input)
	word_freq = Counter(words)
	for word in sorted(word_freq, key=lambda _: word_freq[_], reverse=True):
		print("{:20} {}".format(word, word_freq[word]))
	print("Unique: {}\nActual: {}".format(len(list(word_freq)), sum(word_freq.values())))


if __name__ == '__main__':
	analyse()
