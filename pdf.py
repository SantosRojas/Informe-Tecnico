import cv2
import datetime
def make_pdf(textos,checks,n_informe=1):
    img = cv2.imread('scr/imgformato.jpg')
    cv2.putText(img, f"001 No {n_informe:06}", (1150,290), font, 2, (0,0,255), 2, cv2.LINE_AA)
    cv2.putText(img, f"001 No {n_informe:06}", (1150+space_x,290), font, 2, (0,0,255), 2, cv2.LINE_AA)
    for loc in ubicacion_text1:
        index = ubicacion_text1.index(loc)
        cv2.putText(img, textos[index], ubicacion_text1[index], font, tamanoLetra, (255,0,0), grosorLetra, cv2.LINE_AA)

    for loc in ubicacion_text2:
        index = ubicacion_text2.index(loc)
        cv2.putText(img, textos[index], ubicacion_text2[index], font, tamanoLetra, (255,0,0), grosorLetra, cv2.LINE_AA)

    for check, ubicacion in zip(checks,ubicacion_checks1):
        if check:
            index = checks.index(check)
            cv2.putText(img, "X", ubicacion, font, 2, (255,0,0), 3, cv2.LINE_AA)
    
    for check, ubicacion in zip(checks,ubicacion_checks2):
        if check:
            index = checks.index(check)
            cv2.putText(img, "X", ubicacion, font, 2, (255,0,0), 3, cv2.LINE_AA)

    #Guardar imagen
    cv2.imwrite(f'informes/informe_{textos[3]}.jpg', img)

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
date = str(datetime.date.today())
tamanoLetra = 2
grosorLetra = 2
colorLetra = (0,0,0)
space_x = 1760       
#La ubicación mantiene en 50 el eje X (ancho)
# y cambia en multiplos de 70 el eje Y (alto)

ubicacion_text1 = [
    (250,370),(1300,370),
    (200,440),(670,440),(1030,440),(1350,440),
    (1250,860),
    (540,1254),
    (1220,1005),
    (1100,1645),
    (80,1930),
    (1100,2150)]

ubicacion_checks1 = [
    (80,535),(610,535),
    (80,685),(525,685),(875,685),(1280,685),
    (80,750),(525,750),(875,750),(1280,750),
    (80,815),(525,815),(875,815),
    (80,870),(525,870),(875,870),
    (80,1014),(488,1014),
    (80,1074),(488,1074),
    (80,1134),(488,1134),
    (80,1194),
    (80,1254),
    (1455,1017),(1590,1017),
    (1455,1079),(1590,1079),
    (1455,1139),(1590,1139),
    (1455,1199),(1590,1199),
    (1455,1259),(1590,1259),
    (80,1400),(527,1405),(931,1405),(1323,1405),
    (80,1460),(527,1465),(931,1465),(1323,1465),
    (80,1520),(527,1525),(931,1525),(1323,1525),
    (80,1580),(527,1585),(931,1585),
    (80,1640),(527,1645),
    (80,1790),(535,1790),(1000,1790)
    ]

ubicacion_text2 = [(element[0]+ space_x,element[1]) for element in ubicacion_text1]
ubicacion_checks2 = [(element[0]+ space_x,element[1]) for element in ubicacion_checks1]
