from flask import Flask, render_template, request
import pafy

app = Flask(__name__)

def scrape_info(url):
   video = pafy.new(url)
   return f'<h2>{video.title}</h2> <img src={video.bigthumb}><br> It"s rated {str(round(video.rating, 2))} out of ten<br> {str(video.viewcount)} views<br> {str(video.likes)} likes<br> {str(video.dislikes)} dislikes<br>'

@app.route("/")
def home():
   #return '<form method="POST"><input placeholder="Enter video url" name="text" type="text"></form>'
   return render_template('index.html')

@app.route('/', methods=['POST'])
def form():
   text = request.form['text']
   url = text
   data = scrape_info(url)
   print(text)
   video = pafy.new(url)
   #return '<form method="POST"><input name="text" type="text"></form><br>' + str(data)
   return render_template('stats.html', video=video)

if __name__ == "__main__":
   app.run()