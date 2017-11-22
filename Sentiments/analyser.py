```
import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # set the class objects to empty sets
        self.P = set()
        self.N = set()
        
        # iterate through the words in positive words collection and store in the P object
        file = open(positives, "r")
        for line in file:
            if line[0] == ";":
                continue
            self.P.add(line.rstrip("\n"))
        file.close()
        
        # iterate through the words in negative words collection and store in the N object
        file = open(negatives, "r")
        for line in file:
            if line[0] == ";":
                continue
            self.N.add(line.rstrip("\n"))
        file.close()



    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        score = 0
        words = text.split(" ") # split the text into a list of words
        
        # iterate through the word in the list of words
        # increment or decrement the score if the word matches a word in P or N object
        for word in words:
            for p_word in self.P:
                if word == p_word:
                    score += 1
                    break
            for n_word in self.N:
                if word == n_word:
                    score -= 1
                    break
        return score
```
