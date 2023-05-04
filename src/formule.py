
import math

def area_rettangolo(b:float,h:float):
    '''Calcola l'area di un rettangolo'''
    area = b*h
    #print("L'area del rettangolo è",area,"m²")
    return area 

def area_cerchio(r:float):
    '''Calcola l'area del cerchio'''
    area = (r**2)*math.pi
    #print("L'area del cerchio è",area,"m²")
    return area
    
def area_triangolo(b:float,h:float):
    '''Calcola l'area del triangolo'''
    area = (b*h)/2
    #print("L'area del triangolo è",area,"m²")
    return area

def perimetro_rettangolo(b:float,h:float):
    '''Calcola il perimetro di un rettangolo'''
    perimetro = (b+h)*2
    #print("Il perimetro del rettangolo è",perimetro,"m")
    return perimetro

def circonfenenza_cerchio(r:float):
    '''Calcola circonferenza cerchio'''
    circonferenza = r*(2*math.pi)
    #print("La circonferenza del cerchio è",circonferenza,"m")
    return circonferenza

def area_vol_quadr(l:float):
    '''Calcola l'area e il volume di un quadrato'''
    area= l**2
    volume= l**3
    return area , volume

