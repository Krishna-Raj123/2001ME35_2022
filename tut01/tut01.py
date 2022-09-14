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
X = df['U'] - U_avg
Y = df['V'] - V_avg
Z = df['W'] - W_avg

#made column for storing X and named the column as U'=U - U_avg,similarily Y for V'=V - V_avg and Z for W'=W - W_avg.
df["U'=U - U_avg"] = X
df["V'=V - V_avg"] = Y
df["W'=W - W_avg"] = Z

df.to_csv('octant_output.csv')
df.head()
df.insert(10, column="Octant", value="")

#using loop
for i in range(0,x):
    M= df["U'=U - U_avg"][i]
    N= df["V'=V - V_avg"][i]
    O= df["W'=W - W_avg"][i]
    
    
    if M>0 and N>0 and O>0:
        print(1)
        df["Octant"][i] = 1
    elif M>0 and N>0 and O<0:
        print(-1)
        df["Octant"][i] =-1
    elif M<0 and N>0 and O<0:
        print(-2)
        df["Octant"][i] =-2
         elif M<0 and N>0 and O>0:
        print(2)
        df["Octant"][i] =2
    elif M<0 and N<0 and O>0:
        print(3)
        df["Octant"][i] =3
    elif M<0 and N<0 and O<0:
        print(-3)
        df["Octant"][i] =-3
    elif M>0 and N<0 and O>0:
        print(4)
        df["Octant"][i] =4
    elif M>0 and N<0 and O<0:
        print(-4)
        df["Octant"][i] =-4
df.to_csv('octant_output.csv')

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)