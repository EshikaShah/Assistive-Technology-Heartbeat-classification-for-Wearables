# Assistive-Technology-Heartbeat-classification-for-Wearables

### The files
- model.py coontains the neural network used to train the data
- explorer.py contains the code used to identify the types of ECG for each patient
- datapipeline.py contains the code used to extract data from .mat files and convert it into csv file with categorical coloumns
- data2.csv contains the final dataset used for training

## 🎯 Objective 
To propose and implement an intelligent real time heartbeat classification algorithm and supplement results with Explainable AI.
You are expected to come out with an approach to solve the classification problem as a real-time solution (so it could be
fabricated into wearables) and embed ‘Explainable AI’ to substantiate your classification semantically

## Solutions
We cleaned the data to get all the signals from the ECG. Converted the .mat files into .csv file with corresponding columns which have data about all the diseases that one patient is facing. Then we have used liner layers to train the model.

### 📚 Tech stack
- <code><img height="35" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> Python
- <code><img height="35" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code> GIT
- <code><img height="35" src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/github.svg"></code> Github
