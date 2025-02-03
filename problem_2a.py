import pandas as pd


#Analysing Titanic- dataset

Titanic_data = pd.read_csv("Titanic-Dataset.csv") #reads the csv file

# Now let "S" be the set of people who survived and "C" be the set of people whose 
# ticket class is two . Now  the conditional probability that ticket class is two 
# given the person is survived is written as P(C|S). On expanding the given expression
# we get P(C|S) = P(C ∩ S) / P(S). To calculate this let us calculate P(S) and P(C ∩ S)

# calculating P(S)

#Use principle of boolean masking to find the passengers of dataset satisfying the given criteria.
# Given that the person survived, what is the probability that his ticket Class is two?

no_of_elements_in_S = len(Titanic_data[(Titanic_data["Survived"]== 1)])
# above expression counts the number of 1's in column "Survived" of the data-set Titanic_data(1 means the person survived)

Total_no_of_people = len(Titanic_data)
# gives the the total number of people 
# now P(S) = no_of_elements_in_S / Total_no_of_people
probability_of_S = no_of_elements_in_S/Total_no_of_people

# from this we got P(S)

# now to calculate P(C ∩ S)
# let set Q = C ∩ S 

no_of_elements_in_Q = len(Titanic_data[(Titanic_data["Survived"]==1) & (Titanic_data["Ticket class"]==2)])
# above expression counts the number of rows having 1 in "Survived" column and 2 in "Ticket class" column 
# which is the number of elements in Q . 
# now P(C ∩ S) = P(Q) = no_of_element_in_Q / Total_no_of_people
probability_of_Q = no_of_elements_in_Q/Total_no_of_people

# we found both P(S) and P(C ∩ S) above
# substituting these values to get P(C|S) = P(C ∩ S)/P(S) = P(Q)/p(S)

required_probability = probability_of_Q/probability_of_S # gives P(C|S)

print(f"The probability that a person's Ticket class is two given that he survived is: {required_probability}")


