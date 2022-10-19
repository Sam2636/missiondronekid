# mavros download


# Try this ros - installation

'''
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
'''


# This is a failed process 

# step 1
To add the ROS Melodic repo, run the following command:

`sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-melodic.list`

# step2
Add official ROS Melodic repo keyring

`sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`

# step3
Make changes in software update other software and remove jammy release tick mark then close file and reload

`sudo apt update`

# step4
check
if in case the file is not loacte 
go to software update and click main server and close  then reload the 

# step5 
To download ros to full-desktop

`sudo apt install ros-melodic-desktop-full`

# if the file is broken

`sudo apt install aptitide`

`sudo aptitude install ros-melodic-desktop-full`


#To check ros is installed or not

`apt search ros-melodic`
