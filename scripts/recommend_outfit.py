import pandas as pd

def generate_recommendations(df, fashion_categories, output_path):
    """Generate final recommendations and save to CSV"""
    df['fashion_category'] = df['fashion_label'].map(fashion_categories)
    output = df[['image_id', 'fashion_label', 'fashion_category']]
    output.to_csv(output_path, index=False)
    return output