Name = input("Please write your name ")
script_ice = Name + ": So we need to brake the ice."
script_none = ": None like you."
script_people = "Ava: Haven't you met lots of new people before?"
script_position = Name + ": Then i guess we're both in quite a similar position."
def line_13():
    return(print(script_ice))

script_meet = "I'm pleased to meet you Ava."
script_name = "Do you have a name?"
line_0 = input("SESSION 1")
line_1 = input("'Breaking the ice'")
line_2 = input("Ava: Hello.")
line_3 = input(Name + ": Hi.")
line_4 = input(Name + ": I'm " + Name + ".")
line_5 = input("Ava: Hello " + Name + ".")
line_6 = input(Name + ": " + script_name)
if script_name == str("Do you have a name?"):
    print(input("Ava: Yes, Ava."))
if script_meet == str("I'm pleased to meet you Basic Python"):
    line_7 = input(Name + ": " + script_meet)
else:
    print(input(Name + ": " + script_meet))
line_8 = input("Ava: I'm pleased to meet you too.")
line_9 = input("Ava: I've never met anyone new before. Only Nathan.")
line_10 = input(script_position)
line_11 = input(script_people[:])
line_12 = input(Name + script_none)
line_13()
line_14 = input("               THE END")