# Face Detecton In Python Using OpenCV

# OpenCV

OpenCV is an open source computer vision and machine learning software library. It is a BSD-licence product thus free for both business and academic purposes.The Library provides more than 2500 algorithms that include machine learning tools for classification and clustering, image processing and vision algorithm, basic algorithms and drawing functions, GUI and I/O functions for images and videos. Some applications of these algorithms include face detection, object recognition, extracting 3D models, image processing, camera calibration, motion analysis etc.

OpenCV is written natively in C/C++. It has C++, C, Python and Java interfaces and supports Windows, Linux, Mac OS, iOS, and Android. OpenCV was designed for computational efficiency and targeted for real-time applications. Written in optimized C/C++, the library can take advantage of multi-core processing.

# Face Detection

Face detection has gained a lot of attention due to its real-time applications. A lot of research has been done and still going on for improved and fast implementation of the face detection algorithm. Why is face detection difficult for a machine? Face detection is not as easy as it seems due to lots of variations of image appearance, such as pose variation (front, non-front), occlusion, image orientation, illumination changes and facial expression.

OpenCV contains many pre-trained classifiers for face, eyes, smile etc. The XML files of pre-trained classifiers are stored in opencv/data/. For face detection specifically, there are two pre-trained classifiers:

1.Haar Cascade Classifier

2.LBP Cascade Classifier

We will explore both face detectors in this tutorial.

# Haar Cascade Classifier

It is a machine learning based approach where a cascade function is trained from a lot of positive (images with face) and negative images (images without face). The algorithm is proposed by Paul Viola and Michael Jones.

The algorithm has four stages:

# 1.Haar Feature Selection:
Haar features are calculated in the subsections of the input image. The difference between the sum of pixel intensities of adjacent rectangular regions is calculated to differentiate the subsections of the image. A large number of haar-like features are required for getting facial features.
# 2.Creating an Integral Image: 
Too much computation will be done when operations are performed on all pixels, so an integral image is used that reduce the computation to only four pixels. This makes the algorithm quite fast.
# 3.Adaboost: 
All the computed features are not relevant for the classification purpose. Adaboost is used to classify the relevant features.
# 4.Cascading Classifiers: 
Now we can use the relevant features to classify a face from a non-face but algorithm provides another improvement using the concept of cascades of classifiers. Every region of the image is not a facial region so it is not useful to apply all the features on all the regions of the image. Instead of using all the features at a time, group the features into different stages of the classifier.Apply each stage one-by-one to find a facial region. If on any stage the classifier fails, that region will be discarded from further iterations. Only the facial region will pass all the stages of the classifier.

# LBP Cascade Classifier 

LBP is a texture descriptor and face is composed of micro texture patterns. So LBP features are extracted to form a feature vector to classify a face from a non-face. Following are the basic steps of LBP Cascade classifier algorithm:

# 1.LBP Labelling:
A label as a string of binary numbers is assigned to each pixel of an image.
# 2.Feature Vector: 
Image is divided into sub-regions and for each sub-region, a histogram of labels is constructed. Then, a feature vector is formed by concatenating the sub-regions histograms into a large histogram.
# 3.AdaBoost Learning:
Strong classifier is constructed using gentle AdaBoost to remove redundant information from feature vector.
# 4.Cascade of Classifier:
The cascades of classifiers are formed from the features obtained by the gentle AdaBoost algorithm. Sub-regions of the image is evaluated starting from simpler classifier to strong classifier. If on any stage classifier fails, that region will be discarded from further iterations. Only the facial region will pass all the stages of the classifier.

# Steps :

       # 1.Loading HaarCascadeFace Algorithm
       
       # 2.Initializing Camera
       
       # 3.Reading Frame from Camera
       
       # 4.Converting Color image into Grayscale Image
       
       # 5.Obtaining Face coordinates by passing algorithm
       
       # 6.Drawing Rectangle on the Face Coordinates
       
       # 7.Display the output Frame

# Output :

To see the output video, go to the media file and check the output video
