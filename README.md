# ✨ StyleSense AI –  Personalized Fashion Recommendation System

StyleSense AI is a machine learning-powered web application that provides personalized fashion styling suggestions based on user attributes like gender, body type, occasion, and personality.

## 🚀 Live Demo
You can try the live app here: 
**[👉 Click here to open StyleSense AI](https://my-stylist-ai.streamlit.app)**

---

## 🛠️ Features
- **Personalized Recommendations**: Suggests outfits based on 10+ user inputs (Age, Body Type, Skin Tone, etc.).
- **Occasion-Specific**: Tailored advice for Weddings, Office, Gym, Parties, and more.
- **AI-Powered**: Uses a trained Scikit-Learn model to predict the best fashion style.
- **Dynamic Accessories**: Fetches matching accessories from a custom dataset.

## 📂 Project Structure
```text
stylesenseai/
├── app.py                # Main Streamlit UI
├── recommendation_engine.py # Prediction logic & preprocessing
├── requirements.txt      # Required Python libraries
├── models/               # Trained ML models (.pkl files)
└── data/                 # Accessories dataset (.csv)
