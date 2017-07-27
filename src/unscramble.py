# coding: utf-8


from PIL import Image
import numpy as np
import random

def storePixels(name, size, pixels):
    outImg = Image.new("L", size)
    # Create a PIL image from the 1D pixel array
    outImg.putdata(pixels) 
    outImg.save(name)

def scrambledIndex(image_1d_array):
    idx = range(len(image_1d_array))
    random.shuffle(idx)
    return idx

#flatten the 2D image into a 1D array
def flattenImage(img):
    image_2d_array = np.array(img)
    image_1d_array = image_2d_array.flatten()
    return image_1d_array

def unScramblePixels(img):
    random.seed(2)
    image_1d_array = flattenImage(img)
    idx = scrambledIndex(image_1d_array)
    out = range(len(image_1d_array))
    cur_pos = 0
    for i in idx:
        out[i] = image_1d_array[cur_pos]
        cur_pos += 1
    return out

def main():
    img = Image.open('scrambled.jpg')
    pixels = unScramblePixels(img)
    storePixels("unscrambled.jpg", img.size, pixels)
    
if __name__ == "__main__":
    main()
