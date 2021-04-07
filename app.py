from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index(): 
    title = "The Artist"
    name = "Hello"
    content = "Welcome to the Gallery"
    return render_template('index.html', title=title)

#add another
@app.route('/artist/<name>')
def showinfo(name): 
    if escape(name)=="Hung":
        return render_template('index.html', title="Simp man", name = "Hung", content= "Simp lord", intro= "One of the main Simp of UCC, a closet wjbu as he refuses to accept being a Simp lord, that is why he gets teased alot by the members of USTH Coder Club")
    if escape(name)=="Phuong":
        return render_template('index.html', title="Kimime Kimi", name = "Phuong", content= "The Artist")
    else:
        return render_template('index.html', title="Unknown", content= "Into the Unkknown!")

@app.route('/whatismyheight/<int:height>')
def show_height(height):
    doubleh = height * 2
    return "Your doubleh height is: " + str(doubleh)

#main_function
if __name__ == "__main__":
    app.run(debug=True)