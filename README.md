# roblox triggerbot

* main files are yolo.py and train.py
* train.py creates files in runs. you can see the outputted model in the train and then weights under the file extention .pt


# the triggerbot is in yolo.py
## How it works
1. Takes screenshot around the crosshair coordinates.
2. Uses model and checks if any detected objects' bounded box is inside the crosshair
3. Fires if that's the case.
