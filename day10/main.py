myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))

bill_with_tip = (tip/100 * myBill) + myBill
final_amount = round(bill_with_tip/numberOfPeople, 2)
print("You all owe", final_amount)