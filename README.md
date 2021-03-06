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


### If you use  __geolocalization_and_clustering.ipynb__
  
  This file it's a Notebook that explain each step, and can visualize inline the results.
  It useful to uderstand the process of the algorithm for the data extraction and visualization.
  
### If you use __geolock.py__ 
  
  It's a script that import __data_cities.py__ for the data of the different cities.
  with this script you have choice for interact through the terminal and insert the different
  options of the script, such as the name of the city and the number of the cluster.
  
  
  
Each python file/notebook have automatic save for the images in a determinate path in the project directory.

### Configurations
#### Map Configuration
1. insert your dataset .csv or .txt inside data/ <br>
	The data shuold be like this: <br>
	LAT,LNG <br>
	45.7787739,12.0604744 <br>
	45.77895,12.0606032 <br>
2. Map Configuration
	- insert the map from Google Maps inside data_city
	- insert the the extremes of the map coordinates: 
	  lat_max, lat_min, lng_max, lng_min

#### Path configuration
You can change the input and the output paths manually inside the scrips. 

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

optional arguments: <br>
  -h --help      help <br> 
  -s --store     Code Store  (see data_cities.py) <br>
  -c --cluster   Number of Clusters <br>
  
