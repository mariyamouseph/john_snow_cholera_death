#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D


sns.set(style='whitegrid', palette='pastel', color_codes=True) 
sns.mpl.rc('figure', figsize=(10,6))


#opening the vector map
shp_path = 'D:\DataAnalysis\Mariyam\John Snow\Replotted\Pumps.shp'
#reading the shape file by using reader function of the shape lib
sf = shp.Reader(shp_path)


def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' 
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df


df = read_shapefile(sf)


#opening the vector map
shp_path_2 = 'D:\DataAnalysis\Mariyam\John Snow\Replotted\Cholera_Deaths.shp'
#reading the shape file by using reader function of the shape lib
sf2 = shp.Reader(shp_path_2)

df2 = read_shapefile(sf2)

# In[21]:


def plot_map_final(sf, df2, x_lim = None, y_lim = None, figsize = (11,9)):
    '''
    Plot map with lim coordinates
    '''
    plt.figure(figsize = figsize)
    
    id=0    
    for coord in df2['coords']:
        x = coord[0][0]
        y = coord[0][1]
        plt.plot(x, y, color='green', linestyle='dashed', marker='o',
     markerfacecolor='red', markersize=df2.iloc[[id]]['Count']*2, label="Deaths")
        id=id+1
        
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, color='green', linestyle='dashed', marker='D',
     markerfacecolor='blue', markersize=12,label="Pump")
    
    colors = ['red', 'blue']
    lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='-') for c in colors]
    labels = ['Deaths', 'Pump']
    plt.legend(lines, labels)
    plt.tight_layout()
    plt.savefig('Cholera_Deaths.png')
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim)


# In[26]:


plot_map_final(sf,df2)





