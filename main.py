

# Import python CSV Library

import csv
import os

#Test the Driect File Access Method

# Set path for file
# ##csvpath = '/Users/Owner/PycharmProjects/Election_Results/Resources/Election_Results.csv'
file_to_open = '/Users/Owner/PycharmProjects/Election_Results/Resources/Election_Results.csv'
# Open the CSV
# ##with open(csvpath) as csvfile:
# ##    print(csvfile)

with open(file_to_open) as election_data:

 print(election_data)

# ##    csvreader = csv.reader(csvfile,delimiter=',')


# ##    print(csvreader)

# To Do: Perform Analysis

# Close the File
 #election_data.close



