import numpy as np
import os

# Path to the metadata folder
metadata_path = "metadata"

# List all .npy files in the metadata folder
npy_files = [f for f in os.listdir(metadata_path) if f.endswith(".npy")]

# Loop through each file and print its content
for file in npy_files:
    file_path = os.path.join(metadata_path, file)
    
    # Load with allow_pickle=True
    data = np.load(file_path, allow_pickle=True)
    
    print(f"Contents of {file}:")
    print(data, "\n")  # Print with spacing for readability



file_path = "metadata\mHealth_MSTCN_noplatprob_random_0.8_10_2.0_0.npy"
data = np.load(file_path, allow_pickle=True)

# Unpack the structure
timing_info = data[0]
more_metrics = data[1]
detailed_metrics = data[2]  # This seems to contain meaningful per-class or per-epoch data
true_labels = data[3]
prediction_confidences = data[4]
losses = data[5]
padding_or_placeholder = data[6]

# For example, print the first few "detailed metrics"
print("Sample of detailed metrics:")
for i, arr in enumerate(detailed_metrics[:3]):
    print(f"Metric {i}:", arr)
