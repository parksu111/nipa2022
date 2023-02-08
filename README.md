# 2022 NIPA Online AI Competition
English | [한국어](https://github.com/parksu111/nipa2022/blob/main/README_ko.md)

## Introduction
The **NIPA Online AI Competition** is an annual competition hosted by the [National IT Industry Promotion Agency](https://www.nipa.kr/eng/index.do) in order to support Korean startups in the AI industry. In 2022, the competition consisted of 10 tasks in total, with the top performing 2 teams of each task receiving KRW 200M (~USD 160K) in funding. Startups could only use the data that was provided and had to submit their code for evaulation.

As a Data Scientist at [MNC](https://mnc.ai/), I was responsible for developing 2 of the 10 tasks. This repository contains code for the preparation and evaluation of these 2 tasks, along with the baseline models provided to participating teams.

## Task 02: Beef Grade Classification
### Overview
* [Competition Page](https://aichallenge.or.kr/competition/detail/1/task/2/taskInfo)
* Task: Image Classification
* Description: Using images of beef slices, classify the grade of beef into one of 5 grades (1++,1+,1,2,3).
* Evaluation: Submissions are evaluated on the *Quadratic Weighted Kappa*.
  * An explanation and implementation of the metric in python can be found in this [notebook]().
  * Final scores are calculated on both the public(30%) and private(70%) test datasets.
* Data: Images of beef slices & labels in a csv file.
  * Sample data can be found [here](https://github.com/parksu111/nipa2022/tree/main/cow_grade/01_DATA).
  * The full train dataset is available for download [here](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=158).

### Data / Code
All the code for this project can be found in the 'cow_grade' folder of this repository.
* **01_DATA**
  * Sample dataset
* **02_WORKSPACE**
  * *qwk.ipynb* - Explanation of the evaluation metric.
* **03_BASELINE**
  * The baseline model for this task uses the pretrained Efficientnet-b4.
* **04_SUBMIT**
  * *evaluate.py* - Script to receive submissions and calculate the final score.
  * Due to privacy issues, the actual answer file is not shared with the public.

## Task 09: Pipe Leak Detection
### Overview
* [Competition Page](https://aichallenge.or.kr/competition/detail/1/task/9/taskInfo)
* Task: Tabular Classification
* Description: Using data from vibration sensors, determine whether or not the pipe is leaking and the type of leak if it is leaking (5 classes).
* Evaluation: Submissions are evaluated using the macro F1 score.
* Data: Spectral Density estimates obtained from FFT on raw signals from vibration sensors in a csv file.
  * Sample data can be found [here](https://github.com/parksu111/nipa2022/tree/main/pipe_leak/01_DATA).
  * The full train dataset is available for download [here](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=138).

### Data / Code
All the code for this project can be found in the 'pipe_leak' folder of this repository.
* **01_DATA**
  * Sample dataset
* **02_WORKSPACE**
  * Currently empty
* **03_BASELINE**
  * The baseline model for this task uses a LGBM.
* **04_SUBMIT**
  * *evaluate.py* - Script to receive submissions and calculate the final score.
  * Due to privacy issues, the actual answer file is not shared with the public.
  
 
