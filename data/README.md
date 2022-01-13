# Data

This folder contains the datafiles. <br>
They are provided into txt, zip or serialized format (pickling).

## Folder contents

**data_21_1947** contains the observations of 21 observatories/stations over the years 1947-2013. 

This file is composed of:

* _Ns_ : number of sunspots
* _Ng_ : number of sunspot groups
* _Nc_ : composites (Ns + 10Ng)
* _station_names_ : codenames of the stations
* _time_ : index of time, expressed in fraction of years 
    

**data_1981** contains the observations of the entire network (of ~278 stations) over the years 1981-2019. 

This file is composed of:

* _Ns_ : number of sunspots
* _Ng_ : number of sunspot groups
* _Nc_ : composites (Ns + 10Ng)
* _station_names_ : codenames of the stations
* _time_ : index of time, expressed in fraction of years 
 

**kisl_wolf** contains the data of the station KS (Kislovodsk) over the years 1954-2020, which are partly missing from the database. 
The three first columns of the file correspond to the datetime of the observations. 
The fourth column (labelled 'W') contains the composite (Nc) of the station. The other columns are not used in this analysis. <br>

## Instructions

The files in serialized format (**data_21_1947** and **data_1981**)  can be opened with the module 
[pickle](https://docs.python.org/3/library/pickle.html) (with appropriate path): 

````
with open('data_21_1947', 'rb') as file:
     my_depickler = pickle.Unpickler(file)
     Ns = my_depickler.load() 
     Ng = my_depickler.load() 
     Nc = my_depickler.load() 
     station_names = my_depickler.load() 
     time = my_depickler.load() 
     
with open('data_1981', 'rb') as file:
     my_depickler = pickle.Unpickler(file)
     Ns = my_depickler.load() 
     Ng = my_depickler.load() 
     Nc = my_depickler.load() 
     station_names = my_depickler.load() 
     time = my_depickler.load() 
     
````




