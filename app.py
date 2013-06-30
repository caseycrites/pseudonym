from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')

AUTHOR = app.config['AUTHOR']

@app.route("/")
def index():
    author = {
        "name": AUTHOR,
        "works": [
            {
                "url": "work1/toc/",
                "name": "Work 1"
            },
            {
                "url": "work2/toc/",
                "name": "Work 2"
            }
        ]
    }
    return render_template("index.html", author=author)

@app.route("/<workslug>/toc/")
def toc(workslug):
    work = {
        "name": "Work 1",
        "author": {
            "name": AUTHOR,
            "url": "/"
        },
        "chapters": [
            {
                "url": "/" + workslug + "/c1/p1",
                "number": 1
            },
            {
                "url": "/" + workslug + "/c2/p1",
                "number": 2
            }
        ]
    }
    return render_template("toc.html", work=work)

@app.route("/<workslug>/c<chapter>/p<page>")
def page(workslug, chapter, page):
    page = {
        "number": 1,
        "is_title": True,
        "previous_page": "/" + workslug + "/toc/",
        "next_page": "/" + workslug + "/c1/p2",
        "chapter": {
            "url": "/" + workslug + "/c1/p1",
            "number": 1
        },
        "work": {
            "url": "/" + workslug + "/toc/",
            "name": "Work 1"
        },
        "author": {
            "url": "/",
            "name": AUTHOR,
        }
    }
    return render_template("page_base.html", page=page)

if __name__ == "__main__":
    app.run(debug=True)
