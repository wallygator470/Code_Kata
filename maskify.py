def maskify(string):
    return (len(string) - 4) * "#" + string[-4::]

print(maskify("karenanderewrweqdqwefwerwfwally"))