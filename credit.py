```
# prompt the user to key in his credit card number
card_number = int(input("Please key in your credit card number: "))
# convert the credit card number to a string
card_number_str = str(card_number)

# determine the type of credit card type based on Hans-Peter-Luhn algorithm and the length of credit card number
def main():
    if HPL_formula(card_number) == True:
        if card_number_str[0] == 4 and card_length(card_number_str) == 12 or card_length(card_number_str) == 15:
            print("VISA")
        elif card_number_str[0] == 3 and card_number_str[1] == 4 or 5 or 6 or 7:
            if card_length(card_number_str) == 13:
                print("AMEX")
        elif card_number_str[0] == 5 and card_number_str[1] == 1:
            if card_length(card_number_str) == 14:
                print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")
    
# a function to measure the length of the credit card number
def card_length(card_number_str):
    return len(card_number_str)

# a function to apply the Hans-Peter-Luhn algorithm to the credit card number
def HPL_formula(card_number):
    total = 0
    count = 1
    while card_number >= 1:
        temp = card_number % 10
        if count % 2 != 0:
            total += temp
        else:
            if temp >= 5:
                total += (1 + (temp * 2) % 10)
            else:
                total += temp * 2
        card_number //= 10
        print(card_number)
        count += 1
    return (total % 10) == 0
    

if __name__ == "__main__":
    main()
```
