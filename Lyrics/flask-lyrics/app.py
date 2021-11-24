from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
from main import findLyrics

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/lyrics')
def lyrics():
    return render_template('lyrics.html')

class RegisterForm(Form):
    SongName = StringField('SongName', [validators.Length(min=1, max=50)])
    SongArtist = StringField('SongArtist', [validators.Length(min=1, max=50)])

@app.route('/searchLyrics', methods=['POST', 'GET'])
def searchLyrics():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        lyrics = findLyrics(form.SongName.data, form.SongArtist.data)
        return render_template('lyrics.html', lyrics=lyrics, song_name=form.SongName.data)
    return render_template('searchLyrics.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
