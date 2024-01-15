from PIL import Image

# Opening the original image
original_img_p = 'chapter1.jpg'
original_img = Image.open(original_img_p)

# Generating a number using the provided algorithm
import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

# Function to convert pixels in the image
def convert_pixels(pixel):
    return tuple([p + generated_number for p in pixel])

# Creating a new image with converted pixels
new_image = Image.new('RGB', original_img.size)
for x in range(original_img.width):
    for y in range(original_img.height):
        original_pixel = original_img.getpixel((x, y))
        new_pixel = convert_pixels(original_pixel)
        new_image.putpixel((x, y), new_pixel)

# Saving the new image
new_image_path = 'chapter1out.png'
new_image.save(new_image_path)

# Calculating the sum of red pixel values in the new image
red_pixel_sum = sum(new_image.getdata(band=0))  # 'band=0' represents the red channel

# Printing the sum of red pixel values
print("Sum of red pixel values:", red_pixel_sum)
