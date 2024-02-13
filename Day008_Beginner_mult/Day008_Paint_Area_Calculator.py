# Write your code below this line 👇

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.
def paint_calc(height, width, cover):
    if (height*width)%cover:
        cans = round((height*width)/cover) + 1
    else:
        cans = round((height*width)/cover)

    print(f"You'll need {cans} cans of paint.")


# 🚨 Don't change the code below 👇
test_h = 4 # Height of wall (m)
test_w = 9 # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
