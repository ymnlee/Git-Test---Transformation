import numpy as np

# Creates transformation matrix given the linkage lengths and rotation angles

a1 = 5 # Length of link a1 in cm
a2 = 6 # Length of link a2 in cm
a3 = 2 # Length of link a3 in cm
a4 = 5 # Length of link a4 in cm

T1 = 30  # Theta 1 angle in degrees
T2 = 90  # Theta 2 angle in degrees

T1 = (T1/180.0)*np.pi # Theta 1 in radians
T2 = (T2/180.0)*np.pi # Theta 2 in radians

R0_1 = [[np.cos(T1), -np.sin(T1), 0], [np.sin(T1), np.cos(T1), 0], [0, 0, 1]]
R1_2 = [[np.cos(T2), -np.sin(T2), 0], [np.sin(T2), np.cos(T2), 0], [0, 0, 1]]

print('Rotational matrix 0 to 1:')
print(np.matrix(R0_1))
print('\n')
print('Rotational matrix 1 to 2: ')
print(np.matrix(R1_2))
print('\n')
print('*To compute the rotational matrix from fram 0 to 2, simply dot product the previous two matrices to get:')
print(np.dot(R0_1, R1_2))
print('\n')
print('*Next, form the displacement vectors with the link lengths and given equation.')

# Computes displacement vectors, the final key to form the homogeneous transformation matrix
d0_1 = [[a2*np.cos(T1)], [a2*np.sin(T1)], [a1]]
d1_2 = [[a4*np.cos(T2)], [a4*np.sin(T2)], [a3]]

print('Displacement matrix 0 to 1:')
print(np.matrix(d0_1))
print("\n")
print('Displacement matrix 1 to 2')
print(np.matrix(d1_2))
print('\n')

H0_1 = np.concatenate((R0_1, d0_1), 1)
H0_1 = np.concatenate((H0_1, [[0, 0, 0, 1]]), 0)

H1_2 = np.concatenate((R1_2, d1_2), 1)
H1_2 = np.concatenate((H1_2, [[0, 0, 0, 1]]), 0)

print('*Now that the rotational and displacement matrices are computed, you can concatenate the vectors to form the transform matrices!')
print('\n')
print('Transform matrix 0 to 1:')
print(H0_1)
print('\n')
print('Transform matrix 1 to 2:')
print(H1_2)
print('\n')

H0_2 = np.dot(H0_1, H1_2)

print('*Finally, dot product the matrices to get the Homogeneous Transform Matrix:')
print(np.matrix(H0_2))




