from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Serve favicon
@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/favicon.png')
def favicon_png():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'favicon.png', mimetype='image/png')

# Expose the Flask app as 'application' for Vercel
application = app

if __name__ == '__main__':
    app.run(debug=True)