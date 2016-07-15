class Vector(object):
    def plus(self , v):
        new_coordinates = [x+y for x,y in zip(self.coordinates , v.coordinates)]
        return Vector(new_coordinates)
    
    def minus(self , v):
        new_coordinates = [x-y for x,y in zip(self.coordinates , v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self , c ):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    
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
    

v = Vector([1.671 , -1.012,-0.318])
w = Vector([-8.223 ,0.878])
c = 7.41
print v.times_scalar(c)

