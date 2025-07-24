# GenMerch-AI

### 🛍️ AI-Powered Ecommerce Product Mockup Generator
This project demonstrates an end-to-end AI-powered pipeline that creates and visualizes ecommerce product ideas. It uses large language models (LLMs) to generate product content, OpenAI's DALL·E for visuals, and a browser-based mockup tool to display the final product. It also simulates a backend publishing flow for demo purposes.

---

## 📌 Features

- 🤖 **AI-Generated Product Ideas** — Uses Groq’s LLaMA 3.3 model to create unique ecommerce products with title, description, and tags.
- 🎨 **DALL·E-Driven Image Generation** — Automatically generates a matching product image using OpenAI’s DALL·E 3.
- 🖼️ **Browser-Based Visual Mockups** — Combines template and generated image using HTML5 Canvas.
- 🌐 **Fake Product Publisher** — Simulates publishing the product to a Node.js server endpoint with JSON output.
- 🧩 **Fully Modular Architecture** — Separated into orchestrator, generator, mockup, and server components for clarity and maintainability.

---

### Components

| Step | Description | Tech |
|------|-------------|------|
| 1    | Product idea & image generation | Python (Groq + DALL·E) |
| 2    | Visual mockup generator | JavaScript/HTML5 canvas |
| 3    | Fake publishing API | Node.js |
| 4    | Automation script | Python |

### How to Run
1. Install dependencies
2. Run `app.py` to test content generation
3. Launch `index.html` in a browser
4. Start the fake API: `node server.js`
5. Run `orchestrator.py` to simulate the full pipeline

### Sample Output
- Product JSON
- Mockup image
- Fake product ID returned from the publisher