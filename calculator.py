
def main():
	# inputs
	num1 = input('Enter the first number: ')
	if not num1.isnumeric():
		print('no istahbiling please, only numbers.')
	elif num1.isnumeric():
		num2 = (input('Enter the second number: '))
		if not num2.isnumeric():
			print("sorry we're still not accepting any istihbal")
		elif num2.isnumeric():
			operation = str(input('choose your operation (+, -, /, *): '))
			operations = ('+', '-', '/', '*')
			if not operation in operations:
				print("you're istihabal fund has expired please call customer support")
			elif operation in operations:
				
	# validators
	# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

				# output
				print(f'{num1} {operation} {num2} is ')


				# operations
				def add():
					result = int(num1) + int(num2)
					print( result)
				def subtract():
					result = int(num1) - int(num2)
					print(result)
				def devide():
					result = int(num1) / int(num2)
					print(result)
				def multiply():
					result = int(num1) * int(num2)
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
