#!/usr/bin/env python3
''' retrieve words from a url

Args:
    url you want to retrieve from
'''
import sys
from urllib.request import urlopen

def fetch_words(url):
    ''' this is an example of a docstring for google style guide

    Args:
        url: the URL of a UTF-8 txt document

    Returns:
        A list of strings containing the word from
        the document.
    '''
    with urlopen (url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

def main(url):
    words = fetch_words(url)
    print_words(words)

if __name__ == '__main__':
    main(sys.argv[1])