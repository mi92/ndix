from collections import defaultdict

class Dict(defaultdict):
    """
    This class is built around defaultdict, with the following two added features:
        1. arbitrarily deep nesting of the nested dictionary, while still having a  
        2. pretty representation of the dictionary object (as compared to nested function names) 
    """
    def __init__(self, *args, **kwargs):
        defaultdict.__init__(
            self,
            *args, 
            **kwargs)

    def __repr__(self):
        return str(dict(self)) 

    @classmethod
    def nest(self):
        return Dict(lambda: Dict(Dict.nest))


if __name__ == "__main__":
    
    # Example usage: 
    d = Dict.nest()

    d['first']['second']['third']['fourth']['fifth'] = 100 

    print(d)
