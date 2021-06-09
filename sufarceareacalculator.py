def question():
    print("enter r to start")
    selection = (input())
    if selection == "r":
        print("enter length")
        L = float(input())
        print("enter width")
        W = float(input())
        print("enter height")
        H = float(input())
        SA = 2 * W * L + 2 * L * H + 2 * H * W
        print(SA)
    print("another question?")
    yesno = input()
    if yesno == "yes":
        question()


question()
