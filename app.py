from flask import Flask,redirect,render_template,send_file,Response,request
from pytube import YouTube


app = Flask(__name__)



@app.route('/')
def home():
   return render_template('index.html')


def descargar_video(url):
   video = YouTube(url)
   video.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
   return video



@app.route('/descarga',methods=['GET','POST'])
def descargar():
   if request.method == 'POST':
     try:
         url = request.form['url']
         video = descargar_video(url)
         return render_template('index.html',video=video)
     except:
        return redirect('/descarga')
  
   return render_template('index.html')
      


    




if __name__ == '__main__':
   app.run(debug=True,port=4000, host='localhost')
