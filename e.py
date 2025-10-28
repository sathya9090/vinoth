a=100
b=20
c=a+b
print(c)

# ...existing code...
a=100
b=20
c=a+b
print(c)
# ...existing code...
# replaced with voting-age code
def can_vote(age):
    try:
        age = int(age)
    except ValueError:
        return None
    if age < 0:
        return None
    return age >= 20

if __name__ == "__main__":
    age_input = input("Enter your age: ")
    result = can_vote(age_input)
    if result is None:
        print("Please enter a valid non-negative integer for age.")
    elif result:
        print("You are eligible to vote.")
    else:
        years = 18 - int(age_input)
        print(f"You are not eligible to vote. Come back in {years} year{'s' if years != 1 else ''}.")
        print("thanks for use this code")                
# ...existing code...
