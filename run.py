from flask import Flask
import yaml
import os
import socket

ENV = os.environ.get("ENV")
if ENV == "development":
    config_file = 'config/development.yml'
else:
    config_file = 'config/local.yml'
with open(config_file, 'r') as f:
    config = yaml.load(f)

app = Flask(__name__)


@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(
        name=os.getenv("NAME", "world"), hostname=socket.gethostname()
    )

if __name__ == "__main__":
    app.run(
        host=config['app']['host'], port=config['app']['port'],
        debug=config['app']['debug']
    )
