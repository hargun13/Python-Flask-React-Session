from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/math')
def math():
    return 'Mathematics is the study of numbers, quantities, and shapes.'

@app.route('/science')
def science():
    return 'Science is the systematic enterprise that builds and organizes knowledge in the form of testable explanations and predictions.'

@app.route('/history')
def history():
    return 'History is the study of past events, particularly in human affairs.'

@app.route('/programming')
def programming():
    return 'Programming is the process of designing and building an executable computer program to accomplish a specific task.'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
