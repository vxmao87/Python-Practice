# Prints 2^n stars depending on the value of n
def star_string(n):
    # error case
    if n < 0:
        raise ValueError("This number is invalid. Try again!")

    # base case
    if n == 0:
        return "*"
    else:
        return star_string(n - 1) + star_string(n - 1)

def main():
    print(star_string(4))   # Prints 16 stars
    print(star_string(3))   # Prints 8 stars
    print(star_string(2))   # Prints 4 stars
    print(star_string(1))   # Prints 2 stars
    print(star_string(0))   # Prints 1 star

main()