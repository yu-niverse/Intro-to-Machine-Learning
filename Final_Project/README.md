# Final Project
【 NYCU 2022 Fall Semester 】 by Professor 林彥宇

## Brief Introduction
The task is to participate in [The August 2022 edition of the Tabular Playground Series Competition](https://www.kaggle.com/competitions/tabular-playground-series-aug-2022/overview). 

The purpose of the competition is to predict individual product failures with their test results with past product testing results. I put my main focus on different feature engineering methods and chose to utilize the logistic regression model for the task. Find my implementation details [here](109550182_Final.pdf).

## Environment Setting
To rebuild the environment : 
```
pip install -r requirements.txt
```

## Result Reproduction
1. Download [weights.joblib](https://drive.google.com/file/d/1VpMwJZM-_5BqptHdmMkM6DwHA-XKV7fH/view?usp=sharing) and [109550182_Final_inference.ipynb](109550182_Final_inference.ipynb)
2. Change the path of test.csv and weights.joblib
3. Execute [109550182_Final_inference.ipynb](109550182_Final_inference.ipynb) to get submission.csv
