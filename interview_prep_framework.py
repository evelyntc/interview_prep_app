import streamlit as st
from pydantic import BaseModel, Field
from datetime import datetime

st.set_page_config(
    page_title="Interview Prep Framework",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Pydantic Models
class Story(BaseModel):
    setup: str = ""
    action: str = ""
    impact: str = ""
    complete: bool = False

class Story2(BaseModel):
    angle: str = ""
    thinking: str = ""
    complete: bool = False

class Story3(BaseModel):
    situation: str = ""
    skill: str = ""
    outcome: str = ""
    complete: bool = False

class Questions(BaseModel):
    q1: str = ""
    q2: str = ""
    q3: str = ""
    q4: str = ""
    complete: bool = False

class YourQuestions(BaseModel):
    q1: str = ""
    q2: str = ""
    q3: str = ""
    complete: bool = False

class InterviewPrepData(BaseModel):
    story1: Story = Field(default_factory=Story)
    story2: Story2 = Field(default_factory=Story2)
    story3: Story3 = Field(default_factory=Story3)
    keywords: list[str] = Field(default_factory=list)
    keyword_notes: str = ""
    questions: Questions = Field(default_factory=Questions)
    your_questions: YourQuestions = Field(default_factory=YourQuestions)

# Dark mode CSS with better text contrast
st.markdown("""
<style>
    body {
        background-color: #0e1117;
        color: #e6edf3;
    }
    .main {
        padding: 2rem 1rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1rem;
    }
    .step-header {
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
    }
    .tip-box {
        background-color: #1c2128;
        border-left: 4px solid #1976d2;
        padding: 1rem;
        border-radius: 0.25rem;
        margin: 1rem 0;
        color: #e6edf3;
    }
    .success-box {
        background-color: #1c3329;
        border-left: 4px solid #3fb950;
        padding: 1rem;
        border-radius: 0.25rem;
        margin: 1rem 0;
        color: #e6edf3;
    }
    textarea {
        background-color: #0d1117 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
    }
    input {
        background-color: #0d1117 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
    }
    select {
        background-color: #0d1117 !important;
        color: #e6edf3 !important;
    }
    ::placeholder {
        color: #6e7681 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'prep_data' not in st.session_state:
    st.session_state.prep_data = InterviewPrepData()

def calculate_progress():
    """Calculate overall prep progress"""
    data = st.session_state.prep_data
    completed = 0
    total = 6
    
    if data.story1.complete:
        completed += 1
    if data.story2.complete:
        completed += 1
    if data.story3.complete:
        completed += 1
    if data.keywords:
        completed += 1
    if data.questions.complete:
        completed += 1
    if data.your_questions.q1:
        completed += 1
    
    return completed, total

# Header
st.markdown("# 🎯 Interview Prep Framework")
st.markdown("*Use this framework to help you dust off the interview cobwebs and start preparing without stress. No data is collected so answer freely!*")

# Progress at top
col1, col2, col3 = st.columns(3)
data = st.session_state.prep_data

stories_complete = sum([data.story1.complete, data.story2.complete, data.story3.complete])
with col1:
    st.metric(label="Stories Ready", value=f"{stories_complete}/3")

questions_complete = int(bool(data.keywords)) + int(data.questions.complete)
with col2:
    st.metric(label="Questions Reviewed", value=f"{questions_complete}/2")

completed, total = calculate_progress()
percentage = int((completed / total) * 100)
with col3:
    st.metric(label="Prep Progress", value=f"{percentage}%")

st.markdown("---")

# Main tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📖 Story 1",
    "🧠 Story 2",
    "💪 Story 3",
    "🔑 Keywords",
    "❓ Questions",
    "🤔 Your Questions"
])

# TAB 1: Your Strongest Story
with tab1:
    st.markdown('<div class="step-header"><h2>Your Strongest Story</h2><p>Let\'s start with the accomplishment you\'re most proud of</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    This is your anchor. The story you tell when everything else is uncertain. It should show:
    - What problem or opportunity you identified
    - What action you took (and why your approach mattered)
    - What changed as a result
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### The Setup")
        st.markdown('<div class="tip-box">What was the situation? What was the problem or opportunity?</div>', unsafe_allow_html=True)
        st.session_state.prep_data.story1.setup = st.text_area(
            "Setup",
            value=st.session_state.prep_data.story1.setup,
            placeholder="e.g., Teams were overwhelmed with manual work and couldn't deliver insights fast enough",
            height=100,
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### What You Did")
        st.markdown('<div class="tip-box">What action did you take? What was your thinking?</div>', unsafe_allow_html=True)
        st.session_state.prep_data.story1.action = st.text_area(
            "Action",
            value=st.session_state.prep_data.story1.action,
            placeholder="e.g., I identified the bottleneck wasn't thinking—it was manual work. I designed an AI solution to automate the manual part",
            height=100,
            label_visibility="collapsed"
        )
    
    st.markdown("### The Impact")
    st.markdown('<div class="tip-box">What changed? What was the outcome? Why does it matter?</div>', unsafe_allow_html=True)
    st.session_state.prep_data.story1.impact = st.text_area(
        "Impact",
        value=st.session_state.prep_data.story1.impact,
        placeholder="e.g., Analysis turnaround went from weeks to days. The team could focus on strategy instead of manual work",
        height=100,
        label_visibility="collapsed"
    )
    
    if st.session_state.prep_data.story1.setup and st.session_state.prep_data.story1.action and st.session_state.prep_data.story1.impact:
        st.session_state.prep_data.story1.complete = True
        st.markdown('<div class="success-box">✓ Story 1 ready to practice</div>', unsafe_allow_html=True)
    else:
        st.info("Fill in all three sections to complete this story")
    
    if st.button("📝 Practice This Story", key="practice1"):
        st.info("Read it out loud. Close your eyes and tell it in your own words. Record yourself. Listen back.")

# TAB 2: How You Work
with tab2:
    st.markdown('<div class="step-header"><h2>How You Work</h2><p>Your process and thinking</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    Show them HOW you think, not just WHAT you do. Pick a story that demonstrates your process or approach.
    """)
    
    st.markdown("### What's the angle?")
    st.markdown("Pick one:")
    angle_options = [
        "A time you had to learn something new",
        "How you approach a big, ambiguous problem",
        "A time you failed and what you learned",
        "Your process for making decisions"
    ]
    selected_angle = st.selectbox(
        "Angle",
        angle_options,
        index=angle_options.index(st.session_state.prep_data.story2.angle) if st.session_state.prep_data.story2.angle in angle_options else 0,
        label_visibility="collapsed"
    )
    st.session_state.prep_data.story2.angle = selected_angle
    
    st.markdown("### Tell the story")
    st.markdown('<div class="tip-box">Write 2-3 sentences about the situation, what you did, and what you learned about how you approach problems</div>', unsafe_allow_html=True)
    st.session_state.prep_data.story2.thinking = st.text_area(
        "Your Story",
        value=st.session_state.prep_data.story2.thinking,
        placeholder="e.g., When I moved into a new domain, I...",
        height=150,
        label_visibility="collapsed"
    )
    
    if st.session_state.prep_data.story2.thinking:
        st.session_state.prep_data.story2.complete = True
        st.markdown('<div class="success-box">✓ Story 2 ready</div>', unsafe_allow_html=True)
    else:
        st.info("Write out your story to complete this section")

# TAB 3: Specific Skills
with tab3:
    st.markdown('<div class="step-header"><h2>Demonstrating Skills</h2><p>Show the specific competencies they care about</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    Pick a story that demonstrates 2-3 of these:
    - **Leadership**: When you influenced others or took ownership
    - **Collaboration**: How you worked across teams or handled disagreement
    - **Impact**: A time you moved a metric or changed something concrete
    - **Problem-solving**: When you found a non-obvious solution
    - **Adaptability**: How you handled change or ambiguity
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### The Situation")
        st.markdown('<div class="tip-box">What was happening? What was the challenge?</div>', unsafe_allow_html=True)
        st.session_state.prep_data.story3.situation = st.text_area(
            "Situation",
            value=st.session_state.prep_data.story3.situation,
            placeholder="e.g., I disagreed with a colleague about the best approach",
            height=100,
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### What Skill Did You Show?")
        st.markdown('<div class="tip-box">Which of the 5 skills above did you demonstrate?</div>', unsafe_allow_html=True)
        st.session_state.prep_data.story3.skill = st.selectbox(
            "Skill",
            ["Leadership", "Collaboration", "Impact", "Problem-solving", "Adaptability"],
            label_visibility="collapsed"
        )
    
    with col3:
        st.markdown("### The Outcome")
        st.markdown('<div class="tip-box">What was the result? How did it matter?</div>', unsafe_allow_html=True)
        st.session_state.prep_data.story3.outcome = st.text_area(
            "Outcome",
            value=st.session_state.prep_data.story3.outcome,
            placeholder="e.g., We found a better solution together",
            height=100,
            label_visibility="collapsed"
        )
    
    if st.session_state.prep_data.story3.situation and st.session_state.prep_data.story3.outcome:
        st.session_state.prep_data.story3.complete = True
        st.markdown('<div class="success-box">✓ Story 3 ready</div>', unsafe_allow_html=True)

# TAB 4: Keywords & Language
with tab4:
    st.markdown('<div class="step-header"><h2>Keywords & Language</h2><p>Use their words naturally</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    Read the job description 2-3 times. What words repeat? What skills do they emphasize?
    
    When you tell your stories, weave in these keywords naturally. It signals: "I get what you're looking for."
    """)
    
    st.markdown("### Extract Keywords")
    st.markdown('<div class="tip-box">What language appears most in the job posting? What problems are they trying to solve?</div>', unsafe_allow_html=True)
    
    keywords_input = st.text_area(
        "Keywords",
        value=", ".join(st.session_state.prep_data.keywords) if st.session_state.prep_data.keywords else "",
        placeholder="e.g., user-centric, cross-functional, impact, data-driven (separate by comma)",
        height=100,
        label_visibility="collapsed"
    )
    
    if keywords_input:
        st.session_state.prep_data.keywords = [k.strip() for k in keywords_input.split(",")]
        st.markdown(f'<div class="success-box">✓ Keywords captured: {", ".join(st.session_state.prep_data.keywords)}</div>', unsafe_allow_html=True)
    
    st.markdown("### Notes")
    st.markdown('<div class="tip-box">How will you weave these into your stories?</div>', unsafe_allow_html=True)
    st.session_state.prep_data.keyword_notes = st.text_area(
        "Notes",
        value=st.session_state.prep_data.keyword_notes,
        placeholder="e.g., When I tell Story 1, I'll emphasize how I was 'user-centric' in my approach...",
        height=100,
        label_visibility="collapsed"
    )

# TAB 5: Common Interview Questions
with tab5:
    st.markdown('<div class="step-header"><h2>Common Interview Questions</h2><p>Know the framework, not the script</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    These questions are likely to come up. Don't memorize answers—know the *framework* so you can answer naturally.
    """)
    
    questions_list = [
        ("Tell me about yourself", "Background → Key accomplishment → Why you're interested in this role"),
        ("Why are you interested in this role?", "What excites you about it → How your skills fit → What you want to learn/contribute"),
        ("Tell me about a time you solved a problem others couldn't see", "Situation → What you noticed → What action you took → The impact"),
        ("Tell me about a project or situation where you had to learn something new quickly", "What did you need to learn → How did you approach it → How did you apply it")
    ]
    
    for i, (q, framework) in enumerate(questions_list):
        with st.expander(f"**Q{i+1}: {q}**"):
            st.markdown(f"**Framework:** {framework}")
            question_key = f'q{i+1}'
            st.session_state.prep_data.questions.__dict__[question_key] = st.text_area(
                f"Your answer for Q{i+1}",
                value=st.session_state.prep_data.questions.__dict__.get(question_key, ''),
                placeholder="Think through how you'd answer this...",
                height=100,
                label_visibility="collapsed"
            )
    
    answered = sum([bool(st.session_state.prep_data.questions.__dict__.get(f'q{i+1}', '')) for i in range(4)])
    if answered >= 2:
        st.session_state.prep_data.questions.complete = True
        st.markdown(f'<div class="success-box">✓ You\'ve thought through {answered}/4 questions</div>', unsafe_allow_html=True)

# TAB 6: Your Questions
with tab6:
    st.markdown('<div class="step-header"><h2>Questions to Ask Them</h2><p>Show you think strategically</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    At the end of the interview, they'll ask: "Do you have any questions for me?"
    
    This is your moment to show you've done your homework and think like a partner.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### About the Role")
        st.markdown('<div class="tip-box">"What would success look like in the first 90 days?"</div>', unsafe_allow_html=True)
        st.session_state.prep_data.your_questions.q1 = st.text_area(
            "Q1",
            value=st.session_state.prep_data.your_questions.q1,
            placeholder="Or: What are the biggest priorities in this role?",
            height=100,
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### About the Team")
        st.markdown('<div class="tip-box">"What\'s the biggest challenge the team is facing right now?"</div>', unsafe_allow_html=True)
        st.session_state.prep_data.your_questions.q2 = st.text_area(
            "Q2",
            value=st.session_state.prep_data.your_questions.q2,
            placeholder="Or: What does your team struggle with most?",
            height=100,
            label_visibility="collapsed"
        )
    
    with col3:
        st.markdown("### About the Company")
        st.markdown('<div class="tip-box">"How do you measure impact in this position?"</div>', unsafe_allow_html=True)
        st.session_state.prep_data.your_questions.q3 = st.text_area(
            "Q3",
            value=st.session_state.prep_data.your_questions.q3,
            placeholder="Or: What would you want the person in this role to accomplish?",
            height=100,
            label_visibility="collapsed"
        )
    
    answered_q = sum([bool(st.session_state.prep_data.your_questions.__dict__.get(f'q{i}', '')) for i in range(1, 4)])
    if answered_q >= 2:
        st.markdown(f'<div class="success-box">✓ You have {answered_q}/3 questions ready</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
completed, total = calculate_progress()
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.markdown(f"### You're {int((completed/total)*100)}% Ready")
    if completed == total:
        st.markdown("🎉 **You're fully prepped!** Go crush that interview.")
    else:
        st.markdown(f"Keep going. {total - completed} sections left.")

with col3:
    if st.button("💾 Save & Download My Prep", use_container_width=True):
        prep_json = st.session_state.prep_data.model_dump_json(indent=2)
        st.download_button(
            label="Download as JSON",
            data=prep_json,
            file_name=f"interview_prep_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )

st.markdown("""
---
### Tips for Interview Day
1. **Tell your stories out loud** — Practice until they flow naturally
2. **Use their language** — Weave in the keywords from the job description
3. **Answer frameworks, not scripts** — Know the structure but answer authentically
4. **Ask your questions** — Show you've thought about the role strategically
5. **Breathe & Listen to music** — You've prepared. You're ready. Now shake off the nerves!

**Built with ❤️ for people who want to be strategic about their careers.**
""")