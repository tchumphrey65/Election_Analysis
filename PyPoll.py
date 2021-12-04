# Election Analysis Python Module
# Woring Section of the file
# -----------------------------------------------------

# 1) Import python CSV Library
# add our dependencies
import csv
import os

# 2) Create Paths to input and output files (Direct Method) (Question for Nick on Indirect Method)

#Assign a variable to load a file from a path - Direct Method
file_to_load = '/Users/Owner/PycharmProjects/Election_Results/Resources/Election_Results.csv'

#Assign a variable to save the file to a path - Direct Method
file_to_save = '/Users/Owner/PycharmProjects/Election_Analysis/Resources/Election_Analysis.txt'

# Open the election results file
with open(file_to_load) as election_data:

# To do: read and analyze the data here
    # Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     # print the header row
     headers = next(file_reader)
     print(headers)

     # Print each row in the CSV file
     ##for row in file_reader:
     ##  print(row)







#Create a File to Save

file_to_save = '/Users/Owner/PycharmProjects/Election_Analysis/Resources/Election_Analysis.txt'
print(file_to_save)
# Open file to save

with open(file_to_save, "w") as txt_file:
 # Write data to the file
 txt_file.write("Counties in the Election:\n")
 txt_file.write("-------------------------\n")
# Write 3 counties to the file
 txt_file.write("Arapahoe\nDenver\nJefferson")




# To Do: Perform Analysis

# Close the File
 #election_data.close

# -------------------------------------------------------------------------------------------
# WORK AND COMMENTS SAVED DURING MODULE #
# Set path for file
# ##csvpath = '/Users/Owner/PycharmProjects/Election_Results/Resources/Election_Results.csv'

# Open the CSV
# ##with open(csvpath) as csvfile:
# ##    print(csvfile)
