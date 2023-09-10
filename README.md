# Contador de Galinhas

Este é um projeto que utiliza a biblioteca OpenCV em Python para manipulação de imagem para contar quantas galinhas há em uma região de interesse da imagem. Neste trabalho, irei demonstrar como demarcar a região de interesse e fazer os processamentos necessários para a contagem das galinhas.
## Sobre o trabalho

- Disciplina: OP63I-CC8 - Processamento de Imagens e Reconhecimento de Padrões
- Turma: 2023/2 - 8° Período
- Professor: Pedro Luiz de Paula Filho

## Pré-requisitos e Instalação no Linux

### Python (versão recomendada: 3.11 ou superior)

A maioria das distribuições Linux já vem com o Python instalado. Para verificar se o Python está instalado, abra o terminal e digite:

`python3 --version`

Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição. Por exemplo, no Ubuntu/Debian:

`
sudo apt-get update
sudo apt-get install python3
`

No Arch Linux:

`
sudo pacman -Sy python
`

### PyCharm (ou qualquer outra IDE de sua escolha)

Você pode baixar o PyCharm diretamente do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/) ou, se preferir, pode usar o gerenciador de pacotes da sua distribuição para instalar a versão Community:

#### Ubuntu/Debian:

`
sudo snap install pycharm-community --classic
`

#### Arch Linux:

`
sudo pacman -Sy pycharm-community
`

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes Python:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Pré-requisitos e Instalação no Windows

### Python (versão recomendada: 3.11 ou superior)

1. Baixe o instalador Python para Windows no site oficial (https://www.python.org/downloads/windows/).

2. Execute o instalador e marque a opção "Adicionar o Python X.Y ao PATH" durante a instalação, onde X.Y é a versão do Python (por exemplo, 3.11).

### PyCharm (ou qualquer outra IDE de sua escolha)

1. Baixe o instalador do PyCharm Community ou Professional do site oficial da JetBrains (https://www.jetbrains.com/pycharm/download/).

2. Execute o instalador e siga as instruções na tela.

### OpenCV

Você pode instalar o OpenCV via pip, o gerenciador de pacotes de pacotes Python:

Abra o prompt de comando (cmd) e execute:

`
pip install opencv-python
`

### NumPy

NumPy é uma biblioteca amplamente usada para computação numérica em Python. Você pode instalá-lo via pip:

`
pip install numpy
`

## Executando o Projeto

1. Clone este repositório em seu sistema:

`
git clone https://github.com/seuusuario/python-opencv-trabalho.git
`

2. Abra o projeto no PyCharm (ou sua IDE preferida).

## Modo de Uso

![Screenshot_20230909_234556](https://github.com/emanuelamaral/contador_de_galinhas/assets/105809178/2e52df39-fa8b-4da7-b23a-5ad3af342c79)

1. **Aplicação de Filtros:**

   - Clique na imagem no formato de um retangulo para demarcar a região de interesse
   - Após isso é apresentado o passo a passo do processo até chegar na quantidade das galinhas detectadas
     
2. **Sair do Programa:** Pressione a tecla `q` para sair do programa.

## Autores

- Amoz Emanuel

## Referências

- [OpenCV Documentation](https://docs.opencv.org/)
- [Python.org](https://www.python.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
