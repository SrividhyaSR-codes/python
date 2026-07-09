import streamlit as st
from questions import questions

st.set_page_config(
    page_title="GenAI Quiz",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Generative AI Quiz")

st.write(
    "Test your knowledge on Generative AI technologies."
)

score = 0

answers = []

for index, question in enumerate(questions):

    st.subheader(f"Question {index+1}")

    user_answer = st.radio(
        question["question"],
        question["options"],
        key=index
    )

    answers.append(user_answer)

if st.button("Submit Quiz"):

    score = 0

    for i in range(len(questions)):
        if answers[i] == questions[i]["answer"]:
            score += 1

    st.success(f"Your Score: {score} / {len(questions)}")

    percentage = (score / len(questions)) * 100

    st.write(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        st.balloons()
        st.success("Excellent! You're a GenAI Expert!")

    elif percentage >= 70:
        st.info("Great Job! You have good GenAI knowledge.")

    elif percentage >= 50:
        st.warning("Good effort! Keep learning.")

    else:
        st.error("Keep practicing GenAI concepts.")

    st.divider()

    st.header("Correct Answers")

    for i in range(len(questions)):
        st.write(f"**Q{i+1}. {questions[i]['question']}**")
        st.write(f"Your Answer : {answers[i]}")
        st.write(f"Correct Answer : {questions[i]['answer']}")
        st.write("---")