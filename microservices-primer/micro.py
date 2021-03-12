import os, time
from flask import Flask, json, request, jsonify

micro = Flask(__name__)
users_seen = {}

@micro.route("/")
def hello():
    m_user_agent = request.headers.get('User-Agent')
    return f"Hello! I see you are using {m_user_agent}"

@micro.route("/checkin/<user>", methods=['POST'])
def check_in(user):
    global users_seen
    users_seen[user] = time.strftime('%Y-%m-%d')
    return jsonify(success=True, user=user)

@micro.route("/last-seen/<user>")
def last_seen(user):
    global users_seen
    if user in users_seen:
        return jsonify(user=user, date=users_seen[user])
    else:
        return jsonify(error='Who dis?', user=user), 404


if __name__ == "__main__":
    micro.run(
        host=os.environ.get("HTTP_HOST", "127.0.0.1"),
        port=os.environ.get("HTTP_PORT", "5000"),
        debug=os.environ.get("HTTP_DEBUG", True)
    )