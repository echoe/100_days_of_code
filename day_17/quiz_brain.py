#TODO: asking questions
#TODO: checking if answer is correct
#TODO: checking if we are at the end of the quiz
#attributes: question_number (keeping track of the question the user is on)
#questions_list (list of questions)
#methods: next_question()
#This displays question number, question text, and then asks the user for an input (True/False)

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        thequestion = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"q.{self.question_number}: {thequestion.text} ? (True/False): ")
        self.check_answer(user_answer, thequestion.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")