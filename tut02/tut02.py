def octant_transition_count(mod=5000):
#Here we have imported pandas library for accessing the input file 
#then I used shape to fetch the dimensions of pandas type object
import pandas as pd
df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut02\input_octant_transition_identify.xlsx")
x = df.shape[0]
df.head()
#here I have used the mean() function for finding the average of U
U_avg = df['U'].mean()
#similarly here we used mean function for V and W
V_avg = df['V'].mean()
W_avg = df['W'].mean()

#hear I have made a column to store average of U
df['U Avg']=U_avg
#and here I have given only 1st place of line to U avg otherwise average value will print in whole column
df['U Avg']=df['U Avg'].head(1)

#similarly here I made column for average of V and W
#also here given only 1st place of line to W and V average otherwise average value will print in whole column
df['V Avg']=V_avg
df['V Avg']=df['V Avg'].head(1)

df['W Avg']=V_avg
df['W Avg']=df['W Avg'].head(1)

df.to_csv('octant_output.csv')
df.head()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)