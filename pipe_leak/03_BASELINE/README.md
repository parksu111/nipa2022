# 2022 인공지능 온라인 경진대회
## [수치해석] 상수관로 누수감지 및 분류 문제


### 코드 구조

```
${PROJECT}
├── config/
│   ├── train_config.yaml
│   ├── predict_config.yaml
│   └── preprocess_config.yaml
├── models/
│   ├── ML_model.py
├── modules/
│   └── utils.py
├── README.md
├── train.py
├── predict.py
└── preprocess.py
```

- config: 학습/추론에 필요한 파라미터 등을 기록하는 yaml 파일
- models:
    - ML_model.py: 모델 클래스
- modules:
    - utils.py: 여러 확장자 파일을 불러오거나 여러 확장자로 저장하는 함수 등을 포함한 파일
- train.py: 학습 시 실행하는 코드
- predict.py: 추론 시 실행하는 코드

---

### 학습

1. 데이터 폴더 생성
    1. 아래 구조와 같이 데이터 폴더를 생성하고 train.csv, test.csv, sample_submission.csv를 이동
```
${DATA}
├── 00_source/
│   └── train.csv
├── 01_split/
│   └── test.csv
└── sample_submission.csv
```
2. 'config/preprocess_config.yaml' 수정
    1. DIRECTORY/srcdir: train.csv가 들어있는 00_source 폴더의 경로 지정
    2. DIRECTORY/dstdir: test.csv가 들어있는 01_split 폴더의 경로 지정
3. 'python preprocess.py' 실행
    1. 아래와 같이 학습 데이터셋이 train 과 validation 데이터셋으로 나누어.
```
${DATA}
├── 00_source/
│   └── train.csv
├── 01_split/
│   ├── train.csv
│   ├── valid.csv
│   └── test.csv
└── sample_submission.csv
```
4. 'config/train_config.yaml' 수정
    1. DIRECTORY/data: train.csv, valid.csv, test.csv가 위치한 01_split 폴더의 경로 지정
    2. 이외 파라미터 조정
5. 'python train.py' 실행
6. 'results/train/' 내에 결과(model.pkl 등)가 저장됨


### 추론

1. 'config/predict_config.yaml' 수정
    1. DIRECTORY/data: train.csv, valid.csv, test.csv가 위치한 01_split 폴더의 경로 지정
    2. DIRECTORY/sample: sample_submission.csv의 파일 경로 지정
    3. EXPERIMENT/serial: 파라미터를 불러올 train serial number (result/train 내 폴더명) 지정
2. 'python predict.py' 실행
3. 'results/predict/' 내에 결과 파일(predictions.csv)이 저장됨