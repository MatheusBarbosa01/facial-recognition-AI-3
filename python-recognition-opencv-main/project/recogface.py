import cv2
import numpy as np
import os
import json
from datetime import datetime

# Caminho para os dados dos usuários
data_path = 'C:/Users/marco/Downloads/facial-recognition-AI-3-main/facial-recognition-AI-3-main/python-recognition-opencv-main/faces'
log_path = os.path.join(data_path, 'reconhecimentos.txt')

def log_reconhecimento(cpf):
    with open(log_path, 'a') as f:
        f.write(f'{cpf}, {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

def reconhecer_usuario():
    face_cascade = cv2.CascadeClassifier(r'C:\Users\marco\Downloads\facial-recognition-AI-3-main\facial-recognition-AI-3-main\.venv\Lib\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar imagem")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            face_img = gray[y:y + h, x:x + w]
            face_img = cv2.resize(face_img, (200, 200))

            # Carregar dados dos usuários
            for file in os.listdir(data_path):
                if file.endswith('.json'):
                    with open(os.path.join(data_path, file), 'r') as f:
                        user_data = json.load(f)
                        user_cpf = user_data['cpf']

                    # Verificar se a face corresponde ao usuário
                    # Aqui você pode adicionar o código para verificar a correspondência da face usando um modelo treinado

                    # Se a correspondência for encontrada, exibir o CPF e registrar a data e hora
                    cv2.putText(frame, user_cpf, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                    log_reconhecimento(user_cpf)

        cv2.imshow('Reconhecimento Facial', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reconhecer_usuario()
