import streamlit as st

def main():
    st.title("MCQ Quiz App")

    # Sidebar for inputting questions
    st.sidebar.header("Create Your Quiz")
    num_questions = st.sidebar.number_input("Number of Questions", min_value=1, max_value=50, step=1, value=5)

    # List to store questions and options
    questions = []

    for i in range(num_questions):
        st.sidebar.subheader(f"Question {i + 1}")
        question_text = st.sidebar.text_input(f"Enter Question {i + 1}:", key=f"question_{i}")
        options = [
            st.sidebar.text_input(f"Option {j + 1} for Q{i + 1}", key=f"q{i}_opt{j}")
            for j in range(4)
        ]
        correct_option = st.sidebar.selectbox(
            f"Select Correct Option for Q{i + 1}",
            options=[f"Option {j + 1}" for j in range(4)],
            key=f"correct_q{i}"
        )
        questions.append({
            "question": question_text,
            "options": options,
            "correct": options[int(correct_option.split()[-1]) - 1] if question_text and all(options) else None,
        })

    if st.sidebar.button("Generate Quiz"):
        if all(q["question"] and all(q["options"]) and q["correct"] for q in questions):
            st.success("Quiz generated! Scroll down to start.")
        else:
            st.error("Please fill in all fields before generating the quiz.")

    # Quiz section
    st.header("Quiz Section")

    if questions:
        user_answers = {}
        for idx, q in enumerate(questions):
            st.subheader(f"{idx + 1}. {q['question']}")
            user_answers[idx] = st.radio("Select your answer:", options=q["options"], key=f"answer_{idx}")

        if st.button("Submit Quiz"):
            score = 0
            for idx, q in enumerate(questions):
                if user_answers[idx] == q["correct"]:
                    score += 1
            st.success(f"Your Score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
