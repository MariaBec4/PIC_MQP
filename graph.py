import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.optimize import curve_fit


num = 5
mode = "TM"

rr = pd.read_csv(f'/Users/maria/Downloads/NCMS_Chip1_10_28_24/Data/Ring{num}_{mode}_1547-1553.csv', skiprows = 1, delimiter=',')

#/Users/maria/Downloads/NCMS_Chip1_10_28_24/Data/Ring1_TE_1547-1553.csv

plt.xlabel("Wavelength [nm]")
plt.ylabel("Transmission [dB]")
plt.title(f"Transmission vs. Wavelength of Ring {num} in {mode}")

plt.scatter(rr["wavelength"], rr["channel_4"])

#plt.savefig(f'/Users/maria/Downloads/NCMS_Chip1_10_28_24/Raw_Graphs/Ring{num}_{mode}_1547-1553.png')

plt.show()