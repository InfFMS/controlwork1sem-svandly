n = int(input())
a = 2
function = 1
while a < n:
    a +=1
    function2 = function+2**(a-1)
    function = function2
print(function)