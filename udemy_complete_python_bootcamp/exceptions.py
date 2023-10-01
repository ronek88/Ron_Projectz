try:
    result = 1 + 1 #"a"
except:
    print("Something error")
else:
    print(result)
    print("Added well!")
finally:
    print("The first expection is done! about 1 plus a")



def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Something went terribly wrong")
            continue
        else:
            print("Everything is OK!")
            break
        finally:
            print("while loop end!")


ask_for_int()