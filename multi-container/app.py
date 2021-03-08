import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    m_retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if m_retries == 0:
                raise exc
            m_retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"Hit refresh if you think Flask is a great engine. You've only refreshed {count} times. REFRESH MORE.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)