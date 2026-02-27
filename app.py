import streamlit as st
from recommendation_engine import predict_style_and_accessories

st.set_page_config(page_title="StyleSense AI", layout="wide")

st.title("✨ StyleSense AI – Intelligent Fashion Stylist")
st.markdown("Fill details and get AI-powered styling suggestions 👇")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 18, 60, 25)
    body_type = st.selectbox("Body Type", ["Slim", "Athletic", "Average", "Curvy"])
    skin_tone = st.selectbox("Skin Tone", ["Fair", "Medium", "Dark", "Wheatish"])
    occasion = st.selectbox("Occasion", ["Casual", "Hangout", "Wedding", "Festival", "Office", "Party", "Evening Event", "Brunch", "Cultural Event", "Social Event", "Gym"])
    season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])
    personality = st.selectbox("Personality", ["Calm", "Professional", "Trendy", "Traditional", "Bold", "Energetic", "Creative"])

with col2:
    height_category = st.selectbox("Height Category", ["Short", "Medium", "Tall"])
    profession = st.selectbox("Profession", ["Student", "Doctor", "Engineer", "Designer", "Manager", "Lawyer", "Entrepreneur", "Freelancer"])
    budget = st.slider("Budget", 10000, 50000, 25000)
    color_preference = st.selectbox("Color Preference", ["Bright", "Neutral", "Pastel", "Dark"])
    sustainability_preference = st.selectbox("Sustainability Preference", [0, 1])
    trend_interest = st.selectbox("Trend Interest", ["Low", "Medium", "High"])

if st.button("Generate Styling Plan"):

    user_input = {
        "gender": gender,
        "age": age,
        "profession": profession,
        "body_type": body_type,
        "skin_tone": skin_tone,
        "height_category": height_category,
        "personality": personality,
        "occasion": occasion,
        "season": season,
        "budget": budget,
        "color_preference": color_preference,
        "sustainability_preference": sustainability_preference,
        "trend_interest": trend_interest
    }

    style, accessories = predict_style_and_accessories(user_input)

    st.subheader(f"🎯 Predicted Style: {style}")
    st.subheader("🧥 Outfit & Accessories")

    for key, value in accessories.items():
        if key not in ["style", "gender"]:
            st.markdown(f"**{key}** : {value}")