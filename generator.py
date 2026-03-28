# generator.py
# This module uses Generative AI to create scenario-specific policy drafts
# Works with ANY uploaded policy document - not hardcoded to any specific policy

import os
from groq import Groq
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Define your 3 scenarios
SCENARIOS = {
    "Scenario A: Rural Small Business Owner": {
        "audience": "Small business owners and farmers in rural Sri Lanka",
        "priorities": "Affordable internet access, digital payment adoption, MSME digital support programs",
        "tone": "Simple, clear, and practical language avoiding technical jargon",
        "focus": "How this policy affects everyday business operations and rural livelihoods"
    },
    "Scenario B: Foreign Tech Investor": {
        "audience": "International technology investors and foreign financial institutions",
        "priorities": "Export potential, startup ecosystem, investment climate, regulatory framework",
        "tone": "Formal, data-driven, and internationally aligned language",
        "focus": "Return on investment potential and the country as a digital innovation hub"
    },
    "Scenario C: Ministry of Education Policymaker": {
        "audience": "Government education ministers and national curriculum designers",
        "priorities": "Digital skills in schools, AI education, youth workforce development, digital literacy",
        "tone": "Formal policy language with clear action items and measurable targets",
        "focus": "Building a future-ready digitally skilled generation"
    }
}


def generate_policy_draft(summary_sentences, scenario_name):
    """
    Generates an adapted policy draft for a given scenario.
    Works with any policy document — not hardcoded to any specific policy.

    Input:
        summary_sentences: list of key sentences from NLP summarization
        scenario_name: one of the 3 scenario keys above
    Output:
        Generated policy draft as a string
    """
    # Get the selected scenario details
    scenario = SCENARIOS[scenario_name]

    # Join the extracted sentences into one paragraph
    summary_text = ' '.join(summary_sentences)

    # Build the structured prompt for the AI
    prompt = f"""
You are an expert policy communication specialist working for a government advisory body.

You have been given a summary of a government policy document.
Your task is to ADAPT this policy for a specific scenario.

ORIGINAL POLICY SUMMARY:
{summary_text}

SCENARIO DETAILS:
- Target Audience: {scenario['audience']}
- Key Priorities: {scenario['priorities']}
- Required Tone: {scenario['tone']}
- Focus Area: {scenario['focus']}

INSTRUCTIONS:
1. Rewrite and adapt the policy specifically for the target audience above
2. Reorganize priorities to match what matters most to this audience
3. Use the exact tone described above
4. Structure your output with these exact sections:
   - POLICY TITLE
   - POLICY OBJECTIVES (3-4 bullet points)
   - KEY MEASURES AND STRATEGIES (4-5 bullet points)
   - EXPECTED OUTCOMES (3-4 bullet points)
   - IMPLEMENTATION NOTES (2-3 sentences)
5. Length: approximately 350 words
6. Do NOT copy the summary directly — genuinely adapt it for the audience
7. Do NOT assume or mention any specific policy name — base everything only on the summary provided
8. IMPORTANT: Include specific facts, figures, statistics and targets throughout:
   - Use percentages (e.g. "increase digital literacy by 40%")
   - Use numbers (e.g. "reach 2.3 million rural businesses")
   - Use deadlines (e.g. "by 2027", "within 18 months")
   - Use financial figures (e.g. "LKR 500 million investment")
   - Use rankings or comparisons (e.g. "top 10 digital economies in Asia")
   - Make every bullet point contain at least one number or statistic
   - This makes the policy feel realistic, credible and data-driven

Generate the adapted policy draft now:
"""

    # Call the Groq API
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an expert policy writer. Always produce formal, structured, professional policy documents tailored to the given audience. Never assume the name of the policy — always base your response only on the summary provided."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content


def generate_abstractive_summary(summary_sentences):
    """
    Takes NLP-extracted sentences and creates a clean readable summary.
    This is Layer 2 of the summarization pipeline.
    Works with any policy document.

    Input: list of extracted sentences from NLP
    Output: clean readable summary paragraph
    """
    summary_text = ' '.join(summary_sentences)

    prompt = f"""
You are a policy analyst reviewing a government policy document.

Below are the most important sentences extracted from the policy document using NLP analysis:

EXTRACTED KEY SENTENCES:
{summary_text}

Your task: Write a clean, concise summary (200-250 words) that clearly covers:
1. The main goals of the policy
2. Key measures and strategies proposed
3. The overall direction and intent of the policy

Write in clear professional language in paragraphs. Do not use bullet points.
Do NOT assume or mention any specific policy name — base your summary only on the content provided.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=600
    )

    return response.choices[0].message.content