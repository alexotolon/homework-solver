def getLastNumber(theString):
    return 7


variables = input("What letters are there? ")
variables = variables.split(",")

lookup = {}
for b in variables:
    lookup[b] = input("what number should be " + b + "? ")
if not lookup[b].isalpha():
    while True:
        previoslySign = True
        problem = input("what is the question ")
        problem2 = ""
        for b in problem:
            newb = ""
            if b.isspace():
                continue
            if b.isalpha():
                newb = lookup[b]
                if not previoslySign:
                    newb = "*" + newb
            if b.isalnum():
                previoslySign = False
            else:
                previoslySign = True
            if newb != "":
                b = newb
            problem2 = problem2 + b
        # print(problem2)
        print(eval(problem2))
else:
    problem = input("what is the question ")
    problem = problem.split(lookup[b])
