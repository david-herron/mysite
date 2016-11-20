from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from forms import ContactForm

mail = Mail()

app = Flask(__name__)

app.secret_key = '123'

app.config["Mail_SERVER"] = "smtp.gmail.com"
app.config["Mail_PORT"] = 465
app.config["Mail_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'herrondavid1@gmail.com'
app.config["MAIL_PASSWORD"] = 'Orange1Green5'

mail.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/portfolio')
def view_portfolio():
    return render_template('portfolio.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact_me():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash("All fields are required.")
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
            msg.body = """
                  From: %s <%s>
                  %s
                  """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run()
