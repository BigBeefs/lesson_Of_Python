import math

def perimetro_rettangolo(b:float,h:float):
    '''Calcola il perimetro di un rettangolo'''
    perimetro = (b+h)*2
    print("Il perimetro del rettangolo è",perimetro,"m")
    return perimetro

def main():
    h=5
    b=6
    perimetro_rettangolo(b,h)
    
if __name__ == "__main__":  
    main()