import streamlit as st
import openai


st.markdown("""
<style>

    /* Set background and default text color */
    html, body, [data-testid="stApp"] {
        background-color: #1e1e1e;
        color: #ffffff;
    }

    /* Input field styling */
    input[type="text"] {
        background-color: #2a2a2a;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #444;
    }

    /* Select box container */
    div[data-baseweb="select"] {
        background-color: #2a2a2a;
        color: white;
        border-radius: 10px;
    }

    /* Selected value styling */
    div[data-baseweb="select"] > div {
        color: white !important;
        background-color: #2a2a2a !important;
    }

    /* Button styling */
    button[kind="primary"] {
        background-color: #ff4d6d;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        padding: 10px 16px;
        font-size: 15px;
        margin-top: 10px;
    }

    button[kind="primary"]:hover {
        background-color: #e0435d;
    }
    
    /* Center the button */
    div.stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    }

    label {
    color: #c084fc; /* purple — or use #60a5fa for blue */
    font-weight: bold;
    font-size: 1.05em;
    }

    /* Fix double border & style response box */
    .stMarkdown, .stText, .stContainer {
        border: none !important;
        box-shadow: none !important;
    }

    /* Optional: Style the “Your AI Bestie Says” box */
    .your-response-box {
        background-color: #223;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 1.1em;
        line-height: 1.6em;
        color: #d0e6ff;
    }

</style>
""", unsafe_allow_html=True)


# open ai api key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# app configuration
st.set_page_config(page_title="SlayTrackr", page_icon="💅")
st.markdown("""
<h1 style='text-align: center; font-size: 3em; color: #ff4d6d; text-shadow: 0 0 10px #ff4d6d;'>
💅 SlayTrackr
</h1>
""", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center; color: #f0a8c1; font-size: 1.1em; text-shadow: 0 0 6px #ff4d6d; margin-top: -10px;'>
Track your habits or mood... and get a ✨vibe check✨ from your AI bestie.
</p>
""", unsafe_allow_html=True)


# inputs
user_input = st.text_input("What did you do or how are you feeling?", placeholder="e.g., I drank water / I feel exhausted")

vibes = {
    "Delulu 💖": "Hype me up like a delusional bestie who lies to make me feel amazing.",
    "Tough Love 💪": "Speak like a strict coach or Nigerian aunty — no sugarcoating.",
    "Therapist 🧘‍♀️": "Respond like a gentle, emotionally supportive therapist.",
    "Drama Queen 👑": "React dramatically like a drag queen or reality show diva."
}

vibe_choice = st.selectbox("Choose your vibe:", list(vibes.keys()))


if st.button("Get Your Slay Response 💬"):
    if not user_input:
        st.warning("Tell me something first, bestie 💁‍♀️")
    else:
        system_prompt = vibes[vibe_choice]
        client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        ai_reply = response.choices[0].message.content.strip()

        st.markdown("""
        <h3 style='font-size: 1.6em; font-weight: bold; margin-top: 30px;'>💬 Your AI Bestie Says:</h3>
        """, unsafe_allow_html=True)
        st.markdown(f"<div class='your-response-box'>{ai_reply}</div>", unsafe_allow_html=True)


