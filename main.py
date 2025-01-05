import streamlit as st

def main():
    st.title("MCQ Quiz App")

    # Predefined questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct": "Paris",
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "options": ["Python", "Java", "JavaScript", "C++"],
            "correct": "JavaScript",
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct": "4",
        },
    ]

    # Session state to track current question and score
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0

    # Display current question
    current_question = st.session_state.current_question
    if current_question < len(questions):
        q = questions[current_question]
        st.subheader(f"Question {current_question + 1}: {q['question']}")
        user_answer = st.radio("Select your answer:", options=q["options"], key=f"answer_{current_question}")

        if st.button("Submit Answer"):
            if user_answer == q["correct"]:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! The correct answer is: {q['correct']}")

            st.session_state.current_question += 1
    else:
        st.success(f"Quiz completed! Your final score: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()
