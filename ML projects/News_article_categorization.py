# Step 1: Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load dataset
data = pd.read_csv(r"C:\ML-models\ML projects\bbc-text.csv")

# Step 3: View dataset information
print("Sample Data:\n", data.head())
print("\nCategories:", data['category'].unique())

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['category'], test_size=0.2, random_state=42)

# Step 5: Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Step 6: Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Step 7: Predict categories on the test data
y_pred = model.predict(X_test_tfidf)

# Step 8: Evaluate model performance
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Step a: Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

# Step b: Display the confusion matrix
disp.plot(cmap="Blues", xticks_rotation=45)

# Step 9: Test the model with a custom article
test_article = ["The government passed a new policy regarding foreign investments."]
test_tfidf = vectorizer.transform(test_article)
prediction = model.predict(test_tfidf)
print("\nPredicted Category for Sample Article:", prediction[0])

# Step 10: Test the model with multiple custom news articles
test_articles = [
    "India's GDP growth rate has surpassed major global economies.",
    "The football team won their third championship title this year.",
    "NASA announced the discovery of water on Mars in their latest mission.",
    "The stock market saw significant growth after the latest tech boom.",
     "Apple unveiled its latest iPhone model featuring AI-powered tools.",
    "The new superhero movie broke box office records this weekend."
]

# Transform and predict
test_tfidf = vectorizer.transform(test_articles)
predictions = model.predict(test_tfidf)

# Display predictions
print("\n Model Predictions on Sample Articles:")
for article, category in zip(test_articles, predictions):
    print(f"\n Article: {article}\n Predicted Category: {category}")