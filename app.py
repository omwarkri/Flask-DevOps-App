from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Simple API endpoint
@app.route('/api/hello', methods=['GET'])
def api_hello():
    name = request.args.get('name', 'DevOps Learner')
    return jsonify({
        "message": f"Hello, {name}! 🚀",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
