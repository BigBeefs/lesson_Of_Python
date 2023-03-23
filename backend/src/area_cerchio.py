import math


def area_cerchio(r:float):
    '''Calcola l'area del cerchio'''
    area = (r**2)*math.pi
    print("L'area del cerchio è",area,"m²")
    return area

def main():
    r=5
    area_cerchio(r)
    
if __name__ == "__main__":  
    main()