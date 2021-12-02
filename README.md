# Customers clustering

DISCLAIMER! 
For privacy IP data are omitted on the .csv file

## Customers geolocalization and clustering for advertisement optimization
Project to identify the "hot-zone" of the cities where customers watch the site.
With this analysis the store can optimize the distribution of advertisement.

The project use Machine Learning to identify clusters of customers based on geolocalization areas.
The Machine Learning algorithm used is agglomerative clustering, a sub class of hierarchical clustering.

## Usage
You can run the file .ipynb alone or run the geolock_script.py. 

1. Download the map of the zone you need to analyze. Download the map as .png into the /img/map-only/ folder.
   Remember the max/min latitude and longitude of the map for the second step.
3. In both, you will need to update your data structure contained in data_cities with the new map data, 
    such as: the name of the file .png, the max and the min of the latitude and longitude map that you downloaded.
3. Start the script or the notebook.


### If you use  __client_geolocalization_and_clustering.ipynb__
  
  This file it's a Notebook that explain each step, and can visualize inline the results.
  It useful to uderstand the process of the algorithm for the data extraction and visualization.
  
### If you use __geolock_script.py__ 
  
  It's a script that import __data_cities.py__ for the data of the different cities.
  with this script you have choice for interact through the terminal and insert the different
  options of the script, such as the name of the city and the number of the cluster.
  
  
  
Each python file/notebook have automatic save for the images in a determinate path in the project directory.



### Args
/GeoLock$ python3 geolock.py -s PD1 -c 4
 
### Output
  Your image has been saved to 
 /home/localhost/Desktop/GeoLock/img/map-with-points/ 


### Help
/GeoLock$ python3 geolock.py -h

### Output
usage: geolock3.py [-h] -s  -c

Generate client cluster map

optional arguments:
  -h, --help       show this help message and exit
  -s , --store     Code Store
  -c , --cluster   Number of Clusters
  
