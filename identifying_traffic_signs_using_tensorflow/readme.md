# Traffic Sign Classification with TensorFlow

With the advancement of self-driving car technology, computer vision plays a crucial role in enabling vehicles to interpret and respond to their surroundings. A key aspect of this is the ability to accurately classify road signs from images, such as stop signs, speed limit signs, and yield signs.

## Background
 
This project uses TensorFlow to build a neural network that can classify images of road signs based on their visual content. We'll utilize the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which includes thousands of images categorized into 43 different types of road signs.

## Getting Started

1. **Download the Distribution Code**: Clone or download the distribution code from  ```git clone https://github.com/naman39/projects/tree/main/identifying_traffic_signs_using_tensorflow```

2. **Download the German Traffic Sign Recognition Benchmark (GTSRB) dataset:** ```https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip```
   
3. **Install Dependencies**: Inside the `traffic` directory, run `pip3 install -r requirements.txt` to install necessary dependencies (`opencv-python`, `scikit-learn`, `tensorflow`).

## Understanding the Project

- **Dataset Structure**: The `gtsrb` directory contains 43 subdirectories (numbered 0 through 42), each representing a different category of road signs. Each subdirectory contains images of that particular type of traffic sign.

- **Project Files**:
  - **`tensoriffic.py`**: This file manages loading the data, building the neural network model, training the model, evaluating its performance, and optionally saving the trained model.
  - **`README.md`**: Documenting experimentation process and insights gained during the project.
  
- **Specification**:
  - Implement `load_data` in `tensoriffic.py` to load and preprocess images from the dataset.
  - Implement `get_model` in `tensoriffic.py` to create and compile a neural network model for traffic sign classification.

## Experimentation Process

Throughout this project, I experimented with various configurations and techniques to optimize the traffic sign classification model:

- **Data Loading and Preprocessing**: Initially, I used OpenCV (`cv2`) to read and resize images to a standard size (`IMG_WIDTH x IMG_HEIGHT`). This step is crucial to ensure all images are compatible with the neural network input layer.

- **Neural Network Architecture**: I experimented with different architectures:
  - Variations in the number of convolutional layers and pooling layers.
  - Different kernel sizes and numbers of filters in convolutional layers.
  - Various sizes and activation functions for hidden layers.
  - Incorporation of dropout layers to prevent overfitting.

- **Training and Evaluation**: I trained the models on the training set and evaluated performance on the test set. Adjustments were made based on metrics such as accuracy, loss, and validation accuracy to improve model performance.

- **Challenges and Discoveries**: 
  - **Overfitting**: Initially faced issues with overfitting due to complex model architectures. Addressed this by introducing dropout layers and reducing layer complexity.
  - **Model Tuning**: Experimented with learning rates, batch sizes, and epochs to find optimal training parameters.
  - **Data Augmentation**: Explored techniques like image rotation, scaling, and flipping to increase dataset diversity and improve generalization.

## Usage

To run the traffic sign classification:
```python tensoriffic.py [data_directory] [optional: model_filename.h5]```
- `data_directory`: Path to the directory containing the `gtsrb` dataset.
- `model_filename.h5` (optional): Filename to save the trained model.

## Conclusion

Through this project, I gained valuable experience in building and optimizing neural networks for image classification tasks using TensorFlow. Experimentation with different architectures and techniques provided insights into the challenges and considerations involved in developing robust computer vision applications for real-world scenarios.

![Screenshot 2024-06-17 at 5 08 14 AM](https://github.com/naman39/projects/assets/59209974/af462ca0-4120-4710-ba3b-562f8f5291c5)
