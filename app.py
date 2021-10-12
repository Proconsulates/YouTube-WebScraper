from flask import Flask, render_template, request
import pafy

app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.html')

@app.route('/', methods=['POST'])
def form():
   text = request.form['text']
   url = text
   print(text)
   video = pafy.new(url)
   return render_template('stats.html', video=video)

if __name__ == "__main__":
   app.run()