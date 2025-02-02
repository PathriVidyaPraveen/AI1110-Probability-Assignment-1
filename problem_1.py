
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
