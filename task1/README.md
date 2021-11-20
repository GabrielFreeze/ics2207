# Dataset References
Positive face images and bounding boxes: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html

Negative non-face images: http://www.vision.caltech.edu/Image_Datasets/Caltech101/
						  https://www.kaggle.com/jessicali9530/caltech256

# Parameters used to train
• Positive Samples: 5000
• Negative Samples: 2500
• Acceptance Ratio Break Value: 10e-5
• Max Number of Stages: 38
• Actual Number of Stages till break value was reached: 14
• Width and Height of training window: 24,24

# Extra Remarks

The face dataset had all the images aligned by their eyes and were cropped to 178x218 pixels. I overlayed some hundred faces on top of each other, and made the bounding box for all the images equal to the bounding box for this face amalgamation which I manually croppped. The bounding box is (x,y,w,h) = (30, 57, 127, 137).

I used opencv_createsamples in order to generate a .vec file from the positive images. I created info.dat by running a shell script which lists all the files in the positive image folder and then appends (30, 57, 127, 137) for each file's bounding box. bg.txt was also created using this shell script.
