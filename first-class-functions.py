# https://www.youtube.com/watch?v=kr0mpwqttM0
# Programming Terms: First-Class Functions

def xtimes(x):

    def ytimes(y):
        print(x*y)

    return ytimes

fx5 = xtimes(5)

fx5(3)
