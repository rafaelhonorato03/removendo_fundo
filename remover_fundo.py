from rembg import remove
from PIL import Image

input_path = 'divulgacao quimica.png'  # Arqvuivo de entrada
output_path = 'output.png'  # Arquivo para ser salvo

inp = Image.open(input_path)  # Abrindo a imagem de entrada
output = remove(inp)  # Removendo o fundo da imagem
output.save(output_path)  # Salvando a imagem