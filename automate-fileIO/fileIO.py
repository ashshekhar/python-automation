
f = open('/Users/ashshekhar/Desktop/Ex_Files_Python_Automation/Exercise Files/OrganizeMe/inputFile.txt','r');

f_pass = open('/Users/ashshekhar/Desktop/Ex_Files_Python_Automation/Exercise Files/OrganizeMe/passFile.txt','w');
f_fail = open('/Users/ashshekhar/Desktop/Ex_Files_Python_Automation/Exercise Files/OrganizeMe/failFile.txt','w');

## File IO: Print the info for only people who have passed the test
for line in f:
    split = line.split();
    if split[2] == 'P':
        f_pass.write(line);
    else:
        f_fail.write(line);

f.close();
f_pass.close();
f_fail.close();



