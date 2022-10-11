
from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():
  import pandas as pd
  df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut04\input_octant_longest_subsequence_with_range.xlsx")
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
  df.insert(11,column=" ",value=" ")
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
  q_list = [1,-1,2,-2,3,-3,4,-4]
  count =1
  for j in range(0,x-1):
       if(df.loc[j,"Octant"] == df.loc[j+1,"Octant"]):
          df.loc[j,"update"]=count
          count = count+1
       else:
          df.loc[j,"update"]=count
          count = 1
  df.loc[x-1,"update"]=count
  for j,i in zip(q_list,range(0,8)):
    mx = 0
    for t in range(0,x-1):
      if(df.loc[t,'Octant']==j):
         c = df.loc[t,'update']
         mx = max(mx,c)
    l=0
    flag =0
    for l in range(0,x-1):
      if((mx==df.loc[l,'update']) and (df.loc[l,'Octant']==j)):
        flag = flag+1
    df.loc[i,'New_octant']=j
    df.loc[i,"Longest Subsequence Length"] = mx 
    df.loc[i,'Count']= flag 
  print("****")
  for x,y in zip(range(0,8),q_list):
    get_time_range(x,df,df.loc[x,"Longest Subsequence Length"],y,df.loc[x,"Count"])
       
  df=df.drop(['update'],axis=1)
  df.insert(15,column="   ",value="  ")
  df.to_excel("output_octant_longest_subsequence_with_range.xlsx",index=False)
def get_time_range(x,df,max_val,value,ount):
    list_of_index = []
    for j in range(0,len(df["Octant"])-1):
        if(df.loc[j, "Octant"]==value):
            if(df.loc[j, "update"]==max_val):
                list_of_index.append(j)
        maximum_time = []
    minimum_time = []
    for j in list_of_index:
        maximum_time.append(df.loc[j, "Time"])
    for j in list_of_index:
        minimum_time.append(df.loc[j-max_val+1, "Time"])
    length=0
    if(value!=1):
        for i in range(0,x):
            length = length+df.loc[i,"Count"]+2
    df.loc[length,"octant_num"] = value
    df.loc[length,"longest subsequence length"] = max_val
    df.loc[length,"count"] = ount 
    df.loc[length+1,"octant_num"] = "Time"
    df.loc[length+1,"longest subsequence length"] = "From"
    df.loc[length+1,"count"] = "To"
    for i in range(0,len(maximum_time)):
        df.loc[i+length+2,"longest subsequence length"],df.loc[i+length+2,"count"] =minimum_time[i],maximum_time[i]  
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count_with_range()








#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
