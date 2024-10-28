
import os
import time

os.system('clear')


counter = 0
while counter < 3: # this will run forever unless it reaches a break statement
	print()
	os.system('date')
	opts = input("\nChoose arithmetic: \n\nA Addition \nS Subtract \nD Division \nM Multiply\n").lower()
	counter += 1  # this is an incrementer
	if opts == 'a':
		num1 = float(input("\nEnter your first number: "))
		num2 = float(input("Enter your second number: "))
		z = num1 + num2
		print(f'\nAnswer is: {z}\n')
		break

	elif opts == 's':
		num1 = float(input("\nEnter your first number: "))
		num2 = float(input("Enter your second number: "))
		z = num1 - num2
		print(f'\nAnswer is: {z}\n')
		break

	elif opts == 'd':
		num1 = float(input("\nEnter your first number: "))
		num2 = float(input("Enter your second number: "))
		z = num1 / num2
		print(f'\nAnswer is: {z}\n')
		break

	elif opts == 'm':
		num1 = float(input("\nEnter your first number: "))
		num2 = float(input("Enter your second number: "))
		z = num1 * num2
		print(f'\nAnswer is: {z}\n')
		break

	else:
		print("\nChoice doesn't exist, try again..")
		print(f'You have {3-counter} attempts left')
		time.sleep(2)
		os.system('clear')

		if counter < 3:
			continue

		else:
			print(f'\nGoodbye...\n'.upper())
			break
		
