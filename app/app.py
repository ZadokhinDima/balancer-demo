import argparse
from flask import Flask, abort

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--server_name", help="Name of the server")
args = parser.parse_args()

server_name = args.server_name

active = True

@app.route('/', methods=['GET'])
def handle_request():
    return "Handled by: " + server_name

@app.route('/switch', methods=['GET'])
def switch():
    global active
    active = not active
    return server_name + " active = " + str(active)

@app.route('/health', methods=['GET'])
def health():
    if active:
        return "Healthy"
    else:
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0')