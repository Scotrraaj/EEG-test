
#Function definition
def wordcheck(filename, listwords):
    try:
        file = open(filename,'r', encoding='utf8')
        read = file.readlines()
        file.close()
        for word in listwords:
            word = word.lower()
            count2 = 0
            for sentence in read:
                sentence = sentence.lower()
                if word in sentence:
                    count2+=1
                    continue
            if count2 >= 1:
                #print('Found approx. %d in %s' %(count2, filename))
                matches.append('1')
            else:
                matches.append('0')
    except FileExistsError:
        print("The file is not there!")

import os
import pandas as pd

count=0

session_records_df = pd.DataFrame()
file_path = []
matches = []
for root, dirs, files in os.walk(r'S:\Testing Python\reports'):
    #for loop to 'walk' around the directory
    for file in files:
        #a for loop to check every file in the subdirectories
        if file.endswith('.txt'):
            count+=1#setting up a condition for reading only textfiles
            path1= os.path.join(root, file)
            file_path.append(path1)
            wordcheck(path1 , ["alzheimer"])
session_records_df["File Path"] = file_path
session_records_df["matches_keyword"] = matches
print('TOTAL NUMBER OF TEXT FILES:', count)
print(session_records_df)
print(session_records_df.loc[session_records_df["matches_keyword"]=='1'])

session_records_df.to_csv(r'S:\Testing Python\Filtered.csv')


#########################
"""
has_epilepsy = []
for file in your_list_of_files
    checkfile
    has_epilepsy.append()
yourstring = "bla%^&testbla"

if "test" in yourstring:
    print("found test")
else:
    print("not found")

# heading

## subheading

- item
- item




return has_epilepsy

storingdata = pd.DataFrame({paths:listoffiles, has })


has_epilepsy = wordcheck(listoffiles, wordtocheck)

###############################

"""