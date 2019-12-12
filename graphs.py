"""
    take a files.csv with results of db
                            J-code
"""
from carga_Array import columnaToArray
import matplotlib.pyplot as plt
import pandas as pd
import folium #to geomaps
import seaborn as sns
import numpy as np

def donutGraph(categories,size):
    # create a figure and set different background
    fig = plt.figure()
    fig.patch.set_facecolor('black')
    # Change color of text
    plt.rcParams['text.color'] = 'white'
    # Create a circle for the center of the plot to make this more cute
    my_circle = plt.Circle((0, 0), 0.7, color='black')
    # Pieplot + circle on it
    plt.pie(size, labels=categories)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()

def DotsAndLines():
    # Make a data frame
    df = pd.DataFrame({'x': range(1, 11),
                       'y1': np.random.randn(10),
                       'y2': np.random.randn(10) + range(1, 11),
                       'y3': np.random.randn(10) + range(11, 21),
                       'y4': np.random.randn(10) + range(6, 16),
                       'y5': np.random.randn(10) + range(4, 14) + (0, 0, 0, 0, 0, 0, 0, -3, -8, -6),
                       'y6': np.random.randn(10) + range(2, 12),
                       'y7': np.random.randn(10) + range(5, 15),
                       'y8': np.random.randn(10) + range(4, 14)})

    # plt.style.use('fivethirtyeight')
    #plt.style.use('seaborn-darkgrid')
    #my_dpi = 96
    #plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)

    # multiple line plot
    for column in df.drop('x', axis=1):
        plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.4)

    # Now re do the interesting curve, but biger with distinct color
    plt.plot(df['x'], df['y5'], marker='', color='orange', linewidth=4, alpha=0.7)
    # Change xlim
    plt.xlim(0, 12)
    # Let's annotate the plot
    num = 0
    for i in df.values[9][1:]:
        num += 1
        name = list(df)[num]
        if name != 'y5':
            plt.text(10.2, i, name, horizontalalignment='left', size='small', color='grey')

    # And add a special annotation for the group we are interested in
    plt.text(10.2, df.y5.tail(1), 'Mr Orange', horizontalalignment='left', size='small', color='orange')

    # Add titles
    plt.title("Evolution of Mr Orange vs other students", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Time")
    plt.ylabel("Score")
    plt.show()

def cakeGraph(categories,size):
    # create a figure and set different background
    fig = plt.figure()
    fig.patch.set_facecolor('black')
    # Change color of text
    plt.rcParams['text.color'] = 'white'
    # Pieplot + circle on it
    plt.pie(size, labels=categories)
    plt.show()

def barGraph(bars,height):
    # Choose the height of the bars
    # Choose the names of the bars
    y_pos = np.arange(len(bars))
    # Create bars
    plt.bar(y_pos, height)
    # Create names on the x-axis
    plt.xticks(y_pos, bars, color='orange')
    plt.yticks(color='orange')
    # Show graphic
    plt.show()

def stackAreaGraph(categories,width):
    # test:
    #categorires = range(1, 6)
    #width = [[2, 4, 6, 8, 10], [5, 5, 5, 5, 5], [9, 9, 9, 9, 10]]
    plt.stackplot(categories,witdh, labels=['A', 'B', 'C'])
    plt.legend(loc='upper left')
    plt.show()

def bubbleGraph():
    # create data
    x = np.random.rand(15)
    y = 2 + x
    z = x + np.random.rand(15)
    z = z * z
    # Change color with c and alpha. I map the color to the X axis value.
    plt.scatter(x, y, s=z * 2000, c=x, cmap="Blues", alpha=0.4, edgecolors="grey", linewidth=2)
    # Add titles (main and on axis)
    plt.xlabel("the X axis")
    plt.ylabel("the Y axis")
    plt.title("A colored bubble plot")
    plt.show()


def cleanOutput(arr):
    for i in range(len(arr)):  # clean output
        pass
    arr[i] = arr[i].replace("\n", "")


"""
# Data categories   
file = "results/RcategoriasNameViews.csv"
categories = columnaToArray(1,file)
print(categories)

for i in range(len(categories)): # clean output
    categories[i] = categories[i].replace("\n", "")
#this is a result o print, maybe i have this convert the list to string ...
categories = 'Film & Animation', 'Autos & Vehicles', 'Music', 'Pets & Animals', 'Sports', 'Travel & Events', 'Gaming', 'People & Blogs', 'Comedy', 'Entertainment', 'News & Politics', 'Howto & Style',\
             'Education', 'Science & Technology', 'Shows'
#size = columnaToArray(0,file)
size = '461919619', '49190861', '4159713283', '45629022', '1389337978', '15413050', '421961773', '1229501908', '794647488', '4027574336', '491449042', '465587429', '43205309', '202863454', \
       '65436',
donutGraph(categories,size)
"""
"""
file = "results/canalesNoticias2.csv"
chanels = columnaToArray(1,file)
chanels = cleanOutput(chanels)
chanels.append("")
print(chanels)
chanels = 'Noti7', 'Noticias Mix', 'AFmedios Noticias de Colima', \
          'Noticiero Mundial News', 'Noticias Reales TV', 'Reality Noticias y mas', \
          'NOTICIAS EN ESPAÃ‘OL', 'DCNoticias', 'Noticias Youtube con Regina Blue y Ax Mode O','Parecen Noticias Extra',

views = columnaToArray(0,file)
views = cleanOutput(views)
print(views)
views = '1347705', '852390', '652239', '637506', '632995', '624684', '420675', '307765', '219617', '195128',
##data = {'canales':chanels,'views':views}
cakeGraph(chanels,views)
"""