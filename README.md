# Decoding-a-scrambled-image

### Some facts about the input grayscale image X:
* Image X was scrambled in Python 2.7 using the Mersenne Twister random number generator seeded with the number 2.
* The numpy flatten() function is used to flatten the 2D image into a 1D array.
* The random.shuffle(...) function (not the numpy one) is used to shuffle a list of numbers [0, 1, 2, …, n-1] where n is the number of pixels in image X.
* The shuffled list was used to assign the pixels in the scrambled image like Y[i] = X[shuffled[i]] for all i in [0, 1, 2, …, n-1].

