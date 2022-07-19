# Download bandas Sentinel

## Sentinel 2A Multispectral Instrument - Surface Reflectance
## Modo de usar

* Instale o plugin Google Earth Engine no QGIS
* Esteja logado em sua conta do Google e Google Earth Engine
* Baixe a biblioteca geemap em https://github.com/giswqs/geemap/tree/master/geemap 
* Cole a pasta geemap na pasta de scripts do QGIS, em C:\Users\seuUsuario\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts
* Abra um projeto em branco no Qgis
* Navegue até o ponto de interesse, pode carregar alguma imagem de fundo com a ajuda do plugin QuickMapServices
* Defina o CRS do projeto para EPSG:4326
* Clique no ponto de interesse para centralizar a tela
* As imagens serão recortadas de acordo com a extensão do Canvas (tela) do QGIS
* Escolha as datas de início e fim, é possível digitar no formato 'yyyy-dd-mm' ou escolher no calendário
* Ative a checkbox das bandas desejadas para download
* Altere o filtro de porcentagem máxima de nuvens
* Confira se os campos Latitude e Longitude estão corretos
* Escolha um diretório para salvas as imagens
* Clique em executar
