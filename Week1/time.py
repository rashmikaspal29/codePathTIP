def blackjack(score: int):
    if score == 21:
        print("Blackjack")
    if score > 21:
        print("Bust!")
    if score > 17:
        print("Nice hand!")
    if score < 17:
        print("Hit me!")
    
def main():
    blackjack(21)
    blackjack(24)
    blackjack(19)
    blackjack(10)
main()