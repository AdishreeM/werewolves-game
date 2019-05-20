from . import config
from random import randint

def generate():

    adj_file = open(config.ADJECTIVES, 'r')
    noun_file = open(config.NOUNS, 'r')

    adjectives = adj_file.read().splitlines()
    nouns = noun_file.read().splitlines()

    adj_file.close()
    noun_file.close()

    return adjectives[randint(0, len(adjectives))] + '-' + nouns[randint(0, len(nouns))]