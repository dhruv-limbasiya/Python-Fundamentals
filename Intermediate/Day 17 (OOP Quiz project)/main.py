# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1= User("1","Dhruv")
# user_2=User("2","Elon Musk")
#
# user_2.follow(user_1)
#
# print(user_1.followers)
# print(user_2.followers)

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for que in question_data:
    question_text = que["text"]
    question_answer = que["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    if quiz.question_number == len(question_bank):
        print(f"You've completed the quiz.")
        print(f"Your final score was: {quiz.score}/{len(question_bank)}")
