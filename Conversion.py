#Name: Harlan Chang
#Assignment: Unit 6

def convertTemp(temp):
	temp = (temp * 1.8) + 32
	print('That number converted to Fahrenheit is ', format(temp, '.2f'))

def convertWeight(temp):
	temp = temp * 0.45359237
	print('That number converted to kilograms is ', format(temp, '.2f'))

def convertLength(temp):
	temp = temp * 0.0003048
	print('That number converted to kilometers is ', format(temp, '.2f'))

def main():
	print('Welcome to the converter system.')
	print('Choose a conversion from below by typing its corresponding number:')
	print('1. Celsius to Fahrenheit ')
	print('2. Pounds to Kilograms ')
	print('3. Feet to Kilometers ')
	choice = int(input('Conversion: '))
	
	if choice == 1:
		temp = float(input('Enter the number to convert: '))
		convertTemp(temp)
	elif choice == 2:
		temp = float(input('Enter the number to convert: '))
		convertWeight(temp)
	elif choice == 3:
		temp = float(input('Enter the number to convert: '))
		convertLength(temp)
	else:
		print('That is not a valid option!')
		
main()