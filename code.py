from PIL import Image, ImageEnhance, ImageColor, ImageFilter
import os

image = Image.open("pic.jpg")
# image.show()

## RESIZING of the Image
# newsize = (300,300)
# img_resized = image.resize(newsize)
# img_resized.save("resized.jpg")
# print(img_resized.size)

## IMAGE INFORMATION
# print(image.size)
# print(image.filename)
# print(image.format)
# print(image.format_description)

## Get all the image with same extension from a folder
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         print(f)


## Create a Blank image
# image_blank = Image.new('RGBA', (1000,600))
# # image_blank.show()

# print(image_blank.size)


## ROTATE an image

# image_rotate = image.rotate(60, expand = True, fillcolor = ImageColor.getcolor('green', 'RGB') )
# image_rotate.show()

## Crop an Image
#(left_x, top_y, right_x, bottom_y)
# image_crop = image.crop((0,0,1500, 1500))
# image_crop.show()

## FLIP an image

# image_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# image_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# image_transpose = image.transpose(Image.Transpose.TRANSPOSE)
# image_transverse = image.transpose(Image.Transpose.TRANSVERSE)
# image_rotate_90 = image.transpose(Image.Transpose.ROTATE_90)
# image_rotate_90.show()


# ## INCREASE the size of the image
# scale_factor = 2
# new = (image.size[0]*scale_factor , image.size[1]*scale_factor)
# new_image= image.resize(new)
# # new_image.show()
# print(image.size)
# print(new_image.size)


# img = image.convert('L')
# img.save("grayscaled.jpg")
# brightness_enhancer = ImageEnhance.Brightness(image)
# color_enhancer = ImageEnhance.Color(image)
# contrast_enhancer = ImageEnhance.Contrast(image)
# sharpness_enhancer = ImageEnhance.Sharpness(image)

# enhanced_image = sharpness_enhancer.enhance(6)
# enhanced_image.show()

## using filters
# image_blur = image.filter(ImageFilter.BLUR)
# image_contour = image.filter(ImageFilter.CONTOUR)
# image_detail = image.filter(ImageFilter.DETAIL)
# image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
# image_edge_more = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
# image_find = image.filter(ImageFilter.FIND_EDGES)
# image_emboss = image.filter(ImageFilter.EMBOSS)
# image_sharp = image.filter(ImageFilter.SHARPEN)
# image_smooth = image.filter(ImageFilter.SMOOTH)

# image_smooth.show()

# rank filters
# image_min = image.filter(ImageFilter.MinFilter(size = 5))
# image_median = image.filter(ImageFilter.MedianFilter(size = 5))


# image_median.show()


# Combine filters
image_emboss = image.filter(ImageFilter.EMBOSS)
image_embos_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius = 3))
image_embos_blur.save('99.png')
