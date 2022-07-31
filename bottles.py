
def bottles():
    word = "bottles"

    for num in range(99, 0 , -1):
        print(num, word, "of beer on the wall.")
        print(num, word, "of beer")

        print("Take one down")
        print("Pass it around")

        if num == 1:
            print("No more bottles of beer on the wall.")
        else:

            new_num = num - 1
            if new_num == 1:
                word = "bottle"
            
            print(new_num, word, "of beer on the wall")
        print()

print(bottles())