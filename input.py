import pandas as pd
import streamlit as st


# Define function to get user input
def get_user_input():
    mean_radius = st.sidebar.number_input(label="Enter Mean Radius", min_value=6.00, max_value=28.00)
    mean_texture = st.sidebar.number_input(label="Enter Mean Texture", min_value=9.00, max_value=40.00)
    mean_perimeter = st.sidebar.number_input(label="Enter Mean Perimeter", min_value=43.00, max_value=188.00)
    mean_area = st.sidebar.number_input(label="Enter Mean Area", min_value=143.00, max_value=2501.00)
    mean_smoothness = st.sidebar.number_input(label="Enter Mean Smoothness", min_value=0.05, max_value=0.17)
    mean_compactness = st.sidebar.number_input(label="Enter Mean Compactness", min_value=0.01, max_value=0.35)
    mean_concavity = st.sidebar.number_input(label="Enter Mean Concavity", min_value=0.00, max_value=0.43)
    mean_concave_pts = st.sidebar.number_input(label="Enter Mean Concave Points", min_value=0.00, max_value=0.21)
    mean_symmetry = st.sidebar.number_input(label="Enter Mean Symmetry", min_value=0.1, max_value=0.31)
    mean_fractal = st.sidebar.number_input(label="Enter Mean Fractal Dimension", min_value=0.04, max_value=0.1)
    radius_se = st.sidebar.number_input(label="Enter SE of Radius", min_value=0.1, max_value=2.9)
    texture_se = st.sidebar.number_input(label="Enter SE of Texture", min_value=0.36, max_value=4.9)
    perimeter_se = st.sidebar.number_input(label="Enter SE of Perimeter", min_value=0.75, max_value=21.98)
    area_se = st.sidebar.number_input(label="Enter SE of Area", min_value=6.8, max_value=542.2)
    smoothness_se = st.sidebar.number_input(label="Enter SE of Smoothness", min_value=0.00, max_value=0.32)
    compactness_se = st.sidebar.number_input(label="Enter SE of Compactness", min_value=0.00, max_value=0.14)
    concavity_se = st.sidebar.number_input(label="Enter SE of Concavity", min_value=0.00, max_value=0.4)
    concave_pts_se = st.sidebar.number_input(label="Enter SE of Concave Points", min_value=0.00, max_value=0.06)
    symmetry_se = st.sidebar.number_input(label="Enter SE of Symmetry", min_value=0.00, max_value=0.08)
    fractal_se = st.sidebar.number_input(label="Enter SE of Fractal Dimension", min_value=0.00, max_value=0.03)
    radius_worst = st.sidebar.number_input(label="Enter Worst Radius", min_value=7.93, max_value=36.04)
    texture_worst = st.sidebar.number_input(label="Enter Worst Texture", min_value=12.02, max_value=49.54)
    perimeter_worst = st.sidebar.number_input(label="Enter Worst Perimeter", min_value=50.41, max_value=251.2)
    area_worst = st.sidebar.number_input(label="Enter Worst Area", min_value=185.2, max_value=4254.0)
    smoothness_worst = st.sidebar.number_input(label="Enter Worst Smoothness", min_value=0.07, max_value=0.23)
    compactness_worst = st.sidebar.number_input(label="Enter Worst Compactness", min_value=0.02, max_value=1.06)
    concavity_worst = st.sidebar.number_input(label="Enter Worst Concavity", min_value=0.00, max_value=1.252)
    concave_pts_worst = st.sidebar.number_input(label="Enter Worst Concave Points", min_value=0.00, max_value=0.3)
    symmetry_worst = st.sidebar.number_input(label="Enter Worst Symmetry", min_value=0.15, max_value=0.64)
    fractal_worst = st.sidebar.number_input(label="Enter Worst Fractal Dimension", min_value=0.05, max_value=0.21)

    user_data = {'mean radius': mean_radius,
                 'mean texture': mean_texture,
                 'mean perimeter': mean_perimeter,
                 'mean area': mean_area,
                 'mean smoothness': mean_smoothness,
                 'mean compactness': mean_compactness,
                 'mean concavity': mean_concavity,
                 'mean concave points': mean_concave_pts,
                 'mean symmetry': mean_symmetry,
                 'mean fractal dimension': mean_fractal,
                 'radius se': radius_se,
                 'texture se': texture_se,
                 'perimeter se': perimeter_se,
                 'area se': area_se,
                 'smoothness se': smoothness_se,
                 'compactness se': compactness_se,
                 'concavity se': concavity_se,
                 'concave points se': concave_pts_se,
                 'symmetry se': symmetry_se,
                 'fractal dimension se': fractal_se,
                 'radius worst': radius_worst,
                 'texture worst': texture_worst,
                 'perimeter worst': perimeter_worst,
                 'area worst': area_worst,
                 'smoothness worst': smoothness_worst,
                 'compactness worst': compactness_worst,
                 'concavity worst': concavity_worst,
                 'concave points worst': concave_pts_worst,
                 'symmetry worst': symmetry_worst,
                 'fractal dimension worst': fractal_worst}
    features = pd.DataFrame(user_data, index=[0])
    return features
