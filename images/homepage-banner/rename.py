import os

# Folder contain images
folder = "./"

# Get files with format banner{i}.jpg
image_files = []

for fname in os.listdir(folder):
    if fname.startswith("banner") and fname.endswith(".jpg"):
        try:
            idx = int(fname[len("banner"):-len(".jpg")])
            image_files.append(idx)
        except ValueError:
            pass

# Sort descent to avoid overwriting
image_files.sort(reverse=True)

# Rename banner{i}.jpg -> banner{i+1}.jpg
for idx in image_files:
    old_path = os.path.join(folder, f"banner{idx}.jpg")
    new_path = os.path.join(folder, f"banner{idx + 1}.jpg")

    os.rename(old_path, new_path)
    print(f"{old_path} -> {new_path}")