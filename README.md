# 📸 Automated Screenshot Processor

A Python automation script that captures a screenshot, applies multiple image-processing transformations, and archives the final result into a ZIP file for efficient storage.

---

## 🚀 About My Learning Journey

I am a *Computer Engineering graduate* and currently a *trainee at Tuwaiq Academy (Software Development Bootcamp)*.  
This project represents a practical milestone in my learning journey, where I focus on:

•⁠  ⁠✅ *Professional Workflow:* Applying clean coding standards and proper project structure.

•⁠  ⁠✅ *Modern Tooling:* Using AI-assisted tools to accelerate learning, debug efficiently, and follow industry best practices.

•⁠  ⁠✅ *Automation:* Building scripts that perform real-world file and image processing tasks programmatically.

This repository reflects my commitment to continuous learning and building a solid foundation in software development.

---

## 🛠 Features

•⁠  ⁠📸 *Screen Capture:* Automatically captures a screenshot after a 3-second delay.


•⁠  ⁠🎨 *Image Processing:*
  - Mirrors the image horizontally.
  - Inverts the colors (negative effect).
  - Converts the image to Grayscale (Black & White).
    
•⁠  ⁠📦 *Archiving:* Compresses the processed image into a ⁠ .zip ⁠ file.

•⁠  ⁠🧹 *Auto-Cleanup:* Deletes the temporary image file after archiving.

---

## 📂 Project Structure

```bash
.
├── screen_process.py
├── README.md
```

---

## 📦 Dependencies


install the required libraries before running the project:

`pip install pyautogui Pillow`


---

## 💻 How to Run

1.⁠ ⁠Clone the repository:
`git clone <MY_REPO_URL>`

2.⁠ ⁠Navigate to the project directory:
`cd <your-project-folder>`

3.⁠ ⁠Run the script:
`python screen_process.py`


> A ZIP file containing the processed screenshot will be generated automatically.


---

## ✅ Output

•⁠  `⁠screenshot_archive.zip`
Contains the final mirrored, inverted, and grayscale screenshot.


---

## 🌱 Future Improvements

•⁠  ⁠Add GUI interface.

•	Support multiple image filters.

•	Add logging instead of print statements.

•	Cross-platform path handling enhancement




>“Understanding the workflow is the real key to mastering development.”

