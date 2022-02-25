from flask import Flask
from flask import jsonify
import git

app = Flask(__name__)


@app.route('/test')
def get_logs_from_github():
    repo = git.Git('https://github.com/MhAiub/flaskProject/')
    logs = repo.log()
    return jsonify(logs), 200


if __name__ == '__main__':
    app.run()
