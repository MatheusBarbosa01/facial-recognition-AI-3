# Sistema de Reconhecimento Facial

Este projeto implementa um sistema de reconhecimento facial utilizando Python, OpenCV e Kivy. O sistema detecta rostos em tempo real e identifica usuários comparando-os com um banco de dados pré-existente.

## Estrutura do Projeto

- *main.py*: Script principal que configura a interface gráfica utilizando Kivy e captura o feed da câmera.
- *recogface.py*: Script responsável pelo reconhecimento facial, comparando os rostos detectados com os dados armazenados.
- *faces/*: Diretório onde os dados dos usuários são armazenados.

## Pré-requisitos

- *Python 3.9.13*
- *OpenCV*
- *Kivy*

## Instalação

1. Clone o repositório:
    bash
   
    git clone https://github.com/MatheusBarbosa01/facial-recognition-AI-3.git
   
    cd python-recognition-opencv-main
    

3. Crie um ambiente virtual e ative-o:
    bash
   
    python -m venv venv
   
    source venv/bin/activate

   # Para Windows: venv\Scripts\activate
    

4. Instale as dependências:
    bash
   
    pip install -r requirements.txt
    

6. Configure os diretórios e arquivos necessários:
    - Certifique-se de que o diretório faces/ existe no caminho correto.
    - Insira os arquivos Haar Cascade para detecção de rosto no local especificado no código (haarcascade_frontalface_default.xml).

## Como Executar

### Rodar o script principal

```bash
python main.py
