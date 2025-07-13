# 🚦 Day 22 - Road Sign Recognition for Autonomous Vehicles

This project uses a Convolutional Neural Network (CNN) to classify traffic signs using the GTSRB dataset.

## 🛠️ Requirements

```bash
pip install tensorflow opencv-python matplotlib numpy scikit-learn
```

## 📁 Dataset

Download the dataset from Kaggle:  
👉 https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-preprocessed

- Unzip the dataset and place the `train/` folder in the project directory.

## ▶️ Run the Model

```bash
python road_sign_cnn.py
```

## 📈 Output

- Trained CNN model saved as `model.h5`
- Predict using any road sign image resized to 30x30

---
