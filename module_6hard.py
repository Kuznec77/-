import math

from module_6_4 import circle1


class Figure:
    sides_count = 0
    filled = True

    def __init__(self, color):
        if self.__is_valid_color(color):
            self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        for i in color:
            if isinstance(i, int) and i>=0 and i<=255:
                pass
            else:
                return False
            if len(color)==3:
                return True

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color=color

    def set_sides(self, *new_sides):
        if self.check_len(sides):
            self.__sides=new_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def check_len(self,args):
        if len(args)==self.sides_count:
            return True

        else:
            return False

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color)
        if self.check_len(sides):
            self.__sides=sides
        else:
            self.__radius = self.get_radius()

    def set_sides(self, *new_sides):
        if self.check_len(new_sides):
            self.__sides=new_sides

    def get_sides(self):
        return self.__sides
    def get_radius(self):
        return self.__sides[0]/(2*math.pi)
    def get_square(self):
        return math.pi*(self.get_radius()**2)

class Triangle(Figure):
    sides_count=3

    def __init__(self, color, *sides):
        super().__init__(color)
        if self.check_len(sides):
            self.__sides=sides
        else:
            self.__sides=(1,)*3

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.check_len(new_sides):
            self.__sides=new_sides

    def get_square(self):
        sides=self.get_sides()
        p=sum(sides)/2
        s=abs((p*(p-sides[0])*(p-sides[1])*(p-sides[2])))
        s=math.sqrt(s)
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color)
        if self.check_len(sides):
            self.__sides=sides
        elif len(sides)==1:
            self.__sides=(sides[0],)*12
        else:
            self.__sides=(1,)*12

    def set_sides(self, *new_sides):
        if self.check_len(new_sides):
            self.__sides=new_sides
    def get_sides(self):
        return self.__sides
    def get_volume(self):
        return self.get_sides()[0]**3

circlel = Circle((200, 200, 100), 10, 5)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цвета:
circlel.get_color(55, 66, 77) # Изменится
print(circlel.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circlel.set_sides(15) # Изменится
print(circlel.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circlel))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади круга
print(circle1.get_square())

# Проверка площади треугольника
triangle1=Triangle((45,55,75),4,15)
print(triangle1.get_sides())
print(triangle1.get_square())

cube3=Cube((255,280,10),4)

print(cube3.get_sides())














