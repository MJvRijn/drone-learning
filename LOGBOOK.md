
# Logbook
Matthew van Rijn (10779353)

Project: Imitation learning with drones

Supervisor: Tom Runia

## 13-04-2017 (Thursday, week 2)
### General
First meeting with supervisor. Discussed basic objectives of project.

Next meeting: 20-04-2017 (Thursday, week 3)

Objectives:
* Investigate API for Parrot Bebop drone
* Collect literature on Inverse Reinforcement Learning
* Think of simple tasks for the drone

## 18-04-2017 (Tuesday, week 3)
### Literature
Collected:
* Argall 2009 - A survey of robot learning from demonstration
* Stadie 2017 - Third Person Imitation Learning
* Zhang 2015 - Learning Deep Control Policies for Autonomous Aerial Vehicles with MPC-Guided Policy Search
* Finn 2016 - Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization
* Isaac 2003 - Goal-directed Learning to Fly
* Wulfmeier 2016 - Maximum Entropy Deep Inverse Reinforcement Learning
* Abbeel 2011 - Inverse Reinforcement Learning

These papers are suggested by my supervisor.

## 19-04-2017 (Wednesday, week 3)
### General
Nothing notable happened on this day

## 20-04-2017 (Thursday, week 3)
### General
Meeting with supervisor. Discussed problem definition. Suggested two simple tasks:
* Take off and fly to a surface of a certain colour
* Fly between objects

The second task is very similar to one previously attempted. So the problem is now the first task.

The focus for the rest of the week will be on completing the literature overview. Tom suggested a couple of extra sources, which are amongst those listed in the literature section below.

Next meeting: 24-04-2017 (Monday, week 4)

Objectives:
* Investigate simulators/ROS
* (Choose papers for review)

### Literature
Collected:
* Abbeel 2004 - Apprenticeship learning via inverse reinforcement learning
* Andersson 2015 - Model-based reinforcement learning in continuous environments using real-time constrained optimization
* Ranchod 2015 - Nonparametric Bayesian Reward Segmentation for Skill Discovery
* Ross 2011 - A Reduction of Imitation Learning and Structured Prediction
to No-Regret Online Learning
* Ross 2013 - Learning monocular reactive uav control in cluttered natural environments
* Sutton 1998 - Reinforcement Learning:
An Introduction

Some of the papers may not be completely relevant to the project.

## 21-04-2017 (Friday, week 3)
### General
This simple concept map has been produces for the literature overview:
![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/cmap.png)

### Literature
An early version of the literature review has been written using six of the collected sources. It contains only the most relevant sources, and as such does not discuss many algorithms or applications.

## 23-04-2017 (Sunday, week 3)
### Simulator
![AirSim](https://github.com/Microsoft/AirSim) is a simulator for autonomous drone research. It allows you to fly a drone in any unreal environment. The build process is complicated, and the performance poor. The built-in traning data recorder does not work, but there is an API available to get hold of it.

## 24-04-2017 (Monday, week 4)
### General
Meeting with supervisor. Discussed the simulator progress and upcoming project proposal presentation and document.

Next meeting: 26-04-2017 (Wednesday, week 4)

Objectives:
* Investigate DAGGER algorithm
* Investigate AirSim simulator
* Send project proposal slides for feedback (Tuesday)

### Literature
Collected:
* Daftry 2016 - Learning transferable policies for monocular reactive mav control

## 25-04-2017 (Tuesday, week 4)
### General
Created project propsal slides and received feedback on them.

## 26-04-2017 (Wednesday, week 4)
### General
Meeting with supervisor. Little progress since last meeting, so not much to discuss. Supervisor is abroad next week, so the next meeting is not until the week after. In the mean time the objective is to implement DAGGER according to the berkeley RL course, and set up the interaction on a simulator.  

The project proposal slides have been expanded upon in the project proposal document, due tonight.

### Simulator
Another possible simulator is the ROS-based ARDrone simulator. To be investigated.

## 01-05-2017 (Monday, week 5)
### Simulator
The ROS-based tum_simulator runs well and is easier to interact with tham AirSim. Manual control is possible using a DS3 controller. A DS4 controller needs remapping. AirSim performance can be brought to a usable level by lowering the quality settings.

## 03-05-2017 (Wednesday, week 5)
### Simulator
The ROS simulator easily outputs a video stream. A python layer has been created inbetween the joystick and the simulator, which maps controller inputs to actions in a basic action space (TAKEOFF, LAND, UP, DOWN, HOVER).

## 04-05-2017 (Thursday, week 5)
### Simulator
The actions from the python layer are now passed to the simulator. They reveal two major issues:
* The takeoff action causes the drone to rise indefinitely
* The hover action is very unstable, with the drone swerving around trying to balance itself.

## 08-05-2017 (Monday, week 6)
### Simulator
The following action space is now available in the simulator:
* Forward
* Backward
* Left
* Right
* Up
* Down
* Clockwise (yaw)
* Anticlockwise (yaw)

## 09-05-2017 (Tuesday, week 6)
### Simulator
The simulator now allows for the recording and playback of training data (command (action) and image (state))

## 11-05-2017 (Thursday, week 6)
### General
Meeting with supervisor. The progress with the simulator has been discussed.

Next meeting: 17-05-2017

Objectives:
* Create a placeholder model training system, with tensorflow or equivalent.
* Use it to implement DAGGER

## 16-05-2017 (Tuesday, week 7)
### DAGGER
Collected some training data from the simulator for DAGGER: 4 expert runs of the red square task and prepared them for tensorflow.

## 17-05-2017 (Wednesday, week 7)
### DAGGER
Tensorflow last-layer retraining is used to create a usable model for dagger. Tensorflow requires at least 20 examples per class, so some classes (LAND, TAKEOFF, LEFT, RIGHT and BACKWARD) have been temporarily removed for the test. After 1000 training steps a train accuracy of ~92%, a validation accuracy of ~80% and a final test accuracy of 72.9% is achieved. On CPU, training time is 2 minutes, not including the time needed to run the training images through the net (~2 img/s). This is with the images in their raw 640x360 resolution.

This image testing time might pose a problem, since a rate of 2hz is quite low. Using a GPU would improve this, but the GPU drivers don't work. Instead, the images might be able to be scaled down further.

### General
I met with my supervisor. We discussed the following topics:
* What kind of (convolutional) neural network to use
* How to collect enough data for training/how to efficiently label data with DAGGER
* We decided to simplify the action space further (at least initially), leaving FORWARD, BACKWARD, LEFT, RIGHT, and possibly LAND
* Complications with GPUs

Tom kindly offered to provide a tensorflow implementation of a neural network used by (Mnih 2013/2015) to perform deep reinforcement learning on ATARI games.

## 18-05-2017 (Thursday, week 7)
### General
In order to create an environment which is both able to run the simulator and has a powerful GPU, an attempt is made to install ubuntu 14.04 on my home pc. There is no spare hard drive space, so the installation is made one a 32GB USB drive, but booting from here is not successful.

I received the neural network implementation, but due to the complications above am not able to run it yet

## 19-05-2017 (Friday, week 7)
### Literature
Collected:
Mnih 2013 - Playing atari with deep reinforcement learning
Mnih 2015 - Human-level control through deep reinforcement learning

Updated the literature review to include a passage about deep-q learning, and the need for large data sets. Also rewrote some parts in better academic English for the academic English assignment.

## 20-05-2017 (Saturday, week 7)
### Learning
Today I'm not at home, so I only have my laptop. I hadn't tried to install tensorflow with GPU support ebcause I couldn't get the Nvidia driver running, but it turns out that it works fine for CUDA. I installed tensorflow-gpu, and tried to train the convnet. Unfortunately 2GB of video memory does not appear to be enough to train at 84x84x4, or indeed any size at all. Hopefully it is sufficient to use a trained model.

## 21-05-2017 (Sunday, week 7)
### Learning
After returning home I have quickly been able to install CUDA and cuDNN on my windows machine, with a 4GB GTX970. I am able to run the training at 80% max video memory (3.2GB), but this is still not enough for training at 84x84x4. After some testing I have found I can train at 56x56x4 (680 examples/s). 

## 22-05-2017 (Monday, week 8)
### General
Meeting with supervisor. We discussed the technical issues surrounding video memory. To train the convolutional neural network I would need an account on the Titan X machine. We also noted that a lot of time has been spent solving technical issues and not much time has been spent on deep learning. 

Objectives:
* Use a feed-forward network to finish the simulator interaction
* Collect a lot of training examples using the reduces action space
* Investigate Titan X machine

## 24-05-2017 (Wednesday, week 8)
### Learning
Successfully set up tensorflow on the Titan X machine and trained the CNN. Using the settings from Mnih's paper requires about 9GB of video memory. 

## 25-05-2017 (Thursday, week 8)
### Learning
To implement the feed-forward neural network I though it would be possible to remove the convolution layers from the convolutional network and replace them with fully connected ones. Unfortunately this results in vague InvalidArgumentErrors, even if the input data is the same shape as the output data.

## 26-05-2017 (Friday, week 8)
### Learning
To be able to continue on this weeks objectives despite not being able to easily implement the feed-forward network. I decided to use the convolutional network, and perform the training on the server. This required some server communication and data transfer to be set up, but this (thankfully) did not present too many problems.

## 27-05-2017 (Saturday, week 8)
### Learning
Today I modified the training code to save a model. To my surprise the model is over 2.6GB! This makes the transfer of the model I had envisioned for the dagger algorithm rather problematic. To classify an image, the model needs to be loaded into the video memory, requiring almost as much data as for training. This means the convolutional network cannot be run on the same system as the simulator, which is potentially a huge problem. The feedforward network is meant for testing, and is unlikely to produce satisfactory results. The only way around this in tensorflow seems to be to run the classification on the Titan X machine.

For the time being this means that a working feed-forward network is needed to continue. I will discuss these problems with my supervisor.

## 29-05-2017 (Monday, week 9)
### General
By the morning my frustrations had died down somewhat, which gave me the opportunity to come up with some solutions. For one, I realised that the ROS integration did not have to run as a node. This allows me to integrate all the (local) code into one system, which I have started doing. I also discovered that the reason the simulator was not working was graphics driver related. Basically, it is not possible to run tensorflow on GPU and run the simulator at the same time on my system. It is therefore probably best to perform the learning and classification remotely.

## 30-05-2017 (Tuesday, week 9)
### General
Meeting with supervisor. We discussed the difficulties experienced with the learning system. The decision was made to perform all learning and classifying on the remote server. This resolved issues with CUDA, graphics drivers and a lack of video memory. The next immediate target is having a feed-forward neural network running on the server which is able to train and classify on demand. 

We also discussed the use of the real drone, and concluded that it would introduce too many new technical issued. The plan is now to dedicate one day to the real drone to see if anything can be done with it.

Next meeting: friday, after presentation.

## 31-05-2017 (Wednesday, week 9)
### Progress Presentation
I devised the plan for the rest of the project. As I noted yesterday, the amount of time allocated to the real drone has been reduced significantly. This means the answer to the research question mighht have to be presented differently.

## 01-06-2017 (Thursday, week 9)
### Progress Presentation
I completed the progress presentation slides and received feedback on the from my supervisor.

## 02-06-2017 (Friday, week 9)
### Progress Presentation
For obvious reasons, my progress presentation was centred around the planning more than actual results. The reaction to the contents of the presentation seemed positive, and has not lead to any changes to the plan.

## 03-06-2017 (Saturday, week 9)
### Learning
Finished migrating all code to the new system. All previously working functions are now available and have been improved.

## 04-06-2017 (Sunday, week 9)
### Learning
Implemented the server communications, allowing the system to pass images from the simulator to the server for classification (currently random). Also added uploading of training data. Reduced the number of steps neccessary to record a trajectory, allowing for faster collection of trajectories. Collected 25 demonstrations of the task, known as dataset A.

## 05-06-2017 (Monday, week 10)
### General
Today I wrote a draft introduction to submit for the assignment on academic English.

## 06-06-2017 (Tuesday, week 10)
### Learning
Implemented a feedforward neural network using Keras, which simplifies the process significantly. Trained it on dataset A. No immediate results, need to look at parameters.

## 07-06-2017 (Wednesday, week 10)
### General
Meeting with supervisor. Showed progress. We discussed the aims for the remainder of the project:
* Experiment with feedforward NN
* Experiment with different NN
* Experiment with DAGGER (build DAGGER interface)
* Experiment with changing environment (moving houses, etc)
* Experiment with changing goal (moving red square)
* Experiment with different amounts of trajectories in the training set
* Do as many possible experiments in the current learning environment.

Immediate objectives:
* Visualise the representation of the image as input to the neural network to see if the correct information is visible.

There will be no introductions of new algorithms, such as inverse reinforcement learning. Testing on the drone is also unlikely to happen due to time constraints.

From now on, some of the time every week will be dedicated to the thesis. This was our last meeting before the end of the project.

### Learning
During the meeting we tried changing parameters, but to no avail. Will look at this tomorrow.

## 09-06-2017 (Friday, week 10)
## Learning
Hooked up model to server, improved speed.

## 11-06-2017 (Sunday, week 10)
### FF network
![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/input_example.jpg)

## 12-06-2017 (Monday, week 11)
### General
Uvavpn down, so decided to start thesis. Created a basic layout etc.

## 15-06-2017 (Thursday, week 11)
### FF network
Network params:
 - FC 512
 - Dropout 0.3
 - FC 256
 - rmsprop (lr=0.0001)

Problem: Accuracy low (0.2419)

Observation: Input image is triple channel, contains excess information

Tried: reducing image to greyscale while preserving standout colour (red) by setting areas where red > 250 and green/blue < 25 to max, while dividing rest (from red channel) by three.

![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/input_example_standout.jpg)

Potential caveat: distinction between walls and background reduced

Result: Accuracy significantly improved (0.62 after 10 epochs, 0.67 after 25)

Observation: unneccesary action 'HOVER' included. This is never a desirable action for the drone to take.

Tried: removing 'hover' from training data and possible actions

Result: Accuracy significantly improved (0.75 after 10 epochs, 0.79 after 25)

Potential caveat: this may be because of an unbalanced training set, and the network just learning to predict the most common.

Tried: counting examples of each type in training set

Result: 
Forward (1488), Clockwise (291), Anticlockwise (271)
Forward = 72.7%

So the hypothesis is potentially correct

Tried: evaluating test accuracy
Result: test accuracy quickly rises to ~82%, but does not progress after that. Occasional epochs show very low accuracy

Tried: balancing training set so that forward == clockwise+anticlockwise (~500)
Result: test accuracy = 0.4067, does not change between epochs, after epoch 12 suddenly increases

Tried: running unbalanced model in simulator
Result: success! The drone clearly displays some of the desired behaviour. It is of course not perfect, but the drone flies forward when there is a large red square in sight and turns circles most of the time if there is not (mostly anticlockwise).

Observation: the drone loves windows alsmost as much as the red square, must check to see how these are represented.

## 16-06-2017 (Friday, week 11)
### Thesis
Worked on method & approach

## 19-06-2017 (Monday, week 12)
### FF network
Parameter testing (100 epochs, 90/10 train/test, ~2000 examples/25 trajectories):
D512/DR0.3/D256 lr 0.0001 ba 32 im 64: tr 0.8461 te: 0.8098
D512/DR0.3/D256 lr 0.0001 ba 32 im 32: tr 0.8531 te: 0.8146
D512/DR0.3/D256 lr 0.00001 ba 32 im 64: tr 0.8623 te: 0.7854 (accuracy more stable)
D1024/DR0.3/D128 lr 0.00001 ba 32 im 64: tr 0.8634 te: 0.8341
D1024/DR0.5/D128 lr 0.00001 ba 32 im 64: tr 0.8585 te: 0.8146
D1024/DR0.3/D128 lr 0.00001 ba 16 im 64: tr 0.8986 te: 0.8000
D1024/DR0.3/D128/DR0.3/D64/DR0.3 lr 0.00005 ba 32 im 64: tr 0.8260 te: 0.7951
D16 lr 0.00005 ba 32 im 64: tr 0.8575 te: 0.8293
D16 lr 0.005 ba 32 im 64: no learning
D16 lr 0.0005 ba 32 im 64: tr 0.8108 te: 0.8000 (unstable)
D512/DR0.5 lr 0.0005 ba 32 im 64: no learning
D512/DR0.5 lr 0.0001 ba 32 im 64: tr 0.8434 te 0.7854
D512/DR0.5 lr 0.0001 ba 32 im 64 (balanced/less data): tr 0.7497 te 0.7075
D25000/DR0.2 lr 0.0001 ba 32 im 64 (balanced/less data): no learning
D2048/DR0.2 lr 0.0001 ba 32 im 64 (balanced/less data): no learning
D1024/DR0.3/D128/DR0.3 lr 0.00001 ba 32 im 64 (balanced/less data): tr 0.8000 te: 0.6321
D1024/DR0.3/D128/DR0.3 lr 0.00001 ba 32 im 64: tr 0.8493 te: 0.8732

Conclusion: the differences between vastly different networks are relatively small

Previous observation: the drone likes windows
Tried: looking at representation of window

![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/window_image.png)
![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/window_image_standout.png)

There are clearly some white dots in the window, which may be the cuase of the drone's interest in it.

Drone behaviour test using last tested model:
The drone is now more likely to fly forward, even if the red square is more visible. This makes it more likely to find the red square, but also causes more crashes. When the red square is right infront of the drone, the desire to fly forward is far more pronounced.

Changed the image processing code to fix the window dots:
![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/window_image_standout_new.png)

Make sure the red square is still right:
![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/input_example_standout_new.jpg)

### DAGGER
[PDF](http://rll.berkeley.edu/deeprlcourse-fa15/docs/2015.10.5.dagger.pdf) here shows dagger working using steering inputs as mistakes are made, similar to my earlier dagger idea. (Let drone fly and correct with keyboard when mistake made)

Started implementation
Finished basic implementation

## 20-06-2017 (Tuesday, week 12)
### Experiments
Using best FFNN: D1024/DR0.3/D128/DR0.3 lr 0.00001
Test data: 10% from entire dataset of 25 traj

Testing different number of trajectories (accuracy, loss, confusion matrix):
1. 44/44 [==============================] - 0s - loss: 0.2327 - acc: 0.9091 - val_loss: 1.9503 - val_acc: 0.3073 AC FW CW [[  0   4  15]  [  0  41 122]  [  0   1  22]]
2. 114/114 [==============================] - 0s - loss: 0.2784 - acc: 0.9123 - val_loss: 0.7224 - val_acc: 0.7317 AC FW CW [[ 11  14   1]  [ 16 139   6]  [  3  15   0]]
3. 212/212 [==============================] - 0s - loss: 0.1398 - acc: 0.9717 - val_loss: 0.9041 - val_acc: 0.7268 AC FW CW [[ 13  16   1]  [  6 130   8]  [  2  23   6]]
4. 248/248 [==============================] - 0s - loss: 0.1408 - acc: 0.9516 - val_loss: 1.0778 - val_acc: 0.6000 AC FW CW [[ 7  6 19]  [ 8 97 38]  [ 5  6 19]]
5. 306/306 [==============================] - 0s - loss: 0.1334 - acc: 0.9739 - val_loss: 0.9585 - val_acc: 0.7024 AC FW CW [[  8  19   4]  [  4 130   4]  [  5  25   6]]
6. 489/489 [==============================] - 0s - loss: 0.1614 - acc: 0.9468 - val_loss: 1.6733 - val_acc: 0.5268 AC FW CW [[ 8  4 16]  [26 78 41]  [ 1  9 22]]
7. 533/533 [==============================] - 0s - loss: 0.1697 - acc: 0.9475 - val_loss: 1.0720 - val_acc: 0.7122 AC FW CW [[  0  13  16]  [  5 138  15]  [  0  10   8]]
8. 572/572 [==============================] - 0s - loss: 0.1946 - acc: 0.9423 - val_loss: 0.8633 - val_acc: 0.7220 AC FW CW [[  0  23  11]  [  2 129  11]  [  0  10  19]]
9. 629/629 [==============================] - 0s - loss: 0.2046 - acc: 0.9332 - val_loss: 0.9005 - val_acc: 0.7415 AC FW CW [[  1  10  18]  [  5 135  13]  [  1   6  16]]
10. 726/726 [==============================] - 0s - loss: 0.2172 - acc: 0.9242 - val_loss: 1.0711 - val_acc: 0.6683 AC FW CW [[  3   9  18]  [  3 113  26]  [  1  11  21]]
11. 835/835 [==============================] - 0s - loss: 0.2299 - acc: 0.9257 - val_loss: 1.0452 - val_acc: 0.7317 AC FW CW [[  5  10  11]  [  9 132  10]  [  7   8  13]]
12. 873/873 [==============================] - 0s - loss: 0.2454 - acc: 0.9187 - val_loss: 1.2042 - val_acc: 0.6195 AC FW CW [[  1   5  19]  [  4 103  45]  [  0   5  23]]
13. 944/944 [==============================] - 0s - loss: 0.2594 - acc: 0.9142 - val_loss: 0.6614 - val_acc: 0.7951 AC FW CW [[  3  11  13]  [  1 139   8]  [  2   7  21]]
14. 993/993 [==============================] - 0s - loss: 0.2561 - acc: 0.9144 - val_loss: 0.8862 - val_acc: 0.7268 AC FW CW [[  0  13  19]  [  0 135  10]  [  2  12  14]]
15. 1023/1023 [==============================] - 0s - loss: 0.2408 - acc: 0.9110 - val_loss: 0.6575 - val_acc: 0.7902 AC FW CW [[  4  12   8]  [  2 136  11]  [  2   8  22]]
16. 1082/1082 [==============================] - 0s - loss: 0.2452 - acc: 0.9113 - val_loss: 0.7250 - val_acc: 0.7512 AC FW CW [[ 17   7  11]  [  8 121  17]  [  3   5  16]]
17. 1227/1227 [==============================] - 0s - loss: 0.2837 - acc: 0.9006 - val_loss: 0.8955 - val_acc: 0.6683 AC FW CW [[  5   7  21]  [  5 116  31]  [  2   2  16]]
18. 1318/1318 [==============================] - 0s - loss: 0.2820 - acc: 0.9014 - val_loss: 0.6848 - val_acc: 0.7951 AC FW CW [[  7  15  10]  [  2 140   7]  [  1   7  16]]
19. 1407/1407 [==============================] - 0s - loss: 0.3194 - acc: 0.8842 - val_loss: 0.5449 - val_acc: 0.8390 AC FW CW [[  8   9   3]  [  2 146   7]  [  8   4  18]]
20. 1449/1449 [==============================] - 0s - loss: 0.3368 - acc: 0.8778 - val_loss: 0.6652 - val_acc: 0.7122 AC FW CW [[ 21   4   4]  [ 25 117   5]  [ 16   5   8]]
21. 1497/1497 [==============================] - 0s - loss: 0.3230 - acc: 0.8771 - val_loss: 0.6206 - val_acc: 0.8146 AC FW CW [[ 17  10   5]  [  7 134   4]  [  3   9  16]]
22. 1552/1552 [==============================] - 0s - loss: 0.3324 - acc: 0.8776 - val_loss: 0.6169 - val_acc: 0.7512 AC FW CW [[  4   8  18]  [  4 131  16]  [  1   4  19]]
23. 1606/1606 [==============================] - 0s - loss: 0.3567 - acc: 0.8630 - val_loss: 0.5133 - val_acc: 0.8098 AC FW CW [[  6  13   4]  [  1 153   3]  [  4  14   7]]
24. 1704/1704 [==============================] - 0s - loss: 0.3292 - acc: 0.8750 - val_loss: 0.5819 - val_acc: 0.8195 AC FW CW [[ 18   7   1]  [  9 134   3]  [  7  10  16]]
25. 1845/1845 [==============================] - 0s - loss: 0.3565 - acc: 0.8737 - val_loss: 0.6214 - val_acc: 0.8000 AC FW CW [[  1  13   7]  [  0 150   1]  [  2  18  13]]

## 21-06-2017 (Wednesday, week 12)
### Thesis
Worked on method & approach

## 22-06-2017 (Thursday, week 12)
### Thesis
Worked on literature review

## 23-06-2017 (Friday, week 12)
### Thesis
Worked on method & approach

## 24-06-2017 (Saturday, week 12)
### Results
Collect: accuracy, loss, description (avg time, num crashes/completions)

#### CNN
Conv 8x8/4 out 32
Conv 4x4/2 out 64
Conv 3x3/1 out 64
Flatten
FC512
DR0.5
FC3
lr 0.00005
45 epochs peak accuracy = 80%

Testing different number of trajectories (accuracy, loss, confusion matrix):
1. 44/44 [==============================] - 0s - loss: 0.3651 - acc: 0.7955 - val_loss: 1.5763 - val_acc: 0.4585 AC FW CW [[ 0 14 18]  [ 0 77 70]  [ 0  9 17]]
2. 108/108 [==============================] - 0s - loss: 0.4084 - acc: 0.8333 - val_loss: 0.9561 - val_acc: 0.5707 AC FW CW [[ 11  22   5]  [ 21 105  10]  [  6  24   1]]
3. 214/214 [==============================] - 0s - loss: 0.2550 - acc: 0.9112 - val_loss: 0.8652 - val_acc: 0.6390 AC FW CW [[  1  20   7]  [ 10 122  20]  [  2  15   8]]
4. 251/251 [==============================] - 0s - loss: 0.1994 - acc: 0.9363 - val_loss: 0.8491 - val_acc: 0.6488 AC FW CW [[  3  13  13]  [  8 121  21]  [  3  14   9]]
5. 299/299 [==============================] - 0s - loss: 0.2570 - acc: 0.9264 - val_loss: 0.8203 - val_acc: 0.6976 AC FW CW [[  3  14   7]  [ 12 130   6]  [  4  19  10]]
6. 486/486 [==============================] - 0s - loss: 0.2602 - acc: 0.9095 - val_loss: 1.2027 - val_acc: 0.5805 AC FW CW [[  1   8  21]  [ 16 104  29]  [  0  12  14]]
7. 534/534 [==============================] - 0s - loss: 0.2597 - acc: 0.9195 - val_loss: 1.2224 - val_acc: 0.5415 AC FW CW [[ 1 12 26]  [ 1 91 47]  [ 1  7 19]]
8. 578/578 [==============================] - 0s - loss: 0.2646 - acc: 0.9256 - val_loss: 0.8898 - val_acc: 0.6927 AC FW CW [[  0  16  12]  [  1 127  24]  [  0  10  15]]
9. 641/641 [==============================] - 0s - loss: 0.2660 - acc: 0.9158 - val_loss: 1.0933 - val_acc: 0.6195 AC FW CW [[ 0  8 20]  [ 1 98 41]  [ 0  8 29]]
10. 734/734 [==============================] - 0s - loss: 0.2842 - acc: 0.9183 - val_loss: 0.9653 - val_acc: 0.7073 AC FW CW [[  3  11   9]  [ 13 123  16]  [  1  10  19]]
11. 837/837 [==============================] - 0s - loss: 0.2968 - acc: 0.9068 - val_loss: 0.8159 - val_acc: 0.7024 AC FW CW [[  6  15  11]  [  6 131  10]  [  5  14   7]]
12. 870/870 [==============================] - 0s - loss: 0.3033 - acc: 0.9115 - val_loss: 0.8216 - val_acc: 0.6976 AC FW CW [[  5  12  12]  [  5 127  26]  [  1   6  11]]
13. 943/943 [==============================] - 0s - loss: 0.2956 - acc: 0.9046 - val_loss: 0.7619 - val_acc: 0.7659 AC FW CW [[  4   6  11]  [  4 137  16]  [  3   8  16]]
14. 981/981 [==============================] - 0s - loss: 0.2855 - acc: 0.9103 - val_loss: 0.7940 - val_acc: 0.7659 AC FW CW [[  5  14  12]  [  3 141   5]  [  4  10  11]]
15. 1028/1028 [==============================] - 0s - loss: 0.2825 - acc: 0.9202 - val_loss: 0.9139 - val_acc: 0.7463 AC FW CW [[  3  10  14]  [  2 140   8]  [  5  13  10]]
16. 1075/1075 [==============================] - 0s - loss: 0.3027 - acc: 0.9060 - val_loss: 0.7939 - val_acc: 0.7366 AC FW CW [[  2  10  16]  [  2 130  15]  [  2   9  19]]
17. 1221/1221 [==============================] - 0s - loss: 0.2958 - acc: 0.9058 - val_loss: 0.7750 - val_acc: 0.7415 AC FW CW [[  7  11   8]  [  0 129   9]  [  4  21  16]]
18. 1324/1324 [==============================] - 0s - loss: 0.3265 - acc: 0.8860 - val_loss: 0.6421 - val_acc: 0.7659 AC FW CW [[  4   8   9]  [  2 133  14]  [  6   9  20]]
19. 1404/1404 [==============================] - 0s - loss: 0.3320 - acc: 0.8718 - val_loss: 0.6049 - val_acc: 0.7659 AC FW CW [[ 11  15  10]  [  4 129   6]  [  3  10  17]]
20. 1446/1446 [==============================] - 0s - loss: 0.3695 - acc: 0.8624 - val_loss: 0.4065 - val_acc: 0.8537 AC FW CW [[  5   7   8]  [  2 157   4]  [  2   7  13]]
21. 1496/1496 [==============================] - 0s - loss: 0.3751 - acc: 0.8603 - val_loss: 0.5809 - val_acc: 0.7902 AC FW CW [[  9  10  16]  [  0 142   9]  [  3   5  11]]
22. 1553/1553 [==============================] - 0s - loss: 0.3650 - acc: 0.8583 - val_loss: 0.5015 - val_acc: 0.8244 AC FW CW [[  5   6   7]  [  4 152   5]  [  4  10  12]]
23. 1606/1606 [==============================] - 0s - loss: 0.3599 - acc: 0.8624 - val_loss: 0.6343 - val_acc: 0.8000 AC FW CW [[  8  13   4]  [  4 151   1]  [  2  17   5]]
24. 1703/1703 [==============================] - 0s - loss: 0.3729 - acc: 0.8602 - val_loss: 0.5644 - val_acc: 0.7756 AC FW CW [[ 10  10   8]  [  7 137   2]  [  4  15  12]]
25. 1845/1845 [==============================] - 0s - loss: 0.3848 - acc: 0.8564 - val_loss: 0.5357 - val_acc: 0.8195 AC FW CW [[  9   9   1]  [  1 151   1]  [  9  16   8]]

Create various models:
ff 25 traj - done
cnn 25 traj - done
ff dagger various - ...
cnn dagger various - ...

Test them:
Moving goal
Moving buildings

![](https://raw.githubusercontent.com/MJvRijn/drone-learning/master/logbook/eval_locations.png)


cnn 25 traj evaluation:
General:
The drone has exploratory tendencies (does not sit still and turn)
The drone flies straight at the red square when visible and turns to correct its path when close
The drone avoids the concrete barriers, blue house and brown plaything
The drone sometimes flies into the white houses and the grey wall
The drone likes to fly into the grey nothingness at the edge of the world
The drone sometimes gets stuck turning back ans forth

10 trajectory test (max 1 min):
1. The drone flies anticlockwise around the outside of the buildings, no goal achieved, no crash
2. The drone flied around the barriers and to the red square, goal achieved in 20s, no crash
3. The drone crashes into the barrier after 4 seconds
4. The drone turns clockwise and flies to the north, stopping to turn back and forth indefinitively, no goal achieved, no crash
5. Same behaviour as 1, no goal, no crash
6. Flies past the goal and gets stuck just like 4, no goal, no crash
7. Immediately gets stuck like 4, no goal, no crash
8. Flies to right of goal, crashes into white building at 17s
9. Turns left, flies past goal and crashes into concrete barrier at 22s
10. Same behaviour as 8, crash into white biulding at 23s

ff 25 traj evaluation:
General:
The drone has limited exploratory tendencies
The drone flies at the red square when visible, and makes constant course corrections on the way
The drone flies into the white house, but is hesitant about it
The drone flies into the grey wall and brown plaything
The drone avoids the concrete barriers and blue house
The drone turn anticlockwise and moves forward when in grey areas

10 trajectory test (max 1 min):
1. Flies to goal, achieved at 22s
2. Crash into brown plaything at 18s
3. Flies to goal, achieved at 10s
4. Turns clockwise, gets stuck looking at white house, crashes into it at 38s
5. Flies to wall and crashes at 7s
6. Flies to goal, achieves at 9s
7. Flies forward, gets stuck looking north, gets unstuck, flies past goal, time up, no crash, no goal
8. Flies left of goal, crashes into blue building window at 13s
9. Same as 8, but crash at 22s
10. Goes left, crashes into blue building at 21s

Dagger:
collect 10 trajectories per iteration

ff-dagger:
1. 2737/2737 [==============================] - 0s - loss: 0.5275 - acc: 0.7965 - val_loss: 0.8371 - val_acc: 0.6842 AC FW CW [[  9  36  23]  [  0 155   9]  [  2  26  44]]
2. 3535/3535 [==============================] - 0s - loss: 0.6209 - acc: 0.7488 - val_loss: 0.7326 - val_acc: 0.6607 AC FW CW [[ 20  24  29]  [  6 150  16]  [ 21  37  89]]
3. 4782/4782 [==============================] - 1s - loss: 0.7119 - acc: 0.6999 - val_loss: 0.8220 - val_acc: 0.6591 AC FW CW [[ 26  24  67]  [  3 158  57]  [ 10  20 166]]
4. 6529/6529 [==============================] - 1s - loss: 0.7766 - acc: 0.6615 - val_loss: 1.1920 - val_acc: 0.4897 AC FW CW [[ 58 129  23]  [  7 239   5]  [ 27 179  58]]


Observation:
The accuracy decreased with DAGGER, this may be due to the fact that a much smaller proportion of the dagger dataset contains the red square than the original dataset, ans that the action FORWARD is less common. This make the classification task harder.

Observation:
The performance of the drone decreases with DAGGER, as it becomes much more indecive. Maybe a different form of DAGGER where the drone follows the expert overrides, and only records those, would be better. Known henceforth as SPREADINGKNIFE.

Observation:
After 4 dagger iterations the training set is pretty balanced, from original 72% forward: Counter({'FORWARD': 2574, 'CLOCKWISE': 2560, 'ANTICLOCKWISE': 2120})

cnn-dagger:
1. 2475/2475 [==============================] - 0s - loss: 0.4570 - acc: 0.8065 - val_loss: 0.7520 - val_acc: 0.7236 AC FW CW [[ 28  19   9]  [ 11 161   2]  [ 13  22  10]]
2. 3478/3478 [==============================] - 0s - loss: 0.6015 - acc: 0.7386 - val_loss: 0.7262 - val_acc: 0.6762 AC FW CW [[ 32  32  21]  [ 15 189   8]  [ 16  33  40]]
3. 4325/4325 [==============================] - 1s - loss: 0.6278 - acc: 0.7348 - val_loss: 0.8619 - val_acc: 0.6021 AC FW CW [[ 49  48  29]  [ 20 202   9]  [ 34  51  38]]
4. 5163/5163 [==============================] - 1s - loss: 0.6643 - acc: 0.7155 - val_loss: 0.9240 - val_acc: 0.5829 AC FW CW [[ 65  44  46]  [ 23 206  31]  [ 46  49  63]]


Observation: 
Dagger seems to be overriding good policy, good argument for spreadingknife. Spreadingknife should only override before critical mistakes to preserve good policy

Observation:
CNN dagger dataset less balanced than ff:
Counter({'FORWARD': 2661, 'ANTICLOCKWISE': 1588, 'CLOCKWISE': 1487})
Dataset also 1100 smaller (shorter trajectories)

ff 25 traj + 40 dagger traj evaluation:
General:
The drone has reasonable exploratory tendencies
The drone flies at the red square when straight ahead, but makes no course corrections
The drone flies into the grey wall, brown plaything, white house and blue house windows
The drone avoids the concrete barriers and blue house
The drone flies straight in grey areas

10 trajectory test (max 1 min):
1. Flies straight into the greyness, no goal, no crash
2. Flies forward, gets confused, no goal, no crash
3. Flies forward, turns left, flies into greyness, no goal, no crash
4. Turns clockwise slightly confused, flies past goal to the left and crashes into NE house at 26s
5. Flies away into greyness, no goal, no crash
6. Flies forward slightly confused, flies away into northern greyness, no goal, no crash
7. Same as 6, no goal, no crash
8. Flies straight towards goal, achieves at 6s
9. Turns right, crashes into building at 6s
10. Flies straight towards goal, achieves at 11s

cnn 25 traj + 40 dagger evaluation:
General:
The drone has slight exploratory tendencies
The drone flies at the red square when it is staight ahead, but sometimes veers off to one side.
The drone avoids the brown plaything, but crashes into other buildings ocasionally
In grey areas the drone turns around looking for a target
The drone is generally very indecisive

10 trajectory test (max 1 min):
1. Indecisively flies around barrier, achieves goal at 32s
2. The drone flied around the barriers and to the red square, goal achieved in 20s, no crash
3. Similar to 2, but crashes into blue building at 26s
4. Crashes into concrete barrier at 8s
5. Hugs grey wall, crashes into it at 50s
6. Hugs blue building, crashes into it at 18s
7. Gets confused, crashes into blue building at 18s
8. Flies to left of goal, crashes into blue building at 25s
9. Crashes into white building at 7s
10. Flies indecisively to goal, crashes into blue building at 17s

Observation:
Terrible from cnn which seems more interested in buildings now than the goal. FF performs pretty similarly to before but in a different way.

Time for spreadingknife (sk)

## 25-06-2017 (Sunday, week 12)
### Plan
Outline of the plan for the final week:
Sunday: 
* Complete thesis method & approach
* Complete thesis evaluation

Monday:
* Collect results from final simplified dagger tests (sk)
* Collect results for moving goal, buildings
* Create visualisations for results
* Hand in logbook

Tuesday:
* Make presentation
* Write thesis results

Wednesday:
* Write thesis conclusion & discussion
* Prepare presentation

Thursday:
* Present
* Update thesis introduction & write abstract
* Review & amend thesis

Friday:
* Final thesis review
* Hand in thesis

### Thesis
Worked on method & approach, evaluation

## 26-06-2017 (Monday, week 13)
### DAGGER
SK: ~500 samples per iteration

sk-ff:
1. 2309/2309 [==============================] - 0s - loss: 0.4895 - acc: 0.8133 - val_loss: 0.6176 - val_acc: 0.7969 AC FW CW [[  5  20   9]  [  1 169   2]  [  2  18  30]]
2. 2769/2769 [==============================] - 0s - loss: 0.4791 - acc: 0.8075 - val_loss: 0.8939 - val_acc: 0.7068 AC FW CW [[  6  35   6]  [  1 195   2]  [  6  40  16]]

### General
Final meeting with supervisor. Discussed plan for final days and reviewed thesis draft.


