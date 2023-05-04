import math

def area_vol_quadr(l:float):
    '''Calcola l'area e il volume di un quadrato'''
    area= l**2
    volume= l**3
    return area , volume

def main():
    l=5
    area_vol_quadr(l)
    
if __name__ == "__main__":  
    main()