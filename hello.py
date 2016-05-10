from flask import Flask, render_template
import os
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html', APP_ROOT)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()

