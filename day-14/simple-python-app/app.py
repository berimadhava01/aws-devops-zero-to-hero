from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

#adding line to check codepipeline
a = 2
b =3
sum(a, b)
