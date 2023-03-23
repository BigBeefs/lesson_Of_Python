def somma(a:float,b:float):
    '''Funzione prova'''
    s=a+b
    print(s)
    return s

def main():
    a=5
    b=6
    somma(a,b)
    
if __name__ == "__main__":  #Permette di importare il contenuto sia come esecution che come libreria
    main()