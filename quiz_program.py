""" A quiz program that asks the user questions and counts all the right answers, if all the answers are correct it says so"""

# the data structure- a list of dictionarys whose values are lists of dictionaries

# You've got single-key dictionaries in this list. OK, but if a dictionary only ever has one key there's probably a better way. 
# How about replacing the list with a containing dictionary? This will make looking up a topic easier too, you don't need to deal with indexes. 
# Use indentation to make this more readable, for example,
topics = {
    'art': [
        {'Who painted the Mona Lisa? ': 'Leonardo Da Vinci'},
        {'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz lazuli'},
        {'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?': 'Chicago'},
        {'Which kid\'s TV characters are named after Renaissance artists?': 'Teenage Mutant Ninja Turtles'},
        {'The graphite in an artist\'s pencil is made of what chemical element?':  'Carbon'}
    ],
    'space': [
        {'Which planet is closest to the sun?': 'Mercury'},
        {'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus'},
        {'How many moons does Mars have?': '2'},
        {' What was the first human-made object to leave the solar system?': 'Voyager 1'},
        {'When an asteroid enters the Earth\'s atmosphere and burns up, it is known as what?': 'Meteor'},
    ],
    'sport': [
        {' Which gymnast is the "triple-twisting double-tucked salto backwards" skill named after?': 'Simone Biles'},
        {'Which country has won the soccer world cup the most times?': 'Brasil'},
        {'What does MLB stand for?': 'Major League Baseball'}    
    ]
}



# This isn't the main starting point of the program - can you think of a better name for this function? get_topic ? 
# Can you create a list 
def get_topic(topic_choices):
    is_topic = True
    while is_topic:
        # input returns string so no need to convert. 
        # What happens if a new topic is added? Or 'sport' is removed? 
        # Your dictionary uses the topics as keys, so topics.keys() is a list of the available topics. 
        # use topic_choices to print the choices 
        topic = input('Available questions are art, space , or sport, what kind would you like? ').lower()
        #ends the loop if a corrct catagory is entered or prints not a correct question
        # if topic == 'art' or topic =='space' or topic == 'sport':  # What happens if a new topic is added? Or 'sport' is removed? 
        if topic in topic_choices:  
#             is_topic = False  # you don't need this
            return topic  # because returning something will automatically end the loop
        else:
            print('That is not a correct topic, please try again.')

                 
def get_question(topic_question):  # I'm not sure what this function does. 
    # making a variable to use for the number in the list of catagory dictionarys to use later
    # Can this handle more topics? 
    # What happens if the order of topics in the topics list changes? 
    if topic_question == 'art':
        y = 0
    if topic_question == 'space':
        y = 1
    if topic_question == 'sport':
        y = 2 
    return topic_question, y   # What is the variable y ? Can you think of a more descriptive name? 


# does this ask one question or many? ask_questions (with a s) would be a better name.  
def ask_question(topic_question):
    # variables to keep track of number of questions and number of correct answers
    count = 0
    correct = 0
    # a loop to ask the questions from the list of catagory dictionaries 
    for topic in topics[topic_question]:   # Avoid variable names like x, k, v... use something more descriptive 
        #a loop to get the keys and values nested in a catagories values
            for question, correct_answer in topic.items():
                # asks question from keys in dictionary and puts it in a variable
                answer = input(question).lower() # str is redundant.  Does it make sense to store the answer the user enters in a variable called 'question'?
                count += 1

                if correct_answer.lower() == answer.lower():
                    print('correct')
                    correct +=1
                else:
                    print(f'sorry the correct answer is {correct_answer}')
    
    print('End of quiz')
    print(f'You got {correct} out of {count} answers correct')
    if correct == count:
        print('You got all correct')
             
     
# The function called main should be renamed something like get_topic.
# This code should be in a main function - this is the high-level tasks the program does 
def main():
    # getting the topic from main()

    topic_choices = topics.keys() 

    question_topic = get_topic(topic_choices)
    # calling get_question the question topic variable
    get_question(question_topic)
    #putting the topic of question and the number for place in list of the correct dictionary needed in variables 
    topic_question, y = get_question(question_topic)  # What is y ? 
    ask_question(topic_question)

                 
main() 


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
