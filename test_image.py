from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from num2words import num2words
import textwrap

# Load background and fonts
background = Image.open("background.png").resize((400, 713))
font_number = ImageFont.truetype("./Montserrat-Bold.ttf", 50)
font_text = ImageFont.truetype("./Montserrat-Bold.ttf", 22)

center_x, center_y = (background.width // 2, background.height // 2)

# Create frame
frame = background.copy()
draw = ImageDraw.Draw(frame)

# Number
number = 999999
num_with_commas = f"{number:,}"
# Number in words
number_as_text = num2words(number)
number_as_text=number_as_text.replace("-", " ").capitalize()
# Draw the number at a fixed position (e.g., slightly above center)
number_bbox = draw.textbbox((0, 0), num_with_commas, font=font_number)
number_width = number_bbox[2] - number_bbox[0]
number_height = number_bbox[3] - number_bbox[1]
num_x = center_x - number_width // 2
num_y = center_y - 95  # fixed vertical position
draw.text((num_x, num_y), num_with_commas, font=font_number, fill=(0,0,0))


# Wrap text if too wide
image_width, image_height = background.size
max_text_width = image_width * 0.8  # 80% of image width
wrapped_lines = textwrap.wrap(number_as_text, width=25)  # simple wrap

# Starting vertical position for words (below number)
line_gap = 5
font_size = 30
start_y = num_y + number_height + 80  # 80px gap below number

for line in wrapped_lines:
    line_width = font_text.getlength(line)
    x = (image_width - line_width) / 2  # horizontal center
    draw.text((x, start_y), line, font=font_text, fill=(0,0,0))
    start_y += font_size + line_gap

# Convert to OpenCV and show
frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
cv2.imwrite("test.png", frame_cv)
cv2.imshow("Live Count", frame_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
