from flask import Flask
from flask import jsonify
import git
import  os
from pydriller import Repository
app = Flask(__name__)

# def run():
#     unknown_dir = os.system("git log")
#     return unknown_dir

@app.route('/test')


def get_logs_from_github():
    g = git.Git('https://github.com/MhAiub/flaskProject/')
    hexshas = g.log()
    return jsonify(hexshas)



if __name__ == '__main__':

    app.run()

