# AI Agent Model Locally

An interactive, local AI chatbot interface powered by Streamlit and served via Ollama using the Qwen model.

## 🚀 Dev Stacks
* **AI Model:** Qwen 3.5 (9B Parameter)
* **Local Backend:** Ollama
* **Frontend UI:** Streamlit

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following prerequisites installed on your system.

### 1. Ollama Setup
1. Download and install Ollama from [ollama.com](https://ollama.com).
2. Open your terminal and pull the model locally:
   ```bash
   ollama run qwen3.5:9b
   ```
3. Keep the Ollama application or service running in the background.

### 2. Python Environment
Ensure you are using a stable Python release (Python 3.10 to 3.13 is recommended).

---

## 📦 Installation & Setup

Follow these steps to set up your local development environment.

1. **Clone or navigate to your project directory:**
   ```bash
   cd your-project-folder
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Create environment
   python -m venv .venv

   # Activate environment (Windows)
   .venv\Scripts\activate

   # Activate environment (macOS/Linux)
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install streamlit ollama
   ```

---

## 🏃 How to Run the App

1. Ensure your virtual environment is active and Ollama is running.
2. Launch the Streamlit application interface:
   ```bash
   streamlit run app.py
   ```
3. Your browser will automatically open to `http://localhost:8501` to display your local AI agent.
