import random
import tkinter as tk
from chatbot import main, chatbot
root = tk.Tk()
root.title("RNN chatbot")
root.geometry('650x400')
user_input = tk.Entry(root)
user_input.pack()

net, sess, chars, vocab, n, beam_width, relevance, temperature, topn = main()

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?','what is your name?','can you help me?']
responses = ['Okay', "I'm fine", 'My name is Chatbot','sure!, I am happy to help you']


def cb(event):
    user_text = user_input.get()
    if user_text in greetings:
        bot_text = random.choice(greetings)
    elif user_text in question:
        bot_text = responses[question.index(user_text)]
    else:
        bot_text = chatbot(net, sess, chars, vocab, n, beam_width, relevance, temperature, topn, user_text)
    output.config(text=bot_text+'\n')


user_input.bind("<Return>", cb)
output = tk.Label(root, text='\n')
output.pack()
tk.mainloop()
