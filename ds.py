import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('tdata/Sample.csv',sep=",", encoding='Latin-1')
hd=df.columns.values.tolist()
def flat(lis):
    flatl = []
    # Iterate with outer list
    for elem in lis:
        for i in elem:
            flatl.append(i)
    return flatl
list=['COUNTRY', 'QUANTITYORDERED']
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
plt.style.use('seaborn-darkgrid')
 
# Create a color palette
palette = plt.get_cmap('Set1')
 
# Plot multiple lines

plt.plot(x, y, marker='', linewidth=1, alpha=0.9)

# Add legend
plt.legend(loc=2, ncol=2)
 
# Add titles
plt.title("A (bad) Spaghetti plot", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time")
plt.ylabel("Score")

# Show the graph
plt.show()
