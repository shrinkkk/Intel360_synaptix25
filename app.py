from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdfFile']
    if file:
        text = "Extracted text from PDF (to be implemented)"
        return jsonify({"text": text})
    else:
        return jsonify({"error": "No file uploaded"})

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text', '')
    summary = "Summary (to be generated)"
    return jsonify({"summary": summary})

@app.route('/qa', methods=['POST'])
def qa():
    question = request.json.get('question', '')
    answer = "Answer (to be generated)"
    return jsonify({"answer": answer})

@app.route('/trends', methods=['POST'])
def trends():
    trends = "Trends (to be fetched from DeepSeek)"
    return jsonify({"trends": trends})

if __name__ == '__main__':
    app.run(debug=True)
