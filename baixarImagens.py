import requests;

def download_images(links):
    counter = 1
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            file_extension = link.split('.')[-1]
            file_name = f'image{counter}.{file_extension}'
            counter += 1
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f'Imagem {file_name} baixada com sucesso!')
        else:
            print(f'Falha ao baixar a imagem do link {link}.')

# Exemplo de uso
image_links = [
"url-da-imagem.com",
"url-da-imagem.com",
"url-da-imagem.com"
];

download_images(image_links);