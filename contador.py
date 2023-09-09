import cv2
import numpy as np


class GalinhaCounter:
    def __init__(self, image_path):
        self.img = cv2.imread(image_path)
        self.points = []
        self.gray_roi = None

    def adjust_threshold(self, valor):
        _, threshold = cv2.threshold(self.gray_roi, valor, 255, cv2.THRESH_BINARY)
        cv2.imshow("Imagem processada e binarizada", threshold)

    def count_galinhas_na_regiao(self, x1, y1, x2, y2):
        roi = self.img[y1: y2, x1:x2]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
        self.gray_roi = gray_roi
        cv2.imshow("Roi em Escala de Cinza", gray_roi)
        blurred_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)
        cv2.imshow("Roi em escala de cinza com blur", blurred_roi)
        edges = cv2.Canny(blurred_roi, 50, 120)
        cv2.imshow("Filtro Canny", edges)
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        count = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 7:
                count += 1
        return count

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.points.append((x, y))
            if len(self.points) == 4:
                cv2.rectangle(self.img, self.points[0], self.points[2], (0, 255, 0), 2)
                galinhas_contadas = self.count_galinhas_na_regiao(self.points[0][0], self.points[0][1],
                                                                  self.points[2][0], self.points[2][1])
                print(f'Número de galinhas na região: {galinhas_contadas}')
                cv2.imshow("Imagem Gerada", self.img)
                self.points = []

    def run(self):
        cv2.imshow("Image", self.img)
        cv2.setMouseCallback("Image", self.click_event)

        while True:
            key = cv2.waitKey(1) & 0xFF

            # Se a tecla 'q' for pressionada, saia do loop
            if key == ord('q'):
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    galinha_counter = GalinhaCounter('galinha.png')
    galinha_counter.run()
