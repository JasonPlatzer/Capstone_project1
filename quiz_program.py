""" A quiz program that asks the user questions and counts all the right answers, if all the answers are correct it says so"""

# the data structure- a list of dictionarys whose values are lists of dictionaries
topics = [{'art':[
{'Who painted the Mona Lisa? ': 'Leonardo Da Vinci'},
{'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli'},
{'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'},
{'Which kid\'s TV characters are named after Renaissance artists?': 'Teenage Mutant Ninja Turtles'},
{'The graphite in an artist\'s pencil is made of what chemical element?':  'Carbon'}
]},
{'space': [
{'Which planet is closest to the sun?': 'Mercury'},
{'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus'},
{'How many moons does Mars have?': '2'},
{' What was the first human-made object to leave the solar system?': 'Voyager 1'},
{'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?': 'Meteor'},
]
},
{'sport':
[
{' Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': 'Simone Biles'},
{'Which country has won the soccer world cup the most times?': 'Brasil'},
{'What does MLB stand for?': 'Major League Baseball'}    
]
}
]


def main():
    is_topic = True
    while is_topic:
        topic = str(input('Available questions are art, space , or sport, what kind would you like? ').lower())
        #ends the loop if a corrct catagory is entered or prints not a correct question
        if topic == 'art' or topic =='space' or topic == 'sport':
            is_topic = False
            return topic
        else:
            print('That is not a correct topic')

def get_question(topic_question):
    # making a variable to use for the number in the list of catagory dictionarys to use later
    if topic_question == 'art':
        y = 0
    if topic_question == 'space':
        y = 1
    if topic_question == 'sport':
        y = 2
    return topic_question, y

def ask_question(topic_question, y):
    # variables to keep track of questions and correct answers
    count = 0
    correct = 0
    # a loop to ask the questions from the list of catagory dictionaries 
    for x in topics[y][topic_question]:
        #a loop to get the keys and values nested in a catagories values
            for k,v in x.items():
                # asks question from keys in dictionary and puts it in a variable
                question = str(input(k).lower())
                count += 1

                if question == v.lower():
                    print('correct')
                    correct +=1
                else:
                    print(f'sorry the correct answer is {v}')
    
    print('End of quiz')
    print(f'You got {correct} out of {count} answers correct')
    if correct == count:
        print('You got all correct')
            

       
    


            
     
# getting the topic from main()
question_topic = main()
# calling get_question the question topic variable
get_question(question_topic)
#putting the topic of question and the number for place in list of the correct dictionary needed in variables 
topic_question, y = get_question(question_topic)
ask_question(topic_question, y)



# topic = input('Would you like art, space , or sport questions? ')

# if topic == 'art':

#     print('Who painted the Mona Lisa?')
#     answer = input('Enter your answer: ')
#     if answer == 'Vincent Van Gogh':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the answer is Leonardo Da Vinci.')
    
#     print('What precious stone is used to make the artist\'s pigment ultramarine?')
#     answer = input('Enter your answer: ')
#     if answer == 'Lapiz lazuli':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Lapiz lazuli.')

#     print('Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?')
#     answer = input('Enter your answer: ')
#     if answer == 'Chicago':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Chicago.')

#     print('End of quiz!')
#     print(f'Your total score on {topic} questions is {total_score} out of 3.')

#     if total_score == 3:
#         print('You got all the answers correct!')


# elif topic == 'space':
    
#     print('Which planet is closest to the sun?')
#     answer = input('Enter your answer: ')
#     if answer == 'Mercury':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Mercury.')

#     print('Which planet spins in the opposite direction to all the others in the solar system?')
#     answer = input('Enter your answer: ')
#     if answer == 'Venus':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is Venus.')

#     print('How many moons does Mars have?')
#     answer = input('Enter your answer: ')
#     if answer == '2':
#         print('Correct!')
#         total_score += 1
#     else:
#         print('Sorry, the correct answer is 2.')

#     print('End of quiz!')
#     print(f'Your total score on {topic} questions is {total_score} out of 3.')

#     if total_score == 3:
#         print('You got all the answers correct!')

# else:
#     print('That is not a valid topic. Restart the program to try again.')