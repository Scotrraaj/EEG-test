
#Function definition
def wordcheck(filename, listwords):
    try:
        file = open(filename,'r', encoding='utf8')
        read = file.readlines()
        file.close()
        longline = ''.join(read)
        longline=longline.lower()
        found = False
        for word in listwords:
            word = word.lower()
            if word in longline:
                matches.append('1')
                found = True
                break
        if not found:
            matches.append('0')
    except FileExistsError:
        print("The file is not there!")

import os
import pandas as pd

count=0

file_path = []
matches = []
for root, dirs, files in os.walk(r'S:\Testing Python\reports'):
    for file in files:
        if file.endswith('.txt'):
            count+=1
            path1= os.path.join(root, file)
            file_path.append(path1)
            wordcheck(path1 , ["alzheimer", "dementia" , "donepezil" , ""])

#session_records_df = pd.DataFrame({'File Path': file_path},{'matches_keyword': matches})
print('TOTAL NUMBER OF TEXT FILES:', count)
tempdf=pd.DataFrame({'Matches': matches})
print(tempdf)
print('\n')
print(tempdf.loc[tempdf["Matches"]=='1'])
#df = pd.DataFrame({'File Path': file_path , 'Match' : matches})
#print(df)
#print(session_records_df)
#print(session_records_df.loc[session_records_df["matches_keyword"]=='1'])

#session_records_df.to_csv(r'S:\Testing Python\Filtered.csv')


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