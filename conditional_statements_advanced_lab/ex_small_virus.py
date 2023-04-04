import os

counter = 0

while counter < 3:
    counter += 1
    var = os.system("start cmd")
    var2 = os.system("start notepad")
    var3 = os.system("start microsoftedge")
    print(var, var2, var3)

#по-долният код го прави безкрайно да отваря прозорците
# while True:
#     var = os.system("start cmd")
#     var2 = os.system("start notepad")
#     var3 = os.system("start microsoftedge")
#     print(var, var2, var3)
