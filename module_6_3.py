class Horse:            
    x_distance = 0      
    _sound = 'Frrr'     

    def run(self, dx):  
        self.x_distance += dx

class Eagle:            
    y_distance = 0      
    sound = 'I train, eat, sleep, and repeat' 

    def fly(self, dy):  
        self.y_distance += dy

class Pegasus(Horse, Eagle):  

    def __init__(self):
         self.sound = super()._sound
         self.sound = super().sound

    def move(self, dx, dy):   
        self.run(dx)
        self.fly(dy)

    def get_pos(self):  
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):   
        print(self.sound)

pegasus1 = Pegasus()
#print(Pegasus.mro())
print(pegasus1.get_pos())
pegasus1.move(12, 6)
print(pegasus1.get_pos())
pegasus1.move(-3, 6)
print(pegasus1.get_pos())
pegasus1.voice()
