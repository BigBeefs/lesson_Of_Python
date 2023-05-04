import math

def area_rettangolo(b:float,h:float):
    '''Calcola l'area di un rettangolo'''
    area=b*h
    print("L'area del rettangolo è",area,"m²")
    return area 

def main():
    h=5
    b=6
    area_rettangolo(b,h)
    
if __name__ == "__main__":  
    main()