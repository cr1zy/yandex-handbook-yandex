numbers = input().split()
beans = []
for number in numbers:
    bean = (bin(int(number)))[2:]
    beans.append({
        "digits": len(bean),
        "units": bean.count("1"),
        "zeros": bean.count("0")
    })
print(beans)