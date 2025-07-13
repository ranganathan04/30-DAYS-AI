import re
import nltk
import heapq
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

# Load text
with open('sample_article.txt', 'r') as f:
    text = f.read()

# Clean text
text = re.sub(r'\s+', ' ', text)
sentences = sent_tokenize(text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(sentences)

# Score sentences by average TF-IDF
sentence_scores = {}
for i, sent in enumerate(sentences):
    score = X[i].toarray().sum()
    sentence_scores[sent] = score

# Get the top sentence (potential title)
best_sentence = heapq.nlargest(1, sentence_scores, key=sentence_scores.get)[0]

print("📝 Suggested Title:\n", best_sentence)
