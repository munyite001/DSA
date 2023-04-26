#!/usr/bin/python3

from tests import tests
from jovian.pythondsa import evaluate_test_cases

"""
QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, 
and lays them out face down in a sequence on a table. 
She challenges Bob to pick out the card containing a given number 
by turning over as few cards as possible. 
Write a function to help Bob locate the card.
"""

def locate_card_linear(cards, query):
    """
    cards: the cards array sorted in descending order
    query: the card to find
    Returns: the index position of query if any, else -1
    """

    #   Iterate over the cards array
    for position in range(len(cards)):
        #   If card at that position is the query return it's position
        if cards[position] == query:
            return position
        #   If we didn't find the card, or incase of any other error return -1
    return -1

evaluate_test_cases(locate_card_linear, tests)