import os
from flask import Flask, redirect, request, render_template, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Home page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# About me page
@app.route("/about")
def about_me():
    about_me = {
        "name": "Ronja",
        "age": 219,
    }

    return f"<p>My name is {about_me['name']} and I am {about_me['age']} years old.</p>"

# Form page
@app.route("/form")
def form():
    return render_template("form.html")

# Form submission page
@app.route("/submit", methods=['GET', "POST"])
def form_post():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        return render_template("form_sent.html", name=name, email=email)
    return render_template("form.html")

# File upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Check if file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# File upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('list_uploaded_files'))
    return render_template('upload.html')

# List uploaded files
@app.route('/upload/list')
def list_uploaded_files():
    files = os.listdir(app.config['UPLOAD_FOLDER']) 
    return render_template('uploaded_files.html', files=files)

# Display uploaded file
@app.route('/upload/files/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(error):
    return "<p>Page not found</p>", 404

if __name__ == "__main__":
    app.run(debug=True)