import tensorflow as tf
import os
# ignore warnings about AVX compling
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print("TensorFlow's version:", tf.__version__)
print("TensorFlow GPU support:", tf.test.is_gpu_available())
print("TensorFlow find GPU devices:", tf.test.gpu_device_name())



