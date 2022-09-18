from sentences import get_determiner, get_noun, get_prepositional_phrase, get_verb, get_preposition
import random
import pytest


def test_get_determiner():
    
    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        word = get_determiner(1)

        assert word in single_determiners

   
    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):

        word = get_determiner(2)

        assert word in plural_determiners

def test_get_noun():
    
    single_nouns = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):

        word = get_noun(1)

        assert word in single_nouns

   
    plural_nouns = ["birds", "boys", "cars", "cats", "children", 
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):

        word = get_noun(2)

        assert word in plural_nouns        

def test_get_verb():
    
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):

        word = get_verb(1,"past")

        assert word in past_verbs

   
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):

        word = get_verb(1,"present")

        assert word in present_single_verbs        

    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        word = get_verb(2,"present")             
        assert word in present_plural_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        word = get_verb(1,"future")
        assert word in future_verbs

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():
    single_phrase = [f'{get_preposition()}{get_determiner(1)} {get_noun(1)}']

    for _ in range(4):
        phrase = get_prepositional_phrase()
        assert phrase in single_phrase

    plural_phrase = [f'{get_preposition()} {get_determiner(2)} {get_noun(2)}']

    for _ in range(4):
        phrase= get_prepositional_phrase()
        assert phrase in plural_phrase    
        
        
pytest.main(["-v", "--tb=line", "-rN", "-s", __file__])      




















