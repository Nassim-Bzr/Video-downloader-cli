import yt_dlp

def telecharger_video(url, dossier="downloads/"):
    ydl_opts = {
        'outtmpl': f'{dossier}%(title)s.%(ext)s',
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Téléchargement terminé !")
    except Exception as e:
        print(f"❌ Erreur : {e}")

def choisir_plateforme():
    print("Bienvenue dans Video Downloader !")
    print("Choisis ta plateforme :")
    print("1. YouTube")
    print("2. Twitter")
    print("3. Instagram")
    print("4. Facebook")

    choix = input("Numéro de la plateforme : ")
    lien = input("Colle le lien de la vidéo ici : ")

    if lien:
        print("🔄 Téléchargement en cours...")
        telecharger_video(lien)
    else:
        print("❌ Lien invalide.")

if __name__ == "__main__":
    choisir_plateforme()
