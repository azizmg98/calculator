
def main():
	# inputs
	while True:
		try:
			num1 = int(input('Enter the first number: '))
		except ValueError:
			print('That won\'t work!')
			continue
		else:
			break
		
	while True:
		try:
			num2 = int(input('Enter the second number: '))
		except ValueError:
			print('That won\'t work!')
			continue
		else:
			break
		
	while True:
		operation = str(input('choose your operation (+, -, /, *): '))
		operations = ('+', '-', '/', '*')
		if not operation in operations: 
			print('please enter one of the following operations (+, -, /, *)')
		else:
			break

	# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
	
	# validators

	# output
	calculation = print(f'{num1} {operation} {num2} is ')


	# operations
	def add():
		result = num1 + num2
		print( result)
	def subtract():
		result = num1 - num2
		print(result)
	def devide():
		result = num1 / num2
		print(result)
	def multiply():
		result = num1 * num2
		print(result)

	# conditions for performing operations
	if operation == '+':
		add()
	elif operation == '-':
		subtract()
	elif operation == '/':
		devide()
	elif operation == '*':
		multiply()

if __name__ == '__main__':
	main()
