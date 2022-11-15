import pandas as pd
    df1=pd.read_csv(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut06\input_attendance.csv")
    df2=pd.read_csv(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut06\input_registered_students.csv")
    for i in range(0,len(df2["Roll No"])):
        cntv=0
        cntnv=0
        for j in range(0,len(df1["Attendance"])):
            if df2.loc[i,'Roll No'] in df1.loc[j,"Attendance"]:
                if "14" in df1.loc[j,"Timestamp"] or "15:00" in df1.loc[j,"Timestamp"] :
                  cntv=cntv+1
                else:
                  cntnv=cntnv +1; 
        df = pd.DataFrame()
        df.loc[1,"Roll"]=df2.loc[i,'Roll No']
        df.to_excel("{0}.xlsx".format(df2.loc[i,'Roll No']),index=False)