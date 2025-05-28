# roblox triggerbot
![Static Badge](https://img.shields.io/badge/Python-000?logo=Python&logoColor=white)

* main files are triggerbot.py 
* training is in the training branch
* train.py creates files in runs. you can see the outputted model in the train and then weights under the file extention .pt


# the triggerbot is in yolo.py
## How to use
1. Clone the main branch of this repo
```bash 
git clone --single-branch --branch main https://github.com/someonecantcode/triggerbot.git
```
2. Install all python depencies
```bash
pip install -r requirements.txt
```
3. Run triggerbot.py
```bash
python triggerbot.py
```

## How it works
1. Takes screenshot around the crosshair coordinates.
2. Uses model and checks if any detected objects' bounded box is inside the crosshair
3. Fires if that's the case.


## How to contribute
1. Fork this training branch of this repo.
2. Make your changes and send in a pull request.
3. I will review and merge.