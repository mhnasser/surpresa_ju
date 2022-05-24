from flask import Flask, render_template
import os

application = Flask(__name__)

@application.route("/")
def pag_inicial():

    return render_template('index.html')

@application.route("/playlists")
def pag_playlist():

    return render_template('album.html')

@application.route("/Pisero")
def musicas_piseiro():

    return render_template('pisero.html')

@application.route("/Sertanejo")
def musicas_sertanejo():

    return render_template('sertanejo.html')

@application.route("/Lovesongs")
def musicas_lovesongs():

    return render_template('lovesongs.html')

@application.route("/Us")
def musicas_us():

    return render_template('us.html')


if __name__ == "__main__":

    application.run(host='0.0.0.0', port = 80)