import streamlit as st

# Title
st.title("Customer Churn Prediction")

# Upload data
uploaded_file = st.file_uploader("C:\Users\shan2\pandas\Churn.csv", type="csv")
if uploaded_file:
    input_data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:", input_data.head())

    # Preprocess and predict
    input_data = scaler.transform(input_data)  
    predictions = model.predict(input_data)
    st.write("Predictions:", predictions)
