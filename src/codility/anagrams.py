"""
This module is created for testing two functions those separate anagrams from a list of words.
Anagrams are words with same characters but in different orders.
First function (written by ChatGPT) uses sorting technique and has the time complexity of O(n.mlog m)
Second function (My Idea) uses arrays and tuples as a key for the anagrams dictionary with the time complexity of O(n.m)

However, It does not mean that my code is faster.
For the cases with long words my approach operates more efficient but for the short words the other solution is faster.
"""

import time
from collections import defaultdict
from typing import Any


def separate_anagrams(words: list[str]) -> list[list]:
    groups: defaultdict[Any, list] = defaultdict(list)
    for item in words:
        # Create a sorted word from item
        item_chars = ''.join(sorted(item))
        groups[item_chars].append(item)

    return [anagram for anagram in groups.values()]


def separate_anagrams_2(words: list[str]) -> list[list]:
    groups: defaultdict[Any, list] = defaultdict(list)

    for word in words:
        # Create a frequency count tuple for the word
        count = [0] * 26  # Assuming the input words contain only lowercase a-z
        for char in word:
            count[ord(char) - ord('a')] += 1
        # Convert count to a tuple to use as a dictionary key
        key: tuple[int, ...] = tuple(count)
        groups[key].append(word)

    # Extract grouped anagrams as a list of lists
    return list(groups.values())


if __name__ == '__main__':

    import random
    import string


    def generate_base_words(num_words, min_length=300, max_length=400):
        """Generate a list of random base words."""
        words = []
        for _ in range(num_words):
            length = random.randint(min_length, max_length)
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            words.append(word)
        return words


    def create_anagrams(list_of_base_words, number_of_anagrams_per_word=3):
        """Create anagrams for each base word.
        """
        anagram_words = []
        for word in list_of_base_words:
            for _ in range(number_of_anagrams_per_word):
                anagram = ''.join(random.sample(word, len(word)))
                anagram_words.append(anagram)
        return anagram_words


    def generate_random_words(num_words, min_length=300, max_length=400):
        """Generate a list of random words."""
        words = []
        for _ in range(num_words):
            length = random.randint(min_length, max_length)
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            words.append(word)
        return words


    # Parameters
    num_base_words = 1000  # Number of base words to generate
    anagrams_per_word = 20  # Number of anagrams per base word
    num_random_words = 5000  # Number of additional random words

    # Generate base words
    base_words = generate_base_words(num_base_words)

    # Create anagrams
    anagrams = create_anagrams(base_words, anagrams_per_word)

    # Generate additional random words
    random_words = generate_random_words(num_random_words)

    # Combine all words into a single list
    all_words = base_words + anagrams + random_words

    # Shuffle the list to mix base words, anagrams, and random words
    random.shuffle(all_words)

    start = time.time()
    separate_anagrams(all_words)
    print(time.time() - start)

    start_2 = time.time()
    separate_anagrams_2(all_words)
    print(time.time() - start_2)
