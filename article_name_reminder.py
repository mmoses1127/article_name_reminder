

# Import modules required for importing contents of web-based news article and for processing natural language


from newspaper import Article
import nltk


# Allow user to input url of desired news article
# url = input("Please input the entire URL of the news article you'd like to read:")
url = "https://www.nbcnews.com/news/us-news/justice-clarence-thomas-says-abortion-leak-changed-supreme-court-rcna28864"
# Specify the language of the news article
article = Article(url)
article.download()
article.parse()
article.authors

# Create dictionary to match all names with a description
names = {}

# #Search article for each instance of 2 capitalized words in a row, then add them as keys to the above dictionary, each paired with a value of the 3 sentences appearing around the first instance of the name in the article
# for word in article:
#       names[word1= word2] = # How select 3 sentences around the word?
# Import natural language kits for processing sentences and words, useful for harvesting sentences for the descreiptions.
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
sentences = sent_tokenize(article.text)
sent = ""
for idx, word in enumerate(article.text.split()):
    if idx > 0:
        prev_word = str(article.text.split()[idx - 1])
        if prev_word.isupper() and word.isupper():
            for i in range(len(sentences)):
                if word.lower() in word_tokenize(sentences[i].lower()) and prev_word.lower() in word_tokenize(sentences[i].lower()):
                    sent = sentences[i]
            names["{} {}".format(prev_word, word)] = sent
for idx, word in enumerate(article.text.split()):
    if word in names:
        word = ("<em>",word,"<em>")


# for k, v in names.items():
#     print (k, '-->', v)
#
#
# import tkinter as tk
#
# def show_info(text):
#     label.configure(text=key)
#
# root = tk.Tk()
# text_widget = tk.Text(root)
# label = tk.Label(root)
#
# label.pack(side="top", fill="x")
# text_widget.pack(fill="both", expand=True)
# message =article.text
#
# for key in (names):
#     tag = key
#     text = key
#     text_widget.insert("end", text+"\n", (tag, ))
#
#     text_widget.tag_configure(tag, background="green", foreground="white")
#     text_widget.tag_bind(tag, "<Enter>",
#                          lambda event, color="blue": show_info(color))
#     text_widget.tag_bind(tag, "<Leave>",
#                          lambda event, color="orange": show_info(""))
#
# tk.mainloop()


import tkinter as tk
from tkinter import *

# ws = Tk()
# ws.title(article.title)
# ws.geometry('600x600')
# ws.config(bg='#84BF04')
#
# message =article.text
#
# text_box = Text(
#     ws,
#     height=30,
#     width=80
# )
# text_box.pack(expand=True)
# text_box.insert('end', message)
# text_box.config(state='disabled')
#
# ws.mainloop()

# # Tooltip Time!
#
# try:
#     # for Python2
#     import Tkinter as tk
# except ImportError:
#     # for Python3
#     import tkinter as tk
#
# class CreateToolTip(object):
#     """
#     create a tooltip for a given widget
#     """
#     def __init__(self, widget, text='widget info'):
#         self.waittime = 500     #miliseconds
#         self.wraplength = 180   #pixels
#         self.widget = widget
#         self.text = text
#         self.widget.bind("<Enter>", self.enter)
#         self.widget.bind("<Leave>", self.leave)
#         self.widget.bind("<ButtonPress>", self.leave)
#         self.id = None
#         self.tw = None
#
#     def enter(self, event=None):
#         self.schedule()
#
#     def leave(self, event=None):
#         self.unschedule()
#         self.hidetip()
#
#     def schedule(self):
#         self.unschedule()
#         self.id = self.widget.after(self.waittime, self.showtip)
#
#     def unschedule(self):
#         id = self.id
#         self.id = None
#         if id:
#             self.widget.after_cancel(id)
#
#     def showtip(self, event=None):
#         x = y = 0
#         x, y, cx, cy = self.widget.bbox("insert")
#         x += self.widget.winfo_rootx() + 25
#         y += self.widget.winfo_rooty() + 20
#         # creates a toplevel window
#         self.tw = tk.Toplevel(self.widget)
#         # Leaves only the label and removes the app window
#         self.tw.wm_overrideredirect(True)
#         self.tw.wm_geometry("+%d+%d" % (x, y))
#         label = tk.Label(self.tw, text=self.text, justify='left',
#                        background="#ffffff", relief='solid', borderwidth=1,
#                        wraplength = self.wraplength)
#         label.pack(ipadx=1)
#
#     def hidetip(self):
#         tw = self.tw
#         self.tw= None
#         if tw:
#             tw.destroy()

# # testing ...
# if __name__ == '__main__':
#     root = tk.Tk()
#     btn1 = tk.Button(root, text=names[1])
#     btn1.pack(padx=10, pady=5)
#     button1_ttp = CreateToolTip(btn1, \
#    'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, '
#    'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
#    'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam '
#    'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.')
#
#     btn2 = tk.Button(root, text=names[2])
#     btn2.pack(padx=10, pady=5)
#     button2_ttp = CreateToolTip(btn2, \
#     "First thing's first, I'm the realest. Drop this and let the whole world "
#     "feel it. And I'm still in the Murda Bizness. I could hold you down, like "
#     "I'm givin' lessons in  physics. You should want a bad Vic like this.")
#     root.mainloop()

# FROM NET: Code for deriving people's names by chunking adjacent proper nouns. Currently having trouble with dependencies.
# https://www.geeksforgeeks.org/nlp-proper-noun-extraction/
# !!!DO not create entries for duplicates or for 1-word proper nouns.!!!
# from nltk.chunk import ChunkParserI
# from nltk.chunk.util import conlltags2tree
# from nltk.corpus import names

# class PersonChunker(ChunkParserI):
#     def __init__(self):
#         self.name_set = set(names.words())

#     def parse(self, tagged_sent):

#         iobs = []
#         in_person = False
#         for word, tag in tagged_sent:
#             if word in self.name_set and in_person:
#                 iobs.append((word, tag, 'I-PERSON'))
#             elif word in self.name_set:
#                 iobs.append((word, tag, 'B-PERSON'))
#                 in_person = True
#             else:
#                 iobs.append((word, tag, 'O'))
#                 in_person = False

#         return conlltags2tree(iobs)

# If using above solution, how to best add the chunked names to a list/dictionary for later access?

# Parse the rest of the document for words contained in the dictionary key. When matching, change the color of the word(s) to blue and create a tooltip on hover with the description from the dictionary.
# How to allow matching of just one word instance with just one word of the chunked name in dictionary key? How to allowing chunking when 2 word names are again present?


# FROM NET FOR MAKING TOOLTIP: Import the tkinter library
# How to use tooltip without making a box or button. I just want to have the text change color and allow hover on it.
from tkinter import *
from tkinter.ttk import *

# # Iterate through all the words in the article.
# button_created = False
# for idx, word in enumerate(article.text):
#     for name in names.keys():
#         if word in name:
#             # Create a button
#             button_created = True
#
#     if not button_created:
#         # Create a label.
#         pass

#       my_button = Button(win, text = word, font = ('Helvetica bold', 20))
# my_button.pack(pady = 20)

# Put each word in a label or a button.


# Create an instance of tkinter frame
# win = Tk()
# # Set the geometry
# win.geometry("400x200")
#
# # Create a tooltip
# tip = Balloon(win)

# # Create a Button widget
# my_button = Button(win, text=word, font=('Helvetica bold', 20))
# my_button.pack(pady=20)
#
# # Bind the tooltip with button
# tip.bind_widget(my_button, balloonmsg=names[word])
# win.mainloop()

# OPTIONAL:
# Add a list of all names and their descriptions? How display to user?
# Include a Wikipedia or other link to the tooltip text for more info?
# Add integration to browser or reader apps?

# create an html page with the article text

# write-html-2-windows.py

import webbrowser

f = open('helloworld.html','w')
message = """<html>
<head></head>
<body><h1>Title Here</h1>
<p>{article}<p>
<h2>List of Names</h2>
<p></p>
</body>
</html>""".format(article=article.text)

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')
