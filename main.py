from flask import Flask, render_template, request
from colorthief import ColorThief
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return 'No image provided', 400

    image = request.files['image']
    color_thief = ColorThief(image)

    colors = color_thief.get_palette(color_count=5)

    image.seek(0)
    encoded_image = base64.b64encode(image.read()).decode('utf-8')

    return render_template('result.html', colors=colors, uploaded_image=f'data:image/png;base64,{encoded_image}')

if __name__ == '__main__':
    app.run(debug=True)