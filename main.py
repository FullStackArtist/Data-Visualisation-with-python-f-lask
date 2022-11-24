from flask import Flask, render_template,Response,request,flash, request, redirect, url_for
import psutil
app = Flask(__name__)
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#from werkzeug import secure_filename
from PIL import Image

df=pd.DataFrame()
bdf=pd.DataFrame()
d=pd.DataFrame()
n=[]
m=[]
hd=[]

UPLOAD_FOLDER = 'C:/Users/USER/Documents/flask/flask0/chart/tdata'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def img():
    image_path = "static/Chart.png"
    image_file = Image.open(image_path)
  
# the default
    image_file.save("static/qChart.png", quality=95)

def flat(lis):
    flatl = []
    # Iterate with outer list
    for elem in lis:
        for i in elem:
            flatl.append(i)
    return flatl

def line(list):
    bdf=df[list[0:len(list)-1]]
    bd=bdf.groupby([list[0]]).sum().reset_index()
    xl=bd[[list[0]]]
    yl=bd[[list[1]]]
    print("---------------")
#print(type(xl))
    rx=xl.values.tolist()
    cy=yl.values.tolist()
    r=flat(rx)
    y=flat(cy)
    x=np.asarray(r)
    y=np.asarray(y)
    print("---------------")
    plt.style.use('seaborn-darkgrid')
    palette = plt.get_cmap('Set1')
 
# Plot multiple lines
    plt.plot(x, y, marker='', linewidth=1, alpha=0.9)

# Add legend
    plt.legend(loc=2, ncol=2)
 
# Add titles
    plt.title("A (bad) Spaghetti plot", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel(list[0])
    plt.ylabel(list[1])

    plt.title('Line Chart for '+list[0]+"/"+list[1])
    plt.savefig('static/Chart.png')


def donut(list):
    bdf=df[list[0:len(list)-1]]
    bd=bdf.groupby([list[0]]).sum().reset_index()
    xl=bd[[list[0]]]
    yl=bd[[list[1]]]
    print("---------------")
#print(type(xl))
    rx=xl.values.tolist()
    cy=yl.values.tolist()
    r=flat(rx)
    y=flat(cy)
    x=np.asarray(r)
    y=np.asarray(y)
    print("---------------")
    plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')  
    plt.tight_layout()
    plt.title('Donut Chart for '+list[0]+"/"+list[1])
    plt.savefig('static/Chart.png')

def bar(list):
    bdf=df[list[0:len(list)-1]]
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
    plt.figure(figsize=(14,9.5))
    print("---------------")
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.title('Bar Chart for '+list[0]+"/"+list[1])
    plt.savefig('static/Chart.png')

def pie(list):
    explode = [0.1]
    bdf=df[list[0:len(list)-1]]
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
    for i in range(1,len(x)):
        explode.append(0)
    explode=tuple(explode)
    #plt.figure(figsize=(14,9.5))
    ax.pie(y, explode=explode, labels=x, autopct='%1.1f%%',radius=1500,shadow=False, startangle=90)
    ax.axis('equal')  
    plt.tight_layout()
    plt.title('Pie Chart for '+list[0]+"/"+list[1])
    plt.savefig('static/Chart.png')


def histogram(list):
    bdf=df[list[0:len(list)-1]]
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
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
   
# Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
 
# Add x, y gridlines
    ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
    N, bins, patches = axs.hist(x, bins = len(x))
    racs = ((N**(1 / 5)) / N.max())
    norm = colors.Normalize(fracs.min(), fracs.max())
 
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
 
# Adding extra features   
    plt.xlabel(list[0])
    plt.ylabel(list[1])
    plt.title(' Customized histogram '+list[0]+" / "+list[1])
    plt.savefig('static/Chart.png')
    
    
@app.route('/')
def main():
    m.clear()
    n.clear()
    return render_template("main.html")


def call(list):
    if list[-1]=="Donut":
        donut(list)
    elif list[-1]=="Bar":
        bar(list)
    elif list[-1]=="Pie":
        pie(list)
    elif list[-1]=="Histogram":
        histogram(list)
    

@app.route('/chart',methods=['POST','GET'])
def chart():
    data=request.form
    list = [(v) for k, v in data.items()]
    print(list)
    call(list)
    img()
    return render_template('chart.html',val=list[-1])

@app.route('/index',methods=['GET', 'POST'])
def index():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if 'files' not in request.files:
        #flash('Please upload a file ')
        print("First")
        #return render_template("index.html")
    print("-----------------------------------------------")
    #f=request.files.get('files')
    #print(f)
    
    """if file.filename == '':
        print("Second")
       #flash('No selected file')
       
        return render_template("index.html")"""
    """if file :
        print("Third")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df=pd.read_csv(file)
        hd=df.head
        return render_template('index.html',Df=df,Hd=hd)"""

    
    f =request.files['file']
    #filename = f.filename
    filename=secure_filename(f.filename)
    #f=os.path.join(app.instance_path, 'file', "Sample.csv")
    #fil.save(f1)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    old_name="C:/Users/USER/Documents/flask/flask0/chart/tdata/"+filename
    new_name="C:/Users/USER/Documents/flask/flask0/chart/tdata/"+'Sample.csv'
    os.rename(old_name,new_name)
    global df
    df=pd.read_csv('tdata/Sample.csv',sep=",", index_col=False, encoding='Latin-1')
    

    

    global n
    global m
    global hd
    hd=df.columns.values.tolist()
    for i in hd:
        try:
            int(df[i][2])
        #print("int")
            n.append(i)
        except:
        #print("string")
            m.append(i)
    print(hd)

    return render_template('index.html',HD=m,HM=n)
    #return render_template('index.html')
if __name__  == "__main__":
    app.run(debug=True)





