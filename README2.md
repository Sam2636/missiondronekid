mavros download



# step 1
'''sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-melodic.list'''

# step2
'''sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654'''

# make changes in software update other software and remove jammy release tick mark then close file and reload
'''sudo apt update'''

# if in case the file is not loacte 
# go to software update and click main server and close  then reload the 

# To download ros to full-desktop
'''sudo apt install ros-melodic-desktop-full'''

# if the file is broken
'''sudo apt install aptitide'''
'''sudo aptitude install ros-melodic-desktop-full'''


#To check ros is installed or not
'''apt search ros-melodic'''
