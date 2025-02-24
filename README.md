# AI Image Generator using Stable Diffusion  

This project is a Python-based **AI Image Generator** that interacts with the **Stable Diffusion WebUI API** to create images from text prompts. 
It automates the process of sending requests, retrieving generated images, and displaying or saving them.

## Features  
- Uses **Stable Diffusion WebUI API** for AI-based image generation  
- Allows customization of **steps, resolution, CFG scale, and sampler**  
- Automatically decodes and saves generated images  
- Displays images using **Pillow (PIL)**  

## 🛠️ Installation  
### **1. Install Dependencies**  
Ensure you have Python installed (recommended: **Python 3.11.2**). Then, install required libraries:  
pip install requests pillow



**2. Run the Script**
Start the Stable Diffusion WebUI (running on http://127.0.0.1:7860/), then execute:
python generate_image.py
