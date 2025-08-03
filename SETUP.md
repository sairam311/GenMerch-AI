# 🚀 GenMerch-AI Setup Guide

<div align="center">

### Complete Installation & Configuration Instructions

*Get GenMerch-AI running in under 5 minutes*

</div>

---

## 📋 Prerequisites

Before starting, ensure you have the following installed on your system:

### Required Software

| Software | Version | Download Link | Verification Command |
|----------|---------|---------------|---------------------|
| **Python** | 3.8+ | [python.org](https://python.org/downloads) | `python --version` |
| **Node.js** | 16+ | [nodejs.org](https://nodejs.org/download) | `node --version` |
| **Git** | Latest | [git-scm.com](https://git-scm.com/downloads) | `git --version` |
| **pip** | Latest | Included with Python | `pip --version` |
| **npm** | Latest | Included with Node.js | `npm --version` |

### API Account Requirements

You'll need accounts and API keys for:

| Service | Purpose | Cost | Sign-up Link |
|---------|---------|------|--------------|
| **Groq** | AI text generation | Free tier available | [console.groq.com](https://console.groq.com) |
| **OpenAI** | Image generation | Pay-per-use (~$0.04/image) | [platform.openai.com](https://platform.openai.com) |

---

## ⚡ Quick Setup

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/sairam311/GenMerch-AI.git

# Navigate to project directory
cd GenMerch-AI
```


### Step 2: Install Python Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install required packages
pip install openai groq python-dotenv requests

```

### Step 3: Install Node.js Dependencies

```bash
# Initialize package.json (if not exists)
npm init -y

# Install required packages
npm install express body-parser

```
---

## 🔑 API Key Setup

### Step 1: Create Environment File

```bash
# Create .env file in project root
.env
```

### Step 2: Configure API Keys

Add the following to your `.env` file:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# OpenAI API Configuration  
OPENAI_API_KEY=your_openai_api_key_here

```

### Step 3: Obtain API Keys

#### 🤖 Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in to your account
3. Navigate to **API Keys** section
4. Click **Create API Key**
5. Copy the key (starts with `gsk_...`)
6. Replace `your_groq_api_key_here` in `.env`

#### 🎨 OpenAI API Key

1. Visit [platform.openai.com](https://platform.openai.com)
2. Sign up or log in to your account
3. Go to **API Keys** in your dashboard
4. Click **Create new secret key**
5. Copy the key (starts with `sk-...`)
6. Replace `your_openai_api_key_here` in `.env`

**💡 Pro Tip:** Add some initial credit to your OpenAI account (~$5-10 is sufficient for testing)


---

## 🚀 Running the Application

### Method 1: Full Automated Pipeline (Recommended)

Run these commands in **separate terminal windows**:

#### Terminal 1: Start Mock Server
```bash
# Navigate to project directory
cd GenMerch-AI
cd publisher

# Start the mock publishing server
node server.js
```
**Expected output:** `📡 Fake product publisher running at http://localhost:4000`

#### Terminal 2: Start Web Server
```bash
# Start local web server for mockup visualizer
# Option 1: Using Python
python -m http.server 5500

# Option 2: Using Node.js (if http-server is installed)
npx http-server -p 5500

# Option 3: Use VS Code Live Server extension
# Right-click on mockup_visualizer/index.html -> "Open with Live Server"
```
**Expected output:** Web server running on `http://localhost:5500`

#### Terminal 3: Run Main Application
```bash
# Run the complete GenMerch-AI pipeline
python orchestrator/orchestrator.py
```

### Method 2: Step-by-Step Execution

```bash
# Step 1: Generate product content and image only
python product_generator/app.py

# Step 2: Start mock server (in separate terminal)
node server.js

# Step 3: Start web server (in separate terminal)
python -m http.server 5500

```

---

## ✅ What Happens When You Run the Application

When you execute `python orchestrator/orchestrator.py`, the system will:

1. **🤖 Generate Product Idea**
   - Uses Groq AI to create unique product concept
   - Generates title, description, and tags
   - Saves as `product_info.json`

2. **🎨 Create Product Image**  
   - Uses OpenAI DALL-E 3 to generate product image
   - Saves as `product_image.png`

3. **📡 Simulate Publishing**
   - Sends product data to mock server
   - Receives fake product ID and timestamp

4. **🌐 Launch Visualization**
   - Automatically opens browser
   - Displays interactive mockup with your generated product
   - Shows product details in JSON format


