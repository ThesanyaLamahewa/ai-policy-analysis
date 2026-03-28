# 🏛️ PolicyAI Studio

An AI-powered policy analysis platform that summarizes complex policy documents and generates intelligent policy recommendations using NLP and Generative AI.



## 🚀 Features

* 📄 **Policy Summarization**

  * Extractive summarization using NLP
  * Abstractive summarization using AI for human-like insights

* 🤖 **AI Policy Generator**

  * Generates policy recommendations based on user-defined scenarios

* 🧠 **NLP-Powered Analysis**

  * Identifies key sentences and important policy content

* 📊 **Insight Extraction**

  * Helps understand large policy documents quickly and effectively

* ⚡ **Real-World Use Case**

  * Based on *National Digital Economy Strategy 2030 – Sri Lanka*

---

## 🛠️ Tech Stack

| Layer       | Technology                                    |
| ----------- | --------------------------------------------- |
| Backend     | Python, Flask                                 |
| AI/NLP      | SpaCy, Generative AI (Groq API)               |
| Processing  | Custom NLP Summarization                      |
| Frontend    | HTML, CSS, JavaScript                         |
| Environment | Python-dotenv                                 |


---

## 📁 Project Structure

```
policyai-studio/
├── app.py                # Main Flask application
├── summariser.py         # Extractive summarization logic
├── generator.py          # AI policy generation module
├── utils.py              # Helper functions
├── policy.pdf            # Input policy document
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (API keys)
└── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. **Policy Input**

   * A real-world policy document is provided as input

2. **Text Processing (NLP)**

   * SpaCy processes and cleans the text

3. **Extractive Summarization**

   * Key sentences are selected based on importance

4. **Abstractive Summarization**

   * AI generates a refined, human-like summary

5. **Policy Generation**

   * AI produces new policy ideas based on given scenarios

---

## 🔧 Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/policyai-studio.git
cd policyai-studio

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Create .env file
GROQ_API_KEY=your_api_key_here

# Run the app
python app.py
```

---

## 📊 Core Functionalities

| Feature        | Description                                 |
| -------------- | ------------------------------------------- |
| Summarization  | Extracts key insights from policy documents |
| AI Generation  | Produces scenario-based policy drafts       |
| NLP Processing | Cleans and analyzes policy text             |

---

## 🧠 Key Insight

* AI can significantly reduce the complexity of policy analysis
* Combining extractive and abstractive methods improves understanding
* Generative AI enables smarter, faster policymaking

## 👩‍💻 Author

**Thesanya Lamahewa**

* GitHub: [@ThesanyaLamahewa](https://github.com/ThesanyaLamahewa)



## 📄 License

This project is open source and available under the **MIT License**.



* Or help you **deploy it like your outbreak project** 🚀
