import pandas as pd

def load_celeba_attributes(attr_path):
    """Load CelebA attributes from CSV file"""
    df = pd.read_csv(r'C:\Users\mitta\OneDrive\Desktop\Company Tasks\facial-fashion-recommender\list_attr_celeba.csv')
    return df

def get_fashion_categories():
    """Return Fashion MNIST category mapping"""
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