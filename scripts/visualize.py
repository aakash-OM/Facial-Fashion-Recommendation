import os
import pandas as pd
from matplotlib import pyplot as plt

def show_sample_recommendations(csv_path, celeb_dir, n=5):
    """Display sample recommendations with CelebA images"""
    try:
        df = pd.read_csv(csv_path).sample(n)
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_path}")
        return

    fig, axs = plt.subplots(n, 2, figsize=(10, 2*n))
    
    for idx, (_, row) in enumerate(df.iterrows()):
        # Construct image path
        celeb_path = os.path.join(celeb_dir, row['image_id'])
        
        ##################################################
        # ADD VALIDATION HERE
        if not os.path.exists(celeb_path):
            print(f"Missing image: {celeb_path}")
            continue  # Skip to next iteration
        ##################################################
        
        try:
            img = plt.imread(celeb_path)
            axs[idx, 0].imshow(img)
            axs[idx, 0].axis('off')
        except Exception as e:
            axs[idx, 0].text(0.5, 0.5, f"Error: {str(e)}", ha='center')
        
        axs[idx, 1].text(0.5, 0.5, 
                         f"Recommended:\n{row['fashion_category']}",
                         ha='center', va='center', fontsize=12)
        axs[idx, 1].axis('off')
    
    plt.tight_layout()
    plt.show()