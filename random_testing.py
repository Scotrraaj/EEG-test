
#Function definition
def wordcheck(filename, listwords):
    try:
        file = open(filename,'r', encoding='utf8')
        read = file.readlines()
        file.close()
        for word in listwords:
            word = word.lower()
            count = 0
            for sentence in read:
                sentence = sentence.lower()
                if word in sentence:
                    count+=1
                    continue
            if count >= 1:
                print('Found approx. %d in %s' %(count, filename))
    except FileExistsError:
        print("The file is not there!")

import os                                                                      #import os package

for root, dirs, files in os.walk(r'S:\Testing Python\reports'):           #for loop to 'walk' around the directory
    for file in files:                                                         #a for loop to check every file in the subdirectories
        if file.endswith('.txt'):                                              #setting up a condition for reading only textfiles
            path1= os.path.join(root, file)
            wordcheck(path1 , ["alzheimer"])

            cleaning up unnecessary bla blas
            more blas
            some more blas

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
