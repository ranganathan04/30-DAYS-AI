# 🧠 Day 13: CNN-Based Image Classifier

This project demonstrates how to classify images using a Convolutional Neural Network (CNN) in Keras.

---

## ✅ Components

- **add_on.py**: Downloads images from Google for dataset creation
- **validate.py**: Loads trained model and predicts class labels on test images
- **model.json**: CNN model architecture (placeholder)
- **model.h5**: Trained weights (placeholder)
- **Dataset/test/**: Folder to store test images

---

## 🧪 Types of Image Classification

- **Binary Classification**
- **Multi-Class Classification**
- **Multi-Label Classification**

---

## 🧱 CNN Architecture

1. **Input Layer**
2. **Convolution Layer**
3. **ReLU Activation**
4. **Pooling Layer**
5. **Flatten**
6. **Fully Connected Layer**
7. **Output Layer (Softmax/Sigmoid)**

---

## ▶️ How to Run

### 1. Install dependencies:

```bash
pip install keras tensorflow pygoogle_image numpy pillow
```

### 2. Add your trained model files:

- `model.json`
- `model.h5`

### 3. Add test images to `Dataset/test/`

### 4. Run validation:

```bash
python validate.py
```

---

## 📌 Notes

- You can modify `add_on.py` to download images for other classes
- Ensure your model was trained on 64x64 image inputs (or modify accordingly)
