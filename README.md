# Processamento Básico de imagens 

## Processamento de Cores: Separação de Canais R, G e B
Foi utilizado a biblioteca OpenCV  para carregar uma imagem colorida e separar seus canais de cor vermelho (**R**ed), verde (**G**reen) e azul (**B**lue). Em seguida, exibe os canais de cor separadamente em janelas individuais e salva cada canal em arquivos de imagem separados.


## Conversão de Colorido RGB para Tons de Cinza
Foi utilizado a biblioteca PIL (Python Imaging Library) para carregar uma imagem colorida e converter para tons de cinza. O filtro realiza a conversão de uma imagem RGB (**Red, Green, Blue**) para uma imagem em escala de cinza, onde cada pixel possui apenas um valor de intensidade representando o nível de cinza correspondente.


## Conversão de Tons de Cinza para Preto e Branco (Limiarização/Binarização Manual)
Foi utilizado a biblioteca PIL (Python Imaging Library) para carregar uma imagem em tons de cinza e realizar a conversão para uma imagem em preto e branco. O filtro aplica uma técnica de limiarização manual, onde cada pixel da imagem em tons de cinza é comparado a um valor de limiar. Se o valor do pixel for maior ou igual ao limiar, ele é definido como branco (valor máximo), caso contrário, é definido como preto (valor mínimo).


## Filtro de Média
Foi feita a aplicação do filtro de média em uma imagem utilizando a biblioteca PIL (Python Imaging Library), a função **uniform_filter** e **scipy.ndimage**.

  . É feita a importação das bibliotecas **munpy**, **image** do PIL e a função **uniform_filter** do **scipy.ndimage**.
  
  . Tendo fornecido o caminho da imagem escolhida, é carregada pela função **image.open()**.
  
  . Após isso, a imagem é convertida para um array **numpy** utilizando a função **np.array()**.
  
 . Aplica o filtro de média ao array da imagem utilizando a função **uniform_filter()**.
 
 . É criada uma imagem pela função **image.fromarray()**.
 
 . E para garantir queo formato é adequado a iamgem, é utilizado a **np.uint8**.
 
 . E como foi feito em todos os filtros, a imagem gerada é salva utilizando o método **save()**


## Filtro de Mediana
Foi feita uma aplicação do filtro de mediana na imagem utilizando o PIL (Python Imaging Library) e a função **median_filter** do **scipy.ndimage**.


## Filtro de Desfoque Gaussiano
Foi feita a aplicação do filtro de desfoque Gaussiano em uma imagem utilizando a biblioteca OpenCV. Esse filtro suaviza a imagem, reduzindo os detalhes e o ruído, resultado em uma aparência mais suave e borrada. E para fazer isso, foi definido o tamanho do kernel que determina a intensidade do desfoque, e do sigma que determina a dispensão dos valores de pixel no cálculo do desfoque.


## Filtro do Ajuste de Bilho
Foi utilizado a biblioteca **numpy**, para realizar o ajuste, foi usado **np.clip(image.astype(np.int16) + brilho, 0, 255).astype(np.uint8)**. O ajuste de bilho permite aumentar ou diminuir a intensidade luminosa da imagem, resultando em uma imagem mais clara ou mais escura. 

## Filtro do Ajuste do Contraste
Foi definido os parâmentros de ajuste de contraste com:

  . **alpha**: fator de multiplicação para aumentar o contraste.
  
  . **beta**: valor a ser adicionado para ajustar o brilho.
  
O ajuste de contraste permite aumentar ou diminuir a diferença entre os valores de intensidade dos pixels na imagem, resultando em uma imagem mais vibrante e com maior variação de tons de cinza.
A função **cv2.convertScaleAbs()** aplica uma transformação linear na imagem, multiplicando cada pixel pelo fator _alpha_ e adicionando o valor _beta_.
O resultado é convertido para o tipo **uint8** usando a função **cv2.convertScaleAbs()**.
  
