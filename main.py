"""
📝 Project 3: Bulk Image Renamer Script
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today's date]

🧠 Description:
This Python script automatically renames all image files in a folder to a clean and consistent format 
(e.g., image_1.png, image_2.png). It’s perfect for photographers, content creators, or developers 
who want to organize files neatly.

📦 Features:
- Detects all PNG, JPG, and JPEG files in the target folder
- Automatically renames files in sequence
- Keeps original file extensions intact

🧰 Tools & Modules Used:
- os: for directory and file operations

💡 How to Use:
1. Place all the image files in one folder.
2. Update `folder_path` to that folder’s location.
3. Run the script.
4. Files will be renamed as image_1.png, image_2.png, etc.

✅ Example:
Before: our services thfnexus.png  
         our services thfnexus2.png  
         our services thfnexus3.png  
After:  image_1.png, image_2.png, image_3.png

"""

import os

# ✅ Set your folder path where images are
folder_path = r"c:\Users\ads\Desktop\py\proj 3"

# ✅ Find only image files (supports png, jpg, jpeg)
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_files.sort()

# ✅ Rename files to image_1.png, image_2.png, ...
for index, file in enumerate(image_files, start=1):
    old_path = os.path.join(folder_path, file)
    ext = os.path.splitext(file)[1]  # Get original extension
    new_filename = f"image_{index}{ext}"
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)
    print(f"🔁 {file} → {new_filename}")

print("✅ All images renamed successfully!")
