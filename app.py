from flask import Flask, render_template, request
import pafy

app = Flask(__name__)

def scrape_info(url):
   video = pafy.new(url)
   return video.viewcount

@app.route("/")
def home():
   return render_template('index.html')

@app.route('/', methods=['POST'])
def form():
   text = request.form['text']
   url = text
   data = scrape_info(url)
   print(text)
   return str(data) + ' views'

if __name__ == "__main__":
    app.run()