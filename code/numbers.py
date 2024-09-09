'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

answer=1.1
dictionary={'odd':[], 'even':[]}
while answer!=0:
    answer=int(input('Give an integer: '))
    while round(answer)!=answer:
        answer=int(input("Give an integer: "))
    if answer!=0:
        if answer%2==0:
            dictionary['even'].append(answer)
        elif answer%2!=0:
            dictionary['odd'].append(answer)
print(dictionary)