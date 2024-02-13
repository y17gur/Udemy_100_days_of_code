from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for _ in question_data:
    question_bank.append(Question(_["question"], _["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
quiz.final()
