from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    # '0.0.0.0' allows external access (useful for Docker or Render)
    app.run(host='0.0.0.0', port=5000, debug=True)
