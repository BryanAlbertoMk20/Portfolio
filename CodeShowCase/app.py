from flask import Flask, render_template

app = Flask(__name__)


APPS = [
    {
        'id': 1,
        'app_name': 'Send Email App'
    },
    {
        'id': 2,
        'app_name': 'Study App'
    },
    {
        'id': 3,
        'app_name': 'Create PDF App'
    },
    {
        'id': 4,
        'app_name': 'Image Converter App'
    }
]

@app.route("/")
def home_page():
    return render_template('home.html', aps=APPS, site_name='Bryans Code')

if __name__ == '__main__':
    app.run(debug=True)