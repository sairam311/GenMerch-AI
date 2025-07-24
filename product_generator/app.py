import os
import json
import openai
import requests
from groq import Groq
from dotenv import load_dotenv

# Load API keys
load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_product_details():
    prompt = (
        "Create a creative and catchy ecommerce product idea. "
        "Return the result as JSON with the following fields:\n"
        "- title (string)\n- description (2-3 lines)\n- tags (array of 3 relevant tags)\n"
    )
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a creative AI that designs unique, marketable ecommerce product ideas in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=512
        )
        message = response.choices[0].message.content
        print("LLM Response:\n", message)
        return message
    except Exception as e:
        print("Error generating product details:", e)
        return None

def parse_product_json(product_text):
    try:
        start = product_text.find("{")
        end = product_text.rfind("}") + 1
        json_str = product_text[start:end]
        return json.loads(json_str)
    except Exception as e:
        print("JSON parse error:", e)
        return None

def generate_image_dalle(prompt_text):
    print(f"Generating image with DALL·E for: '{prompt_text}'")

    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=f"ecommerce product design of '{prompt_text}' on a plain white background, centered, high quality",
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        image_data = requests.get(image_url).content

        with open("product_image.png", "wb") as f:
            f.write(image_data)

        print("✅ Image saved as product_image.png")
        return "product_image.png"
    except Exception as e:
        print("Image generation error:", e)
        return None

if __name__ == "__main__":
    product_text = generate_product_details()
    if product_text:
        product = parse_product_json(product_text)
        if product:
            with open("product_info.json", "w") as f:
                json.dump(product, f, indent=2)
            image_path = generate_image_dalle(product.get("title", "cool ecommerce product design"))
        else:
            print("Failed to parse product JSON.")
    else:
        print("Failed to generate product details.")
