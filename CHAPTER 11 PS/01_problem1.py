# Create a class ( 2- D vector) and use it to create another class representing a 3-D vector.

class TwoDVector:
    def __init(self, i, j):
        self.i = i 
        self.j = j

        def show(self):
            print(f"The vector is {self.i} + {self.j}")

            class ThreeDVector(TwoDVector):
                def __init__(self, i, j, k):
                    super().___init__(i ,j)
                    self.k =k

                    def shiw(self):
                        print(f"The vector is{self.i}i + {self.j}j + {self.k}k")


a = TwoDVector(1,2)
a.show()
b = ThreeDVector(5 , 2, 3)
b.show