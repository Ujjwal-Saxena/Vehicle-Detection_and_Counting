# Vehicle-Detection_and_Counting


In this project, eith the help of OpenCV library and Image Processing Techniques, I have created a model that can identify, detect and count the total number of vehicles on road.

For this, I first imported all the libraries, like cv2, numpy, time.

Secondly, I imported my video files (.mp4 format). In this  project, to test my model accuracy, I tested my model on 2 different videos.

I specified the coordinates to make a line that will actually act as a threshold value for all the moving vehicles. Those vehicles which will cross the threshold value (from either direction), the count value will be incremented.

I performed Image Processing techiniques on the video frames to get insights of the contours, grayscale, Gaussian_Blurring, Kernel definition, dilation.

I then defined a rectangle to detect vehicles with their centres. 


Execute main.py to see the result of vehicle detection and counting for a daylight video.

Execute video1.py to see the result of vehicle detection and counting for a night video. 
