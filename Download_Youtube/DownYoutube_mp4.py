# Importando as bibliotecas
from pytube import YouTube
import os

# Solicitando URL ao usuário
link = YouTube(
	str(input('Insira a URL do vídeo que deseja baixar: \n>> ')))

# Extraindo vídeo em alta resolução
video = link.streams.get_highest_resolution()

# Solicitando o local onde será salvo o arquivo
print('Insira o local em deve ser feito o download '
      '(deixe em branco e será feito o download no diretório atual): ')
destination = str(input(">> ")) or '.'

# Download do arquivo
out_file = video.download(output_path=destination)

# Salvando o arquivo com o nome do vídeo de origem
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)

print(link.title + ' foi baixado com sucesso :)')
