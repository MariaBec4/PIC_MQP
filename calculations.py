import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.optimize import curve_fit

# Import Ring Resonator Data
folder_path = r"/Users/maria/Downloads/NCMS_Chip1_10_28_24/Data/"
num = 5
mode = "TE"

rr = pd.read_csv(f'{folder_path}Ring{num}_{mode}_1547-1553.csv', skiprows = 1,delimiter=',')


# Append wavelength and transmission to two lists (make sure transmission isn't negative)
wavelength = rr["wavelength"]
power = rr["channel_4"]
base = -26.5 #base power when there's no resonance
# This block of code identifies peaks in the data
j = 0
scatter = [0]
scatterwave = [0]
matrixwave = []
matrixscatter = []
for i in range(len(power)):
    if power[i] > base:
        scatterwave.append(wavelength[i])
        scatter.append(power[i])


#This block of code seperates the peaks and their data points into seperate rows of a matrix
newwave = []
newpower = []
for i in range(1,len(scatterwave)-1):
    newpower.append(scatter[i]) #appending the ith resonance to newpower and newwave
    newwave.append(scatterwave[i])
    if scatterwave[i + 1] - 0.05 > scatterwave[i]:
        j += 1
        matrixwave.append(newwave)
        matrixscatter.append(newpower)
        newwave = []
        newpower = []

"""        
#Defining Lorentzian
def lorentz(x,mu,g,a):
    result = g/((x-mu)**2 + g**2)
    return a*result + base

#Fitting Lorentzian to each peak in the matrix 
#Unfortunately, non-linear least squares method requires a fairly accurate guess to fit to the peaks.
guess1 = "Insert approx FWHM"
guess2 = "Insert approx normalisation factor"
guess3 = base
qfactor = []
for i in range(j):
    pars,cov = curve_fit(lorentz,matrixwave[i],matrixscatter[i],p0=[np.mean(matrixwave[i]),guess1,guess2,guess3])
    plt.scatter(np.arange(matrixwave[i][0],matrixwave[i][-1],0.0001),-lorentz(np.arange(matrixwave[i][0],matrixwave[i][-1],0.0001),*pars),color='blue',marker='.')
    freq = pars[0]
    fwhm = 2*pars[1]
    q = freq/fwhm
    ferr = np.sqrt(cov[0][0])
    herr = 2*np.sqrt(cov[1][1])
    err = q*np.sqrt((ferr/freq)**2 + (herr/fwhm)**2)
    qfactor.append([q,pars[0],err])
    
        
fsr = []
for i in range(2,j):
    fsr.append(qfactor[i][1] - qfactor[i-2][1])
    
        


plt.xlabel("Wavelength (nm)")
plt.ylabel("Power (dBm)")
plt.title("Title")
plt.grid()
"""
