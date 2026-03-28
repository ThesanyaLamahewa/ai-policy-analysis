# ai-policy-analysis
AI-assisted policy analysis using data science techniques
Overview

PolicyAI Studio is an AI-powered web application designed to support policy analysis using Natural Language Processing (NLP) and Generative AI.

The system analyzes real-world government policy documents and provides:

Concise summaries using NLP techniques
AI-generated policy drafts for different scenarios
A combination of extractive and abstractive summarization

This project demonstrates how AI can enhance policy understanding, evaluation, and decision-making.

Key Features
Policy Summarization
Extractive summarization using NLP techniques
Abstractive summarization using AI models

Policy Generation
Generates scenario-based policy drafts using Generative AI

Real-World Application
Uses National Digital Economy Strategy 2030 (Sri Lanka) as the case study

Technologies Used

Python
Flask (for web application)
SpaCy (NLP processing)
Generative AI (Groq API)
Environment Variables (.env)

Supporting modules:
summariser.py
generator.py
utils.py

Methodology

Input Policy Document
A real government policy document is used

Extractive Summarization
Key sentences are extracted using NLP

Abstractive Summarization
AI generates a refined, human-like summary

Policy Generation
AI creates scenario-based policy recommendations

Key Insights
AI can significantly improve the efficiency of policy analysis
Combining extractive + abstractive methods produces better summaries
Generative AI enables adaptive and scenario-based policymaking
