"""
2.	Tämän tehtävän ohjelmien tekemiseksi tarvittava informaatio on seuraava: 
•	Fahrenheit-asteikossa jään sulamispiste on 32 astetta ja veden kiehumispiste 212 astetta. 
•	Celsius-asteikossa jään sulamispiste on 0 astetta ja veden kiehumispiste 100 astetta. 

Tee ohjelma, joka tekee C-F-muunnoksen samassa ohjelmassa molemmin päin: 
a)	Pyytää käyttäjältä lämpötilan Fahrenheit-asteina ja ilmoittaa sen Celsius-asteina. 
b)	Pyytää käyttäjältä lämpötilan Celsius-asteina ja ilmoittaa sen Fahrenheit-asteina. 
"""

# Funktion määrittely C-F-muunnokseen

def convert(temperature, scale):
	if scale == 'c' or scale == 'C':
		return (temperature - 32) * 5/9
	if scale == 'f' or scale == 'F':
		return (temperature * 9/5) + 32

	return f'Can\'t convert a scale of {scale}. Give a scale of C or F.'

# Pyytää käyttäjältä lämpötilan Fahrenheit-asteina ja ilmoittaa sen Celsius-asteina
f = 57
to_celcius = round(convert(f, 'C'), 1)
print(f'{f}°F to Celcius converts to {to_celcius}°C')

# Pyytää käyttäjältä lämpötilan Celsius-asteina ja ilmoittaa sen Fahrenheit-asteina
c = 100
to_fahrenheit = round(convert(c, 'F'), 1)
print(f'{c}°C to Fahrenheit converts to {to_fahrenheit}°F')