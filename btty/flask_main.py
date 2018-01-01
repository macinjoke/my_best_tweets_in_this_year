from btty import util_tiwtter
from flask import Flask, render_template
from functools import reduce
import requests

app = Flask(__name__, template_folder="../templates")


@app.route("/")
def index():
    statuses = util_tiwtter.get_statues_in_this_year()
    sorted_statuses = sorted(statuses, key=lambda status: - status.favorite_count)

    favorite_amount = 0
    for status in sorted_statuses:
        favorite_amount += status.favorite_count

    top_10 = sorted_statuses[:10]
    tweets_info = [{
        'status': status,
        'oembed': requests.get(
            f'https://publish.twitter.com/oembed?url=https://twitter.com/{status.user.screen_name}/status/{status.id_str}'
        ).json()
    } for status in top_10]

    return render_template(
        'index.html', tweets_info=tweets_info, tweets_number=len(statuses),
        favorite_amount=favorite_amount
    )
