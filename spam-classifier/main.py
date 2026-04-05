# Importing libraires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Loadiung dataset
df = pd.read_csv("dataset.csv",sep="\t", names=["label", "message"])
df["label"] = df["label"].map({"ham":0,"spam": 1})

# Split features and target
X = df["message"]
y = df["label"]

# Split train test
X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Converting text to numbers 
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# msg = ["Win a  FREE MacBool now!! Limited offer"]
# msg = ["Congratulations! You have won a prize. Claim now."]
msg = ["Hey, are we meeting tomorrow?"]
msg_vec = vectorizer.transform(msg)
prediction = model.predict(msg_vec)
print("Spam" if prediction[0] ==1 else "Not Spam")
