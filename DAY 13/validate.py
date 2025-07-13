from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
import os

# Load model architecture
with open("model.json", "r") as json_file:
    model = model_from_json(json_file.read())

# Load model weights
model.load_weights("model.h5")
print("✅ Model loaded successfully")

# Define test dataset path
test_path = "Dataset/test/"

# Loop through test images
for img_name in os.listdir(test_path):
    img_path = os.path.join(test_path, img_name)
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    result = model.predict(img_array)
    if result[0][0] == 1:
        prediction = 'Object A'
    else:
        prediction = 'Object B'

    print(f"{img_name} → {prediction}")
