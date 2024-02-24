# Timothy Rutkowski 02/22/2024 timothyRutkowski_lab4-2

# This program will display a table of Celsisus/Fahrenheit temperatures,
# based on the user input of a temperature range with the output 
# Celsius/Fahrenheit equivalent.

# Define function for temperature conversion
def celsius_to_fahrenheit(C): # C = Celsius
    return (9/5) * C + 32

def fahrenheit_to_celsius(F): # F = Fahrenheit
    return (F - 32) * (5/9)

# Ask user for temperature scale and range
while True: # Outer Loop Function
    temp_scale = input("\nPlease select the temperature scale: Enter 'C' for Celsius or 'F' for Fahrenheit: ").upper()
    if temp_scale not in ['C', 'F']:
        print("Invalid Input. Please enter 'C' for Celsius or 'F' for Fahrenheit") # Error message if anything other than 'C' or 'F' is input
        continue
    
    start_temp = float(input('\nPlease input the beginning temperature: '))
    end_temp = float(input('Please input the ending temperature: '))

# Inner Loop Function based on user input
    if temp_scale == 'C':
        print('\nCelsius\t\tFahrenheit')
        for C in range(int(start_temp), int(end_temp) +1, 1):
            F = celsius_to_fahrenheit(C)
            print(f'{C:.2f}\t\t{F:.2f}')
        
    else:
        print('\nFahrenheit\tCelsius')
        for F in range(int(start_temp), int(end_temp) +1, 1):
            C = fahrenheit_to_celsius(F)
            print (f'{F:.2f}\t\t{C:.2f}')

# User chooses if they want to continue the program
    choice = input('\nDo you want to continue (yes/no)? ').lower()
    if choice != 'yes':
        break
