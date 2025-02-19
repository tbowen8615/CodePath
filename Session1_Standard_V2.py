def batman():
    print("I am vengeance. I am the night. I am Batman!")
    return None

batman()

def madlib(verb):
    print(f"I have one power. I never {verb}. - Batman")
    return None

verb = "shit my pants"
madlib(verb)

def trilogy(year):
    if year == 2005:
        print("Batman Begins")
    elif year == 2008:
        print("The Dark Knight")
    elif year == 2012:
        print("The Dark Knight Rises")
    else:
        print(f"Christopher Nolan did not release a Batman movie in year {year}")

year = 2008
trilogy(year)