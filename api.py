from flask import Flask, render_template, url_for, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter

app = Flask(__name__)


@app.route('/')
def home():
    return '''<h1>Welcome to A NLP api</h1><p>by Pengfei Liu.</p>'''


@app.route('/count', methods=['GET'])
def count():
    message = request.form['message']
    text = [message]
    Counter = Counter(text.split())
    most_occur = Counter.most_common(10)
    results = 'The 10 most comment words is %s'
    most_occur
    return jsonify(results)


@app.route('/sent', methods=['GET', 'POST'])
def sent():
    analyzer = SentimentIntensityAnalyzer()
    message = request.form['message']
    text = [message]
    results = analyzer.polarity_scores(text)
    if request.method == 'POST':
        return render_template('result.html', prediction=results)
    if request.method == 'GET':
        return jsonify(results)


if __name__ == '__main__':
    app.run()