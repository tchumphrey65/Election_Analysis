# Election Analysis Python Module
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

# Initialize Candidate Options and Candidate Votes dictionary
candidate_options = []
candidate_votes = {}

# Declare variables to track winning candidate, vote count and vote percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# To do: read and analyze the data here
# Open the election results and read the file file
with open(file_to_load) as election_data:
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

# Save the Results to the text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"----------------------------\n")
    print(election_results, end="")
    # Save the Final vote count to the text file.
    txt_file.write(election_results)
# Determine the percentage of votes for each candidate by looping through the candidates vote counts
# use a for loop to iterate through candidate list
    for candidate_name in candidate_votes:
        #Retrieve the vote count for current candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To Do: Print out each candidate's name, vote count and percentage of votes to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print Each candidate, their vote count and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to the text output file
        txt_file.write(candidate_results)



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

    # Save the Winning candidate's name in the text output file


    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


