from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests
"""What did I get wrong here?
-I forgot to add self to the beginning of the functions in the class.
-The 'correct' answer also has more functions. I didn't make a check_answer function - 
I just checked it within the next_question function.
-I also printed in main instead of in quiz_brain. YMMV of course!!
-To make up for this I've created a new function get_new_questions that will pull new True/False questions from opentdb."""

def get_new_questions():
    """Pull new questions from opentdb.com. The fun never ends!"""
    opentdb_api_url = "https://opentdb.com/api.php?amount=10&type=boolean"
    response = requests.get(opentdb_api_url)
    try:
        return response.json()['results']
    except Error:
        exit("There was an error pulling new questions! Sorry.")

newquestions = input("Would you like to get random new questions? Type 'y' to get new questions.")
if newquestions == "y":
    question_data = get_new_questions()
else:
    print("Okay, we'll do the built-in bank of questions!")

question_bank = []
for question in question_data:
    # question_text = question['text']
    # question_answer = question['answer']
    # new_question = Question(question_text, question_answer)
    # question_bank.append(new_question)
    question_bank.append(Question(question['question'], question['correct_answer']))
# print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}")