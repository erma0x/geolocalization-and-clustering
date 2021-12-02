import sys
main_path =sys.path[0]
path_map_img = main_path+"/img/only-map/"
path_to_save_imgs = main_path+"/img/map-with-points/"

cities = { 'PD1':{'map_path':path_map_img+'padova.png',  
                                     'lat_max':45.4476,
                                     'lat_min':45.3657,
                                     'lng_max':11.9868,
                                     'lng_min':11.7942,
                     
                     'coordinate_store':{'lat':43.412749,
                                         'lng':11.919453
                                        },
                     'city_name':'padova'
                    },
      
                       
          'UD24':{'map_path':path_map_img+'udine.png',
                                     'lat_max':46.1543,
                                     'lat_min':45.9926,
                                     'lng_max':13.3889,
                                     'lng_min':13.0895,

                     'coordinate_store':{'lat':45.110771,
                                         'lng':13.226971
                                        },
                    'city_name':'udine'
          
                 }
         
         }
