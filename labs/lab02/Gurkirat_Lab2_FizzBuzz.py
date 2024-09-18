while True:
    # ask input range
    num_elements = int(input("Enter a number: "))
     
    num_fizz=0
    num_buzz=0
    num_fizz_buzz=0
     
    for i in range(1,num_elements+1):
      print(f"Iteration no.: {i}")
      if (i%3==0):
        print("Fizz")
        num_fizz+=1
      if(i%5==0):
        print("Buzz")
        num_buzz+=1
      if(i%3==0 and i%5==0):
        print("FizzBuzz")
        num_fizz_buzz+=1
     
    print(f"Fizz: {num_fizz}, Buzz: {num_buzz}, FizzBuzz: {num_fizz_buzz}")
    
    # Exit question
    choice = input("Would you like to exit? (yes/no): ").lower()
    if choice=='yes':
        print("Exiting the program, see ya!")
        break
    else:
        print("Let's continue...")
    