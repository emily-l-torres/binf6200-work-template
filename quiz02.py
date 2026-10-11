answer = input("Minimum length: ") 
try: 
    minimum = int(answer) 
    print(f"Keeping sequences longer than {minimum}") 
except: 
    print("That isn't a whole number.")