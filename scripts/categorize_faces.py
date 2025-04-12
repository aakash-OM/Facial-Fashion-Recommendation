def categorize_face(row):
    """Categorize face based on CelebA attributes using heuristic rules"""
    if row['Wearing_Necktie'] == 1:
        return 6  # Shirt
    elif row['Wearing_Lipstick'] == 1:
        return 3  # Dress
    elif row['Young'] == 1 and row['Smiling'] == 1:
        return 0  # T-shirt
    elif row['Eyeglasses'] == 1:
        return 4  # Coat
    elif row['Male'] == 1:
        return 6  # Shirt (default for male)
    else:
        return 0  # Default T-shirt