```
# prompt the user the set the height of the pyramid to be built
height = int(input("How high is your pyramid: "))

# limit the height of the pyramid between 0 and 23 both inclusive
while height < 0 or height >= 24:
    height = int(input("Please choose a size between 0 and 23 both inclusive: "))

# build the pyramid
for i in range(height):
    a = i + 1 # get the number of #
    b = height - a # get the number of space
    print(" " * b + "#" * a + "  " + "#" * a)
```
