from tkinter import Image

import requests
import base64
from io import BytesIO
#from PIL import Image

# Set the WebUI API endpoint
API_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"


# Function to generate an image
def generate_image(prompt, steps=20, cfg_scale=7.5, width=512, height=512, sampler="Euler a"):
    # Payload for the API request
    payload = {
        "prompt": prompt,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "width": width,
        "height": height,
        "sampler_index": sampler
    }

    print(f"Sending request for prompt: {prompt}")
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        print("Image generation successful!")
        # Decode the base64 image
        image_data = response.json()["images"][0]
        image = Image.open(BytesIO(base64.b64decode(image_data)))

        # Save and display the image
        output_path = "generated_image.png"
        image.save(output_path)
        print(f"Image saved as {output_path}")
        return image
    else:
        print(f"Failed to generate image. Status code: {response.status_code}")
        print(response.text)
        return None


# Example prompt
prompt = "sun in the morning at the beach"
generated_image = generate_image(prompt)

# Display the generated image
if generated_image:
    generated_image.show()
