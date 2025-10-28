import os
import numpy as np
from collections import defaultdict

def organize_files(directory="."):
    """
    Organizes files by extension and prints a summary using NumPy arrays.
    """
    file_summary = defaultdict(int)

    # Loop through all files
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            ext = os.path.splitext(file)[1].lower() or "no_extension"
            file_summary[ext] += 1

    # Convert dictionary to NumPy array for structured output
    summary_array = np.array(list(file_summary.items()))
    print("\n📁 File Type Summary:\n", summary_array)

if __name__ == "__main__":
    path = input("Enter folder path (press Enter for current folder): ") or "."
    organize_files(path)
