# app.py
import streamlit as st
from mood_detector import predict_mood, use_ml
from food_recommender import recommend_food

st.set_page_config(page_title="Mood → Food Recommender", layout="centered")

st.title("🍽 Mood → Food Recommender (ML demo)")
st.write("Type how you feel and the app will predict your mood and suggest foods.")

st.sidebar.header("Info")
if use_ml:
    st.sidebar.success("ML model loaded: predictions use the trained classifier.")
else:
    st.sidebar.info("ML model not found: using keyword fallback. Run `python train_model.py` to train the model.")

num = st.sidebar.slider("Number of suggestions", 1, 5, 3)
st.sidebar.markdown("---")
st.sidebar.markdown("Acknowledgement: Parts of the project were assisted by OpenAI ChatGPT. All final implementation and dataset choices were made by the team.")

user_text = st.text_area("Describe how you feel (one sentence is fine):", height=120)

if st.button("Recommend"):
    if not user_text.strip():
        st.warning("Please write something about your mood.")
    else:
        mood = predict_mood(user_text)
        st.subheader(f"Detected mood: **{mood}**")
        suggestions = recommend_food(mood, k=num)
        st.write("### Food suggestions:")
        for i, s in enumerate(suggestions, start=1):
            st.write(f"{i}. {s}")

        # small bar chart of counts for transparency (simple demonstration)
        # compute simple scores with keyword fallback to show relative counts (student-level)
        # (this is optional and intentionally simple)
        st.markdown("---")
        st.caption("Note: This demo uses a simple TF-IDF + classifier. See README for training instructions.")
