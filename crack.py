```
from crypt import crypt
import sys
import math

def main():
    # ensure that the user provides a single command-line argument, and store it in variable pw
    if len(sys.argv) != 2:
        print("Please provide a single command-line argument.")
        exit(1)
    else:
        pw = sys.argv[1]
    # slice the first 2 element of pw and store them in variable salt
    salt = pw[:2]
    
    # iterate through A to Z and a to z to find the key combination
    for i in range(65, 123):
        for j in range (65, 123):
            for k in range (65, 123):
                for l in range (65, 123):
                    
                    if l <= 90 or l >= 97:
                        key_1 = chr(l)
                        if k <= 90 or k >= 97:
                            key_2 = chr(l) + chr(k)
                            if j <= 90 or j >= 97:
                                key_3 = chr(l) + chr(k) + chr(j)
                                if i <= 90 or i >= 97:
                                    key_4 = chr(l) + chr(k) + chr(j) + chr(i)
                    
                    if i == 65 and j == 65 and k == 65 and crypt(key_1, salt) == pw:
                        print("{}".format(key_1))
                        exit(0)
                    if i == 65 and j == 65 and crypt(key_2, salt) == pw:
                        print("{}".format(key_2))
                        exit(0)
                    if i == 65 and crypt(key_3, salt) == pw:
                        print("{}".format(key_3))
                        exit(0)
                    if crypt(key_4, salt) == pw:
                        print("{}".format(key_4))
                        exit(0)
    
    # if no key is found, print as such    
    print("The password cannot be found")
    exit(2)


if __name__ == "__main__":
    main()
```
