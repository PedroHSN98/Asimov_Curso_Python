import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision
import numpy as np
import time
import urllib.request
import os

#Tipagem ================================
confidence = float
webcam_image = np.ndarray
rgb_tuple = tuple[int, int, int]
#coords_vector =

#Conexões do esqueleto da mão
_HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

#Modelo da Tasks API
_MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hand_landmarker.task')
if not os.path.exists(_MODEL_PATH):
    print('Baixando modelo (~8MB)...')
    urllib.request.urlretrieve(
        'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task',
        _MODEL_PATH
    )
    print('Modelo pronto.')



#Classe =================================



class Detector():
    def __init__(self,
                 mode: bool = False,
                 number_hands: int = 2,
                 model_complexity: int = 1,
                 min_detec_confidence: confidence = 0.5,
                 min_tracking_confidence: confidence = 0.5):
    #Parametros necessários para inicializar o hands
        self.tip_ids = [4, 8, 12, 16, 20]

    #Inicializar o MediaPipe Hands (Tasks API)
        base_options = mp_python.BaseOptions(model_asset_path=_MODEL_PATH)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=number_hands,
            min_hand_detection_confidence=min_detec_confidence,
            min_tracking_confidence=min_tracking_confidence,
            running_mode=vision.RunningMode.VIDEO
        )
        self._detector = vision.HandLandmarker.create_from_options(options)

    def find_hands(self,
                   img: webcam_image,
                   draw_hands: bool = True):
        #Correção de Cor
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #Coletar resultados do processo das hands e analisar
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_RGB)
        self.results = self._detector.detect_for_video(mp_image, int(time.time() * 1000))

        if self.results.hand_landmarks and draw_hands:
            h, w, _ = img.shape
            for hand in self.results.hand_landmarks:
                for start, end in _HAND_CONNECTIONS:
                    x1, y1 = int(hand[start].x * w), int(hand[start].y * h)
                    x2, y2 = int(hand[end].x * w), int(hand[end].y * h)
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                for lm in hand:
                    cv2.circle(img, (int(lm.x * w), int(lm.y * h)), 5, (255, 0, 0), cv2.FILLED)

        return img
            





#Teste de classe ================================
if __name__ == "__main__":
    # Classe
    Detec = Detector()

    #Captura de imagem
    capture = cv2.VideoCapture(0)
    while True:
        #Captura do frame
        ret, img = capture.read()
        if not ret:
            continue

        #manipulação de frame
        img = Detec.find_hands(img)

        #Processamento da imagem
        cv2.imshow('Camera Principal', img)
       
        #Quitando a camera
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
