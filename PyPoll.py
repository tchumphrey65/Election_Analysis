# Election Analysis Python Module
# Woring Section of the file
# -----------------------------------------------------

# Import python CSV Library / add our dependencies
import csv
import os

#Create Paths to input and output files (Direct Method) (Question for Nick on Indirect Method)

#Assign a variable to load a file from a path - Direct Method
file_to_load = '/Users/Owner/PycharmProjects/Election_Results/Resources/Election_Results.csv'

#Assign a variable to save the file to a path - Direct Method
file_to_save = '/Users/Owner/PycharmProjects/Election_Analysis/Resources/Election_Analysis.txt'

# Initialize a total votes counter called "total_votes"
total_votes = 0

# Initialize Candidate Options
candidate_options = []

# Declare an empty dictionary to hold candidate name and candidate total votes
candidate_votes = {}

# Declare winning candidate variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file file
with open(file_to_load) as election_data:

# To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # if the candidate name does not match an existing candidate ...
        if candidate_name not in candidate_options:
            # Then add new name to the list of candidates
            candidate_options.append(candidate_name)

            # Start tracking the candidates vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidates vote count
        candidate_votes[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the candidates vote counts
# use a for loop to iterate through candidate list

for candidate_name in candidate_votes:
    #Retrieve the vote count for current candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # To Do: Print out each candidate's name, vote count and percentage of votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning candidate and Winning count


# Determine winning vote count and candidate
# Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

    # if True set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #Set the winning candidate equal to candidates name
        winning_candidate = candidate_name

    # Print the Election Summary and results

winning_candidate_summary = (
         f"---------------------------------\n"
         f"Winner: {winning_candidate}\n"
         f"Winning Vote Count: {winning_count:,}\n"
         f"Winning Percentage: {winning_percentage:.1f}%\n"
         f"---------------------------------\n"
        )

print(winning_candidate_summary)


 #   print((f"{candidate_name}: received {vote_percentage: .1f}% of the vote"))

#print(f"There were {total_votes} cast in the election")
# 3. Print the total  votes
# print(total_votes)
# print(candidate_votes)


#Create a File to Save

#file_to_save = '/Users/Owner/PycharmProjects/Election_Analysis/Resources/Election_Analysis.txt'
# print(file_to_save)
# Open file to save

#with open(file_to_save, "w") as txt_file:
 # Write data to the file
# txt_file.write("Counties in the Election:\n")
# txt_file.write("-------------------------\n")
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
