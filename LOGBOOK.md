
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
Meeting with supervisor.

## 30-05-2017 (Tuesday, week 9)

## 31-05-2017 (Wednesday, week 9)
### Progress Presentation

## 01-06-2017 (Thursday, week 9)
### Progress Presentation

## 02-06-2017 (Friday, week 9)
### Progress Presentation

## 03-06-2017 (Saturday, week 9)
### Learning









