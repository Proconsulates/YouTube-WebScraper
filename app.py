from flask import Flask, render_template, request
import pafy

app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.txt')

@app.route('/', methods=['POST'])
def form():
   url = request.form['text']
   try:
      v = pafy.new(url)
   except Exception as e:
      return "<h1>Video not found</h1><a href='/'>Back Home</a>"

   return render_template('stats.txt', video=v, rating=round(v.rating, 2))

if __name__ == "__main__":
   app.run()