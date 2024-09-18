# Function to ask user input

def ask_input(input_arr):
    while True:
        num = input("Enter a number (type 'exit' if you are done): ")
        if (num.lower() == "exit"):
            break # exit the loop
        try:
            input_arr.append(int(num))  # Convert to integer and append to the list
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input
            return ask_input(input_arr)
    return input_arr

input_arr=[]
arr = ask_input(input_arr)

# Check if the array is empty and ask for input again if necessary
while len(arr) == 0:
    print("No valid numbers were entered. Please try again.")
    arr = ask_input(input_arr)

print(f"Entered numbers: {arr}")

smallest = arr[0]
largest = arr[0]

for num in arr:
    if (num > largest):
        largest = num
    if (num < smallest):
        smallest = num

print(f"\nSmallest: {smallest}, largest: {largest}")