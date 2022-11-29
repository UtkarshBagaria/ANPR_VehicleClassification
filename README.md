# ANPR_VehicleClassification

## Execution Instructions for VehicleClassification_Tensorflow
### Training the Model on the dataset
<pre>
Step 1: Download the data folder which contains the pre-processed dataset 
Step 2: Update the path of the data folder in the Multi_Classification_Vehicle.ipynb file
Step 3: Run the Multi_Classification_Vehicle.ipynb file 
Step 4: Update the path to save the model 
</pre>

### Testing the Model 
<pre>
Step 1: Update the path of the model (trained model file can be used model_saved_4_15.h5) in the output_final.ipynb file 
Step 2: Download the test images 
Step 3: Update the path of the test images in the output_final.ipynb file
Step 4: Run the output_final.ipynb file
</pre>

## Execution Instructions for VehicleClassification_Keras

## Execution Instructions for VehicleClassification_Pytorch

### Training the Model on the dataset
<pre>
Step 1: Download the dataset folder which contains the pre-processed dataset and run the first cell in tutorial.ipynb to git clone the yolov5 environment
Step 2: Make a yaml file containing the path of the dataset folder and put the yaml file in the data folder for example
<!-- path: D:\Sem-5\LAB\ANPR\yolov5\data\pre960  # dataset root dir 
train: train\images\ # train images (relative to 'path') 128 images
val: train\images\  # val images (relative to 'path') 128 images
test: test\images\  # test images (optional)

# Classes
names:
  0: number_plate -->
Step 3: Update the path of the yaml file in the tutorial.ipynb in the training cell
Step 4: Run the training cell
Step 5: Update the path of the trained model in the Detect cell the path to the weights will be printed out by the training cell
Step 6: Add Car image path in the Detect cell
Step 7: Run the Detect cell
Step 8: If foreign car go to foreign car cell else Indian car cell update the exp# number as shown in the output of the Detect cell
Step 9: Run the Indian car cell or foreign car cell
</pre> 
