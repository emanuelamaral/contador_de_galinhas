import cv2
import numpy as np

gray_roi = None


def ajustar_threshold(valor):
    global img
    _, threshold = cv2.threshold(gray_roi, valor, 255, cv2.THRESH_BINARY)
    cv2.imshow("Imagem processada e binarizada", threshold)


def contar_galinhas_na_regiao(imagem, x1, y1, x2, y2):
    global gray_roi
    roi = imagem[y1: y2, x1:x2]

    gray_roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)

    cv2.imshow("Roi em Escala de Cinza", gray_roi)

    blurred_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)

    cv2.imshow("Roi em escala de cinza com blur", blurred_roi)

    edges = cv2.Canny(blurred_roi, 50, 120)

    cv2.imshow("Filtro Canny", edges)

    # _, thresh_roi = cv2.threshold(blurred_roi, 135, 255, cv2.THRESH_OTSU)

    # cv2.imshow("Imagem Binarizada", thresh_roi)

    # Encontrar os contornos na imagem binária
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    count = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 7:  # Ajuste esse valor conforme necessário
            count += 1

    return count


# Função para lidar com os cliques do mouse
def click_event(event, x, y, flags, param):
    global points, img

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 4:
            cv2.rectangle(img, points[0], points[2], (0, 255, 0), 2)
            galinhas_contadas = contar_galinhas_na_regiao(img, points[0][0], points[0][1], points[2][0], points[2][1])
            print(f'Número de galinhas na região: {galinhas_contadas}')
            cv2.imshow("Imagem Gerada", img)
            points = []


# Carregar a imagem
img = cv2.imread('galinha.png')

# Inicializar a lista de pontos
points = []

# Associe a função click_event ao evento de clique do mouse
cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)



while True:
    key = cv2.waitKey(1) & 0xFF

    # Se a tecla 'q' for pressionada, saia do loop
    if key == ord('q'):
        break

cv2.destroyAllWindows()


#
# import cv2
# import numpy as np
#
# gray_roi = None
# thresh_value = 250  # Valor inicial do threshold
# points = []
# img = None
#
# # Função de callback para a trackbar
# # Função de callback para a trackbar
# def ajustar_threshold(valor):
#     global thresh_value, gray_roi
#     thresh_value = valor
#     _, threshold = cv2.threshold(gray_roi, valor, 255, cv2.THRESH_BINARY)
#     if threshold is not None:  # Verifique se a imagem não está vazia
#         cv2.imshow("Imagem processada e binarizada", threshold)
#         contar_e_mostrar_galinhas(thresh_value)
#
#
# # Função para contar e mostrar as galinhas
# def contar_e_mostrar_galinhas(thresh):
#     global img, points, gray_roi
#     if points:
#         roi = img[points[0][1]:points[2][1], points[0][0]:points[2][0]]
#         gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#         _, thresh_roi = cv2.threshold(gray_roi, thresh, 255, cv2.THRESH_OTSU)
#         contours, _ = cv2.findContours(thresh_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         count = 0
#         for contour in contours:
#             x, y, w, h = cv2.boundingRect(contour)
#             if 0 <= x <= w and 0 <= y <= h and x + w <= roi.shape[1] and y + h <= roi.shape[0]:
#                 count += 1
#         print(f'Número de galinhas na região: {count}')
#
# # Função para lidar com os cliques do mouse
# def click_event(event, x, y, flags, param):
#     global points, img, gray_roi
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         points.append((x, y))
#         if len(points) == 4:
#             cv2.rectangle(img, points[0], points[2], (0, 255, 0), 2)
#             contar_e_mostrar_galinhas(thresh_value)  # Conta e mostra galinhas ao desenhar o retângulo
#             cv2.imshow("Imagem Gerada", img)
#             points = []
#
# # Carregar a imagem
# img = cv2.imread('galinha.png')
#
# # Inicialize a lista de pontos
# points = []
#
# # Associe a função click_event ao evento de clique do mouse
# cv2.imshow("Image", img)
# cv2.setMouseCallback("Image", click_event)
#
# # Crie uma janela para exibir a imagem com a trackbar
# cv2.namedWindow("Imagem processada e binarizada")
#
# # Crie a trackbar
# cv2.createTrackbar("Valor do Threshold", "Imagem processada e binarizada", thresh_value, 255, ajustar_threshold)
#
# # Inicialize a imagem com o valor de threshold inicial
# ajustar_threshold(thresh_value)
#
# while True:
#     key = cv2.waitKey(1) & 0xFF
#
#     # Se a tecla 'q' for pressionada, saia do loop
#     if key == ord('q'):
#         break
#
# cv2.destroyAllWindows()
