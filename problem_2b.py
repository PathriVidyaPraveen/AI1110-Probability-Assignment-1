import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Given a height - weight dataset , we have to find the number of people with weight greater than 170 and 
# index is lesser than 4


# Read the csv file and make a dataframe out of it
data_set_read_from_csv = pd.read_csv("Height-Weight.csv")
dataset = pd.DataFrame(data_set_read_from_csv)



# Now we can use the principle of boolean masking in pandas on the dataframe that we have created
# from the dataset read from the csv file. This boolean masking helps us to filter the rows of dataframe 
# that satisfy the given conditions 

masked_dataset = dataset[(dataset["Weight"] > 170) & (dataset["Index"] < 4)]
no_of_people_with_given_conditions = len(masked_dataset)
print(no_of_people_with_given_conditions)
