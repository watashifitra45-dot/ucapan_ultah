from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    nama = "AZZAHRA RAMADHANI"
    pesan = [ "🎉🎉.Happy Birthday Zah.🎉🎉",
     "Terimakasih telah bertahan sampai sejauh ini.",
     "Kamu kuat, kamu hebat.",
     "Semoga di usia yang baru ini.",
     "Kamu selalu di kelilingi hal-hal baik.",
     "Tetaplah tersenyum dan bahagia, walau terkadang dunia tak berpihak padamu.",
     "Semoga semua impian dan cita-citamu segera terwujud.",
     "AAMMIIN."
    ]
    return render_template('index.html', nama=nama, pesan=pesan)
    
app = app
if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
