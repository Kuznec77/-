class Horse:
    def __init__(self):
        self.sound = 'Frrr'
        super().__init__()
        self.x_distance = 0

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'
        self.y_distance = 0

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):

    def __init__(self):
         super().__init__()

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):    # печатает значение унаследованного атрибута sound.
        print(self.sound)

pegasus1 = Pegasus()
#print(Pegasus.mro())
print(pegasus1.get_pos())
pegasus1.move(12, 6)
print(pegasus1.get_pos())
pegasus1.move(-3, 6)
print(pegasus1.get_pos())
pegasus1.voice()
