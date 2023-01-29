# Simple function to remove all comments and useless line breaks.
# Run it simply by launching with python

import re

def remover(input) : 
    with open(input, "r") as source: 
        lines = source.readlines()

    result = []   #The result will be written in a an empty list .
    check = False     #variable to tknow if there are comments at end of code lines .
    breaklines = 0         #We want to keep line breaks but not more than 3 .
    breaklines_max = 3

    for line in lines:   #Now we are checking beggining and ending of all linees to know if there are comments to remove
        stripped = line.strip() 

        if check:
            if stripped.endswith("'''") or stripped.endswith('"""'):
                check = False
            continue
        elif stripped.startswith("'''") or stripped.startswith('"""'):
            check = True
            continue  #So if there are comments in the line, we're going to uncomment

        else:
            stripped = re.sub(r'#.*', '', line) #replace all text after "#" in "line" with an empty string then save the result in "stripped"

            if stripped != "": #Count the number of empty lines.
                if stripped.strip() == "":
                    breaklines += 1

                else: #Add new lines if needed
                    if breaklines > 0:
                        result.extend(["\n"] * min(breaklines, breaklines_max))
                        breaklines = 0
                    result.append(stripped) #Print all in the result

    with open(input, "w") as output: #Then remove the whole code , replacing by the new one
        output.writelines(result)


#Here we are launching the code, change the path by yours.
remover("YOUR_PYTHON_FILE.py") 

#Btw you can also change this and add an argument to the function remover, like an output : 



# def remover(input, output_file) : 

#  ....     

# with open(output_file, "a") as output: 
#        output.writelines(result)

# remover("YOUR_PYTHON_FILE.py", "YOUR_PYTHON_OUTPUT_FILE.py") 



#but you will should better use the program I developped to do this instead.