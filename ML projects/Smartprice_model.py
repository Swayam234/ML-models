import pandas as pd
import numpy as np
import re
train=pd.read_csv("C:\Users\Swayam\Documents\Amazon ML challenge\codes\train.csv")
test=pd.read_csv("C:\Users\Swayam\Documents\Amazon ML challenge\codes\test.csv")

#  Function to clean catalog_content
def clean_text(text):
    if isinstance(text, str):
        text = text.lower()                              # lowercase
        text = re.sub(r"<.*?>", " ", text)               # remove HTML tags
        text = re.sub(r"[^a-z0-9\s\-x]", " ", text)      # keep letters, numbers, -, x
        text = re.sub(r"\s+", " ", text).strip()         # remove extra spaces
        return text
    else:
        return ""
    
# Apply to both train and test
train["catalog_content_clean"] = train["catalog_content"].apply(clean_text)
test["catalog_content_clean"] = test["catalog_content"].apply(clean_text)

# Add text length feature
train["text_length"] = train["catalog_content_clean"].apply(lambda x: len(x.split()))
test["text_length"] = test["catalog_content_clean"].apply(lambda x: len(x.split()))
train["ipq"] = train["catalog_content_clean"].apply(extract_ipq)
test["ipq"] = test["catalog_content_clean"].apply(extract_ipq)

#  Extract Item Pack Quantity (IPQ)
def extract_ipq(text):
    match = re.search(r"(?:pack of|x)\s*(\d+)", text)
    if match:
        return int(match.group(1))
    else:
        return 1  # default 1 if not found

#  Remove invalid prices in training data
train = train[train["price"] > 0].copy()
#  Add log_price for stable model training (optional)
train["log_price"] = np.log1p(train["price"])
#  Final check
train.head(3)
test.head(3)

# Step 2: Feature engineering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Use both unigrams and bigrams
tfidf = TfidfVectorizer(max_features=50000, ngram_range=(1, 2))

# Fit on ALL text (train + test) so vector space is same
all_text = pd.concat([train["catalog_content_clean"], test["catalog_content_clean"]])
tfidf.fit(all_text)

# Transform train and test separately
X_train_tfidf = tfidf.transform(train["catalog_content_clean"])
X_test_tfidf = tfidf.transform(test["catalog_content_clean"])
print("TF-IDF shapes:", X_train_tfidf.shape, X_test_tfidf.shape)

svd = TruncatedSVD(n_components=200, random_state=42)
X_train_svd = svd.fit_transform(X_train_tfidf)
X_test_svd = svd.transform(X_test_tfidf)
print("TF-IDF modified shapes:", X_train_svd.shape,X_test_svd.shape)

X_train_num = train[["text_length", "ipq"]].to_numpy()
X_test_num = test[["text_length", "ipq"]].to_numpy()

# Combine text (SVD) + numeric features
X_train_final = np.hstack([X_train_svd, X_train_num])
X_test_final = np.hstack([X_test_svd, X_test_num])

print("Final feature shapes:", X_train_final.shape, X_test_final.shape)
y_train = train["price"].values  # or use train["log_price"]

import lightgbm
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Split data for validation (to check how good your model is)
X_tr, X_val, y_tr, y_val = train_test_split(X_train_final, y_train, test_size=0.2, random_state=42)

# Create and train model
model = LGBMRegressor(
    n_estimators=1000,
    learning_rate=0.05,
    max_depth=-1,
    num_leaves=64,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val)],
    eval_metric="mae",
    callbacks=[
        # early stopping and verbose are now inside callbacks
        lightgbm.early_stopping(stopping_rounds=50),
        lightgbm.log_evaluation(period=50)
    ]
)


# Validate on validation data
y_val_pred = model.predict(X_val)
mae = mean_absolute_error(y_val, y_val_pred)
print(f"Validation MAE: {mae:.2f}")

test_pred = model.predict(X_test_final)
test_pred = np.maximum(test_pred, 0)  # ensure no negative prices


