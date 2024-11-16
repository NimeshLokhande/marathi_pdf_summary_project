from flask import Flask, render_template, request, redirect, url_for
from pdf_processing.extract_text import extract_text_from_pdf
from pdf_processing.summarize_text import summarize_text, extract_keywords
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return redirect(url_for('index'))

    file = request.files['pdf']
    if file.filename == '':
        return redirect(url_for('index'))

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

<<<<<<< HEAD

=======
>>>>>>> c3933b6215cdb0c0b76b9a5c8d030744867a7f08
    extracted_text = extract_text_from_pdf(file_path)

    summary = summarize_text(extracted_text)
    keywords = extract_keywords(extracted_text)


    print("Summary", summary)
    print("Keywords:", keywords)

<<<<<<< HEAD

=======
>>>>>>> c3933b6215cdb0c0b76b9a5c8d030744867a7f08
    return render_template('index.html', summary=summary, keywords=keywords)



if __name__ == '__main__':
    app.run(debug=True)
