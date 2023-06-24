import math
import getopt
import sys
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageColor
import requests

alg = "hello-world"
variance = 0.0
width_pixels = 500
height_pixels = 500
background_color = ImageColor.getrgb("black")

font_family = "Andale Mono"
font_color = ImageColor.getrgb("white")

opts, _args = getopt.getopt(
    sys.argv[1:],
    "hA:V:W:H:",
    [
        "alg=",
        "width=",
        "heigth=",
        "variance=",
        "fontColor=",
        "backgroundColor=",
    ]
)

for opt, arg in opts:
    if opt == '-h':
        print('python3 main.py --alg <algorithm>')
        sys.exit()
    elif opt in ("-W", "--width"):
        width_pixels = int(arg)
    elif opt in ("-H", "--heigth"):
        height_pixels = int(arg)
    elif opt in ("-A", "--alg"):
        alg = arg
    elif opt in ("-V", "--variance"):
        print(f"Variance: {arg}")
        if arg == "random":
            variance = random.randint(0, 99) / 10000
            print(f"Random variance: {variance}")
        else:
            variance = arg
    elif opt in ("--fontColor"):
        font_color = ImageColor.getrgb(arg)
    elif opt in ("--backgroundColor"):
        background_color = ImageColor.getrgb(arg)

font_size = 12
font_char_width = 0.585 * font_size * (1 + variance)
width_chars = math.ceil(width_pixels / font_char_width)
height_chars = math.ceil(width_pixels / font_size)

print(f"Image size: {width_pixels}x{height_pixels} pixels")
print(f"Characters: {width_chars}x{height_chars} chars")
print(f"Background color: {background_color}")
print(f"Font: Andale Mono")
print(f"Font color: {font_color}")
print(f"Font size: {font_size}px, font char width: {font_char_width}px")
print(f"Guessed font char width: {font_char_width}px")
print(f"Exact characters on one line: ", width_pixels / font_char_width)
print(f"Exact characters on one column: ", width_pixels / font_size)


def generate_message(alg: str = "hello-world"):

    print(f"Generating message with algorithm: {alg}")

    if alg == "one":
        return "1"

    if alg == "selenium":
        session = f"{''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(32))}"
        element = f"{''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))}_element_{''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(4))}"
        return f"<selenium.webdriver.remote.webelement.WebElement (session=\"{session}\", element=\"{element}\")>"

    if alg == "hello-world":
        return "Hello world! "
    
    if alg == "pi":
        return f"{str(math.pi)} "
    
    if alg == "bible":
        print("Downloading bible...")
        return requests.get("https://www.o-bible.com/download/kjv.txt").text.replace('\n', ' ')
    
    if alg.startswith("url="):
        url = alg.split("url=")[1]
        print(f"Sending GET {url}")
        return requests.get(url).text.replace('\n', ' ')

    # otherwise return default alg as message
    return alg


# Generate image text
image = Image.new('RGB', (width_pixels, height_pixels), color=background_color)
draw = ImageDraw.Draw(image)

image_text = ""

max_chars = width_chars * height_chars
repeat = generate_message(alg)[0:max_chars]

# repeat message until it fits in image
if len(repeat) < max_chars:
    print("Repeating message...")
    repeats_per_line = math.ceil(width_chars / len(repeat))
    print(f"Repeats per line: {repeats_per_line}")
    repeats_in_image = repeats_per_line * height_chars
    print(f"Repeats in image: {repeats_in_image}")
    repeat = repeat * repeats_in_image
    # print(f"line: {message}")
    print(f"Repeating message with length {len(repeat)}, {repeats_per_line} times, should fit in {width_chars} max chars per line ({ len(repeat) * repeats_per_line })")

# split into list of strings that fit in one line
text_lines = [repeat[i:i+width_chars]
    for i in range(0, len(repeat), width_chars)]

# print every line
for i in range(len(text_lines)):

    font = ImageFont.truetype(font_family, font_size)

    draw.text(
        (0, i * font_size), 
        text_lines[i], font=font, fill=font_color
    )

image.save('image.png')
