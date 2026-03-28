# PolicyAI Studio 🏛️
**LB3114 Assignment I | KDU | Intake 41**  
**Data Science Applications and Artificial Intelligence**

**Student:** Thesanya Lamahewa  
**Registration Number:** D/ADC/24/0003

---

## Project Description

PolicyAI Studio is an AI-powered web application that:
- Summarises real government policy documents using NLP techniques
- Generates scenario-adapted policy drafts using Generative AI
- Demonstrates two-layer summarisation: Extractive (NLP) + Abstractive (AI)

**Policy Document Used:**  
National Digital Economy Strategy 2030 — Ministry of Technology, Sri Lanka

---

## How to Run

### Requirements
- Python 3.9 or higher
- Internet connection (for AI API)
- Groq API key (free to obtain)

### Installation

**Step 1 — Create virtual environment:**
```bash
python -m venv venv
```

**Step 2 — Activate virtual environment:**

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

**Step 3 — Install dependencies:**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**Step 4 — Set up your API key:**

You need a Groq API key to run this application. Follow these steps:

1. **Get a free Groq API key:**
   - Go to https://console.groq.com
   - Sign up for a free account
   - Navigate to "API Keys" section
   - Click "Create API Key"
   - Copy your API key

2. **Create a `.env` file in the project folder:**
   - In the same folder as `app.py`, create a new file
   - Name it exactly: `.env` (including the dot at the start)
   - Open it in a text editor (Notepad, VS Code, etc.)

3. **Add your API key to the `.env` file:**
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
   
   **Example:**
   ```
   GROQ_API_KEY=gsk_abc123xyz456def789
   ```

   **Important:**
   - Replace `your_actual_api_key_here` with your real API key
   - No spaces around the `=` sign
   - No quotes around the key
   - Save the file

4. **Verify your `.env` file:**
   - Make sure it's in the same folder as `app.py`
   - Make sure it's named `.env` (not `.env.txt`)
   - The file should contain exactly one line with your API key

**Step 5 — Run the application:**
```bash
streamlit run app.py
```

**Step 6 — Open browser at:**
```
http://localhost:8501
```

The application should now open in your default web browser!

---

## How to Use

1. Upload `policy.pdf` in the left panel
2. Adjust the NLP extraction depth slider (recommended: 8-10 sentences)
3. Click **"Run NLP Summarisation"**
4. View NLP pipeline steps, extracted keywords, and word cloud
5. Select a scenario from the right panel dropdown
6. Click **"Generate Adapted Policy Draft"**
7. Compare outputs across all 3 scenarios
8. Download summaries and drafts using download buttons

---

## Three Scenarios

| Scenario | Target Audience | Focus |
|---|---|---|
| **A: Rural Small Business Owner** | Farmers and MSMEs in rural Sri Lanka | Affordable internet, digital payments |
| **B: Foreign Tech Investor** | International investors | ICT exports, startup ecosystem |
| **C: Ministry of Education Policymaker** | Government education ministers | Digital skills, AI in schools |

Each scenario produces a uniquely adapted policy draft with different:
- Language style (simple vs. formal vs. governmental)
- Priorities (local business vs. ROI vs. education)
- Metrics and targets
- Tone and presentation

---

## Example Output

**Input:** National Digital Economy Strategy 2030 (48 pages, 12,847 words)

**NLP Summary (Layer 1 — Extractive):**
> 8-10 key sentences selected using spaCy frequency scoring normalized by sentence length

**AI Summary (Layer 2 — Abstractive):**
> 200-250 word coherent summary covering goals, measures and direction of the policy

**Scenario A Draft:**
> Simplified policy for rural business owners focusing on affordable broadband and MSME digitalization

**Scenario B Draft:**
> Formal investment-focused policy highlighting ICT export targets and regulatory framework

**Scenario C Draft:**
> Education-focused policy with measurable targets for digital skills in national curriculum

---

## Technologies Used

| Library | Purpose |
|---|---|
| `streamlit` | Web application framework |
| `spacy` | NLP sentence scoring and linguistic processing |
| `nltk` | Sentence tokenization and stopword filtering |
| `PyMuPDF` (fitz) | PDF text extraction |
| `groq` | Generative AI API (LLaMA 3.1 8B Instant) |
| `python-dotenv` | Environment variable management |
| `wordcloud` | Keyword visualization |
| `matplotlib` | Word cloud rendering |

---

## Technical Implementation

### Two-Layer Summarization Pipeline:

**Layer 1: Extractive NLP Summarization**
- Uses spaCy for linguistic processing
- Applies frequency-based sentence scoring
- **Key Innovation:** Normalizes scores by sentence length to prevent bias toward longer sentences
- Extracts the most information-dense sentences

**Layer 2: Abstractive AI Summarization**
- Uses LLaMA 3.1 via Groq API
- Transforms extracted sentences into coherent prose
- Captures goals, measures, and policy direction

### Scenario-Based Generation:
- Structured prompting with audience parameters
- Context-aware adaptation (tone, priorities, focus)
- Maintains policy formality while shifting emphasis
- Generates realistic metrics and targets

---

## Project Structure
```
policy_assignment/
├── app.py              # Main Streamlit web application
├── summariser.py       # NLP summarization pipeline (Layer 1)
├── generator.py        # AI scenario generation (Layer 2)
├── utils.py            # Text preprocessing utilities
├── requirements.txt    # Python dependencies
├── policy.pdf          # Source policy document
├── .env                # API key configuration (create this yourself)
└── README.md           # This file
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'groq'"
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### "API key error" or "Authentication failed"
**Solution:** 
1. Check that `.env` file exists in the project folder
2. Verify the API key is correct (no extra spaces or quotes)
3. Make sure the line in `.env` is: `GROQ_API_KEY=your_key_here`

### "No module named 'en_core_web_sm'"
**Solution:** Download the spaCy model:
```bash
python -m spacy download en_core_web_sm
```

### "Port 8501 is already in use"
**Solution:** Stop the previous instance or use a different port:
```bash
streamlit run app.py --server.port 8502
```

### PDF upload not working
**Solution:** Make sure `policy.pdf` is in the same folder as `app.py`

---

## Features

✅ **Two-layer summarization** (NLP + AI)  
✅ **Three distinct scenario adaptations**  
✅ **Interactive visualization** (word clouds, keyword extraction)  
✅ **NLP pipeline transparency** (shows preprocessing steps)  
✅ **Download functionality** (export summaries and drafts)  
✅ **Responsive UI** (custom CSS styling)  
✅ **Modular architecture** (separate files for summarization, generation, utilities)

---

## Assignment Compliance

This project demonstrates:
- ✅ Interpretation of real-world policy documents
- ✅ Text preprocessing and summarization using NLP
- ✅ Controlled use of Generative AI for context adaptation
- ✅ Translation of a single document into multiple scenario-specific outputs
- ✅ Functional web-based system integrating multiple AI components
- ✅ Clear technical implementation with well-documented code

---

## Author

**Thesanya Lamahewa**  
D/ADC/24/0003

General Sir John Kotelawala Defence University  
Bachelor of Science in Applied Data Science Communication  
Intake 41 | LB3114 Assignment I | 2026
