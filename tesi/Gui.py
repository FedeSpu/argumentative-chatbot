# MAIN WINDOW
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
from keras.models import load_model
import json
import random
import time
from tkinter import *
from MargotIO import MargotIO
import os.path
import choiceLabel

global isClosing

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
model = load_model('chatbot_model.h5')
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
isClosing = False


def ev_to_str(ev):
    str1 = ""
    for el in ev:
        str1 += "Confidence " + str(el[1]) + ":\n" + str(el[0]) + "\n\n"
    return str1



def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def getResponse(ints, intents_json):
    global isClosing
    tag = ints[0]['intent']
    if tag == 'margot':
        margot.show()
    elif tag == 'goodbye':
        isClosing = True
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    if tag == 'options':
        result = result + " [say 'run margot', 'margot', 'analise']"
    elif tag == 'margot':
        result = result + "\n[say 'show' for showing results]"
    elif tag == 'show':
        # result = margot.get_ev()[0][0]
        result = ev_to_str(margot.get_ev())
        choiceLab = choiceLabel.create(ChatLog, margot.get_ev(), margot.get_ev_user()[0])
        choiceLab.pack(side='bottom')
    return result


# Creating GUI with tkinter
def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12))
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        base.update()
        if isClosing:
            time.sleep(2)
            sys.exit(0)


margot = MargotIO()
base = Tk()
base.title("Argumentation Mining")
base.geometry("800x500")
base.resizable(width=FALSE, height=FALSE)
# Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="90", font="Arial",)
ChatLog.config(state=DISABLED)
# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
# Create Button to send message
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                    command=send)
# Create the box to enter message
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")
# EntryBox.bind("<Return>", send)
# Place all components on the screen
scrollbar.place(x=776, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=770)
EntryBox.place(x=128, y=401, height=90, width=665)
SendButton.place(x=6, y=401, height=90)
# Define closing behavior
# base.protocol("WM_DELETE_WINDOW", renf.save_vocabulary())
base.mainloop()
