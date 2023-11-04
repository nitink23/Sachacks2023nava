from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import json
processed_data =[]

with open("technology_keywords.json", "r") as f:
    processed_data = json.load(f)


# Step 2: Vectorize the data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_data)
print(X)

# Reduce the dimensionality using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())

# Step 3: Apply DBSCAN clustering algorithm
dbscan = DBSCAN(eps=0.001, min_samples=2)  # Adjust the parameters as needed
dbscan.fit(X)

# Step 4: Get the cluster labels
cluster_labels = dbscan.labels_

# Print the cluster labels for each text
for text, label in zip(processed_data, cluster_labels):
    print(f"{text}: Cluster {label}")
