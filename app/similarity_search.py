import os
from sklearn.metrics.pairwise import cosine_similarity
from app.feature_extraction import extract_features

def calculate_similarity(feature1, feature2):
    return cosine_similarity([feature1], [feature2])[0][0]

def find_similar_images(query_image_path, image_directory, top_n=5):
    query_features = extract_features(query_image_path)
    similarities = []
    
    for image_name in os.listdir(image_directory):
        image_path = os.path.join(image_directory, image_name)
        image_features = extract_features(image_path)
        similarity = calculate_similarity(query_features, image_features)
        similarities.append((image_path, similarity))
    
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    return similarities[:top_n]
