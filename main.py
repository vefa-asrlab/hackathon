import os, sys
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give an argument, check for README.md")
    else:
        if sys.argv[1] == "dev":
            app.run(debug=True)
        elif sys.argv[1] == "app":
            from waitress import serve
            print("Running app on port 8080")
            serve(app, host="0.0.0.0", port=8080)
        else:
            print("Wrong argument. Check for README.md")

    
    