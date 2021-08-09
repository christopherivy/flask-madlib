from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Make the home page


@app.route('/')
def questions():
    """ form for asking the words to use """

    prompts = story.prompts

    return render_template('questions.html', prompts=prompts)


@app.route('/story')
def show_story():
    """ Show the story results """
    # add request.args here because we expect user to add something.
    text = story.generate(request.args)

    return render_template('story.html', text=text)
