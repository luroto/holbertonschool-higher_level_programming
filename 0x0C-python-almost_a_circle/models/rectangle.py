
from .base import Base


class Rectangle(Base):
    """ This is the class Rectangle, which inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for the Rectangle class"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ancho = self.__width
        alto = self.__height
        return(ancho * alto)

    def display(self):
        ancho = self.__width
        alto = self.__height
        corre = self.__x
        prof = self.__y
        i = 0
        j = 0
        al = 0
        for al in range(prof):
            print()
        for i in range(alto):
            for j in range(ancho + corre):
                if j < corre:
                    print("{}".format("  "), end="")
                else:
                    print("{}".format('#'), end="")
            print()

    def __str__(self):
        rec = "[Rectangle] "
        sid = str(self.id)
        equis = str(self.__x)
        div = "/"
        parent = "("
        pars = ")"
        ygriega = str(self.__y)
        ancho = str(self.__width)
        alto = str(self.__height)
        retos = (rec + parent + sid + pars + " " + equis + div + ygriega +
                 " " + "-" + " " + ancho + div + alto)
        return(retos)
