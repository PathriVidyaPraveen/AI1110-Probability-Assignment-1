
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Simulate the tossing of a fair coin using flip_coin() function and return true for heads 
# and false for tails

def flip_coin():
    sample_space = [True,False]
    outcome_of_toss = np.random.choice(sample_space)
    return outcome_of_toss


# Write a function biased_decision_with_fair_coin(flip_coin, p) that flip_coin function and returns a
# biased decision with head probability being p.

def biased_decision_with_fair_coin(flip_coin , p):
    no_of_tosses = (np.log10(p))//(np.log10(0.5))


    # Here we make this assumption that the given argument p must be of the form (0.5)^x where x is
    # a natural number so that we can choose the movie if all the x tosses fall heads which will be of 
    # probability p as stated in the question . If it it not of this form , then any natural number of tosses
    # won't work .

    outcomes = []
    #Toss the coin x number of times and store all of the outcomes in a list called outcomes
    for i in range(no_of_tosses):
        result = flip_coin()
        outcomes.append(result)
    # Even if one tail(False) is present in the outcomes list , make the decision value to True as we select 
    # video games. If all outcomes are heads , then we choose movies and make the decision value to False

    decision = False
    
    for outcome in outcomes :
        if outcome == False :
            decision = True
            break
        else :
            continue
    

    return decision


