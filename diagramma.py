f=open('/Users/akimoleshko/Downloads/sequence.txt')
mass=[float(i) for i in f]
sch1=0
sch2=0
sch3=0

for i in range(len(mass)):
    if 0 < mass[i] < 5:
        sch1+=1
    if -5 < mass[i] < 0:
        sch2+=1
    else:
        sch3+=1

all=sch1+sch2
chsl05=sch1*100/all
chsl50=sch2*100/all

def bar(values, total_length=50):
    total = sum(values)
    lengths = [(value / total) * total_length for value in values]
    bar_symbols = [u'\033[41m█',u'\033[42m█' ] 

    for i, (value, length) in enumerate(zip(values, lengths)):
        bar = bar_symbols[i % len(bar_symbols)] * int(length)
        percentage = (value / total) * 100
        print(bar + ' ' + str(round(percentage, 1)) + '%')

bar([chsl05,chsl50])




