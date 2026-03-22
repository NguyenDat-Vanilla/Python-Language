n=int(input("nhap n: "))
    
if n <= 1:
        print(n, "khong phai la so nguyen to")
else:
    for i in range (2, n):
        if n%i==0:
            print(n, "khong phai la so nguyen to")
            break
    else:
        print(n, "la so nguyen to")
                
