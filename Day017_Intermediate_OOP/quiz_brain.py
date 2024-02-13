class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        answer = input(f"Q.{self.question_num}: {question.text} (True/False)? ")
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You are wrong!")
        print(f"The answer is: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_num}\n")

    def final(self):
        print(f"You,ve completed the quiz!\nYour final score is: {self.score}/{self.question_num}\n")
