from flask import Flask

app = Flask(__name__)

def generate_html(message):
    html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="540" width="1200" src="https://i0.wp.com/build5nines.com/wp-content/uploads/2023/02/GitHub_Actions_Featured_Image.jpg">
                <br>
                {0}<br>
            </div>
        </body>
        </html>""".format(message)
    return html

def greet():
    greeting = 'Welcome to CI/CD 101 using GitHub Actions!'
    return greeting

@app.route('/greeting')
def hello_world():
    html = generate_html(greet())
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4049)