#Michela Marchini

from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')
def blah():
    return "<h1><font color = blue>Hi, it's Michela</h1>"

@my_app.route('/second')
def foo():
    return "<b><font color = pink>Oooh look another page!!!!!</b>"

@my_app.route('/third')
def moo():
    return "<b><font color = purple>Guess what, its another page! But this time, it it's </b><i>italics</i>"

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
