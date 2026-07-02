# Machine Learning Projects

A collection of machine learning projects covering computer vision, time-series forecasting, and natural language processing.

---

## Projects

### 1. Face Detection
**Folder:** `Face_Detection/`

Two face-detection approaches using OpenCV:
- **Haar Cascade** â€” image-based face detection using pre-trained cascade classifier
- **DNN SSD (Caffe)** â€” real-time webcam face detection with confidence scoring

**Files:** `face_detect_image.py`, `face_detect_webcam.py`, model files (`.prototxt`, `.caffemodel`, `.xml`)

**Tech:** Python, OpenCV, NumPy

---

### 2. Gesture Detection
**Folder:** `Gesture_detection/`

Hand gesture recognition system with a Flask-based web app. Trains on gesture image data and classifies hand gestures in real time.

**Files:** `app.py`, `requirements.txt`, `data/`, `models/`, `gestures/`, `utils/`

**Tech:** Python, Flask, OpenCV, TensorFlow/Keras

---

### 3. Stock Market Prediction with LSTM
**Folder:** `Stock_Prediction/`

LSTM neural network that predicts next-day closing prices using historical market data from Yahoo Finance. Includes visualization of predicted vs actual prices.

**Files:** `train_lstm.py`, `requirements.txt`

**Tech:** Python, TensorFlow/Keras, yfinance, Matplotlib

---

### 4. Spam Detection
**Folder:** `spam_detection/`

Naive Bayes classifier with TF-IDF vectorization for SMS/email spam classification. Includes a Gradio web interface for real-time predictions.

**Files:** `app.py`, `train_spam.py`, `train_spam_stem.py`, `spam_bot.py`, `requirements.txt`, `artifacts/`, `data/`

**Tech:** Python, Scikit-learn, NLTK, Gradio, Pandas, Joblib

---

### 5. Week 1 — ML Fundamentals (archived)
**Folder:** `archive/ml-programs/week-1/`

Merged from [ML-Programs](https://github.com/ssahilkhan/ML-Programs). Implementation of the FIND-S algorithm with and without libraries, data efficiency evaluation, and a sports/weather application.

**Files:** `finds_efficiency_evaluator.py`, `finds_with_lib.py`, `finds_without_lib.py`, `training_data_*.csv`, `Applications/sports.py`, `Applications/sports_weather.csv`

**Tech:** Python, NumPy

---

## Getting Started

Each project has its own `README.md` and `requirements.txt` with setup instructions. Navigate into any project folder and follow its guide:

```bash
cd Face_Detection
pip install -r requirements.txt
python face_detect_image.py
```
