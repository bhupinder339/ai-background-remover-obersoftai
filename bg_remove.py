from rembg import remove
from PIL import Image

input_path = "input.jpg"
output_path = "no_bg.png"

with open(input_path, "rb") as i:
    input_data = i.read()

output_data = remove(input_data)

with open(output_path, "wb") as o:
    o.write(output_data)

print("BACKGROUND REMOVED")

