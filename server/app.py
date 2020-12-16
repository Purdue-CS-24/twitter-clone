import json
from flask import Flask, request, jsonify, session
from db import get_db, query_db, close_db
from pw import check_pw, generate_pw_hash

app = Flask(__name__)
app.config.from_object('config.Config')

# Close database after application closes
app.teardown_appcontext(close_db)


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route('/api/users/register', methods=['POST'])
def register():
    GET_USER_QUERY = 'SELECT * FROM users WHERE username=?'
    db = get_db()
    data = request.get_json()
    username = data['username']
    password = data['password']

    if query_db(GET_USER_QUERY, [username], one=True):
        return jsonify({
            'message': 'Username already taken. Try another.'
        }), 400

    pw_hash = generate_pw_hash(password)
    db.execute('INSERT INTO users (username, pw_hash) VALUES (?, ?)', [
               username, pw_hash])
    db.commit()

    return jsonify({
        'message': 'Successfully created account. Please log in.'
    }), 200


@app.route('/api/users/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = query_db('SELECT * FROM users WHERE username=?',
                    [username], one=True)

    if user is None or not check_pw(password, user['pw_hash']):
        return jsonify({
            'message': 'Invalid username/password.'
        }), 401

    session['user_id'] = user['id']
    return jsonify({
        'message': 'User succesfully authenticated.',
        'user': {
            'username': user['username']
        }
    }), 200


@app.route('/api/users/logout', methods=['GET'])
def logout():
    if session.get('user_id'):
        session.clear()
    return jsonify({}), 200


@app.route('/api/posts', methods=['GET'])
def get_posts():
    GET_ALL_POSTS_QUERY = 'SELECT posts.id AS id, time_posted, username AS author, content FROM posts JOIN users ON posts.user_id = users.id ORDER BY time_posted DESC'

    posts = query_db(GET_ALL_POSTS_QUERY)
    return jsonify({
        'posts': [dict(post) for post in posts]
    }), 200


@app.route('/api/posts/add', methods=['PUT'])
def add_post():
    INSERT_POST_QUERY = 'INSERT INTO posts (time_posted, user_id, content) VALUES (datetime("now"), ?, ?)'
    db = get_db()

    if not session.get('user_id'):
        return jsonify({
            'message': 'Please sign in.'
        }), 401

    data = request.get_json()
    content = data['content']
    user_id = session['user_id']

    db.execute(INSERT_POST_QUERY, [user_id, content])
    db.commit()
    return jsonify({
        'message': 'Successfully posted.'
    }), 201
