class Vector(object):
    def __init__(self , coordinates):
        try :
            if not coordinates :
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates) 
            
        except ValueError:
            raise ValueError('The coordinates can not be empty')
        
        except TypeError:
            raise TypeError('coordinates must be iterable')
        
    def __str__(self):
        return 'Vector:{}'.format(self.coordinates)
    
    def __eq__(self , v ):
        return self.coordinates == v.coordinates 
    

vec = Vector([2,2,3])
print vec

