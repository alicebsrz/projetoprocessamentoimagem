# Importando as bibliotecas 
import os
import glob
from skimage import io, color
from skimage.util import img_as_ubyte


# Pasta onde estão as imagens coloridas originais
pasta_originais = 'Imagens'
# Pasta onde as novas imagens em cinza serão salvas
pasta_destino_cinza = 'Imagens_Cinza'

# 1. Criar a pasta de destino se ela não existir
# O os.makedirs garante que a pasta seja criada sem erros se ela já existir
print(f"Verificando/Criando a pasta de destino: {pasta_destino_cinza}")
os.makedirs(pasta_destino_cinza, exist_ok=True)

# 2. Encontrar todas as imagens .jpg na pasta original
caminho_imagens_originais = os.path.join(pasta_originais, '*.jpg')
lista_imagens = glob.glob(caminho_imagens_originais)

print(f"\nEncontradas {len(lista_imagens)} imagens para converter.")

# 3. Processar cada imagem da lista
for caminho_imagem in lista_imagens:
    # Extrai apenas o nome do arquivo do caminho completo
    nome_arquivo = os.path.basename(caminho_imagem)
    print(f"Processando: {nome_arquivo}...")

    # Carrega a imagem colorida
    imagem_colorida = io.imread(caminho_imagem)

    # Converte a imagem para níveis de cinza
    # A função rgb2gray retorna a imagem como números de ponto flutuante (0.0 a 1.0)
    imagem_cinza_float = color.rgb2gray(imagem_colorida)

    # Converte a imagem de volta para o formato 8-bit (0 a 255), que é o padrão para .jpg
    # Isso evita problemas de salvamento e garante compatibilidade
    imagem_cinza_8bit = img_as_ubyte(imagem_cinza_float)

    # Cria o caminho completo para salvar a nova imagem
    caminho_destino = os.path.join(pasta_destino_cinza, nome_arquivo)

    # Salva a nova imagem em níveis de cinza na pasta de destino
    io.imsave(caminho_destino, imagem_cinza_8bit)

print("\nConversão concluída com sucesso!")
print(f"Todas as imagens em níveis de cinza foram salvas na pasta '{pasta_destino_cinza}'.")