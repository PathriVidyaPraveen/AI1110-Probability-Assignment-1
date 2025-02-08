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
    # prob_of_movies = p
    # prob_of_video_games = 1-p
    
    # result = np.random.choice([False,True],p=[prob_of_movies,prob_of_video_games])
    # return result

    # We can take biased decision with fair coin as follows. If p = 0.125 i.e 1/8 it means that we can
    # toss a fair coin 3 times and then choose movies if all the tosses outcomes are heads which happens
    # with probability 0.125.Now , we want to extend this to all types of probabilities other than those
    # which are powers of 0.5 . So we take the probability argument p as summation of ((x i)/(2^i))
    # where i is a natural number. In simple words we represent them as sequences of tosses (x1/2) + 
    # (x2/4) + (x3/8) + ..... . 

    prob_argument = p
    no_digits = 0
    arrX = []
    # We store the values of x1 , x2 , x3 , ... in the arrX list. We take this upto x10 so that it is
    # very close to actual probability argument.
    while prob_argument!= 0 and no_digits <10:
        prob_argument = prob_argument*2
        if prob_argument >= 1:
            arrX.append(1)
            prob_argument = prob_argument-1
        else :
            arrX.append(0)
        
        no_digits += 1
    
    # Now we have to make the decision based on this arrX list as follows. The algorithm followed is
    # We find out all the trail outcomes of the number by tossing a fair coin and then add the numbers
    # int another list (not necessarily a list... we can even add them directly to avoid unnecessary memory
    # allocation). Say it be arrY then we find the number obtained by adding all the num_trails values
    # i.e summation of (yi)/(2^i) . If the number obtained is greater than p , we choose video games . 
    # If the number is lessre than p , we choose movies. To explain it in simple words , the probability
    # argument p divides the interval of [0,1] into 2 parts - [0,p] nd [p,1] of lengths p and 1-p
    # respectively. Now it is more of like geometric probability where we calculate lengths of intervals
    # to find out probabilities and choose them for movies and video games accordingly.

    num_trails = len(arrX) # Range of num_trails is 1 to 10 as we take precision of 10 digits as 1/(2^11)
    # is very small and we ignore that
    decision = True

    for index in range(num_trails):
        outcome = flip_coin()
        if outcome == arrX[index]:
            continue
        elif outcome==True and arrX[index]==False :
            decision = True
            break
        else :
            decision = False
            break
    

    return decision






    
    
if __name__ == "__main__":
    movies = 0 #Outcomes favourable to choosing movies
    games = 0  #Outcomes favourable to choosing video games
    prob_movies = float(input("Please enter the probability of choosing movies: "))

    #Conduct the experiment to take biased decision 10000 times and test for the movies probability to 
    # be 1/8 thereby ensuring the correctness of the code if we want our probability of choosing
    # movies to be 0.125

    #To improve the accuracy of probability result to be close to 0.125 , we perform this entire 
    #experiment 10 times and take the mean of all 10 probabilities.
    probabilities = []

    for repeat_exp in range(10):
        for no_of_experiments in range(10000):
            decision = biased_decision_with_fair_coin(flip_coin , prob_movies)
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
    
    fig , (plot1 , plot2 , plot3) = plt.subplots(1,3,figsize=(18,10))

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

    # Plot for biased decision of given value p = 0.125
    x2 = np.array(["Movies" , "Video Games"]) #movies should be of probability p = 0.125 (as per given
    # in question). 
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

    plot2.set_title('Outcomes of biased decision with fair coin(p=0.125)',color = 'red',fontsize=18)
    plot2.set_xlabel('Possible biased decisions',color='orange',fontsize=14)
    plot2.set_ylabel('Probability Mass Function (PMF) of biased decisions',color='magenta',fontsize=14)
    plot2.bar(x2,y2,color=['orange','magenta'])






    # Plot b)
    x3 = np.array(["Movies" , "Video Games"])
    movie , videoGames = 0,0
    for repeat_exp in range(10000):
        decision = biased_decision_with_fair_coin(flip_coin,prob_movies)
        if decision == False:
            movie += 1
        else :
            videoGames += 1
    # Count the frequencies of favorable outcomes to both movies , video games
    y3 = np.array([movie,videoGames])
    # Normalize these frequencies to find corresponding probabilities
    y3 = y3/10000

    plot3.set_title('Outcomes of biased decision with fair coin',color = 'green',fontsize=18)
    plot3.set_xlabel('Possible biased decisions',color='green',fontsize=14)
    plot3.set_ylabel('Probability Mass Function (PMF) of biased decisions',color='indigo',fontsize=14)
    plot3.bar(x3,y3,color=['red','indigo'])



            

    
    plt.tight_layout()
    plt.show()

    













