# ndix ✨ 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ndix)
![PyPI](https://img.shields.io/pypi/v/ndix)

A lightweight solution for **nested dictionaries** that are both 
- arbitrarily *deep*, 
- while having a *pretty* representation.

Usage:  

```$ pip install ndix``` ( or ```$ poetry add ndix``` ) 


Initialize nested dict:  
```python
from ndix import Dict
d = Dict.nest()

# Populate dict with arbitrary nesting:  
d['first']['second']['third']['fourth']['fifth'] = 100 

# check d:
d 
>>> {'first': {'second': {'third': {'fourth': {'fifth': 100}}}}}
```






