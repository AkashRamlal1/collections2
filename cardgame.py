import random
import itertools

soort = ['ruiten', 'harten', 'klaveren', 'schoppen']
kaarten = ['2' , '3', '4', '5', '5', '6', '7', '8','9','10','boer','koningin','aas','koning']

stapel = list(itertools.product(kaarten,soort))
print()
print('kaarten in je hand')
print()
random.shuffle(stapel)
print()
print()
for i in range(7):
    print(str(i) , ':', str(stapel[i]))
print()
print('dit zit in de stapel')
print(stapel)