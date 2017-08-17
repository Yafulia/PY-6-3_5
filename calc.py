import osa

def add(a, b):
    client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Add(
        intA=a,
        intB=b
    )
def subtract(a, b):
    client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Subtract(
        intA=a,
        intB=b
    )

def multiply(a, b):
    client = osa.Client('http://www.dneonline.com/calculator.asmx?WSDL')
    return client.service.Multiply(
        intA=a,
        intB=b
    )

def main():
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")

    print("Сумма чисел:", add(a, b))
    print("Разность чисел:", subtract(a, b))
    print("Произведение чисел:", multiply(a, b))

main()