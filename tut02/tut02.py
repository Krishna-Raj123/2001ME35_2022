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
#here I have defined X,Y,Z and X=U' , Y=V' , Z=W'
X = df['U'] - U_avg
Y = df['V'] - V_avg
Z = df['W'] - W_avg

#here I made the column for storing X and named the column as U'=U - U_avg and similarly I have done for Y and Z.
df["U'=U - U_avg"] = X
df["V'=V - V_avg"] = Y
df["W'=W - W_avg"] = Z

df.to_excel('output octant transition identify.xlsx')
df.head()
#here made the column for storing the value of octant
df.insert(7, column="Octant", value="")

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
    elif M<0 and N>0 and O>0:
        print(2)
        df["Octant"][i] =2
    elif M<0 and N>0 and O<0:
        print(-2)
        df["Octant"][i] =-2
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
df.to_excel('output octant transition identify.xlsx')
df.at[1,''] = 'User Input'
n=30000//mod;
for k in range(0,n+2):
    if(k==0):
        df.at[k,'Octant ID'] = 'Overall Count'
    elif(k==1):
        df.at[k,'Octant ID'] =str(mod)
    elif(k==2):
        df.at[k,'Octant ID'] = str((k-2)*mod) +"-"+str((k-1)*mod)
    else:
        df.at[k,'Octant ID'] = str((k-2)*mod+1) +"-"+str((k-1)*mod)
for j in range(-4,5):
    if(j==0):
        continue
    df.at[0,j] = list(df['Octant']).count(j)
    for i in range(0,n):
        if(i==0):
            df.at[i+2,j] = list(df['Octant'][i*mod:(i+1)*mod]).count(j) 
        else :
            df.at[i+2,j] = list(df['Octant'][i*mod+1:(i+1)*mod]).count(j) 
df.to_excel('output octant transition identify.xlsx')
numbers = sorted(df['Octant'].unique())
print(numbers)
df['C']=df['Octant'].shift(-1)
groups=df.groupby(['Octant','C'])
counts = {i[0]:len(i[1]) for i in groups}
print(counts)
matrix=pd.DataFrame()
for x in numbers:
    matrix[str(x)]=pd.Series([counts.get((x,y),0) for y in numbers], index = numbers)
print(matrix)
df1=matrix
df.append(df1)
df.to_excel('output octant transition identify.xlsx')
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)