# Write __str_() method to print the vector as follows:
#  7i + 8j + 10k

class Vector:
    def __init__(self, i, j, k):
        """
        Initialize the vector with its components.
        :param i: The i component of the vector
        :param j: The j component of the vector
        :param k: The k component of the vector
        """
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        """
        Return the vector in the format '7i + 8j + 10k'.
        :return: A string representation of the vector
        """
        return f"{self.i}i + {self.j}j + {self.k}k"

# Create an instance of the Vector class
vector = Vector(7, 8, 10)

# Print the vector
print(vector)
