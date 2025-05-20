import time

def countdown_timer():
    seconds = int(input("Enter time in seconds: "))
    
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

# Call the function
if __name__ == "__main__":
    countdown_timer()