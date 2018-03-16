from flask import Flask, jsonify, json, request
from modules import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return ''

@app.route('/cat', methods=['GET', 'POST'])
def get_cat_status():
    if request.method == 'POST':
        site_status = get_url_status.get_status_code(request.form['text'])
        message = slack_message.build_slack_message(site_status,"cat",request.form['text'], )
        return jsonify(message)

@app.route('/dog', methods=['GET', 'POST'])
def get_dog_status():
    if request.method == 'POST':
        site_status = get_url_status.get_status_code(request.form['text'])
        message = slack_message.build_slack_message(site_status, "dog", request.form['text'], )
        return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)