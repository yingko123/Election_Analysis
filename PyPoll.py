#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#1 count number of Ballot ID


# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

import csv
import os

#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)
    
#Print each row in the CSV file
    #for row in file_reader:
        #print(row[0])


#with open('Resources/election_results.csv') as election_data:
    #print(election_data)


#print(file_to_save)

#with open(file_to_save,"w") as outfile:
    #outfile.write("Counties in the Election\n")
    #outfile.write("--------------------------\n")
    #outfile.write("Arapahoe\nDenver\nJefferson")

#outfile = open(file_to_save,"w")
#outfile.write("Hello World")
#outfile.close()
