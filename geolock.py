""" 
   Ｇｅｏｌｏｃａｌｉｚａｔｉｏｎ

# What does he do
The code generates a point map.
The points represent the customers of the shops,
when they visit the website
that have active geolocation.

Points can be grouped into 'clusters'
that is groups optimized by the algorithm for
highlight large customer conglomerates
within a city map.


# How to expand the number of maps available
Maps must be insered manually inside
 /img/only-map/

Within the data_cities.py file
the 4 coordinates must be written
to match the downloaded map (eg OpenStreetMap),
with coordinates the map of geolocated customers.

"""
import argparse # parse input

import sys # system operations

import pandas as pd # data Extract Transform Load
import numpy as np # linear algebra

import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # plotting


# machine learning libs
from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc

from data_cities import cities # Data of the Map
from data_cities import  path_map_img, path_to_save_imgs # path

parser = argparse.ArgumentParser(description='Generate client cluster map')
parser.add_argument('-s', '--store',type=str, metavar='', required=True, help=' Code Store ')
parser.add_argument('-c', '--cluster',type=int, metavar='', required=True, help=' Number of Clusters')

args = parser.parse_args()

code_store = args.store 
n_clusters = args.cluster

data_cities=cities

main_path =sys.path[0]
path_data ="/data_geovisitors/onlygeo_with_ip.csv"
df = pd.read_csv(main_path+path_data,';')

# DF
# change columns name
df[df.columns[0]] = 'date'
df[df.columns[1]] = 'time'
df[df.columns[2]] = 'geolock'

def code_store_to_name_city(cities_=cities,code_store_=code_store):
    city_name=cities_[code_store]['city_name']
    return city_name


def extract_boundries(cities=cities,code_store_=code_store):
    """
    extract latitude and longitude min/max
    from the data set with dictionary keys
    """
    lat_min = cities[code_store_]['lat_min']
    lat_max = cities[code_store_]['lat_max']
    lng_max = cities[code_store_]['lng_max']
    lng_min = cities[code_store_]['lng_min']
    
    return([lat_max,lat_min,lng_max,lng_min])

def create_bbox(boundries):
    """ BBox serves for the plotting size figures"""
    BBox = ((boundries[3], boundries[2],      
             boundries[1], boundries[0]))
    return BBox

def filter_df(df,code_store, data_cities):
    """filter dataframe with boundries of the city zone
       that you select with the arguments on the terminal
    """   
    boundries=extract_boundries(data_cities,code_store)
    df_filtered = df[ 
                (df['LAT']< boundries[0]) &
                (df['LAT']>= boundries[1]) &
                (df['LNG']< boundries[2]) &
                (df['LNG']>= boundries[3])]
    
    df_filtered2 = df_filtered[['LAT', 'LNG']]
    return df_filtered2


def hierarchical_clustering(code_store,df,data_cities,N_cluster):

    # machine learning
    cluster = AgglomerativeClustering(n_clusters= n_clusters, affinity='euclidean', linkage='ward')  
    cluster.fit_predict(df)
    

    # PLOT
    plt.figure(figsize=(50, 20))

    # SETTINGs
    point_dimention = 4   # [ 0.1 - 100 ]
    opacity = 0.8         # [ 0.01 - 1 ]
    
    # store coordinates
    X_store_coordinates = data_cities[code_store]['coordinate_store']['lng']
    Y_store_coordinates = data_cities[code_store]['coordinate_store']['lat']

    # load background img
    IMG=plt.imread(path_map_img+code_store+'.png')
    
    # create figure
    fig, ax = plt.subplots()
    
    # plot
    ax.scatter(np.array(df['LNG']),np.array(df['LAT']),
              alpha= opacity , c=cluster.labels_,
              cmap='gist_rainbow_r',marker='o', s = point_dimention)
    
    ax.scatter(X_store_coordinates,Y_store_coordinates, c ='r', s=30)

    # set boundries
    boundries = extract_boundries(data_cities,code_store)
    bbox = create_bbox(boundries)
    
    # set figure boundries
    ax.set_xlim(bbox[0],bbox[1])
    ax.set_ylim(bbox[2],bbox[3])
    
    # estetics
    plt.title(" Clusters of client map of {0} ".format(code_store[:1].upper()+code_store[1:]))
    plt.xlabel('longitude')
    plt.ylabel('latitude')

    # show
    ax.imshow(IMG, zorder=0, extent = bbox, aspect= 'auto')
     
    # save
    fig.savefig(path_to_save_imgs+code_store+'_cluster.png', dpi=1200, bbox_inches='tight')
    
    
def main():
    dataframe=filter_df(df, code_store, data_cities)
    hierarchical_clustering(code_store,dataframe,cities,n_clusters)
            

if __name__ =='__main__':
    main()
    print(' \n Your image has been saved to \n {0} '.format(path_to_save_imgs))

