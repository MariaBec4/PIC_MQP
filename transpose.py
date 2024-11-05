import pandas as pd;
import os;
from scipy.optimize import curve_fit

folder_path1 = r"/Users/maria/Downloads/NCMS_Chip1_10_28_24/Old_Data"
folder_path2 = r"/Users/maria/Downloads/NCMS_Chip1_10_28_24/Data"

for i in range(1,7):
    data = pd.read_csv(f'{folder_path1}/Loopback{i}_TE_1547-1553.csv', skiprows = 16)
    datanew = data.transpose()
    df = pd.DataFrame(datanew)
    string = f'{folder_path2}/LoopBack{i}_TE_1547-1553.csv'
    df.to_csv(string)

    data = pd.read_csv(f'{folder_path1}/Loopback{i}_TM_1547-1553.csv', skiprows = 16)
    datanew = data.transpose()
    df = pd.DataFrame(datanew)
    string = f'{folder_path2}/LoopBack{i}_TM_1547-1553.csv'
    df.to_csv(string)

for i in range(1,19):
    data = pd.read_csv(f'{folder_path1}/Ring{i}_TE_1547-1553.csv', skiprows = 16)
    datanew = data.transpose()
    df = pd.DataFrame(datanew)
    string = f'{folder_path2}/Ring{i}_TE_1547-1553.csv'
    df.to_csv(string)

    data = pd.read_csv(f'{folder_path1}/Ring{i}_TM_1547-1553.csv', skiprows = 16)
    datanew = data.transpose()
    df = pd.DataFrame(datanew)
    string = f'{folder_path2}/Ring{i}_TM_1547-1553.csv'
    df.to_csv(string)