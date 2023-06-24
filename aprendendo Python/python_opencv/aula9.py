import cv2

position_text = (0, 40)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 0, 0)

line_type = 2
logo_original = cv2.imread("fotos/mulher.jpg")

FPS = 20
WIDTH, HEIGHT = 640, 360

codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
video_writer = cv2.VideoWriter('output.avi', codec, FPS, (WIDTH, HEIGHT))

frames_count = 0
scale_percent = 100

while scale_percent >= 20:
    logo_copy = logo_original.copy()
    new_frame = logo_copy

    # escreve texto diretamente na imagem
    cv2.putText(new_frame,
                str(scale_percent),
                position_text,
                font,
                font_scale,
                font_color,
                line_type
                )

    # pra gerar 1 segundo de vídeo
    for f in range(FPS):
        video_writer.write(new_frame)
        frames_count += 1

    scale_percent -= 5

video_writer.release()
import subprocess

subprocess.call(['ffmpeg', '-i', 'output.avi', 'output.mp4', '-y'])  # -y é pra sobreescrever
0
from IPython.display import Video

Video("output.mp4", embed=True)