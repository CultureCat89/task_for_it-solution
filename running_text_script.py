import cv2
import numpy as np
from save_requests import save_request

def create_video(video_file, text, width=100, height=100, duration_sec=3, fps=30):
    
    total_frames = int(fps * duration_sec)
    mp4_format = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_file, mp4_format, fps, (width, height))

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = .5
    font_thickness = 1
    
    text_color = (255, 255, 255)
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_y = int((height + text_size[1]) / 2)


    for count in range(total_frames):
        
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        text_x = int((width + text_size[0]) / 2 - count * duration_sec * width / total_frames)
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
        video_writer.write(frame)

    video_writer.release()


phrase = input('Input phrase:')
save_request(phrase)
create_video('running_text.mp4', phrase)
