class Circulo:

    def __init__(self, value):
        """
         Inits the class
         >>> c = Circulo(-1)
         Only values > 0
         >>> c = Circulo("a")
         Only number are accepted
         >>> c = Circulo(3)
         El perimetro es: 18.84 y el area es:28.26
         """
        try:
            if int(value) <= 0:
                print ValueError("Only values > 0")
            else:
                print ("El perimetro es: %.2f y el area es:%.2f"
                       % (self.get_perimetro(value), self.get_area(value)))
        except ValueError:
            print ValueError("Only number are accepted")

    def get_area(self,value):
        """
               Calculate the area of an circle
               >>> c = Circulo(3)
               El perimetro es: 18.84 y el area es:28.26
               >>> c.get_area(3)
               28.26
               """
        result = 3.14 * (value) ** 2
        return result

    def get_perimetro(self,value):
        """
               Calculate the perimeter of an circle
               >>> c = Circulo(3)
               El perimetro es: 18.84 y el area es:28.26
               >>> c.get_perimetro(3)
               18.84
               """
        result = 2 * 3.14 * value
        return result

import doctest
doctest.testmod()

Circulo()