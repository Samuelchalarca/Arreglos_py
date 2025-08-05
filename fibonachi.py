#region serie fibonachi        "serie": unknon word.
#es sin usar DEF, es decir, sin funciones  "unsar"
#FN = F-1+1F-2
# F-1 va a ser "a"
# F-2 va a ser "b"
a,b =0,1
#a=0 b=1
for i in range(11):
    print (a)
    a,b=b,a+b
    #a =b y b=a+b
#1 a,b=b,a+b a=1 b = 0+1= 1
#2 a,b=b,a+b a=1 b = 1+1=2
#3 a,b=b,a+b a=2 b = 2+1=3
#4 a,b=b,a+b a=3 b = 3+2=5
#5 a,b=b,a+b a=5 b = 5+3=8
#6 a,b=b,a+b a=8 b = 8+5=13
#7 a,b=b,a+b a=13 b=13+8=21
#8 a,b=b,a+b a=21 b=21+13=34
#9 a,b=b,a+b a=34 b=34+21=55
#10 a,b=b,a+b a=55 b=55+34=89
