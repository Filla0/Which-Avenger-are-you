print("Welcome to 'Which Avenger are you?' quiz game!")
print("Please answer the following questions:")

score = 0

q1 = input("What is your favorite color?\n(a) Red\n(b) Blue\n(c) Green\n(d) Black\n")
if q1 == "a":
    score += 1
elif q1 == "b":
    score += 2
elif q1 == "c":
    score += 3
elif q1 == "d":
    score += 4
else:
    print("invalid answer.")

q2 = input("What is your preferred weapon?\n(a) Hammer\n(b) Shield\n(c) Bow and Arrow\n(d) Guns\n")
if q2 == "a":
    score += 4
elif q2 == "b":
    score += 3
elif q2 == "c":
    score += 2
elif q2 == "d":
    score += 1
else:
    print("invalid answer.")

q3 = input("What is your favorite movie type?\n(a) Action\n(b) Drama\n(c) Comedy\n(d) Horror\n")
if q3 == "a":
    score += 4
elif q3 == "b":
    score += 3
elif q3 == "c":
    score += 2
elif q3 == "d":
    score += 1
else:
    print("invalid answer.")

q4 = input("What is your favorite Hobby?\n(a) working out\n(b) Reading\n(c) Playing video games\n(d) watching TV\n")
if q4== "a":
    score += 4
elif q4 == "b":
    score += 3
elif q4 == "c":
    score += 2
elif q4 == "d":
    score += 1
else:
    print("invalid answer.")

q5 = input("What is your favorite food?\n(a) Steak\n(b) Salad\n(c) Pizza\n(d) Sushi\n")
if q5== "a":
    score += 4
elif q5 == "b":
    score += 3
elif q5 == "c":
    score += 2
elif q5 == "d":
    score += 1
else:
    print("invalid answer.")

if score >= 16:
    print("You are Thor!")
elif score >= 12:
    print("You are Captain America!")
elif score >= 8:
    print(("You are Hawkey!"))
elif score >= 4:
    print("You are Black Window!")
else:
    print("You are Iron Man!")