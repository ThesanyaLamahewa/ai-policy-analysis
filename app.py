# app.py
# Policy Summarisation and Scenario-Based Adaptation System
# LB3114 Assignment I | KDU

import streamlit as st
from summariser import extractive_summarize, extract_text_from_pdf, extract_keywords
from generator import generate_policy_draft, generate_abstractive_summary, SCENARIOS

# ── Page Configuration ───────────────────────────────────────────
st.set_page_config(
    page_title="PolicyAI | KDU",
    page_icon="🏛️",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { box-sizing: border-box; }

.stApp {
    background-color: #020b18;
    background-image:
        radial-gradient(ellipse at 20% 20%, rgba(0,200,180,0.07) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(0,120,255,0.07) 0%, transparent 50%);
    font-family: 'DM Sans', sans-serif;
    color: #e2eaf4;
}

.hero-header { text-align: center; padding: 2.5rem 1rem 1.5rem; }

.hero-tag {
    display: inline-block;
    background: rgba(0,200,180,0.12);
    border: 1px solid rgba(0,200,180,0.35);
    color: #00c8b4;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.3rem 1rem;
    border-radius: 100px;
    margin-bottom: 1rem;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 0.5rem;
    background: linear-gradient(135deg, #ffffff 0%, #00c8b4 50%, #0078ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle { font-size: 0.95rem; color: #7a9bb5; margin: 0; }

.hero-divider {
    width: 60px;
    height: 3px;
    background: linear-gradient(90deg, #00c8b4, #0078ff);
    margin: 1.2rem auto 0;
    border-radius: 2px;
}

.step-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 8px;
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 800;
    margin-right: 0.5rem;
}

.step-badge-left { background: linear-gradient(135deg, #00c8b4, #0078ff); color: white; }
.step-badge-right { background: linear-gradient(135deg, #0078ff, #7c3aed); color: white; }

.stat-strip { display: flex; gap: 0.8rem; margin-bottom: 1.2rem; flex-wrap: wrap; }

.stat-chip {
    background: rgba(0,200,180,0.08);
    border: 1px solid rgba(0,200,180,0.2);
    border-radius: 8px;
    padding: 0.4rem 0.8rem;
    font-size: 0.78rem;
    color: #00c8b4;
    font-weight: 500;
}

.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7a9bb5;
    margin-bottom: 0.5rem;
}

[data-testid="stFileUploader"] {
    background: rgba(2,11,24,0.8) !important;
    border: 1.5px dashed rgba(0,200,180,0.35) !important;
    border-radius: 14px !important;
    padding: 0.5rem !important;
}

[data-testid="stFileUploader"] > div,
[data-testid="stFileUploader"] section {
    background: transparent !important;
    border: none !important;
}

[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] div {
    color: #7a9bb5 !important;
    background: transparent !important;
}

[data-testid="stFileUploader"] button {
    background: linear-gradient(135deg, #00c8b4, #0078ff) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

.stTextArea textarea {
    background: rgba(2,11,24,0.9) !important;
    border: 1.5px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: #e2eaf4 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
}

.stTextArea textarea:focus {
    border-color: rgba(0,200,180,0.5) !important;
    box-shadow: 0 0 0 3px rgba(0,200,180,0.1) !important;
}

.stTextArea textarea::placeholder { color: #3d5a73 !important; }

.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #00c8b4, #0078ff) !important;
}

.stSlider label, .stSlider p { color: #7a9bb5 !important; font-size: 0.85rem !important; }

[data-testid="stSelectbox"] > div > div {
    background: #071525 !important;
    border: 1.5px solid rgba(0,120,255,0.35) !important;
    border-radius: 12px !important;
    color: white !important;
}

[data-testid="stSelectbox"] span { color: white !important; }

div[data-baseweb="select"] div,
div[data-baseweb="select"] ul,
div[data-baseweb="select"] li,
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="popover"] div,
div[data-baseweb="popover"] ul,
div[data-baseweb="popover"] li,
div[data-baseweb="menu"],
div[data-baseweb="menu"] > div,
div[data-baseweb="menu"] div,
div[data-baseweb="menu"] ul,
div[data-baseweb="menu"] li,
[class*="MenuList"],
[class*="Option"],
[class*="menu"] {
    background-color: #071525 !important;
    color: #e2eaf4 !important;
}

li[role="option"] {
    background: #071525 !important;
    color: #e2eaf4 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1rem !important;
}

li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background: rgba(0,120,255,0.3) !important;
    color: white !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #00c8b4 0%, #0078ff 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 1.2rem !important;
    box-shadow: 0 4px 20px rgba(0,200,180,0.25) !important;
    transition: all 0.2s ease !important;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(0,200,180,0.4) !important;
}

.stDownloadButton > button {
    background: rgba(0,120,255,0.12) !important;
    border: 1px solid rgba(0,120,255,0.35) !important;
    border-radius: 10px !important;
    color: #60a5fa !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
}

.stDownloadButton > button:hover {
    background: rgba(0,120,255,0.22) !important;
}

.streamlit-expanderHeader {
    background: rgba(2,11,24,0.9) !important;
    border: 1px solid rgba(0,120,255,0.2) !important;
    border-radius: 10px !important;
    color: #e2eaf4 !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
}

.streamlit-expanderContent {
    background: rgba(2,11,24,0.9) !important;
    border: 1px solid rgba(0,120,255,0.2) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    padding: 1rem !important;
}

.streamlit-expanderContent p,
.streamlit-expanderContent span,
.streamlit-expanderContent div,
.streamlit-expanderContent strong,
.streamlit-expanderContent li { color: #c8d8e8 !important; }

.stSuccess {
    background: rgba(0,200,140,0.1) !important;
    border: 1px solid rgba(0,200,140,0.35) !important;
    border-radius: 10px !important;
    color: #00c88c !important;
}

.stWarning {
    background: rgba(251,191,36,0.1) !important;
    border: 1px solid rgba(251,191,36,0.35) !important;
    border-radius: 10px !important;
    color: #fbbf24 !important;
}

.stInfo {
    background: rgba(0,120,255,0.1) !important;
    border: 1px solid rgba(0,120,255,0.35) !important;
    border-radius: 10px !important;
    color: #60a5fa !important;
}

.stError {
    background: rgba(255,60,60,0.1) !important;
    border: 1px solid rgba(255,60,60,0.35) !important;
    border-radius: 10px !important;
    color: #ff6b6b !important;
}

h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; }

h2 {
    color: #ffffff !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    border-bottom: 1px solid rgba(255,255,255,0.08) !important;
    padding-bottom: 0.6rem !important;
}

h3 { color: #00c8b4 !important; font-size: 1.05rem !important; }

p, li { color: #c8d8e8 !important; font-size: 0.9rem !important; line-height: 1.6 !important; }

label { color: #7a9bb5 !important; font-size: 0.85rem !important; }

.stCaption { color: #7a9bb5 !important; font-size: 0.8rem !important; }

hr { border-color: rgba(255,255,255,0.07) !important; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,200,180,0.3); border-radius: 3px; }

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Hero Header ───────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <div class="hero-tag">🏛️ LB3114 · KDU · Intake 41</div>
    <div class="hero-title">PolicyAI Studio</div>
    <p class="hero-subtitle">National Digital Economy Strategy 2030 · Summarisation & Scenario Adaptation</p>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Session State ─────────────────────────────────────────────────
if 'extracted_sentences' not in st.session_state:
    st.session_state.extracted_sentences = []
if 'abstractive_summary' not in st.session_state:
    st.session_state.abstractive_summary = ""
if 'policy_draft' not in st.session_state:
    st.session_state.policy_draft = ""
if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = ""
if 'word_count' not in st.session_state:
    st.session_state.word_count = 0
if 'keywords' not in st.session_state:
    st.session_state.keywords = []

# ── Two Column Layout ─────────────────────────────────────────────
left_col, right_col = st.columns(2, gap="large")

# ══════════════════════════════════════════════════════════════════
# LEFT PANEL
# ══════════════════════════════════════════════════════════════════
with left_col:
    st.markdown("""
    <div style="display:flex; align-items:center; margin-bottom:0.3rem;">
        <span class="step-badge step-badge-left">1</span>
        <span style="font-family:'Syne',sans-serif; font-size:1.25rem;
                     font-weight:700; color:white;">
            Policy Input & Summarisation
        </span>
    </div>
    <p style="color:#7a9bb5; font-size:0.85rem; margin:0 0 1.2rem;">
        Upload your policy document and run AI-powered NLP summarisation.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">📎 Upload Policy PDF</div>',
                unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload Policy PDF", type=["pdf"],
        help="Upload a PDF policy document",
        label_visibility="collapsed"
    )

    st.markdown('<div style="height:0.6rem"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">✏️ Or Paste Policy Text</div>',
                unsafe_allow_html=True)
    pasted_text = st.text_area(
        "Paste text", height=120,
        placeholder="Paste the full text of your policy document here...",
        label_visibility="collapsed"
    )

    st.markdown('<div style="height:0.4rem"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">🎚️ NLP Extraction Depth</div>',
                unsafe_allow_html=True)
    num_sentences = st.slider(
        "Key sentences", min_value=5, max_value=20, value=10,
        label_visibility="collapsed"
    )
    st.caption(f"Extracting **{num_sentences}** most important sentences")

    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)

    summarise_clicked = st.button(
        "🔍  Run NLP Summarisation",
        type="primary", use_container_width=True
    )

    if summarise_clicked:
        raw_text = ""

        if uploaded_file is not None:
            with open("temp_policy.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            with st.spinner("📖 Reading and extracting PDF text..."):
                raw_text = extract_text_from_pdf("temp_policy.pdf")
            st.session_state.word_count = len(raw_text.split())
            st.success(f"✅ PDF loaded — {st.session_state.word_count:,} words extracted")

        elif pasted_text.strip():
            raw_text = pasted_text
            st.session_state.word_count = len(raw_text.split())
            st.success(f"✅ Text received — {st.session_state.word_count:,} words")

        else:
            st.error("❌ Please upload a PDF or paste some text first.")

        if raw_text:
            with st.expander("🔬 NLP Pipeline — Live Steps", expanded=True):
                st.markdown("""
**Step 1 — Text Cleaning** · Removing noise, page numbers, special characters

**Step 2 — Sentence Tokenization** · Splitting into sentences using NLTK

**Step 3 — Frequency Scoring** · Scoring words using spaCy word frequency analysis

**Step 4 — Length Normalization** · Dividing scores by sentence length for fairness

**Step 5 — Top-N Selection** · Selecting the highest-scoring sentences

**Step 6 — Abstractive Pass** · AI rewrites extracted sentences into a clean summary

**Step 7 — Keyword Extraction** · Identifying most significant policy terms
                """)

            with st.spinner("🧠 Running NLP extraction..."):
                sentences = extractive_summarize(raw_text, num_sentences)
                st.session_state.extracted_sentences = sentences

            with st.spinner("🔑 Extracting keywords..."):
                keywords = extract_keywords(sentences, top_n=15)
                st.session_state.keywords = keywords

            with st.spinner("🤖 Generating AI summary..."):
                abstract_summary = generate_abstractive_summary(sentences)
                st.session_state.abstractive_summary = abstract_summary

            st.success("✅ Summarisation complete! Go to Step 2 on the right →")

    if st.session_state.extracted_sentences:
        st.markdown('<div style="height:0.8rem"></div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="stat-strip">
            <div class="stat-chip">📄 {st.session_state.word_count:,} words processed</div>
            <div class="stat-chip">🔢 {len(st.session_state.extracted_sentences)} key sentences</div>
            <div class="stat-chip">🤖 AI summary ready</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📊 Layer 1 · NLP Extracted Key Sentences", expanded=False):
            st.info("Selected by frequency-based NLP scoring (normalized by length):")
            for i, sentence in enumerate(st.session_state.extracted_sentences, 1):
                st.markdown(f"**{i}.** {sentence}")

        st.markdown("### 📝 Policy Summary")
        st.write(st.session_state.abstractive_summary)

        st.download_button(
            label="⬇️  Download Summary",
            data=st.session_state.abstractive_summary,
            file_name="policy_summary.txt",
            mime="text/plain",
            use_container_width=True
        )

        # ── Keyword Extraction ────────────────────────────────────
        if st.session_state.keywords:
            st.markdown("### 🔑 Top Keywords Extracted by NLP")

            # Build keyword chips using single quotes inside f-string
            keyword_html = "<div style='display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;'>"
            for word, count in st.session_state.keywords:
                keyword_html += (
                    f"<span style='background:rgba(0,200,180,0.12);"
                    f"border:1px solid rgba(0,200,180,0.3);"
                    f"border-radius:20px;"
                    f"padding:0.3rem 0.8rem;"
                    f"font-size:0.82rem;"
                    f"color:#00c8b4;"
                    f"font-weight:500;'>"
                    f"{word} "
                    f"<span style='color:#7a9bb5;font-size:0.75rem;'>({count})</span>"
                    f"</span>"
                )
            keyword_html += "</div>"
            st.markdown(keyword_html, unsafe_allow_html=True)

            # ── Word Cloud ────────────────────────────────────────
            st.markdown("### ☁️ Word Cloud Visualisation")

            from wordcloud import WordCloud
            import matplotlib.pyplot as plt

            wordcloud_text = ' '.join([
                word for word, count in st.session_state.keywords
                for _ in range(count)
            ])

            if wordcloud_text.strip():
                wc = WordCloud(
                    width=700,
                    height=280,
                    background_color="#020b18",
                    colormap="cool",
                    max_words=50,
                    prefer_horizontal=0.8,
                    collocations=False
                ).generate(wordcloud_text)

                fig, ax = plt.subplots(figsize=(7, 2.8))
                fig.patch.set_facecolor('#020b18')
                ax.imshow(wc, interpolation='bilinear')
                ax.axis('off')
                plt.tight_layout(pad=0)
                st.pyplot(fig)
                plt.close()


# ══════════════════════════════════════════════════════════════════
# RIGHT PANEL
# ══════════════════════════════════════════════════════════════════
with right_col:
    st.markdown("""
    <div style="display:flex; align-items:center; margin-bottom:0.3rem;">
        <span class="step-badge step-badge-right">2</span>
        <span style="font-family:'Syne',sans-serif; font-size:1.25rem;
                     font-weight:700; color:white;">
            Scenario-Based Policy Generation
        </span>
    </div>
    <p style="color:#7a9bb5; font-size:0.85rem; margin:0 0 1.2rem;">
        Select a scenario to generate a context-adapted policy draft using Generative AI.
    </p>
    """, unsafe_allow_html=True)

    if not st.session_state.extracted_sentences:
        st.warning("⬅️ Complete Step 1 on the left side first to unlock generation.")

    else:
        st.markdown('<div class="section-label">🎭 Select Adaptation Scenario</div>',
                    unsafe_allow_html=True)
        selected_scenario = st.selectbox(
            "Select scenario",
            options=list(SCENARIOS.keys()),
            label_visibility="collapsed"
        )

        scenario_info = SCENARIOS[selected_scenario]

        with st.expander("ℹ️ Scenario Details", expanded=True):
            st.markdown(f"""
**🎯 Target Audience**
{scenario_info['audience']}

**📌 Key Priorities**
{scenario_info['priorities']}

**🗣️ Tone**
{scenario_info['tone']}

**🔍 Focus**
{scenario_info['focus']}
            """)

        st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)

        generate_clicked = st.button(
            "⚡  Generate Adapted Policy Draft",
            type="primary", use_container_width=True
        )

        if generate_clicked:
            with st.spinner(f"✍️ Adapting policy for: {selected_scenario}..."):
                draft = generate_policy_draft(
                    st.session_state.extracted_sentences,
                    selected_scenario
                )
                st.session_state.policy_draft = draft
                st.session_state.current_scenario = selected_scenario
            st.success("✅ Policy draft generated!")

        if st.session_state.policy_draft:
            st.markdown(f"### 📋 {st.session_state.current_scenario}")

            st.markdown(
                f"<div style='"
                f"background:rgba(0,11,30,0.85);"
                f"border:1px solid rgba(0,120,255,0.25);"
                f"border-left:3px solid #0078ff;"
                f"border-radius:12px;"
                f"padding:1.4rem 1.6rem;"
                f"margin-bottom:1rem;"
                f"font-size:0.88rem;"
                f"line-height:1.9;"
                f"color:#c8d8e8;"
                f"white-space:pre-wrap;"
                f"'>{st.session_state.policy_draft}</div>",
                unsafe_allow_html=True
            )

            st.download_button(
                label="⬇️  Download This Draft",
                data=st.session_state.policy_draft,
                file_name=f"draft_{st.session_state.current_scenario[:25].replace(' ','_')}.txt",
                mime="text/plain",
                use_container_width=True
            )

            st.info("💡 Change the scenario above and click Generate to compare outputs!")
            