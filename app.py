from flask import Flask, request, jsonify, render_template, session
from chatbot_logic import get_response
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.json.get('message')
        greeted = session.get('greeted', False)
        response, greeted = get_response(user_message, greeted)
        session['greeted'] = greeted
        return jsonify({'response': response})
    return render_template('chat.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
