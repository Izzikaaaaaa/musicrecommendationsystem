import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


st.set_page_config(page_title="SoulSync", page_icon="🎶", layout="wide")


st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ffdee9, #b5fffc);
            font-family: 'Poppins', sans-serif;
        }
        .main {
            background: transparent;
        }
        h1, h2, h3, h4, h5 {
            color: #3a3a3a;
            text-align: center;
            font-weight: 700;
        }
        .song-card {
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 18px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .song-card:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .recommend-title {
            color: #5a189a;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("spotify_songs.csv")
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

df = load_data()


def create_similarity(df):
    df["combined_features"] = (
        df["Singer/Artists"].fillna('') + " " +
        df["Genre"].fillna('') + " " +
        df["Album/Movie"].fillna('') + " " +
        df["Language"].fillna('')
    )

    vectorizer = TfidfVectorizer(stop_words='english')
    feature_matrix = vectorizer.fit_transform(df["combined_features"])
    similarity = cosine_similarity(feature_matrix)
    return similarity

similarity = create_similarity(df)


def recommend(song_name, df, similarity):
    song_name = song_name.strip().lower()
    if song_name not in df["Song-Name"].str.lower().values:
        return None

    idx = df[df["Song-Name"].str.lower() == song_name].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_songs = sorted(scores, key=lambda x: x[1], reverse=True)
    top_songs = sorted_songs[1:7]

    recommended = []
    for i in top_songs:
        s = df.iloc[i[0]]
        recommended.append({
            "name": s["Song-Name"],
            "artists": s["Singer/Artists"],
            "album": s["Album/Movie"],
            "genre": s["Genre"],
            "rating": s["User-Rating"]
        })
    return recommended


st.title("🎧 SoulSync")
st.markdown("<h3>Find songs that match your vibe — Hindi & English both!</h3>", unsafe_allow_html=True)

song_input = st.text_input("✨ Enter a song name:", placeholder="e.g. Tum Hi Ho or Perfect")

if song_input:
    recs = recommend(song_input, df, similarity)
    if recs is None:
        st.error("😔 No recommendations found for that song. Try another one!")
    else:
        st.markdown("<div class='recommend-title'>🎶 Recommended Songs for You</div>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i, song in enumerate(recs):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="song-card">
                        <h4>{song['name']}</h4>
                        <p><b>Artists:</b> {song['artists']}</p>
                        <p><b>Genre:</b> {song['genre']}</p>
                        <p><b>Album/Movie:</b> {song['album']}</p>
                        <p>⭐ {song['rating']}/5</p>
                    </div>
                """, unsafe_allow_html=True)
else:
    st.info("👆 Type a song name above to get recommendations!")


st.markdown("<br><center>Made with 💜 by SoulSync</center>", unsafe_allow_html=True)
