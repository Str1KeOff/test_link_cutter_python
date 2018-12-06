from links import get_links, add_link, get_full_link
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', links=get_links())


@app.route('/link/<shorter_link>')
def redirect_to_link(shorter_link):
    return redirect(get_full_link(shorter_link))


@app.route('/cut_link', methods=["POST"])
def cut_link():
    link = request.form['link']
    link_name = request.form['link_name']
    add_link(link_name, link)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
