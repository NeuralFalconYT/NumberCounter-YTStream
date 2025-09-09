from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from num2words import num2words
import textwrap

# Load background and fonts once
background = Image.open("background.png").resize((400, 713))
font_number = ImageFont.truetype("./Montserrat-Bold.ttf", 50)
font_text = ImageFont.truetype("./Montserrat-Bold.ttf", 22)
image_width, image_height = background.size
center_x, center_y = (image_width // 2, image_height // 2)
number_y_move= 95
text_y_move= 80
def create_number_image(number,number_as_text):
    """
    Creates an image with the number (with commas) at a fixed position
    and the number in words centered below it.
    Returns the OpenCV frame.
    """
    # Copy background
    frame = background.copy()
    draw = ImageDraw.Draw(frame)

    # Format number
    num_with_commas = f"{number:,}"

    # Draw number at fixed position
    number_bbox = draw.textbbox((0, 0), num_with_commas, font=font_number)
    number_width = number_bbox[2] - number_bbox[0]
    number_height = number_bbox[3] - number_bbox[1]
    num_x = center_x - number_width // 2
    num_y = center_y - number_y_move
    draw.text((num_x, num_y), num_with_commas, font=font_number, fill=(0, 0, 0))

    # Wrap text if too wide
    wrapped_lines = textwrap.wrap(number_as_text, width=25)

    # Draw number in words below number
    line_gap = 5
    font_size = 22
    start_y = num_y + number_height + text_y_move  # vertical gap below number
    for line in wrapped_lines:
        line_width = font_text.getlength(line)
        x = (image_width - line_width) / 2
        draw.text((x, start_y), line, font=font_text, fill=(0, 0, 0))
        start_y += font_size + line_gap 

    # Convert to OpenCV format
    frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
    return frame_cv

from kokoro import KPipeline
import sounddevice as sd
from num2words import num2words

pipeline = KPipeline(lang_code='a')

def play_tts(text):
    generator = pipeline(text, voice='af_heart')
    for i, (gs, ps, audio) in enumerate(generator):
        sd.play(audio, samplerate=24000)
        sd.wait()
        

for number in range(0, 1000001):
    number_as_text = num2words(number).replace("-", " ").capitalize()
    frame_cv = create_number_image(number, number_as_text)
    cv2.imshow("Live Count", frame_cv)
    cv2.waitKey(1)
    play_tts(number_as_text)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # 100ms delay
        break

cv2.destroyAllWindows()
