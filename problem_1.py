
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
    no_of_tosses = int((np.log10(p))/(np.log10(0.5)))


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



if __name__ == "__main__":
    movies = 0 #Outcomes favourable to choosing movies
    games = 0  #Outcomes favourable to choosing video games

    #Conduct the experiment to take biased decision 10000 times and test for the movies probability to 
    # be 1/8 thereby ensuring the correctness of the code if we want our probability of choosing
    # movies to be 0.125

    #To improve the accuracy of probability result to be close to 0.125 , we perform this entire 
    #experiment 10 times and take the mean of all 10 probabilities.
    probabilities = []

    for repeat_exp in range(10):
        for no_of_experiments in range(10000):
            decision = biased_decision_with_fair_coin(flip_coin , 0.125)
            if decision == False :
                movies += 1
            else :
                games += 1
        probabilities.append(movies/10000)
        movies = 0 # Reset the count of movies and video games outcomes for repeating experiment.
        games = 0
    # Make a numpy array out of the probabilities list and calculate mean
    prob_array = np.array(probabilities)
    mean_probability = np.mean(prob_array)

    print(mean_probability)
        



# We retain this experiment of taking biased decision 10000 times for plotting the probability mass
#  function. Now we have to do another experiment of tossing a fair coin 10000 times to plot its
# probability measure using matplotlib. Then we have to plot the Probability Mass Function (PMF) of 
# a) Outcomes of flip_coin() function (plot should show that fair coin produces almost equal 
# probabilities). b) Outcomes of the biased_decision_with_fair_coin() function (unequal probabilities)



