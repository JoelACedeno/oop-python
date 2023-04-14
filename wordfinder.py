"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds random words from a given dictionary
    >>> wd = WordFinder("simple.txt")
    3 words read
    >>> wd.random() in ["cat", "dog", "porcupine"]
    True
    >>> wd.random() in ["cat", "dog", "porcupine"]
    True
    >>> wd.random() in ["cat", "dog", "porcupine"]
    True
"""
    
    def __init__(self, path):
        """Read the sourced dictionary and report the amount of words read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def __repr__(self):
        """Show representation"""
        return f"Word Finder with {len(self.words)} words in the dictionary"

    def parse(self, dict_file):
        """Parse dict_file to words list"""
        return [word.strip() for word in dict_file]
    
    def random(self):
        """Return a random word from the words list"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Parse dict_file into a list of words, skipping blanks and comments
    >>> sf = SpecialWordFinder(complex.txt)
        4 words read
    >>> sf.random() in ["kale", "parsnips", "apple", "mango"]
        True
    >>> sf.random() in ["kale", "parsnips", "apple", "mango"]
        True
    >>> sf.random() in ["kale", "parsnips", "apple", "mango"]
        True"""
    
    def parse(self, dict_file):
        return [word.strip() for word in dict_file
                    if word.strip() and not word.startswith("#")]
