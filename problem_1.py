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

    print("The probability of taking a biased decision to choose movies is {}".format(mean_probability))
        



# We do the same above experiment again in order to plot its PMF. Now we have to do another experiment of tossing a fair coin 10000 times to plot its
# probability measure using matplotlib. Then we have to plot the Probability Mass Function (PMF) of 
# a) Outcomes of flip_coin() function (plot should show that fair coin produces almost equal 
# probabilities). b) Outcomes of the biased_decision_with_fair_coin() function (unequal probabilities)
    
    fig , (plot1 , plot2) = plt.subplots(1,2,figsize=(12,10))

    # Plot a )

    x1 = np.array(["Heads","Tails"]) # True for heads and false for tails
    no_heads_of_fair_coin , no_tails_of_fair_coin = 0,0
    for repeat_exp in range(10000):
        outcome = flip_coin()
        if outcome == True :
            no_heads_of_fair_coin += 1
        else :
            no_tails_of_fair_coin += 1
    # Count the frequencies of outcomes for 10000 trails
    y1 = np.array([no_heads_of_fair_coin,no_tails_of_fair_coin]) 
    y1 = y1/10000 # To find probabilities of heads and tails respectively by normalization

    plot1.set_title('Outcomes of tossing a fair coin',color='blue',fontsize=18)
    plot1.set_xlabel('Possible outcomes of fair coin',color='red',fontsize=14)
    plot1.set_ylabel('Probability Mass Function(PMF) of fair coin',color='purple',fontsize=14)
    plot1.bar(x1 , y1 , color=['blue','green'])


    # Plot b)
    x2 = np.array(["Movies" , "Video Games"]) #movies should be of probability p = 0.125 (as per given
    # in question). We can generalize this to any value of p by counting appropriate number of tosses
    # required
    movie , videoGames = 0,0
    for repeat_exp in range(10000):
        decision = biased_decision_with_fair_coin(flip_coin,0.125)
        if decision == False:
            movie += 1
        else :
            videoGames += 1
    # Count the frequencies of favorable outcomes to both movies , video games
    y2 = np.array([movie,videoGames])
    # Normalize these frequencies to find corresponding probabilities
    y2 = y2/10000

    plot2.set_title('Outcomes of biased decision with fair coin',color = 'green',fontsize=18)
    plot2.set_xlabel('Possible biased decisions',color='orange',fontsize=14)
    plot2.set_ylabel('Probability Mass Function (PMF) of biased decisions',color='magenta',fontsize=14)
    plot2.bar(x2,y2,color=['orange','magenta'])
            

    
    plt.tight_layout()
    plt.show()

    #This code plots for the probability of choosing movies to be 1/8. However , we can extend  this
    # code to any probability by changing the argument p to the biased_decision_with_fair_coin() function






