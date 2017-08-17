import osa
import os

def convert(fromCur, am):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum(toCurrency='RUB', fromCurrency=fromCur, amount=am, rounding=True)

def currencies(current_dir):
    total = []
    with open(os.path.join(current_dir, 'currencies.txt'), 'r') as f:
        for line in f:
            total.append(round(convert(am=int(line.split()[1]), fromCur=line.split()[2])))

    return sum(total)

def main():
    current_dir = input('Введите путь к файлу currencies.txt: ')
    print('Вы потратите на путешествие %d рублей' % currencies(current_dir))

main()