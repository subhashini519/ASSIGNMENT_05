class Point():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sq_sum(self):
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
    
point_instance = Point(1,2,3)
result = point_instance.sq_sum()
print(f"The sum of squares of three nos is {result}")