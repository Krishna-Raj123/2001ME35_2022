def octant_transition_count(mod=5000):
#Here we have imported pandas library for accessing the input file 
#then I used shape to fetch the dimensions of pandas type object
import pandas as pd
df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut02\input_octant_transition_identify.xlsx")
x = df.shape[0]
df.head()

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)