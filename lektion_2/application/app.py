from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    page = f'''<h1>This is a header</h1>
    <h2>This is a subheader</h2>
    <p>This is a paragraph</p>
    <h1>en till header</h1>'''
    
    return page

if __name__ == '__main__':
    app.run(debug=True)
