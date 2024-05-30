class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        while (self.question_number < len(self.questions_list)):
            self.next_question()
        print("You've completed the quiz!")
        print(f"Your final score is {self.score}/{self.question_number}.")

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("Congrats! You are correct!")
            self.score += 1
        else:
            print("Sorry, you are wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
