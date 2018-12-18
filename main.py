from dataloader import DataLoader
import csv
import spacy

nlp = spacy.load('en_core_web_sm')

def parse(string):
    """Parse input string to noun phrases"""
    doc = nlp(string)
    return [str(n) for n in doc.noun_chunks]

def read_file(file):
    text = []
    with open(file, newline='') as f:
        reader = csv.reader(f)
        next(reader, None) # skip header row
        for row in reader:
            text.append(row)
    return text
 
elem_lines = read_file('guide_elements.csv')
item_lines = read_file('guide_items.csv')
chatbot_lines = read_file('guide_chatbot.csv')

dataloader = DataLoader()

for line in elem_lines:
    dataloader.make_element(line[0])
for line in item_lines:
    dataloader.make_item(line[0], [x.strip() for x in line[1].split(',')], line[2])
for line in elem_lines:
    if line[1] != '':
        dataloader.set_followups(line[0], line[1])
line = chatbot_lines[0]
mychatbot =dataloader.make_bot(line[0], [x.strip() for x in line[1].split(',')])


mychatbot.greet()
while True:
    question = mychatbot.ask_question()
    if question == '':
        print("I don't have any other questions. Thanks for chatting. Good-bye.")
        break
    response = input(question)
    noun_phrases = parse(response)
    mychatbot.process_input(noun_phrases)

 