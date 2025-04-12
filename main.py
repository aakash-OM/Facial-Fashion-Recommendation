print("main.py is running...")

import os
import sys
from pathlib import Path

# Add the project root to Python path
sys.path.append(str(Path(__file__).parent))

from scripts.categorize_faces import categorize_face
from scripts.data_loader import load_celeba_attributes, get_fashion_categories
from scripts.recommend_outfit import generate_recommendations
from scripts.visualize import show_sample_recommendations

def main():
    # Path configuration
    attr_path = r'C:\Users\mitta\OneDrive\Desktop\Company Tasks\facial-fashion-recommender\list_attr_celeba.csv'
    output_dir = r'C:\Users\mitta\OneDrive\Desktop\Company Tasks\facial-fashion-recommender\output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    attr_df = load_celeba_attributes(attr_path)
    fashion_categories = get_fashion_categories()
    
    # Categorize faces
    attr_df['fashion_label'] = attr_df.apply(categorize_face, axis=1)
    
    # Generate recommendations
    output_path = os.path.join(output_dir, 'recommendations3.csv')
    recommendations = generate_recommendations(
        attr_df, 
        fashion_categories,
        output_path
    )
    
    print(f"Successfully generated recommendations at {output_path}")
    
    sample_size = 5  # Number of samples to display
    celeb_images_dir = r'C:\Users\mitta\OneDrive\Desktop\Company Tasks\facial-fashion-recommender\img_align_celeba'  # Path to CelebA images
    show_sample_recommendations(output_path, celeb_images_dir, sample_size)

if __name__ == '__main__':
    main()