'''
namafile: SBA2020.py
Lembar kerja/script SBA
Irvan Tristian
0447356121-105
'''

email = 'irvantristian@gmail.com'

# >>>>>>Soal 1
def fungsiIO():
    inputan = input().split()
    input_list = list(map(int, inputan))
    input_list.sort()
    for i in input_list:
        print(i * '*')

# >>>>>>Soal 2
def caseShopia(txt):
    changed_txt = []
    for ch in txt:
        if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            changed_txt.append(ch.lower())
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            changed_txt.append(ch.upper())
    return ''.join(changed_txt)

dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500,
            'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775,
            'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750,
            'IDR': 1}

# >>>>>> Soal 3
def usd2eur(usd):
    return usd * (dcur2idr['USD'] / dcur2idr['EUR'])

# >>>>>>Soal 4
class MoneyChanger:
    def __init__(self, dcurrency, base='IDR', percent=2):
        self.dcurrency = dcurrency
        self.base = base
        self.percent = percent
        self.change_base(base)

    def selling_price(self, nominal, curr):
        curr2base = nominal * (self.dcurrency[curr] / self.dcurrency[self.base])
        return curr2base + (self.percent/100 * curr2base)

    def buying_price(self, nominal, curr):
        curr2base = nominal * (self.dcurrency[curr] / self.dcurrency[self.base])
        return curr2base - (self.percent/100 * curr2base)

    def change_base(self, new_base):
        base_value = self.dcurrency[new_base]
        for k, v in self.dcurrency.items():
            self.dcurrency[k] /= base_value
        self.base = new_base

# Test Case
def main():
    print('test soal 1')
    fungsiIO() # contoh input: 7 4 5 2 1 3

    print('test soal 2')
    print(caseShopia('thXGth876%^$LMn.'))

    print('test soal 3')
    print(usd2eur(100))  # mengubah 100 USD ke EUR

    print('test soal 4')
    mc = MoneyChanger(dcur2idr,base='EUR') # object mc dengan base EUR
    print('base', mc.base)
    print(mc.selling_price(100,'USD')) # nilai jual 100 USD ke EUR (Base)
    print(mc.buying_price(100,'USD')) # nilai beli 100 USD ke EUR (Base)

    mc.change_base('IDR') # Ganti Base object mc ke IDR
    print('base', mc.base)
    print(mc.selling_price(100,'USD')) # nilai jual 100 USD ke IDR (Base)
    print(mc.buying_price(100,'USD'))  # nilai beli 100 USD ke IDR (Base)

if __name__ == '__main__':
    main()
