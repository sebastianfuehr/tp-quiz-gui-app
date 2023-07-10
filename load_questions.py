import csv
import random


def get_questions(filename):
    print('Getting questions')
    questions = None

    try:
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            questions = list(reader)
            random.shuffle(questions)
    except:
        print('Unable to read the questions file.')
    
    return questions

if __name__ == '__main__':
    print(get_questions('questions.csv'))