cp=float(input("Enter a cost price :"))

sp=float(input("enter a selling price:"))

if(sp>cp):
    profit =sp-cp
    profit_per=(profit/cp)*100

    print("profit :",profit)
    print("Profit percentage :",profit_per)

elif(sp<cp):
    loss =cp-sp
    loss_per=(loss/cp)*100

    print("loss :",loss)
    print("loss percentage :",loss_per)
else:
    print("NO profit or loss same price")