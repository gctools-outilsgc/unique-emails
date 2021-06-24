import os
import sys

import pandas as pd

'''
python unique_users.py {year} {month number} {day number}

Only uses csvs from folder, each must have a column 'emails'
'''
if __name__ == "__main__": 
    if len(sys.argv) != 4:
        raise Exception("Invalid args")
    
    path = "user_data/{}-{}-{}".format(sys.argv[1], sys.argv[2], sys.argv[3])
    
    #Ensure directory exists
    if not os.path.exists(path):
        raise Exception("Invalid path")

    print("\nDetermining unique emails in {path}".format( path = path))

    #All of the set up

    files = os.listdir(path)
    
    for a_file in files:
        if a_file[-3:] != "csv": #if file ending isnt csv, don't include it
            files.remove(a_file)

    dataframes = [] 

    #Creates a series of DataFrames from the files, stored in dataframes (the list)
    for a_file in files: #For each file
        with open(path + "/" + a_file, 'r') as f: #open file
                
            data = []
            first = []
            for line in f: #for each line in file
                if "connex" in a_file or "pedia" in a_file:
                    arr = line.split(",")
                    if len(arr) != 4:
                        print(arr)
                else: 
                    if len(first) == 0:
                        arr = line.split(",")
                        first = arr
                    else:
                        arr = line.split(",")
                        #fixes broken ones that had a | in one of the fields (always the last one)
                        if len(arr) != len(first):
                            new_arr = []
                            count = 0
                            end = ""
                            for i in range(len(arr)):
                                if i + 1 < len(first):
                                    new_arr.append(arr[i])
                                else:
                                    end = end + arr[i]
                            new_arr.append(end)
                            arr = new_arr
                data.append(arr)
        if "connex" in a_file or "pedia" in a_file:
            x = pd.DataFrame(data, columns = ["email", "reg_date", "last_action"])
        else:
            x = pd.DataFrame(data, columns = first)
            x.drop([0], inplace = True)
        dataframes.append(x)


    # Now, time to process

    #Put all emails into one list
    all_emails = []
    count = 0
    for dataframe in dataframes:
        count += 1
        for val in dataframe["email"]:
            all_emails.append(val)

    print("Total emails:", len(all_emails))
        
    #use a set to remove duplicates
    unique_emails = set()
    for x in all_emails:
        unique_emails.add(x)

    print("Total unique emails:", len(unique_emails))


        
        