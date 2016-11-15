from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/portfolio')
def view_portfolio():
    return render_template('portfolio.html')


@app.route('/contact')
def contact_me():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
