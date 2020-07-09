dictMapel = {'001': 'Bahasa Indonesia',
        '002': 'Bahasa Inggris',
        '003': 'Matematika',
        '004': 'Biologi',
        '005': 'Fisika'}

kamusWarna = {'grey': 'abu-abu',
        'brown': 'coklat',
        'beige': 'abu-abu coklat',
        'green': 'hijau',
        'light': 'terang',
        'dark': 'gelap',
        'navy': 'biru gelap',
        'turquoise': 'biru hijau',
        'purple': 'ungu',
        'black': 'hitam',
        'pink': 'merah muda',
        'silver': 'perak',
        'gold': 'emas',
        'red': 'merah',
        'orange': 'oranye'}

def daftar_mapel():
    print('\nDaftar Mata Pelajaran:')
    for kode,nama in dictMapel.items():
        print(kode+':', nama)
    print()

def menu_dict():
    daftar_mapel()
    print('a. Masukan mapel baru\nb. Edit mapel')
    menu = input('Pilih menu: ')
    if menu == 'a':
        jml = int(input('Input jumlah mapel yang akan ditambahkan: '))
        print()
        for i in range(jml):
            kode = str(int(list(dictMapel)[-1]) + 1).zfill(3)
            print('Kode mapel:', kode)
            nama = input('Input nama mapel: ')
            dictMapel[kode] = nama
        daftar_mapel()
    elif menu == 'b':
        jml = int(input('Input jumlah mapel yang akan dihapus: '))
        print()
        for i in range(jml):
            kode = input('Input kode mapel: ')
            deleted = dictMapel[kode]
            del dictMapel[kode]
            print(f'Mapel "{kode}: {deleted}" berhasil dihapus')
        daftar_mapel()
    else:
        print('Input menu tidak sesuai')

def menu_translator():
    print('Translator Warna English-Indonesia')
    color = input('Color: ')
    print('Warna:', kamusWarna[color])

def menu_class():
    KotakBiru = Kardus(10, 8, 4)
    KotakMerah = Kardus(15, 5, 1)
    print('\nKotak Biru:')
    traits_kotak(KotakBiru)
    print('\nKotak Merah:')
    traits_kotak(KotakMerah)

def traits_kotak(Kotak):
    print(f'p = {Kotak.p}\nl = {Kotak.l}\nt = {Kotak.t}')
    print(f'volume = {Kotak.volumeKardus()}')
    print(f'luas = {Kotak.luasPermKardus()}')

class Kardus:
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t

    def volumeKardus(self):
        return self.p * self.l * self.t

    def luasPermKardus(self):
        return 2 * (self.p * self.l + self.p * self.t + self.l * self.t)

def pilih_latihan():
    print('1. Dict\n2. Translator\n3. OOP')
    menu = int(input('Pilih menu latihan: '))
    if menu == 1:
        menu_dict()
    elif menu == 2:
        menu_translator()
    elif menu == 3:
        menu_class()
    else:
        print('Input menu latihan salah')

if __name__ == '__main__':
    pilih_latihan()
