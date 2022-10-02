def octant_transition_count(mod=5000):
#Here we have imported pandas library for accessing the input file 
#then I used shape to fetch the dimensions of pandas type object
  import pandas as pd
  df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\New folder\2001mE35_2022\tut02\input_octant_transition_identify.xlsx")
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

  df.head()
#here I have defined X,Y,Z and X=U' , Y=V' , Z=W'
  X = df['U'] - U_avg
  Y = df['V'] - V_avg
  Z = df['W'] - W_avg

#here I made the column for storing X and named the column as U'=U - U_avg and similarly I have done for Y and Z.
  df["U'=U - U_avg"] = X
  df["V'=V - V_avg"] = Y
  df["W'=W - W_avg"] = Z

  df.head()
#here made the column for storing the value of octant
  df.insert(10, column="Octant", value="")

#using loop
  for i in range(0,x):
    m= df["U'=U - U_avg"][i]
    N= df["V'=V - V_avg"][i]
    O= df["W'=W - W_avg"][i]
    
    
    if m>0 and N>0 and O>0:
        print(1)
        df["Octant"][i] = 1
    elif m>0 and N>0 and O<0:
        print(-1)
        df["Octant"][i] =-1
    elif m<0 and N>0 and O>0:
        print(2)
        df["Octant"][i] =2
    elif m<0 and N>0 and O<0:
        print(-2)
        df["Octant"][i] =-2
    elif m<0 and N<0 and O>0:
        print(3)
        df["Octant"][i] =3
    elif m<0 and N<0 and O<0:
        print(-3)
        df["Octant"][i] =-3
    elif m>0 and N<0 and O>0:
        print(4)
        df["Octant"][i] =4
    elif m>0 and N<0 and O<0:
        print(-4)
        df["Octant"][i] =-4
  df.at[1,''] = 'User Input'
  mod_max_value=30000
  n=mod_max_value//mod
  for k in range(0,n+2):
    if(k==0):
        df.at[k,'Octant ID'] = 'Overall Count'
    elif(k==1):
        df.at[k,'Octant ID'] =str(mod)
    elif(k==2):
        df.at[k,'Octant ID'] = str((k-2)*mod) +"-"+str((k-1)*mod-1)
    else:
        df.at[k,'Octant ID'] = str((k-2)*mod) +"-"+str((k-1)*mod-1)
  q_list = [1,-1,2,-2,3,-3,4,-4]
  for j in q_list:
    if(j==0):
        continue
    df.at[0,j] = list(df['Octant']).count(j)
    for i in range(0,n):
        if(i==0):
            df.at[i+2,j] = list(df['Octant'][i*mod:(i+1)*mod]).count(j) 
        else :
            df.at[i+2,j] = list(df['Octant'][i*mod:(i+1)*mod]).count(j) 
  range_value = int(2 + (mod_max_value/mod))
  df.loc[range_value,"Octant ID"] = "Verified"
  sum=0
  for i in q_list:
        temp = sum
        for j in range(2,range_value):
            sum += df.loc[j,i]
        df.loc[range_value, i] = sum
        sum = temp
  df.to_excel("output_octant_transition_identify.xlsx") 
  df['C']=df['Octant'].shift(-1)
  groups=df.groupby(['Octant','C'])
  counts = {i[0]:len(i[1]) for i in groups}
  print(counts)
  matrix=pd.DataFrame()
  for x in q_list:
    matrix[str(x)]=pd.Series([counts.get((x,y),0) for y in q_list], index = q_list)
  print(matrix)
  df1=matrix
  df.loc[range_value+2,"Octant ID"] = "Overall Transition Count"
  df.loc[range_value+5, ""] = "From"
  df.loc[range_value+3, +1] = "To"
  df.loc[range_value+4,"Octant ID"] = "Count"
  for j,i in zip(range(5,13),q_list):
     df.loc[range_value+j,"Octant ID"] = i 
        
  for i in q_list:
     df.loc[range_value+4, i] = i
  for i in range(0,8):
        for k,l in zip(q_list,range(0,8)):
            df.loc[range_value+5+i,k]=df1.iloc[i,l]
  n=30000//mod
  for i in range(0,n):
    print("The x is {} and Y is {}".format(i*mod,(i+1)*mod-1))
    df.loc[range_value+15+(i*12), "Octant ID"] = str(i*mod)+"-"+str((i+1)*mod-1)
    df.loc[range_value+14+(i*12),"Octant ID"] = "mod Transition Count"
    df.loc[range_value+17+(i*12), ""] = "From"
    df.loc[range_value+15+(i*12), +1] = "To"
    df.loc[range_value+16+(i*12),"Octant ID"] = "Count"
    for j,k in zip(range(17,25),q_list):
        df.loc[range_value+j+(i*12),"Octant ID"] = k     
    for k in q_list:
        df.loc[range_value+16+(i*12), k] = k
    df['C']=df['Octant'][i*mod:(i+1)*mod].shift(-1)
    groups=df.groupby(['Octant','C'])
    counts = {i[0]:len(i[1]) for i in groups}
    matrix=pd.DataFrame()
    for x in q_list:
        matrix[str(x)]=pd.Series([counts.get((x,y),0) for y in q_list], index = q_list)
    df2 = matrix
    print(df2)
    for t in range(0,8):
        for k,l in zip(q_list,range(0,8)):
            df.loc[(i*12)+25+t,k]=df2.iloc[t,l]
  df=df.drop(['C'],axis =1)
  df.to_excel('output_octant_transition_identify.xlsx',index=False)
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)