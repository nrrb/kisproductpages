In OS X Terminal, image resizing and conversion can be done with the "sips" command:

# Convert an image from PNG to JPEG:

sips -s format jpeg image.png --out image.jpg

# Resize an image so its largest dimension is 500 pixels

sips -Z 500 image.jpg --out image2.jpg

# Crop an image so it's 500 pixels wide and 400 pixels tall

sips -c 400 500 image.jpg --out image2.jpg

# Pad an image so it's 500 pixels wide and 400 pixels tall, padding with white

sips --padToHeightWidth 400 500 --padColor FFFFFF image.jpg --out image2.jpg