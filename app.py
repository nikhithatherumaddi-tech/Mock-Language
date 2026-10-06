import streamlit as st
import random

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="LinguaAI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "words_learned": 0,
    "quiz_score": 0,
    "quiz_attempts": 0,
    "grammar_checks": 0,
    "tutor_questions": 0,
    "learned_words": [],
    "tutor_history": [],
    "answered_questions": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================================================
# PROFESSIONAL DARK UI
# =========================================================

st.markdown("""
<style>

/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99, 102, 241, 0.25),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(6, 182, 212, 0.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(139, 92, 246, 0.16),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #070b18 0%,
            #0f172a 45%,
            #111827 100%
        );

    color: #f8fafc;
}

/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b1020 0%,
            #111827 100%
        );

    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: #f8fafc;
}

/* ---------- MAIN TITLE ---------- */

.hero-title {
    text-align: center;
    font-size: 52px;
    font-weight: 850;
    letter-spacing: -1px;
    color: #ffffff;
    margin-top: 20px;
}

.hero-subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 19px;
    margin-bottom: 30px;
}

/* ---------- SECTION TITLE ---------- */

.section-title {
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 25px;
}

/* ---------- GLASS CARDS ---------- */

.feature-card {
    background:
        linear-gradient(
            145deg,
            rgba(30,41,59,0.88),
            rgba(15,23,42,0.72)
        );

    border: 1px solid rgba(148,163,184,0.14);
    border-radius: 20px;
    padding: 25px;
    min-height: 155px;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.25);

    backdrop-filter: blur(14px);
}

/* ---------- STAT CARDS ---------- */

.stat-card {
    background: rgba(30,41,59,0.75);
    border: 1px solid rgba(148,163,184,0.14);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 12px;

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #06b6d4
        );

    color: white;
    font-weight: 700;
    padding: 10px 18px;

    box-shadow:
        0 8px 25px rgba(99,102,241,0.20);

    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 12px 30px rgba(6,182,212,0.30);
}

/* ---------- INPUTS ---------- */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input {

    background-color: #111827 !important;
    color: #f8fafc !important;

    border: 1px solid #334155 !important;
    border-radius: 11px !important;
}

/* ---------- SELECT BOX ---------- */

.stSelectbox div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 11px !important;
}

/* ---------- RADIO ---------- */

.stRadio label {
    color: #e2e8f0 !important;
}

/* ---------- METRICS ---------- */

[data-testid="stMetric"] {

    background:
        linear-gradient(
            145deg,
            rgba(30,41,59,0.90),
            rgba(15,23,42,0.80)
        );

    border: 1px solid rgba(148,163,184,0.14);
    border-radius: 17px;
    padding: 18px;
}

/* ---------- DIVIDER ---------- */

hr {
    border-color: rgba(148,163,184,0.13);
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #64748b;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("## 🌍 LinguaAI")
st.sidebar.caption("Smart Language Learning Platform")

st.sidebar.divider()

language = st.sidebar.selectbox(
    "🌐 Learning Language",
    [
        "English",
        "French",
        "Hindi",
        "Spanish"
    ]
)

page = st.sidebar.radio(
    "📚 MENU",
    [
        "🏠 Home",
        "🤖 AI Tutor",
        "📚 Vocabulary",
        "✍️ Grammar Checker",
        "🎯 Quiz",
        "📊 Progress Dashboard"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### ⚡ Quick Progress")

st.sidebar.write(
    f"📚 Words Learned: **{st.session_state.words_learned}**"
)

st.sidebar.write(
    f"🎯 Quiz Score: **{st.session_state.quiz_score}**"
)

st.sidebar.write(
    f"✍️ Grammar Checks: **{st.session_state.grammar_checks}**"
)

st.sidebar.write(
    f"🤖 Tutor Questions: **{st.session_state.tutor_questions}**"
)

# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="hero-title">🌍 LinguaAI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Your Personal AI-Powered Language Learning Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        f"🎓 Currently learning: **{language}**"
    )

    st.divider()

    st.markdown(
        '<div class="section-title">✨ Learn Smarter</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Everything you need to improve your language skills in one place.'
        '</div>',
        unsafe_allow_html=True
    )

    # Feature row 1

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
        <h2>🤖 AI Tutor</h2>
        <p>Ask questions and learn grammar, vocabulary and sentence formation.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
        <h2>📚 Vocabulary</h2>
        <p>Learn new words with meanings, examples, synonyms and antonyms.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
        <h2>✍️ Grammar</h2>
        <p>Find common grammar mistakes and understand their corrections.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # Feature row 2

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("""
        <div class="feature-card">
        <h2>🎯 Quiz</h2>
        <p>Test your knowledge using interactive multiple-choice questions.</p>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="feature-card">
        <h2>📊 Progress</h2>
        <p>Track your vocabulary, quiz performance and learning activities.</p>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div class="feature-card">
        <h2>🏆 Achievements</h2>
        <p>Unlock learning achievements as you complete activities.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("💡 Daily Learning Tip")

    tips = [
        "Learn at least 5 new words every day.",
        "Use every new word in your own sentence.",
        "Read a short paragraph every day.",
        "Speak new vocabulary aloud.",
        "Practice grammar by writing your own examples."
    ]

    st.success(random.choice(tips))

    st.subheader("🎯 Set Your Daily Goal")

    daily_goal = st.slider(
        "Learning activities per day",
        1,
        20,
        5
    )

    st.write(
        f"Your daily target: **{daily_goal} activities**"
    )

# =========================================================
# AI TUTOR
# =========================================================

elif page == "🤖 AI Tutor":

    st.markdown(
        '<div class="section-title">🤖 AI Language Tutor</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Ask questions and practice your language skills.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        tutor_language = st.selectbox(
            "🌐 Language",
            [
                "English",
                "French",
                "Hindi",
                "Spanish"
            ],
            key="tutor_language"
        )

    with c2:

        level = st.selectbox(
            "📈 Learning Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    question = st.text_area(
        "💬 Ask your Tutor",
        placeholder=(
            "Example: Explain present tense in simple words."
        )
    )

    if st.button(
        "🤖 Ask Tutor",
        use_container_width=True
    ):

        if question.strip():

            st.session_state.tutor_questions += 1

            q = question.lower()

            if "noun" in q:

                answer = (
                    "### 📘 Noun\n\n"
                    "A noun is a word used to name a person, "
                    "place, animal, thing or idea.\n\n"
                    "**Examples:** student, school, book, happiness."
                )

            elif "verb" in q:

                answer = (
                    "### 📗 Verb\n\n"
                    "A verb describes an action or state.\n\n"
                    "**Examples:** run, eat, write, study, sleep."
                )

            elif "adjective" in q:

                answer = (
                    "### 📙 Adjective\n\n"
                    "An adjective describes a noun.\n\n"
                    "**Examples:** beautiful, intelligent, large, small."
                )

            elif "present tense" in q:

                answer = (
                    "### ⏰ Present Tense\n\n"
                    "Present tense is used for regular actions, "
                    "habits and facts.\n\n"
                    "**Example:** She goes to college every day."
                )

            elif "past tense" in q:

                answer = (
                    "### ⏪ Past Tense\n\n"
                    "Past tense describes an action that happened "
                    "before now.\n\n"
                    "**Example:** She visited her friend yesterday."
                )

            elif "future tense" in q:

                answer = (
                    "### ⏩ Future Tense\n\n"
                    "Future tense describes an action that will happen "
                    "later.\n\n"
                    "**Example:** She will visit her friend tomorrow."
                )

            elif "vocabulary" in q:

                answer = (
                    "### 📚 Vocabulary Tip\n\n"
                    "Learn a small number of new words every day, "
                    "then use them in your own sentences."
                )

            elif "hello" in q:

                answer = (
                    f"### 👋 Hello!\n\n"
                    f"Welcome to your **{tutor_language}** learning session!"
                )

            else:

                answer = (
                    "### 💡 Learning Tip\n\n"
                    f"You asked: **{question}**\n\n"
                    "Try asking about nouns, verbs, adjectives, "
                    "tenses, grammar or vocabulary."
                )

            st.session_state.tutor_history.append(
                (question, answer)
            )

            st.divider()

            st.subheader("📖 Tutor Response")

            st.markdown(answer)

        else:

            st.warning(
                "Please enter a question first."
            )

    if st.session_state.tutor_history:

        st.divider()

        st.subheader("🕘 Recent Questions")

        for question_text, answer_text in \
                st.session_state.tutor_history[-5:]:

            with st.expander(question_text):

                st.markdown(answer_text)

# =========================================================
# VOCABULARY
# =========================================================

elif page == "📚 Vocabulary":

    st.markdown(
        '<div class="section-title">📚 Vocabulary Builder</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Build your vocabulary with useful words.'
        '</div>',
        unsafe_allow_html=True
    )

    vocabulary = {

        "happy": {
            "meaning": "Feeling pleasure or joy.",
            "example": "She was happy after receiving good news.",
            "synonyms": "Joyful, cheerful, pleased",
            "antonyms": "Sad, unhappy"
        },

        "brave": {
            "meaning": "Having courage in difficult situations.",
            "example": "The brave student answered the question.",
            "synonyms": "Courageous, bold, fearless",
            "antonyms": "Cowardly, fearful"
        },

        "beautiful": {
            "meaning": "Very pleasing or attractive.",
            "example": "The garden looks beautiful.",
            "synonyms": "Lovely, pretty, attractive",
            "antonyms": "Ugly, unattractive"
        },

        "intelligent": {
            "meaning": "Having a good ability to learn and understand.",
            "example": "She is an intelligent student.",
            "synonyms": "Clever, smart, bright",
            "antonyms": "Unintelligent"
        },

        "confident": {
            "meaning": "Feeling sure about your abilities.",
            "example": "He felt confident before the presentation.",
            "synonyms": "Self-assured, positive",
            "antonyms": "Insecure, doubtful"
        },

        "ancient": {
            "meaning": "Belonging to a very old period of history.",
            "example": "India has many ancient monuments.",
            "synonyms": "Old, historic",
            "antonyms": "Modern, new"
        },

        "curious": {
            "meaning": "Wanting to know or learn something.",
            "example": "The curious student asked many questions.",
            "synonyms": "Inquisitive, interested",
            "antonyms": "Uninterested"
        },

        "creative": {
            "meaning": "Having the ability to create new ideas.",
            "example": "She has a creative approach to problems.",
            "synonyms": "Imaginative, inventive",
            "antonyms": "Uncreative"
        }
    }

    word = st.text_input(
        "🔎 Search a word",
        placeholder="Example: confident"
    )

    category = st.selectbox(
        "📂 Category",
        [
            "General",
            "Education",
            "Personality",
            "Daily Life"
        ]
    )

    if st.button(
        "📖 Learn Word",
        use_container_width=True
    ):

        key = word.lower().strip()

        if key in vocabulary:

            data = vocabulary[key]

            if key not in st.session_state.learned_words:

                st.session_state.learned_words.append(key)

                st.session_state.words_learned += 1

            st.success(
                f"📖 {word.title()}"
            )

            c1, c2 = st.columns(2)

            with c1:

                st.subheader("Meaning")

                st.write(
                    data["meaning"]
                )

                st.subheader("Example")

                st.info(
                    data["example"]
                )

            with c2:

                st.subheader("Synonyms")

                st.write(
                    data["synonyms"]
                )

                st.subheader("Antonyms")

                st.write(
                    data["antonyms"]
                )

            st.subheader("🗣️ Pronunciation")

            st.code(
                word.lower()
            )

        else:

            st.warning(
                "Word not found in the demo dictionary."
            )

            st.write(
                "Try: happy, brave, beautiful, intelligent, "
                "confident, ancient, curious or creative."
            )

    if st.session_state.learned_words:

        st.divider()

        st.subheader("✅ Your Learned Words")

        st.write(
            ", ".join(
                word.title()
                for word in st.session_state.learned_words
            )
        )

# =========================================================
# GRAMMAR CHECKER
# =========================================================

elif page == "✍️ Grammar Checker":

    st.markdown(
        '<div class="section-title">✍️ Grammar Checker</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Find common grammar mistakes and learn the correction.'
        '</div>',
        unsafe_allow_html=True
    )

    sentence = st.text_area(
        "📝 Enter your sentence",
        placeholder="Example: She go to college every day."
    )

    if st.button(
        "✅ Check Grammar",
        use_container_width=True
    ):

        if sentence.strip():

            st.session_state.grammar_checks += 1

            original = sentence.strip()
            lower = original.lower()

            rules = {

                "she go": (
                    "She goes",
                    "Use 'goes' with 'she'."
                ),

                "he go": (
                    "He goes",
                    "Use 'goes' with 'he'."
                ),

                "they goes": (
                    "They go",
                    "Use 'go' with 'they'."
                ),

                "i is": (
                    "I am",
                    "Use 'am' with 'I'."
                ),

                "he are": (
                    "He is",
                    "Use 'is' with 'he'."
                ),

                "she are": (
                    "She is",
                    "Use 'is' with 'she'."
                ),

                "they is": (
                    "They are",
                    "Use 'are' with 'they'."
                ),

                "i has": (
                    "I have",
                    "Use 'have' with 'I'."
                ),

                "he have": (
                    "He has",
                    "Use 'has' with 'he'."
                ),

                "she have": (
                    "She has",
                    "Use 'has' with 'she'."
                )
            }

            found = False

            for wrong, correction in rules.items():

                if wrong in lower:

                    corrected, explanation = correction

                    st.error(
                        "❌ Grammar mistake detected."
                    )

                    st.write(
                        "### Original"
                    )

                    st.write(
                        original
                    )

                    st.write(
                        "### Corrected"
                    )

                    st.success(
                        corrected
                    )

                    st.write(
                        "### 💡 Why?"
                    )

                    st.info(
                        explanation
                    )

                    found = True

                    break

            if not found:

                st.success(
                    "✅ No common grammar mistake detected."
                )

                st.write(
                    "Your sentence looks good according to "
                    "the basic grammar rules."
                )

        else:

            st.warning(
                "Please enter a sentence."
            )

    st.divider()

    st.subheader("📌 Grammar Quick Tips")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            "**I → am**\n\nI am a student."
        )

    with c2:
        st.info(
            "**He/She → is**\n\nShe is happy."
        )

    with c3:
        st.info(
            "**They → are**\n\nThey are students."
        )

# =========================================================
# QUIZ
# =========================================================

elif page == "🎯 Quiz":

    st.markdown(
        '<div class="section-title">🎯 Language Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Test your grammar and vocabulary knowledge.'
        '</div>',
        unsafe_allow_html=True
    )

    difficulty = st.selectbox(
        "📈 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    questions = [

        {
            "question":
                "Which sentence is correct?",

            "options": [
                "She go to school.",
                "She goes to school.",
                "She going school.",
                "She gone school."
            ],

            "answer":
                "She goes to school."
        },

        {
            "question":
                "What is the opposite of 'happy'?",

            "options": [
                "Joyful",
                "Excited",
                "Sad",
                "Brave"
            ],

            "answer":
                "Sad"
        },

        {
            "question":
                "What is the plural of 'child'?",

            "options": [
                "Childs",
                "Childes",
                "Children",
                "Childrens"
            ],

            "answer":
                "Children"
        },

        {
            "question":
                "Which word is a verb?",

            "options": [
                "Beautiful",
                "Run",
                "Happy",
                "School"
            ],

            "answer":
                "Run"
        },

        {
            "question":
                "Which word is an adjective?",

            "options": [
                "Quickly",
                "Run",
                "Beautiful",
                "School"
            ],

            "answer":
                "Beautiful"
        },

        {
            "question":
                "Choose the correct word: 'I ___ a student.'",

            "options": [
                "is",
                "are",
                "am",
                "be"
            ],

            "answer":
                "am"
        }
    ]

    question_number = st.number_input(
        "Question Number",
        min_value=1,
        max_value=len(questions),
        value=1
    )

    question_data = questions[
        question_number - 1
    ]

    st.subheader(
        f"Question {question_number} of {len(questions)}"
    )

    st.write(
        f"**{question_data['question']}**"
    )

    answer = st.radio(
        "Choose your answer:",
        question_data["options"]
    )

    if st.button(
        "🎯 Submit Answer",
        use_container_width=True
    ):

        st.session_state.quiz_attempts += 1

        question_id = question_number

        if (
            question_id
            not in st.session_state.answered_questions
        ):

            st.session_state.answered_questions.append(
                question_id
            )

            if answer == question_data["answer"]:

                st.session_state.quiz_score += 1

                st.success(
                    "🎉 Correct! Great job!"
                )

            else:

                st.error(
                    "❌ Incorrect answer."
                )

                st.info(
                    "Correct answer: "
                    f"**{question_data['answer']}**"
                )

        else:

            if answer == question_data["answer"]:

                st.success(
                    "🎉 Correct!"
                )

            else:

                st.error(
                    "❌ Incorrect."
                )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "🏆 Correct Answers",
            st.session_state.quiz_score
        )

    with c2:

        st.metric(
            "📝 Attempts",
            st.session_state.quiz_attempts
        )

# =========================================================
# PROGRESS DASHBOARD
# =========================================================

elif page == "📊 Progress Dashboard":

    st.markdown(
        '<div class="section-title">📊 Progress Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'See your learning activity and achievements.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "📚 Words",
            st.session_state.words_learned
        )

    with c2:

        st.metric(
            "🎯 Quiz Score",
            st.session_state.quiz_score
        )

    with c3:

        st.metric(
            "✍️ Grammar",
            st.session_state.grammar_checks
        )

    with c4:

        st.metric(
            "🤖 Tutor",
            st.session_state.tutor_questions
        )

    st.divider()

    total_activity = (
        st.session_state.words_learned
        + st.session_state.quiz_score
        + st.session_state.grammar_checks
        + st.session_state.tutor_questions
    )

    st.subheader("📈 Overall Progress")

    progress = min(
        total_activity / 20,
        1.0
    )

    st.progress(progress)

    st.write(
        f"You completed **{total_activity} learning activities**."
    )

    if total_activity == 0:

        st.info(
            "🌱 Start learning to build your progress."
        )

    elif total_activity < 5:

        st.warning(
            "🌱 Good beginning! Keep practicing."
        )

    elif total_activity < 10:

        st.info(
            "🔥 Nice progress! Keep going."
        )

    else:

        st.success(
            "🏆 Excellent! You are actively learning."
        )

    st.divider()

    st.subheader("🏆 Achievements")

    if st.session_state.words_learned >= 3:

        st.success(
            "📚 Vocabulary Starter — 3+ words learned"
        )

    else:

        st.write(
            "🔒 📚 Vocabulary Starter — Learn 3 words"
        )

    if st.session_state.quiz_score >= 3:

        st.success(
            "🎯 Quiz Champion — 3+ correct answers"
        )

    else:

        st.write(
            "🔒 🎯 Quiz Champion — Get 3 correct answers"
        )

    if st.session_state.grammar_checks >= 3:

        st.success(
            "✍️ Grammar Explorer — 3+ checks"
        )

    else:

        st.write(
            "🔒 ✍️ Grammar Explorer — Check 3 sentences"
        )

    if st.session_state.tutor_questions >= 3:

        st.success(
            "🤖 Curious Learner — 3+ tutor questions"
        )

    else:

        st.write(
            "🔒 🤖 Curious Learner — Ask 3 questions"
        )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="footer">'
    '🌍 LinguaAI &nbsp;•&nbsp; Learn &nbsp;•&nbsp; Practice '
    '&nbsp;•&nbsp; Improve &nbsp;•&nbsp; Track'
    '</div>',
    unsafe_allow_html=True
)