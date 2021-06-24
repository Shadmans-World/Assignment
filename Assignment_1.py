print("Enter your GPA: ")
a = input()
a = float(a)

if a== 4.00:
    print("Your Grade is A+ (A Plus)")
if a>=3.75 and a<4.00:
    print("Your Grade is A (A Regular)")
elif a>=3.5 and a<3.75:
    print("Your Grade is A- (A Minus)")
elif a>=3.25 and a<3.5:
    print("Your Grade is B+ (B Plus)")
elif a>=3.0 and a<3.25:
    print("Your Grade is B (B Regular)")
elif a>=2.75 and a<3.0:
    print("Your Grade is B- (B Minus)")
elif a>=2.5 and a<2.75:
    print("Your Grade is C+ (C Plus)")
elif a>=2.25 and a<2.5:
    print("Your Grade is C (C Regular)")
elif a>=2.0 and a<2.25:
    print("Your Grade is D (D Regular)")

elif a<2.00:
    print("Your Grade is F (Fail)")