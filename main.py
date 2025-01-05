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

    # Quiz section
    st.header("Quiz Section")

    if questions:
        score = 0
        for idx, q in enumerate(questions):
            st.subheader(f"{idx + 1}. {q['question']}")
            user_answer = st.radio("Select your answer:", options=q["options"], key=f"answer_{idx}")

            if st.button(f"Submit Answer for Question {idx + 1}", key=f"submit_{idx}"):
                if user_answer == q["correct"]:
                    st.success("Correct!")
                    score += 1
                else:
                    st.error(f"Wrong! The correct answer is: {q['correct']}")
                st.write(f"Your current score: {score}/{idx + 1}")

if __name__ == "__main__":
    main()
