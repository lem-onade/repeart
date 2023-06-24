import math, getopt, sys
import random, string
from PIL import Image, ImageDraw, ImageFont

alg = "hello-world"
variance = 0.0

opts, _args = getopt.getopt(sys.argv[1:], "hA:V:", ["alg="])
for opt, arg in opts:
    if opt == '-h':
        print ('python3 main.py --alg <algorithm>')
        sys.exit()
    elif opt in ("-A", "--alg"):
        alg = arg
    elif opt in ("-V", "--variance"):
        print(f"Variance: {arg}")
        if arg == "random":
          variance = random.randint(0,99) / 10000
          print(f"Random variance: {variance}")
        else:
          variance = arg

font_size = 12
font_char_width = 0.585 * font_size * (1 + variance)

width_pixels = 2560
height_pixels = 1440
width_chars = math.ceil(width_pixels / font_char_width)
height_chars = math.ceil(width_pixels / font_size)

print

print(f"Font size: {font_size}px, font char width: {font_char_width}px")
print(f"Guessed font char width: {font_char_width}px")
print(f"Characters on one line: ", width_chars)
print(f"Characters on one column: ", height_chars)
print(f"Characters on one line: ", width_pixels / font_char_width)
print(f"Characters on one column: ", width_pixels / font_size)


def generate_message(alg: str = "hello-world"):

  if alg == "one":
    return "1"

  if alg == "selenium":
    session = f"{''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(32))}"
    element = f"{''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))}_element_{''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(4))}"
    return f"<selenium.webdriver.remote.webelement.WebElement (session=\"{session}\", element=\"{element}\")>"

  if alg == "hello-world":
    return "Hello world! "

  # otherwise return default alg as message
  return alg

# Generate image text
print(f"image size: {width_pixels}x{height_pixels} pixels ({width_chars}x{height_chars} chars, w/h)")
image = Image.new('RGB', (width_pixels, height_pixels), color='black')
draw = ImageDraw.Draw(image)

image_text = ""

repeats_per_line = math.ceil(width_chars / len(generate_message(alg)))
print(f"repeats per line: {repeats_per_line}")
repeats_in_image = repeats_per_line * height_chars
print(f"repeats in image: {repeats_in_image}")
message = generate_message(alg) * repeats_in_image
# print(f"line: {message}")
print(f"Repeating message with length {len(generate_message(alg))}, {repeats_per_line} times, should fit in {width_chars} max chars per line ({ len(generate_message(alg)) * repeats_per_line })")
text_lines = [message[i:i+width_chars] for i in range(0, len(message), width_chars)]
# print(f"text lines: {text_lines}")

for i in range(len(text_lines)):

  font = ImageFont.truetype("Andale Mono.ttf", font_size)

  draw.text((0, i * font_size), text_lines[i], font=font, fill=(255, 255, 255))

image.save('image.png')
