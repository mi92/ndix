# ndix ✨ 

An ultra-lightweight solution for **nested dictionaries** that are both 
- arbitrarily *deep*, 
- while having a *pretty* representation.

Usage:  

```$ pip install ndix``` 

Import:  
```>>> from ndix import Dict ``` 

Initialize nested dict:  
```>>> d = Dict.nest()``` 

Populate dict with arbitrary nesting:  
```>>> d['first']['second']['third']['fourth']['fifth'] = 100 ``` 

The result: ```>>> d ```      
``` {'first': {'second': {'third': {'fourth': {'fifth': 100}}}}} ```






