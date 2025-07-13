import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag

# Download required data (first-time only)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Read text
with open('sample.txt', 'r') as file:
    text = file.read()

# 1. Lowercase
text = text.lower()

# 2. Remove punctuation and special characters
text = re.sub(r'[^\w\s]', '', text)

# 3. Tokenize
tokens = word_tokenize(text)

# 4. Remove stopwords
filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]

# 5. Lemmatize
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# 6. POS Tagging
pos_tags = pos_tag(lemmatized)

# Output
print("📜 Original Text:\n", text)
print("\n🔹 Tokens:\n", tokens)
print("\n🔹 Filtered (No Stopwords):\n", filtered_tokens)
print("\n🔹 Lemmatized:\n", lemmatized)
print("\n🔍 POS Tags:\n", pos_tags)
