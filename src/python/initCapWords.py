def toJadenCase(string):
    return " ".join(word.capitalize() for word in string.split())
 
print(toJadenCase("How can mirrors be real if our eyes aren't real"))
