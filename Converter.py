# VİDEODAN GIF'E DÖNÜŞTÜRMEK
from moviepy.editor import VideoFileClip

# MP4 video dosyasının yolu
video_path = 'C:/Users/Mert/Desktop/PYTHON/Gif/gif.mp4'

# Video dosyasını yükle
video_clip = VideoFileClip(video_path)

# İlk 3 saniyeyi al
clip = video_clip.subclip(0, 3)

# GIF olarak kaydet
gif_path = 'output.gif'
clip.write_gif(gif_path, fps=10)  # FPS (frame per second) değeri, GIF'in hızını belirler

print("GIF dönüştürme başarılı!")
