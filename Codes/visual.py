import numpy as np

# Load the files
X_long = np.load("datasets/mHealth_X_long.npy")
y_long = np.load("datasets/mHealth_y_long.npy")
y_seg_long = np.load("datasets/mHealth_y_seg_long.npy")
file_boundaries = np.load("datasets/mHealth_file_boundaries.npy")

# Print the shape of the arrays
print("X_long shape:", X_long.shape)  # Feature matrix shape
print("y_long shape:", y_long.shape)  # Labels shape
print("y_seg_long shape:", y_seg_long.shape)  # Segmented labels
print("File Boundaries:", file_boundaries)  # File split points

# View some data samples
print("First 5 feature rows:\n", X_long[:5])
print("First 5 labels:\n", y_long[:5])


