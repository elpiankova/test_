f = open("first_script.py", "a")
try:
    print("New line\n", file=f)
    int(f)
finally:
    print("hi!")
    f.close()