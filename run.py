from btty.flask_main import app
from btty.config import config

if __name__ == "__main__":
    app.run(
        host=config['app']['host'], port=config['app']['port'],
        debug=config['app']['debug']
    )
