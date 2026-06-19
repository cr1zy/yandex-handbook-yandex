counter = 0
def click():
    global counter 
    counter += 1
def get_count():
    print(counter)

click()
click()
click()
get_count()