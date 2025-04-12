from tensorflow.keras.datasets import fashion_mnist
import pandas as pd

def load_celeba_attributes(attr_path):
    """Load CelebA attributes"""
    return pd.read_csv(attr_path)

def load_fashion_data():
    """Load Fashion MNIST images/labels"""
    return fashion_mnist.load_data()

def get_fashion_categories():
    """Category mapping for Fashion MNIST"""
    return {
        0: 'T-shirt/top',
        1: 'Trouser',
        2: 'Pullover',
        3: 'Dress',
        4: 'Coat',
        5: 'Sandal',
        6: 'Shirt',
        7: 'Sneaker',
        8: 'Bag',
        9: 'Ankle boot'
    }