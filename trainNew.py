import numpy as np
import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

def load_features(features_root, split):
    all_vectors, all_labels = [], []
    split_path = os.path.join(features_root, split)
    for file in os.listdir(split_path):
        if file.endswith('_vectors.npy'):
            species = file.replace('_vectors.npy', '')
            vectors = np.load(os.path.join(split_path, file))
            labels = np.load(os.path.join(split_path, file.replace('_vectors', '_labels')))
            all_vectors.append(vectors)
            all_labels.append(labels)
    return np.concatenate(all_vectors), np.concatenate(all_labels)

X_train, y_train = load_features('training_data/features', 'train')
X_val, y_val = load_features('training_data/features', 'val')
X_test, y_test = load_features('training_data/features', 'test')

encoder = LabelEncoder()
encoder.fit(y_train)

fallback_classifier = LogisticRegression(max_iter=1000, C=1.0)
fallback_classifier.fit(X_train, encoder.transform(y_train))

print(f"Validation: {fallback_classifier.score(X_val, encoder.transform(y_val))*100:.2f}%")
print(f"Test: {fallback_classifier.score(X_test, encoder.transform(y_test))*100:.2f}%")

with open('florida_fallback.pkl', 'wb') as f:
    pickle.dump({'classifier': fallback_classifier, 'encoder': encoder}, f)