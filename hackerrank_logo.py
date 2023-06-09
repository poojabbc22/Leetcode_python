# Define the thickness of the logo
thickness = 5

# Define the logo text
logo_text = "HackerRank"

# Generate the top row of the logo using the rjust() method
top_row = "H".rjust(thickness, " ")
print(top_row)

# Generate the middle rows of the logo using a for loop and the center() method
for i in range(thickness-1):
    middle_row = "H".ljust(i+1, " ") + "H".center(thickness*2-2*i, " ") + "H".rjust(thickness-i-1, " ")
    print(middle_row)

# Generate the bottom rows of the logo using the ljust() method
for i in range(thickness*2):
    bottom_row = " " * i + "H".ljust(thickness*2-i, " ")
    print(bottom_row)
