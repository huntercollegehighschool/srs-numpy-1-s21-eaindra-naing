# 1. Import the numpy package under the name `np`
import numpy as np

##### DECLARING NUMPY ARRAYS #####

# 2. Use np.array(<list>) to convert the list below into a numpy array. The array should be saved in a variable. Then print both the list and the array.
a = [300, -200, 100, 0, -100, 200, -300]
r = np.array(a)
print (a) #has commas
print (r) #becomes more like a table format, would be better for data

## The array method in numpy has an optional dtype argument which specifies the datatype each element should be. For the array above, it could be implemented using A = np.array(a, dtype=str) ##

# 3. Declare new arrays with different datatypes using the list from #2. Datatypes to use: str, float, np.int32, np.int8, np.uint32, np.uint8.

B = np.array(a,dtype=str)
C = np.array(a,dtype=float)
D = np.array(a,dtype=np.int32) #32bit binary number (-2^31 tp 2^31 -1)
E = np.array(a,dtype=np.int8) #8bit binary number (-128 to 127)
F = np.array(a,dtype=np.uint32) #not negative (0 to 2^31 -1)
G = np.array(a,dtype=np.uint8) #u=unsignd in, (0 to 2^8 -1)

print (B)
print (C)
print (D)
print (E)
print (F)
print (G)

# 4. Use np.zeros(<int>) to create a array of zeroes of size 10. This should be saved in a variable. Then print the array.

H = np.zeros(10)
print (H)

# 5. In your array of zeroes, change the fifth 0 to a 6. (remember how indexing works in lists?) Print the array.

H[4]=6
print (H)

# 6. Use np.arange(<int>, <int>) to create an array with values ranging from 11 to 46. Print the array.

I = np.arange(11,46)
print (I)

# 7. Reverse the array you created in #6. Print the array.

J = np.flip(I)
print (J)

# 8. Use <array>.reshape(<int>, <int>) to turn your array from #6 into a multidimensional 6x6 array. Print the array.

#.reshape   numpy supports matrix operations
b = [3,1,4,1,5,9]
np.reshape (2,3)
np.reshape (2,3)


# 9. Use np.random.random((<int>, <int>)) to create a 10x10 array with random values. Print the array.



# 10. Use np.random.randint(<int>, <int>, size=(<int>, <int>)) to create a 3x3 array with random integers. Print the array.



# 11. Use <array>.max() and <array>.min to identify the maximums and minimums of the arrays you created in #9 and #10. Print the results.


# 12. Use <array>.mean() to find the means of the two arrays you created in #9 and #10. Print the results.


# 13. Convert the following two lists into 2X3 arrays. (You will need to use np.array and .reshape)

a = [2, 3, 5, 7, 11, 13]
b = [3, 1, 4, 1, 5, 9]

# 14. Add the two arrays from #13 (<array> + <array>)


# 15. Multiply both arrays from #13 by 10.