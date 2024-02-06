from flask import Flask, render_template, request, jsonify
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from util import hu_stopwords, ro_stopwords, de_stopwords

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_wordcloud', methods=['POST'])
def generate_wordcloud():
    text = request.form['text']

    # add Hungarian stopwords
    hungarian_stopwords = hu_stopwords()
    # add Romanian stopwords
    romanian_stopwords = ro_stopwords()
    # add German stopwords
    german_stopwords = de_stopwords()

    stop_words = hungarian_stopwords + romanian_stopwords + german_stopwords + list(STOPWORDS)

    # Generate word cloud
    wordcloud = WordCloud(stopwords = stop_words, width=800, height=400, background_color='white').generate(text)

    # Convert word cloud to base64 image
    img = BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    img_str = base64.b64encode(img.getvalue()).decode('utf-8')

    return jsonify({'image': img_str})

if __name__ == '__main__':
    app.run(debug=True)
