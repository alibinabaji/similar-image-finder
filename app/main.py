import streamlit as st
from app.similarity_search import find_similar_images
from app.utils import save_uploaded_file

st.title("Dress Similarity Finder")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    query_image_path = "data/query.jpg"  # Adjust the path as necessary
    save_uploaded_file(uploaded_file, query_image_path)
    
    st.image(query_image_path, caption="Uploaded Image", use_column_width=True)
    
    image_directory = "data/image_database"  # Adjust the path as necessary
    similar_images = find_similar_images(query_image_path, image_directory)
    
    st.write("Similar Images:")
    for image_path, similarity in similar_images:
        st.image(image_path, caption=f"Similarity: {similarity:.2f}", use_column_width=True)
