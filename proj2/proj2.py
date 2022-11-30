import pandas as pd
import streamlit as st
from datetime import datetime
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
start_time = datetime.now()
def get_rank(df,column_no,q_list):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    octant_count = []
    for i in q_list:
        octant_count.append(df.loc[column_no,i]) 
    octant_count.sort(reverse=True)

    for i in q_list:
        for x in range(0,8):
            if(octant_count[x]==df.loc[column_no,i]):
                df.loc[column_no,"Rank Octant "+str(i)] = x+1
    
    for i in q_list:
        if(df.loc[column_no,"Rank Octant "+str(i)]==1):
            df.loc[column_no,"Rank1 Octant ID"] = i
            df.loc[column_no,"Rank1 Octant Name"]=octant_name_id_mapping[str(i)]
    
    for i in q_list:
        val = df.loc[column_no,"Rank Octant "+str(i)]
        #df.style.apply(lambda val:['background:yellow' if val == 1 else " "],axis =0)
        # color = 'yellow' if val == 1 else ''
        # return 'background-color: {}'.format(color)
        df.style.applymap(lambda:['background-color:yellow' if val == 1 else ''],axis=0)
def get_count(df,value):
    return len(df[df['Octant'] == value]) 
def octant(df,x,y,z,i):
       if(x >= 0 and y >= 0 and z >= 0) :
         df.loc[i, "Octant"] = 1
       elif (x < 0 and y >= 0 and z >= 0) :
        df.loc[i, "Octant"] = 2
            
       elif(x < 0 and y < 0 and z >= 0) :
        df.loc[i, "Octant"] = 3
            
       elif(x >= 0 and y < 0 and z >= 0) :
        df.loc[i, "Octant"] = 4
            
       elif(x >= 0 and y >= 0 and z < 0) :
        df.loc[i, "Octant"] = -1
            
       elif(x < 0 and y >= 0 and z < 0) :
        df.loc[i, "Octant"] = -2
            
       elif(x < 0 and y < 0 and z < 0) :
        df.loc[i, "Octant"] = -3
            
       elif(x >= 0 and y < 0 and z < 0) :
        df.loc[i, "Octant"] = -4
def get_max_count(df,value):
    max_val = 0 
    for j in range(0,len(df["Octant"])-1):
        if(df.loc[j, "Octant"]==value):
            val = df.loc[j, "update"] 
            max_val = max(max_val,val)
    return max_val  

def count_of_max_count(df,value):
    z = get_max_count(df,value)
    count=0
    for j in range(0,len(df["Octant"])-1):
        if(df.loc[j, "Octant"]==value):
           if(df.loc[j, "update"]==z):
              count = count+1
    print("The maximum value is {} and The count is {}".format(z,count))
    return count     

def get_time_range(x,df,max_val,value,count):
    list_of_index = []
    for j in range(0,len(df["Octant"])-1):
        if(df.loc[j, "Octant"]==value):
            if(df.loc[j, "update"]==max_val):
                list_of_index.append(j)
    maximum_time = []
    minimum_time = []
    for j in list_of_index:
        maximum_time.append(df.loc[j, "T"])
    for j in list_of_index:
        minimum_time.append(df.loc[j-max_val+1, "T"])

    length=0
    if(value!=1):
      for i in range(0,x):
            length = length+df.loc[i,"Count"]+2
    df.loc[length,"octant_num"] = value
    df.loc[length,"longest subsequence length"] = max_val
    df.loc[length,"count"] = count
    df.loc[length+1,"octant_num"] = "Time"
    df.loc[length+1,"longest subsequence length"] = "From"
    df.loc[length+1,"count"] = "To"
    for i in range(0,len(maximum_time)):
        df.loc[i+length+2,"longest subsequence length"],df.loc[i+length+2,"count"] = round(minimum_time[i],3),round(maximum_time[i],3)
                   
    print("The max_value is {} Minimim time {} and the Maximum time {}".format(max_val,minimum_time,maximum_time))
mod=st.number_input("Enter mod value")
mod=int(mod)
def proj_octant_gui():
	pass
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data
st.title("hi,my first web app")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
out=st.button("Compute")
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    df = pd.read_excel(uploaded_file)
    print(df.head(5))
    if out:
      df.loc[0, "U Avg"] = (df["U"].mean())
      df.loc[0, "V Avg"] = (df["V"].mean())
      df.loc[0, "W Avg"] = (df["W"].mean())
      df["U'=U - U avg"] = (df["U"]-df.loc[0, "U Avg"])
      df["V'=V - V avg"] = (df["V"]-df.loc[0, "V Avg"])
      df["W'=W - W avg"] = (df["W"]-df.loc[0, "W Avg"])
      for i in range(len(df)):
           octant(df,df.loc[i, "U'=U - U avg"], df.loc[i, "V'=V - V avg"],df.loc[i, "W'=W - W avg"],i)
      df.loc[1, "User Input"] = "Mod"+str(mod)
      df.loc[0, "Octant ID"] = "Overall Count"
      q_list = [1,-1,2,-2,3,-3,4,-4]
      for i in q_list:
         df.loc[0, i] = get_count(df,i)

      mod_max_value = 20000
      range_value = int(2 + (mod_max_value/mod))
      print(range_value)
      x = 0
      y = mod
      for j in range(2,range_value):
        print("The x is {} and Y is {}".format(x,y))
        df.loc[j, "Octant ID"] = str(x)+"-"+str(y-1)
        for i in q_list:
            df.loc[j, i] = get_count(df.iloc[x:y],i)
        x = y
        y = x + mod
      df.loc[5, "Octant ID"] = str(x-mod-1)+"-"+"Last Index"
#ranking the values
      octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
      for j in range(0,range_value):
        get_rank(df,j,q_list)
    
      for i,j in zip(q_list,range(0,8)):
        df.loc[range_value+2,1] = "Octant ID"
        df.loc[range_value+2,-1] = "Octant Name"
        df.loc[range_value+2,2] = "Count of Rank 1 Mod Values"
        df.loc[range_value+3+j,1] = i
        df.loc[range_value+3+j,-1] = octant_name_id_mapping[str(i)]
        count = 0
        for x in range(2,range_value):
            if(df.loc[x,"Rank1 Octant ID"]==i):
                count+=1
        df.loc[range_value+3+j,2] = count
# Overall Transition Count 
      columns = ["A","B","C","D","E","F","G","H"]
      df.loc[2," "] = "From"
      df.loc[1,"Overall Transition Count"] = "Count"
      df.loc[0,"A"] = "To"
      for j,i in zip(range(0,8),q_list):
            df.loc[j+2,"Overall Transition Count"] = i     
      for j,i in zip(columns,q_list):
        df.loc[1, j] = i
      df['C']=df['Octant'].shift(-1)
      group=df.groupby(['Octant','C'])
      counts = {i[0]:len(i[1]) for i in group}
      print(counts)
    # prints overall transition count of each octant in the output file
      matrix=pd.DataFrame()
      for i in q_list:
        matrix[str(i)]=pd.Series([counts.get((i,j),0) for j in q_list], index = q_list)
      print(matrix)
      print("     ")

      df1 = matrix
      for x in range(0,8):
            for i,y in zip(columns,range(0,8)):
                df.loc[x+2,i] = df1.iloc[x,y]
# prints overall transition count of each octant for mod ranges in the output file
      n=mod_max_value//mod
      for i in range(0,n):
        print("The x is {} and Y is {}".format(i*mod,(i+1)*mod))
        df.loc[12+(i*12), "Overall Transition Count"] = str(i*mod)+"-"+str((i+1)*mod)
        df.loc[11+(i*12),"Overall Transition Count"] = "Mod Transition Count"
        df.loc[14+(i*12), " "] = "From"
        df.loc[12+(i*12), "A"] = "To"
        df.loc[13+(i*12),"Overall Transition Count"] = "Count"
        for j,k in zip(range(12,20),q_list):
            df.loc[2+j+(i*12),"Overall Transition Count"] = k     
        for j,k in zip(columns,q_list):
            df.loc[13+(i*12), j] = k

        df['C']=df['Octant'][i*mod:(i+1)*mod].shift(-1)
        groups=df.groupby(['Octant','C'])
        counts = {i[0]:len(i[1]) for i in groups}

        matrix=pd.DataFrame()
        for t in q_list:
            matrix[str(t)]=pd.Series([counts.get((t,r),0) for r in q_list], index = q_list)
        print(matrix)
        print("     ")

        df2 = matrix
        for x in range(0,8):
            for k,y in zip(columns,range(0,8)):
                df.loc[x+14+(i*12),k] = df2.iloc[x,y]
        #remove the extra column made 
      df.drop(['C'],axis=1,inplace = True)


    #longest subsequent lengths and their ranges
      counts = 1
      for i in range(0,len(df["Octant"])-1):
        if(df.loc[i,"Octant"] == df.loc[i+1,"Octant"]):
            df.loc[i,"update"] = counts
            counts=counts+1
        else:
            df.loc[i,"update"] = counts
            counts = 1
      df.loc[len(df["Octant"])-1,"update"] = counts

      for x,y in zip(range(0,8),q_list):
        df.loc[x,"Octant_num"] = y
    
      for x,y in zip(range(0,8),q_list):
        df.loc[x,"Longest Subsequence Length"] = get_max_count(df,y)
    
      for x,y in zip(range(0,8),q_list):
        df.loc[x,"Count"] = count_of_max_count(df,y)
    
      df["-"] = " "
      for x,y in zip(range(0,8),q_list):
        get_time_range(x,df,df.loc[x,"Longest Subsequence Length"],y,df.loc[x,"Count"])
    
      df.drop(['update'],axis=1,inplace=True)
      df_xlsx = to_excel(df)
      st.download_button(label='📥 Download Current Result',
                            data=df_xlsx ,
                            file_name= 'df_test.xlsx')
from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


proj_octant_gui()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
