from flask import Flask, render_template

app = Flask(__name__)

# Página
# route
# função

@app.route("/")
def pag_inicial():

    return render_template('index.html')

@app.route("/playlists")
def pag_playlist():

    return render_template('album.html')

@app.route("/Pisero")
def musicas_piseiro():

    return render_template('pisero.html')

@app.route("/Sertanejo")
def musicas_sertanejo():

    return render_template('sertanejo.html')

if __name__ == "__main__":

    app.run(debug=True)