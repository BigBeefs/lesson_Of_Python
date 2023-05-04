import math

def area_triangolo(b:float,h:float):
    '''Calcola l'area del triangolo'''
    area = (b*h)/2
    print("L'area del triangolo è",area,"m²")
    return area

def main():
    h=5
    b=6
    area_triangolo(h,b)
    
if __name__ == "__main__":  
    main()