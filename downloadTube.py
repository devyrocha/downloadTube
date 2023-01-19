from pytube import YouTube

# cria um objeto do tipo Youtube
teste = input('Qual o link? ')
yt = YouTube(teste)

print('Baixando....')
yt.streams.order_by('resolution')[-1].download()
