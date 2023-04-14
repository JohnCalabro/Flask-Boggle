from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'abc123'

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def test_view():
    b = []
    board = Boggle.make_board(b)
    session["board"] = board
    # test = request.args['term']
    # print(test)
    args = request.args.to_dict()
    print(args)
    term = args.get('term')
    print(term)
    
    stri = str(term)
    

    check = boggle_game.check_valid_word(board, stri )
    print(check)
    if check == 'ok':
        msg = 'word!'
    elif check == 'not-on-board':
        print(check)
        msg = 'Not on board'
    
    elif check == 'not-word':
        msg = 'not a word'
    
    print(msg)

    
    return render_template('board.html', board=board, check=check, msg=msg)
    

# @app.route('/testing')
# def test2():
#     # term = request.form['term']
#     return f"""
#         <h1>Ok I guessed {term}</h1>
#     """

# @app.route('/word_check')
# def check_word():
#     print('hello')

# @app.route('/search')
# def search():
#     # term = request.args['term'] # <---- accessing the key's val
#     # we WOULD use term to find db data that matches term. 
#     guess = request.args["guess"]
#     return f"My guess is: {guess}"
#     # return f"<h1>SEARCH RESULTS FOR: {term}</h1>"

@app.route('/post', methods=["POST"])
def post_demo():
    return "YOU MADE A POST"

@app.route('/test-form')
def render_form():
    return """
        <form method="POST">
            <input type="text" name="msg"></input> 
            <input type="text" name="username"></input> 
            <button>Submit</button> 
        </form>
    """

@app.route('/test-form', methods=["POST"])
def save_val():
    msg = request.form["msg"]
    username = request.form["username"]
    

    return f"""
        <h1>Saved {username}'s message with text of {msg}</h1>
    """
        
       


