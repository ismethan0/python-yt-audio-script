import yt_dlp
import os

def youtube_to_mp3_here(url):
    # Script'in bulunduğu klasörü al
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # ffmpeg.exe aynı klasörde olmalı
    ffmpeg_path = os.path.join(script_dir, "ffmpeg.exe")

    # Çıkış dosyası da aynı klasöre kaydedilecek
    output_template = os.path.join(script_dir, "%(title)s.%(ext)s")

    # yt-dlp ayarları
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,  # ffmpeg burada
        'quiet': False
    }

    # İndirme ve dönüştürme işlemi
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n✅ MP3 dosyası oluşturuldu ve script klasörüne kaydedildi.")

# Kullanım örneği
youtube_to_mp3_here("link")
