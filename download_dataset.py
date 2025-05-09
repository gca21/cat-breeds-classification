import kagglehub
import os


# Download latest version
path = kagglehub.dataset_download("nikolasgegenava/cat-breeds")

os.system(f"mv {path} ./dataset")
