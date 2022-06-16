# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# 1 count number of Ballot ID

# Add dependencies
import csv
import os

# Tell Python file path to .cvs data file and .txt output text file
##file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

# Set total_votes to zero | total_votes is the variable to count number of total votes
total_votes = 0

# Declare cadidate_options list to store name for all candidates
candidate_options = []

# Declare candidate_votes dictionary to store vote count for each candidate
candidate_votes = {}

# Open .csv data file
##with open('Resources/election_results.csv') as election_data:
with open(file_to_load) as election_data:

    # check on election_data file already open?
    ##print(election_data)

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row | next() call up next line | first "next" in .csv is the header line
    headers = next(file_reader)
    print(headers)
    
    # Iterate through each row in the CSV file
    for row in file_reader:
        # Accumulator to count total vote (exclusing header row)
        total_votes += 1
        
        # Print each row
        ##print(row)
        
        # Print first item of each row
        ##print(row[0])
        
        # Print the candidate name from each row - 3rd item
        candidate_name = row[2]
        
        # Check for new unquie candidate name to append to the candidate_option list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate_options list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            print(candidate_name)
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


print(candidate_options)
print(candidate_votes)
print(total_votes)      

# Define variables and set to zero for winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by
# looping through the {name:votes} candidate_votes dictionary
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes | float(convert integer to floating-point) | here gave same result
    vote_percentage = float(votes) / float(total_votes) *100
    # Print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    # Winning candidate and winning count tracker
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Set up winning candidate summary
winning_candidate_summary = (
    f"--------------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------------------------\n")

print(winning_candidate_summary)


# Write[Output] analysis to text file
##with open(file_to_save,"w") as outfile:
    ##outfile.write("Counties in the Election\n")
    ##outfile.write("--------------------------\n")
    ##outfile.write("Arapahoe\nDenver\nJefferson")



# Open file without using the "with" function
##outfile = open(file_to_save,"w")
##outfile.write("Hello World")
##outfile.close()


# --- datetime excercise from Module 3
# Import the datetime class from the datetime module.
##import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
##now = dt.datetime.now()
# Print the present time.
##print("The time right now is ", now)