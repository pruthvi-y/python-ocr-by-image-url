from urllib.request import urlopen
from PIL import Image
import pytesseract

def process_image(image_source):
	return pytesseract.image_to_string(Image.open(urlopen(image_source)))

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	# sample test
	data_eng = process_image("https://raw.githubusercontent.com/pruthvi-y/python-ocr-by-image-url/main/resources/testimage1.png")
	print_data(data_eng)
	output_file("results/rawocr.txt", data_eng)

if  __name__ == '__main__':
	main()
