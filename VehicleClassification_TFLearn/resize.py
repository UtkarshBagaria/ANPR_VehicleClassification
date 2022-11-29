from PIL import Image
import os

path = "/Users/vanshikagoel/MI/train/train2/non-vehicles"
dir_list = os.listdir(path)
for i in dir_list:
	image = Image.open(path+'/'+i)
	image.thumbnail((100, 100))
	image.save(i+'2.jpg')

