import math

def circonfenenza_cerchio(r:float):
    '''Calcola circonferenza cerchio'''
    circonferenza = r*(2*math.pi)
    print("La circonferenza del cerchio è",circonferenza,"m")
    return circonferenza

def main():
    
    r=5
    circonfenenza_cerchio(r)
    
if __name__ == "__main__":  
    main()