# Lab 13 Reinforcement Learning Lab Report
all plot data has been uploaded into the file "plot_data" as a .cvs

## Custom Reward Function 1
The first reward function only gives rewards for reaching the final goal with nothing else given or taking for all other steps. This reward function seemed to perform the best as the model found what the goal was, giving less time as the model went on. This function seemed to work very well with very low times. This also leads to set rewards based on what the final goal reward is. 

## Custom Reward Function 2
The second reward function gives rewards for visiting new states and takes away when visiting old states. While this funtion gives high rewards, I worry that the increased time it is taking is due to the AI going to all possible states instead of the goal. This lead me to create function 4 to see if this is a solvable problem. 

## Custom Reward Function 3
The third function gives rewards based on the total distance from the end goal, giving more the closer the AI gets. This should incentivize the program to find the shortest path to the end goal. THe plots also reflect that while relativly matching the reward plot, the time is noticably lower that function 2 & 4. I think that this is the best aproach for a efficient approach. 

## Custom Reward Function 4
The fourth reward is a version of the second with the only difference being that there is a high reward for reaching the final goal. This was added to incentivize finding the goal without going to every single option. The plots reflect that while the time is lower than function 2, the rewards end up higher in the long run. This means that the code does seem to reduce the time needed to get to the end. 