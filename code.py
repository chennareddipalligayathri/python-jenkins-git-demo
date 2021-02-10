import csv
total=[]
z1=0
fl=[]
print('WELCOME TO SUPER STORE ONLINE SHOPPING \n ')
def call():
    q=0
    se=[]
    pl=[]
    br=[]
    st=[]
    pr=[]
    l=0
    r2=1
    z2=1    
    z3=1
    z4=1
    k=10
    r1=0
    se=[]
    with open('mydata.csv') as c:
        re=csv.reader(c)
        p=input("Enter the Product name that u want to buy\n ")
        #print("Brand  Stock ")
        for row in re:
            if p in row:
                print(row[2],row[3])
                pl.append(row[1])
                br.append(row[2])
                pr.append(int(row[3]))
                st.append(int(row[4]))
                l=l+1
        if p in pl:
            while z2==1:
                b=input('Please Enter the brand that you wish to buy\n')
                if b not in br:
                    print("Sorry!Your requested brand is not available Please enter the correct brand name mentioned above\n")
                    z2=1
                else:
                    print("Great!Your requested brand is available\n")
                    while(z3==1):
                        print('Please enter how many',p,'of brand',b,'you wish to buy\n')
                        q=int(input())
                        for i in range (0,l):
                            if br[i]==b and q<st[i]:                   
                                a=q*pr[i]
                                total.append(int(a))                                             
                                k=1
                                se.append(q)
                        if k==1:
                            se.append(str(p))
                            print("Your Order is placed for",q,p,"you have to pay Rs",a,'\- \n ThankYou for Shopping\n')
                            z1=int(input('If you want to continue to shopping press 1 To exit press 0\n'))
                            z3=0
                            fl.append(se)
                            if z1==1:
                                call()
                                break
                        else:
                            print("Sorry!your requested stock for ",p,'of brand',b,'is not available \n Try another quantity\n')
                            z3=int(input('if you want to give another quantity press 1 To exit press 0\n'))
                    z2=0
        else:
            print('Sorry!your requested product is not available in our store\n')
            r1=int(input('if u want search for another product press 1 ,To Exit press 0\n'))
            if(r1==1):
                call()
call()
totala=0
for i in range(0,len(total)):
    totala=totala+total[i]
if(totala>0):
    print('You are requested to pay Total amount of Rs',totala,'\- for\n')
    for x in fl:
        for y in x:
            print(y,end=' ',)
        print('\n')
else:
    print("Your cart is empty")