"""
1.	Laadi ohjelma, joka 
•	kysyy käyttäjältä lukumäärän: kuinka monta satunnaislukua arvotaan?
•	kysyy käyttäjältä satunnaislukuavaruuden ala- ja ylärajan (kokonaislukuja)
•	arpoo halutun määrän satunnaislukuja halutulta väliltä 
•	tulostaa kuvaruudulle satunnaisluvut nousevassa järjestyksessä 
•	tulostaa kuvaruudulle satunnaisluvut laskevassa järjestyksessä
Tarkasta ja säädä kuntoon lopuksi ohjelman toimivuuden ulkoasu mm. tyhjien rivien avulla. 
"""

import random

# Kysyy käyttäjältä lukumäärän: kuinka monta satunnaislukua arvotaan

amount_of_randoms = int(input('How many random numbers should be generated? '))

# Kysee käyttäjältä satunnaislukuavaruuden ala- ja ylärajan (kokonaislukuja)

min_limit = int(input('What would you like to set as the min limit of the generated random numbers? '))
max_limit = int(input('What would you like to set as the max limit of the generated random numbers? '))

# Arpoo halutun määrän satunnaislukuja halutulta väliltä

generated_numbers = []

for i in range(amount_of_randoms):
	random_number = random.randint(min_limit, max_limit)
	generated_numbers.append(random_number)

# Tulostaa kuvaruudulle satunnaisluvut nousevassa järjestyksessä 

asc_numbers = sorted(generated_numbers)
print(asc_numbers)

#	Tulostaa kuvaruudulle satunnaisluvut laskevassa järjestyksessä

desc_numbers = sorted(generated_numbers, reverse=True)
print(desc_numbers)
