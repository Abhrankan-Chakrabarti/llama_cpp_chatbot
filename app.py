from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/completion', methods=['GET', 'POST'])
def completion_api():
    if request.method == "POST":
        data = request.form
        input_text = data['input_text']
        return Response(stream(input_text, model), mimetype='text/event-stream')
    else:
        return Response(None, mimetype='text/event-stream')

def globalize(m, s):
    global model, stream
    model, stream = m, s

def main(model, stream):
    globalize(model, stream)
    app.run(debug=True, use_reloader=False)