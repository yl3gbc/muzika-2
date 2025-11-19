from flask import Flask, render_template


app = Flask(__name__)
name='Pr.Andris Solims mūzikas lapa'
@app.route('/')
def home():
    return  render_template('index.html')
@app.route('/all.index')
def all():
    return render_template('all.html')
if __name__ == '__main__':
    app.run(debug=True)
