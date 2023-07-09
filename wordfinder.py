"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, file_path):
        self.words = []
        self.read_file(file_path) #use the function to open the file
        print(f"{len(self.words)} words read")

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            self.words = file.read().splitlines()

    def random(self):
        return random.choice(self.words)
#____________________________________________________________
    # def __init__(self, path): #single parameter
    #     """Read dictionary and reports # items read."""
    #     dict_file = open(path) #built in open function used to open the path. returns file object assigned to this variable
    #     self.words = self.parse(dict_file) #how to create an attribute to store list of words for later use
    #     print(f"{len(self.words)} words read") #same

    # def parse(self, dict_file):
    #     """Parse dict_file -> list of words."""
    #     return [w.strip() for w in dict_file]

    # def random(self):
    #     """Return random word."""
    #     return random.choice(self.words)
    

    # In both cases, color and words are used to capture specific information associated with the instances of their respective classes. However, the purpose and context of their usage differ. color is used to define a characteristic of a triangle object, while words is used to store a list of words read from a file in the context of word finding operations.

class SpecialWordFinder(WordFinder):
    def parse(self, file_path):
        """Parse file -> list of words (excluding blank lines and comments)."""
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]