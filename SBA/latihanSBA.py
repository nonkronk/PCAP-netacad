'''
namafile: latihanSBA.py
Lembar kerja/script Latihan SBA
Irvan Tristian
0447356121-105
'''

email = 'irvantristian@gmail.com'

#soal 1
class titik2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def ambiltitik(self):
        return (self.x, self.y)
    
    def tambahkan(self, titik):
        self.x += titik.x
        self.y += titik.y

# soal 2
def run():
    while True:
        try:
            point = input().split()
            if len(point) == 2:
                x, y = int(point[0]), int(point[1])
                break
        except:
            continue
    return titik2d(x, y)

if __name__ == '__main__':
    t1 = run()
    print('titik1:',t1.ambiltitik())
    t2 = run()
    print('titik2:',t2.ambiltitik())
    t1.tambahkan(t2)
    print('titik1 + titik2:',t1.ambiltitik())