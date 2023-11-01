# spolupráce s Juli Svatošovou a Mariánkou
a = 5
b = 10
c = 8

D = b * b - 4 * a * c
if a == 0:
    if b==0:
      if c==0:
        print ("x náleží do reálných čísel")
      else:
        print("Oops")
    else:
      print ("1",-c/b)   
else:
   if D == 0:
    print("1:", -b / (2 * a))
   elif D > 0:
    print(
        "1: ", (-b + D ** 0.5) / (2 * a),
        "2: ", (-b - D ** 0.5) / (2 * a)
       )
   else:
    print("Oops")