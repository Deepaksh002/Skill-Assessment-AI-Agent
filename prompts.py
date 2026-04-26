# -------- SKILL EXTRACTION --------
SKILL_EXTRACTION_PROMPT = """
Extract all technical skills from the following text.

Return ONLY a comma-separated list.
No explanation.

Text:
{input_text}
"""

# -------- SKILL EVALUATION --------
EVALUATION_PROMPT = """
You are a technical interviewer.

Skill: {skill}

1. Generate 2 short interview questions
2. Assume an average candidate answer
3. Give a score (0 to 5)
4. Give a short justification

Return format:
Score: X
Reason: ...
"""

# -------- LEARNING PLAN --------
LEARNING_PLAN_PROMPT = """
Create a personalized learning plan.

Target Role: {role}
Missing Skills: {skills}

Include:
- Weekly roadmap
- Free resources (YouTube, docs)
- Realistic timeline
"""