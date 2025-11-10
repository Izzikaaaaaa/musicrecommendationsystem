# 🎧 SoulSync — Music Recommendation System

SoulSync is an intelligent **music recommendation web app** built using **Machine Learning (ML)** and **Streamlit**.  
It recommends **similar Hindi and English songs** based on the song you enter — helping you discover new tracks that match your vibe. 💫

---

## 🚀 Features

- 🎶 **Smart Music Recommendations** using ML (TF-IDF + Cosine Similarity)
- 🌈 **Beautiful Spotify-like UI** with custom gradient design
- 🧠 **Content-Based Filtering** (no user data required)
- ⚡ Fast, interactive app powered by **Streamlit**
- 💬 Supports both **English and Hindi songs**

---

## 🧠 How the Machine Learning Works

This project uses **Content-Based Filtering** with the following ML steps:

1. **Feature Extraction (TF-IDF Vectorizer)**  
   Converts text data (artist, genre, album, language) into numerical vectors.

2. **Similarity Calculation (Cosine Similarity)**  
   Measures how similar two songs are based on their combined features.

3. **Recommendation Generation**  
   Finds top 5–6 songs that are closest to the selected song in feature space.

> 🧩 No deep learning or training data needed — it’s an unsupervised ML approach.

---

## 🏗️ Tech Stack

| Layer | Technologies Used |
|--------|--------------------|
| **Frontend (UI)** | Streamlit, HTML/CSS (custom styling) |
| **Backend / Logic** | Python |
| **Machine Learning** | scikit-learn (`TfidfVectorizer`, `cosine_similarity`) |
| **Data** | CSV file (`spotify_songs.csv`) |
| **Visualization (Optional)** | Matplotlib (for clustering plots if added later) |

---

## 📦 Project Structure

📁 SoulSync/
│
├── app.py # Main Streamlit app
├── spotify_songs.csv # Songs dataset (Hindi + English)
├── README.md # Project documentation
└── requirements.txt # Dependencies



❤️ Credits

Dataset curated with Hindi & English popular songs

ML model: TF-IDF + Cosine Similarity

UI Design: Custom gradient theme with Streamlit

Developed by ishika singh  ✨

🧩 Future Enhancements

🎵 Audio feature-based similarity using Spotify API

🧠 Deep Learning embeddings for improved recommendations

🎨 Album cover image display

👤 User-based collaborative filtering
