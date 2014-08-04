#!/usr/bin/env/python
# This is a typing test application created in python
# Created by Raymond Ho on Aug 4, 2014

import time
import sys

# Open file, and store each line into list.
List = []
total_words = 0
with open(sys.argv[1], 'r') as f:
    List = f.read().splitlines()

# Count the words in the list.
for line in List:
    total_words += len(line.split())

# Prompt user to begin typing, and start timer.
raw_input("Press enter to begin test.\n>> ")
start_time = time.time()
mistakes = {}

for line in List:
    print line
    response = raw_input(">> ")

    # Split lines into words, and count the mistakes.
    word_response = response.split()
    word_line = line.split()
    for i in range(0, len(line.split())):
        if word_response[i] != word_line[i]:
            mistakes[word_response[i]] = word_line[i]

# Calculate time elapsed and convert into minutes.
elapsed_time = time.time() - start_time
wpm = (total_words / elapsed_time) * 60
accuracy = (total_words - len(mistakes)) / float(total_words) * 100

print
print("Your words per minute is: %i." % wpm)
print("Your accuracy: %i%%" % accuracy)
print ("Total words: %s." % total_words)
print("Total errors: %i." % len(mistakes))
for key, val in mistakes.items():
    print "You entered: '%s' : Should be: '%s'" % (key, val)


