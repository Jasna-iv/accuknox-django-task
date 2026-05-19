class Box:
 
    def __init__(self, height: int, breadth: int):
 
        self.height = height
        self.breadth = breadth
 
    def __iter__(self):
 
        yield {"height": self.height}
        yield {"breadth": self.breadth}
 
 
# Testing
 
shape = Box(20, 8)
 
for item in shape:
 
    print(item)