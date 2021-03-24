# Vehicle-Detection_and_Counting


**AIM:-**

The objective of this task is to identify and detect total number of vehicles in a captured video stream.

**TOOLS USED:-**

PC 32/64 bit, Python 3.7 or higher, Opencv Library, numpy library.

**PROCEDURE:-**

In this project, with the help of OpenCV library and Image Processing Techniques, I have created a model that can identify, detect and count the total number of vehicles on road.

**STEP1:-**

For this, I first imported all the libraries, like cv2, numpy, time.

So, to install these libraries, perform the following task:-

**CV2:-**   

pip install opencv

**NUMPY**   

pip install numpy

**TIME;-**  

pip install python-time

**STEP2:**

Secondly, I imported my video files (.mp4 format). In this  project, to test my model accuracy, I tested my model on 3 different videos.

**METHOD:-**

To detect and count total number of vehicles on the road, we need to setup a particular point or a **threshold value** coordinates, so that whenever a car crosses that coordinate we will increment the count value.

I specified the coordinates to make a line that will actually act as a threshold value for all the moving vehicles. Those vehicles which will cross the threshold value (from either direction), the count value will be incremented.

I performed Image Processing techiniques on the video frames to get insights of the contours, grayscale, Gaussian_Blurring, Kernel definition, dilation.

I then defined a rectangle to detect vehicles with their centres. 

**CONCLUSION:-**

Execute main.py to see the result of vehicle detection and counting for a daylight video.

Execute video1.py to see the result of vehicle detection and counting for a night video. 
