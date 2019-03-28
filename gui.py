from tkinter import *
from chatbot import main,chatbot

net, sess, chars, vocab, n, beam_width, relevance, temperature, topn = main()
root = Tk()
user = StringVar()
bot = StringVar()

root.title(" Simple ChatBot ")
Label(root, text=" user : ").pack(side=LEFT)
Entry(root, textvariable=user).pack(side=LEFT)
Label(root, text=" Bot  : ").pack(side=LEFT)
Entry(root, textvariable=bot).pack(side=LEFT)


def cb():
    question = user.get()
    bot_output = chatbot(net, sess, chars, vocab, n, beam_width, relevance, temperature, topn,question)
    # sess.close()
    bot.set(bot_output)


Button(root, text="send", command=cb).pack(side=LEFT)

mainloop()