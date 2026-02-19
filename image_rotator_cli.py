from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input_file")
parser.add_argument("output_file")
parser.add_argument("angle", type=int)

args = parser.parse_args()

im = Image.open(args.input_file)
print(im.size)

rotated = im.rotate(args.angle)
rotated.save(args.output_file)