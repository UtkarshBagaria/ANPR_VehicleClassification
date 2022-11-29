
import os
 
file1 = open("training/dataset.txt", "a")
path = "/Users/vanshikagoel/MI/training/non-vehicles"
dir_list = os.listdir(path)
for i in dir_list:
	p='/content/drive/MyDrive/MI/training/non-vehicles/'+i+' 3\n'
	file1.write(p) 

