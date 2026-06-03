# importing Numpy package 
import numpy as np 

# # creating a Numpy matrix 
n_array = np.array([[ 1, 3,-1, 0, -2],
                    [ 0, 2,-4,-2, -6],
                    [-2,-6, 2, 3, 10],
                    [ 1, 5,-6, 2, -3],
                    [ 0, 2,-4, 5,  9],]) 

# n_array = np.array([[ 3, 3,-3],
#                     [ 3, 4,-4],
#                     [ 2,-3,-5],]) 


# Displaying the Matrix 
print("Numpy Matrix is:") 
print(n_array) 

# calculating the determinant of matrix 
det = np.linalg.det(n_array) 

print("\nDeterminant of given 5X5 matrix:") 
print(int(round(det)))
