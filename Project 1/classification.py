import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# -------------------- Page Config --------------------
st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

# -------------------- Custom CSS --------------------
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .sub-text {
        font-size: 18px;
        color: #555;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🌸 Iris Flower Classifier</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Adjust the sliders and predict the species</p>', unsafe_allow_html=True)

# -------------------- Load Data --------------------
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# -------------------- Train Model --------------------
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# -------------------- Sliders --------------------
st.header("🔧 Input Features")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width  = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.3)
petal_width  = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)
# -------------------- Prediction --------------------
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.success(f"🌼 Predicted Species: **{predicted_species.upper()}**")
