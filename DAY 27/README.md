# 🧠 Day 27 - NLP Essentials

This project demonstrates core NLP steps including tokenization, stop word removal, lemmatization, and POS tagging.

## 📄 Input

- `sample.txt` – contains sample English text.

## 🧰 Requirements

```bash
pip install 

Run this once to download necessary NLTK data:

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

▶️ Run

python nlp_essentials.py

🔍 Output
Cleaned text

Word tokens

Tokens after stopword removal

Lemmatized tokens

POS-tagged words