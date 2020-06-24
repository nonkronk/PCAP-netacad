def segment_display(number):
    number = str(number)
    digit = {
            0:['###','# #','# #','# #','###'],
            1:['#','#','#','#','#'],
            2:['###','  #','###','#  ','###'],
            3:['###','  #','###','  #','###'],
            4:['# #','# #','###','  #','  #'],
            5:['###','#  ','###','  #','###'],
            6:['###','#  ','###','# #','###'],
            7:['###','  #','  #','  #','  #'],
            8:['###','# #','###','# #','###'],
            9:['###','# #','##s','  #','###']
            }
    for i in range(5):
        for j in range(len(number)):
            d = int(number[j])
            if j == len(number) - 1:
                print(digit[d][i]+' ')
            else:
                print(digit[d][i]+' ', end='')

if __name__ == '__main__':
    while True:
        try:
            number = int(input('Enter number: '))
            if number >= 0:
                break
        except:
            continue
    segment_display(number)
