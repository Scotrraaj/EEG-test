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
patient_id = []
session_id = []
has_or_had_alzheimer = []
receive_medication = []
for root, dirs, files in os.walk(r'reports'):
    for file in files:
        if file.endswith('.txt'):
            count+=1
            path1= os.path.join(root, file)
            file_path.append(path1)
            wordcheck(path1 , ["alzheimer", "dementia" , "donepezil" , "rivastigmine" , "aricept" , "memantine"])

for folders in file_path:
    split_folder = folders.split('\\')
    patient = split_folder[-4]
    session = split_folder[-2]
    patient_id.append(patient)
    session_id.append(session)

for every_matches in matches:
    if every_matches == '1':
        has_or_had_alzheimer.append('')
    else:
        has_or_had_alzheimer.append('0')

for every_zero in has_or_had_alzheimer:
    if every_zero == '0':
        receive_medication.append('0')
    else:
        receive_medication.append('')

df = pd.DataFrame({'Patient_ID': patient_id , 'Session_ID': session_id , 'File Path': file_path , 'Match' : matches, 'Has or Had Alzheimer': has_or_had_alzheimer, 'Receive Medication': receive_medication})
df.to_csv(r'Filtered.csv')
print('TOTAL NUMBER OF TEXT FILES:', count)
print('\n')
print(df)

#print(df.loc[df["Match"]=='1'])
#print(tempdf.loc[tempdf["Matches"]=='1'])