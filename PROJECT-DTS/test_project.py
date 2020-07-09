import p1, p2, p3, pytest

# Project 1 Test Case
@pytest.mark.parametrize("items, letter, expected", [
    (['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],'A',['Apple', 'Avocado']),
])
def test_letter_catalog(items, letter, expected):
    assert p1.letter_catalog(items, letter) == expected

def test_counter_item():
    assert p1.counter_item(['Apple','Apple','Apple','Blueberries','Blueberries','Blueberries']) == {'Apple': 3, 'Blueberries': 3}

def test_total_price():
    assert p1.total_price(p1.counter_item(p1.chart),p1.fruit_price) == 103

def test_discounted_price():
    assert p1.discounted_price(p1.total_price(p1.counter_item(p1.chart),p1.fruit_price),10,minprice=100) == 92.7

def test_print_summarry(capfd):
    p1.print_summary(p1.chart, p1.fruit_price)
    out, err = capfd.readouterr()
    assert out == '3 Apple : 18\n4 Blueberries : 48\n1 Grapes : 15\n1 Guava : 8\n2 Jackfruit : 14\ntotal : 103\ndiscount price : 92.7\n'

# Project 2 Test Case
@pytest.mark.parametrize('x, y, r, center, expected', [
    (1,1,1,(0,0),False),
    (1,0,1,(0,0),True),
    (1,1,1,(1,0),True),
    (0,0,1,(1,1),False),
    ])
def test_ispointincircle(x, y, r, center, expected):
    assert p2.isPointInCircle(x, y, r, center) == expected

def test_generaterandomsquarepoint():
    import random
    random.seed(0)
    points = p2.generateRandomSquarePoints(100,1)
    assert points[10:15] == [[-0.18985243068066737, 0.22983174826012864],
 [0.3988382879679935, 0.18398393191544127],
 [-0.027857284547286643, -0.3992987919316342],
 [-0.06582816454621632, 0.1108869734438016],
 [0.4130110532378982, 0.4666063677707588]]

@pytest.mark.parametrize('r, n, center, expected',[
    (1,100,(0,0),3.28),
    (1,10,(10,10),3.2),
    ])
def test_mccirclearea(r,n,center,expected):
    import random
    random.seed(0)
    assert p2.MCCircleArea(r,n,center) == expected

def test_llnpimc():
    import random
    random.seed(0)
    estpi = p2.LLNPiMC(10000,500)
    assert estpi == 3.1416055999999823

def test_relativeerror():
    import math, random
    random.seed(0)
    estpi = p2.LLNPiMC(10000,500)
    assert p2.relativeError(math.pi,estpi) == 0.0004120970353822341

# Project 3 Test Case
def test_caesar():
    msg = 'Haloz DTS mania, MANTAPSZZZ!'
    cpr = p3.caesar_encript(msg,4)
    txt = p3.caesar_decript(cpr,4)
    assert msg == txt

def test_order():
    msg = 'abcd'
    shuffled = p3.shuffle_order(msg,[2,1,3,0])
    deshuffled = p3.deshuffle_order(shuffled,[2,1,3,0])
    assert msg == deshuffled

def test_batch(capfd):
    msg_cpr = p3.send_batch('halo DTS mania, mantaaap!!!',[2,1,3,0],4)
    msg_txt = p3.receive_batch(msg_cpr,[2,1,3,0],4)
    print(msg_txt,msg_cpr,sep='\n')
    out, err = capfd.readouterr()
    assert out == """halo DTS mania, mantaaap!!!
['pesl', 'XHW ', 'eqr ', ',e m', 'rexq', 'eete', '!!_!']
"""

