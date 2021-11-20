
# 1 .A complex number is a number that can be expressed in the form a + bi,where a and b are real numbers and i is the imaginary unit.
# Create class Complex with attributes, constructors and getters/setters.

class Complex:

    def __init__(self,a_r_n, b_r_n, i_img_n):
        self.__a_r_n = a_r_n
        self.__b_r_n = b_r_n
        self.__i_r_n = i_img_n

    def set(self):
        self.__a_r_n = self.__a_r_n
        self.__b_r_n = self.__b_r_n
        self.__i_r_n = self.__i_r_n
    def get(self):
        return self.__a_r_n, self.__b_r_n, self.__i_r_n
    def display(self):
        print("a_r_n: ", self.get())
        print("b_r_n :", self.get())
        print("i_img_n :", self.get())


C = Complex(2,3,8)
C.display()




