import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import seaborn as sns

fig, ax = plt.subplots()
df=pd.read_csv('tdata/Sample.csv',sep=",", encoding='Latin-1')
hd=df.columns.values.tolist()
def flat(lis):
    flatl = []
    # Iterate with outer list
    for elem in lis:
        for i in elem:
            flatl.append(i)
    return flatl
list=['QUANTITYORDERED', 'SALES']

def histogram(list):
    bdf=df[list[0:len(list)]]
    bd=bdf.groupby([list[0]]).sum().reset_index()
    #bdf.reset_index(drop=True)
    #fd=df.groupby(list[0:len(list)-1])
    xl=bd[[list[0]]]
    yl=bd[[list[1]]]
    rx=xl.values.tolist()
    cy=yl.values.tolist()
    r=flat(rx)
    y=flat(cy)
    x=np.asarray(r)
    y=np.asarray(y)

   
 
# Add x, y gridlines
    ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
    N, bins, patches = ax.hist(y, bins = len(x))
    racs = ((N**(1 / 5)) / N.max())
    #print(racs,N,bins)
    norm = colors.Normalize(racs.min(), racs.max())
    for thisfrac, thispatch in zip(racs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
 
# Adding extra features

    plt.xlabel(list[0])
    plt.ylabel(list[1])
    plt.title(' Customized histogram '+list[0]+" / "+list[1])
    plt.show()
histogram(list)
