# Importando as bibliotecas
from pytube import YouTube
import os

# Solicitando URL ao usuário
yt = YouTube(
	str(input('Insira a URL do vídeo que deseja baixar: \n>> ')))

# Extraindo somente o audío do vídeo
video = yt.streams.filter(only_audio=False).first()

# Solicitando o local onde será salvo o arquivo
print('Insira o local em deve ser feito o download '
      '(deixe em branco e será feito o download no diretório atual)')
destination = str(input(">> ")) or '.'

# Download do arquivo
out_file = video.download(output_path=destination)

# Salvando o arquivo
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + ' foi baixado com sucesso :)')
