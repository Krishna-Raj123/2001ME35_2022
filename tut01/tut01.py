def octact_identification(mod=5000):
import pandas as pd
df = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\New folder\2001ME35_2022\tut01\octant_input.csv")
x = df.shape[0]
df.head(15)


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)