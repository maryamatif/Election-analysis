# The data we need to retrieve
#1. The total number of votes casted
#2. A complete list of candidates who received votes
#3. The % of voest each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
# Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results file and read.
# with open(file_to_load) as election_data:
#     # to do: perform analysis.
# #     print(election_data)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
    #print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# #Write some data to the file
# outfile.write("Hello World")
# #Close the file
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0
#4. Creating a new list for candidate name
candidate_options=[]
# Create a dictionary with candidate name and totla votes
candidate_votes={}
#Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    # print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #3. Print the total votes.
        #print(total_votes)
        #5 Print the candidate name from each row
        candidate_name = row[2]
        # Add candidate name to candidate list
        # candidate_options.append(candidate_name)
        # print(candidate_options)
        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
#Save the results to our next file
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
        # Save the final vote count to the text file.
    txt_file.write(election_results)
            # Determine the % of votes by each candidate
            #1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the % of votes.
        vote_percentage = float(votes)/float(total_votes) * 100
        #4. Print the candidate name and % of votes           
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    # # Print each candidate, their voter count, and percentage to the terminal.
    print(winning_candidate_summary)
    # #  Save the candidate results to our text file.
    txt_file.write(winning_candidate_summary)