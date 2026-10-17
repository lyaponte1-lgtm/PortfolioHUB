def calcular(base, altura):
    return (base * altura) / 2 
def main ():
    base = float(input('digite a base:'))
    altura = float(input('digite a altura:'))
    calcular(base, altura)
    print('area do triangulo:', calcular(base, altura))
if __name__ == '__main__':
    main()
