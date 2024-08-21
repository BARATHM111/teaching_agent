from flask import Flask, render_template, request
from agents import teach_concept, analyze_paper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teach', methods=['POST'])
def teach():
    concept = request.form['concept']
    explanation = teach_concept(concept)
    return render_template('results.html', explanation=explanation, concept=concept)

@app.route('/analyze', methods=['POST'])
def analyze():
    paper_content = request.files['paper_content'].read().decode('utf-8')
    analysis = analyze_paper(paper_content)
    return render_template('analysis.html', analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)
