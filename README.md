# 2022 NIPA Online AI Competition
English | [한국어](https://github.com/parksu111/nipa2022/blob/main/README_ko.md)

## Introduction
The **NIPA Online AI Competition** is an annual competition hosted by the [National IT Industry Promotion Agency](https://www.nipa.kr/eng/index.do) in order to support Korean startups in the AI industry. In 2022, the competition consisted of 10 tasks in total, with the top performing 2 teams of each task receiving KRW 200M (USD 159K). Startups could only use the data that was provided and had to submit their code for evaulation.

As a Data Scientist at [MNC](https://mnc.ai/), I was responsible for developing 2 of the 10 tasks. This repository contains code for the preparation and evaluation of these 2 tasks, along with the baseline models provided to participating teams.

## Task 02: Beef Grade Classification
### Overview
* Task: Image Classification
* Description: Using images of beef slices, classify the grade of beef into one of 5 grades (1++,1+,1,2,3).
* Evaluation: Submissions are evaluated on the *Quadratic Weighted Kappa*.
  * An explanation and implementation of the metric in python can be found in this [notebook]().
* Data: Images of beef slices & labels in a csv.
  * Sample data can be found [here](https://github.com/parksu111/nipa2022/tree/main/cow_grade/01_DATA).
  * The full dataset is available for download [here](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=158).

### Baseline Model

