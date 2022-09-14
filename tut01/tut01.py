def octact_identification(mod=5000):
import pandas as pd
df = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut01\octant_input.csv")
x = df.shape[0]
df.head(15)
#finding mean for every value
U_avg = df['U'].mean()
V_avg = df['V'].mean()
W_avg = df['W'].mean()

#making columns to store average value of U,V,W
df['U Avg']=U_avg
#and here I have given only 1st place of line to U avg otherwise average value will print in whole column
df['U Avg']=df['U Avg'].head(1)

#similarly for V and W,doing the same thing
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
octact_identification(mod)