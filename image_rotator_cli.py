from PIL import Image
import argparse

parser = argparse.ArgumentParser(
    description="Rotador de imagen CLI usando Pillow"
)

parser.add_argument("input_file", help="Ruta de la imagen de entrada")
parser.add_argument("output_file", help="Ruta de la imagen de salida")
parser.add_argument("--angle", "-a", type=int, default=90, help="Ángulo de rotación en grados")

args = parser.parse_args()

im = Image.open(args.input_file)
print(im.size)

rotated = im.rotate(args.angle,expand=True)
rotated.save(args.output_file)