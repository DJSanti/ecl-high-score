#######################################################################################################################
# ECL Coding Challenge 2024
# Objective: Write a program that outputs the N highest record IDs by descending score. Output to command line in JSON.
# Date: 04/06/2024
# Coded by: Samantha Santiago
#######################################################################################################################
#
# IMPORTS
import argparse
import json
#
#######################################################################################################################
# Why argparse? As simple as it would be to go with sys.argv (given that we need just the file and number of records to print), 
# argparse allows for better scalability should this command grow and evolve to do more than the objective. Believe me, I'm accustomed to sys, but having the
# option to save myself from juggling arg places on the command line is very refreshing. Plus, I can define the argument types just like that.
#######################################################################################################################
#
# FUNCTIONS
# Defining our functions up here to keep the code organized. Seeing as this is a simple program, I could just have blocks of code
# and call it a day. But, to save my future self (and others) some time when it comes to reasoning with this thing, best to separate the parsing and reading
# from the sorting and printing. Ideally, I'd separate each of these functions further, but this works for now.

def parse_and_read():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File name/path of the input data needed for processing.")
    parser.add_argument("records", help="Number of records to print to stdout.", type=int)
    args = parser.parse_args()
        
    # create an empty array for the score:id pairs
    records_arr = []
    # read each line to create key-value items
    with open(args.file) as f:
        for line in f:
            # separate each line into the score, partition, and JSON data object nested within
            score, partition, data = line.partition(": ")
            # get id from data and create dictionary entry
            dataJSON = json.loads(data)
            score_as_int = int(score)
            records_item = { "score": score_as_int, "id": dataJSON['id'] }
            # add some list comprehension up here to keep duplicates out of the records list
            if records_item not in records_arr:
                records_arr.append(records_item)
    # return dictionary and items to print for next function
    return records_arr, args.records
   
# sort the records by descending score, then print the requested number of records
def print_highest_records(records, num):
   sorted_scores = sorted(records, key=lambda x: x["score"], reverse=True)

    # to keep this moving, only grab the number of score:record pairs given in the argument.
    # add each item to a smaller list, then print that list in JSON format.
   print_list = []
   for pair in sorted_scores[:num]:
        print_list.append(pair)  
   print(json.dumps(print_list, indent=4))


##################
# RUN THE PROGRAM
recs, number = parse_and_read()
print_highest_records(recs, number)