
# Logbook

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
## General
Uvavpn down, so decided to start thesis. Created a basic layout etc.

## 15-06-2017 (Thursday, week 11)
## FF network
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
## Thesis
Worked on method & approach













