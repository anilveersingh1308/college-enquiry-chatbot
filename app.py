from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from fuzzywuzzy import process
import language_tool_python
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
tool = language_tool_python.LanguageTool('en-US')

def init_db():
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL,
            response TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('user_message')
def handle_user_message(data):
    user_input = data['message']
    corrected_input = correct_grammar(user_input)
    response = fetch_response(corrected_input)
    emit('bot_response', {'response': response})

def correct_grammar(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

def fetch_response(user_input):
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT keyword, response FROM responses")
    results = cursor.fetchall()
    conn.close()

    if results:
        keywords = [row[0] for row in results]
        best_match, score = process.extractOne(user_input, keywords)
        if score > 80:  # Threshold for considering a match
            responses = set()
            for row in results:
                if row[0] == best_match:
                    responses.add(row[1])
            return "\n".join(responses)
        else:
            # If no good match is found, try to find the closest keyword
            closest_matches = process.extract(user_input, keywords, limit=3)
            suggestions = [match[0] for match in closest_matches if match[1] > 50]
            if suggestions:
                return f"Did you mean: {', '.join(suggestions)}?"
    
    # Handle yes/no answers for true/false questions
    if user_input.lower() in ['yes', 'no']:
        if user_input.lower() == 'yes':
            return "True"
        else:
            return "False"

    return "I'm sorry, I didn't understand. Can you rephrase your question?"

if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True)
