#Write your code below this line 👇
def paint_calc(height, width, cover):
    global paintcans
    paintcans = (height*width)/cover
    if 0.5 > paintcans%1 > 0:
        paintcans += 1
        paintcans = round(paintcans)
    elif paintcans%1 >= 0.5:
        paintcans = round(paintcans)
    else:
        return
#Write your code above this line 👆

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
print('You\'ll need',int(paintcans),'cans of paint')

