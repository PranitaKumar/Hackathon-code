import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv(r"C:\Users\Pranita\Desktop\datasets\dotathegreat.csv")  # Replace with the path to your dataset

# Assuming your dataset has features and a label column
X = df.drop("label_column_name", axis=1)  # Features
y = df["label_column_name"]  # Labels

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-means clustering
kmeans = KMeans(n_clusters=2)  # Assuming there are 2 clusters: ransomware and non-ransomware
kmeans.fit(X_scaled)

# Get cluster labels
cluster_labels = kmeans.labels_

# Add cluster labels to DataFrame
df["Cluster"] = cluster_labels

# Assuming ransomware files are assigned to cluster 1
ransomware_files = df[df["Cluster"] == 1]

# Display ransomware files
print("Ransomware Files:")
print(ransomware_files)
