def sleep_assesment(hours):
    if hours < 8:
        print("Oof, go back to bed!")
    
    if hours <= 10:
        print("You got a good night's rest!")

    if hours > 10:
        print("You're a sleep prodigy!")

def main():
    sleep_assessment(10)
    sleep_assessment(4)
    sleep_assessment(12)
    sleep_assessment(9)
main()
