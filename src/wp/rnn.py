
"""
Recurrent neural network (RNN) model
"""

from __future__ import print_function, division

import nltk
from nltk import tokenize

import cPickle as pickle # faster version of pickle
from pprint import pprint, pformat


class RnnModel(object):
    """
    Recurrent neural network (RNN) model
    """

    def __init__(self):
        """
        Create an rnn model
        """
        self.name = 'rnn'

    def train(self, tokens):
        """
        Train the rnn model with the given tokens.
        """
        pass

    def predict(self, tokens):
        """
        Get the most likely next k tokens following the given sequence.
        """
        pass

    def save(self, filename=None):
        """
        Save the model to the default or given filename.
        """
        if not filename:
            filename = self.filename
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        """
        Load a model from the given filename.
        """
        with open(filename, 'rb') as f:
            model = pickle.load(f)
            return model




