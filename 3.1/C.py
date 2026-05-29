while (string := input()) != '':

    if string.endswith("@@@"):
        continue

    if string.startswith("##"):
        print(string[2:])
   
    print(string)