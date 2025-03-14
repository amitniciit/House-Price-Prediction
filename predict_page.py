import streamlit as st
import pickle
import numpy as np
import time 

def load_model():
    with open('saved_stepsHouse.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

models = load_model()



def show_predict_page():
    st.title("Housing Price Prediction")

    st.write("""### We need some information to predict the pricing""")

show_predict_page()

# Sidebar for Inputs
st.sidebar.header("Input Features")

furnishing_options = ("furnished", "semi-furnished", "unfurnished")
furnishing = st.sidebar.selectbox("Furnishing", furnishing_options)
furnishing_value = furnishing_options.index(furnishing)

Area = st.sidebar.slider("Area (sq. ft.)", 1650, 16200, 2000)
Bedroom = st.sidebar.selectbox("Bedrooms", (1, 2, 3, 4, 5))
Bathroom = st.sidebar.selectbox("Bathrooms", (1, 2, 3, 4))
Stories = st.sidebar.selectbox("Stories", (1, 2, 3, 4))
Mainroad = st.sidebar.selectbox("Mainroad Access", (0, 1))
Guestroom = st.sidebar.selectbox("Guestroom Available", (0, 1))
Basement = st.sidebar.selectbox("Basement", (0, 1))
Hotwaterheating = st.sidebar.selectbox("Hot Water Heating", (0, 1))
Airconditioning = st.sidebar.selectbox("Air Conditioning", (0, 1))
Parking = st.sidebar.selectbox("Parking Spaces", (0, 1, 2, 3))
Prefarea = st.sidebar.selectbox("Preferred Area", (0, 1))

# Model Selection
model_choice = st.sidebar.selectbox("Choose Regression Model", list(models.keys()))
selected_model = models[model_choice]

print(list(models.keys()))
print("Available models:", models.keys())
print(type(models))  
# Main Page
st.title("🏡 House Price Prediction")
st.write("### Enter the details in the sidebar to predict the house price.")

# Predict Price Button
if st.sidebar.button("Predict Price"):
    X = np.array([[furnishing_value, Area, Bedroom, Bathroom, Stories, Mainroad, 
                   Guestroom, Basement, Hotwaterheating, Airconditioning, Parking, Prefarea]])
    X = X.astype(float)

    # Show a spinner while predicting
    with st.spinner("🔄 Predicting house price... Please wait"):
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)  # Simulate loading time
            progress_bar.progress(percent_complete + 1)

    
    price = selected_model.predict(X)
    
    st.subheader(f"🏠 Estimated House Price: ₹ {price[0]:,.2f}")