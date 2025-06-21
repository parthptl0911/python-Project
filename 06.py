# TASK 1 : accept two numbers from user and check which number is greater 

# TASK 2 : accept two numbers and check entered number is positive or negative 

# 	accept two numbers and check entered number is even and odd  	


# TASK 3 : mini project : 

# KALYAN JWELLERS : 

# M 
# >  65
# purchase > 2lk - 3lk    20% 
# purchase > 3lk - 5lk 	30% 
# purchase > 5lk  	35% 


# <65
# purchase > 2lk - 3lk    10% 
# purchase > 3lk - 5lk 	20% 
# purchase > 5lk  	25% 



# F
# >  65
# purchase > 2lk - 3lk    25% 
# purchase > 3lk - 5lk 	35% 
# purchase > 5lk  	40% 


# <65
# purchase > 2lk - 3lk    15% 
# purchase > 3lk - 5lk 	25% 
# purchase > 5lk  	30% 


# ------------------------------------------------------------
# Enter your name : 
# Enter gender : 
# Enter age : 

# Enter product : Ring 
# Enter product gram : 20  
# current gold price (1 grm) : 5752

# -------------------------------------
# TOTAL GOLD RATE :  XXXXX 


# Making charges (1 gram)  : 845
# Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

# ---------------------------------------
# TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG



# DISCOUNT :   25 (AUTOMATIC) 
# DIS- AMOUNT : except (making charges) 
# -----------------------------------------
# total net amount : 

# --------------------------------------------
# HINT : variables , input , conditional statements 











name = str(input("enter your name :"))
gender = str(input("enter your gender 'M' or 'F':"))
age = int(input("enter your age:"))

product=str(input("enter a product:"))
gram=float(input("enter a product gram:"))
gold_price=9837
mak_charge=845 
total_gold_rate =gram*gold_price
Making_charges =gram*mak_charge
total_amount=total_gold_rate + Making_charges
if gender=='M' or gender=='m':

    if age>=65 :

        print("total gold rate =",total_gold_rate)
        print("Making charges =",Making_charges)
        print("total making charges = ",total_amount)
        print("============================================================")
        if total_amount<=300000 and total_amount>200000:
            print("you have get discount of 20%")
            print("discount amount :",(total_amount)*0.20)
            print("total net amount:",total_amount-((total_amount)*0.20))
        elif total_amount<=500000 and total_amount>300000:
            print("you have get discount of 30%")
            print("discount amount :",(total_amount)*0.30)
            print("total net amount:",total_amount-((total_amount)*0.30))
        elif total_amount>50000:
            print("you have get discount of 35%")
            print("discount amount :",(total_amount)*0.35)
            print("total net amount:",total_amount-((total_amount)*0.35))
        else:
            print("sorry! you have not aligible for discount.")
            print("you have to pay=",total_amount)

    elif age<65 and age>0:
        print("total gold rate =",total_gold_rate)
        print("Making charges =",Making_charges)
        print("total making charges = ",total_amount)
        print("============================================================")
        if total_amount<=300000 and total_amount>200000:
            print("you have get discount of 10%")
            print("discount amount :",(total_amount)*0.10)
            print("total net amount:",total_amount-((total_amount)*0.10))
        elif total_amount<=500000 and total_amount>300000:
            print("you have get discount of 20%")
            print("discount amount :",(total_amount)*0.20)
            print("total net amount:",total_amount-((total_amount)*0.20))
        elif total_amount>50000:
            print("you have get discount of 25%")
            print("discount amount :",(total_amount)*0.25)
            print("total net amount:",total_amount-((total_amount)*0.25))
        else:
            print("sorry! you have not aligible for discount.")
            print("you have to pay=",total_amount)

    else:
        print("please enter a valid age ")

elif gender=='F' or gender=='f':

    if age>=65 :

        print("total gold rate =",total_gold_rate)
        print("Making charges =",Making_charges)
        print("total making charges = ",total_amount)
        print("============================================================")
        if total_amount<=300000 and total_amount>200000:
            print("you have get discount of 25%")
            print("discount amount :",(total_amount)*0.25)
            print("total net amount:",total_amount-((total_amount)*0.25))
        elif total_amount<=500000 and total_amount>300000:
            print("you have get discount of 35%")
            print("discount amount :",(total_amount)*0.35)
            print("total net amount:",total_amount-((total_amount)*0.35))
        elif total_amount>50000:
            print("you have get discount of 40%")
            print("discount amount :",(total_amount)*0.40)
            print("total net amount:",total_amount-((total_amount)*0.40))
        else:
            print("sorry! you have not aligible for discount.")
            print("you have to pay=",total_amount)

    elif age<65 and age>0:
        print("total gold rate =",total_gold_rate)
        print("Making charges =",Making_charges)
        print("total making charges = ",total_amount)
        print("============================================================")
        if total_amount<=300000 and total_amount>200000:
            print("you have get discount of 10%")
            print("discount amount :",(total_amount)*0.10)
            print("total net amount:",total_amount-((total_amount)*0.15))
        elif total_amount<=500000 and total_amount>300000:
            print("you have get discount of 20%")
            print("discount amount :",(total_amount)*0.20)
            print("total net amount:",total_amount-((total_amount)*0.25))
        elif total_amount>50000:
            print("you have get discount of 25%")
            print("discount amount :",(total_amount)*2.5)
            print("total net amount:",total_amount-((total_amount)*0.30))
        else:
            print("you have to pay=",total_amount)

    else:
        print("please enter a valid age ")
else:
    print("pleasee enter a valid gender!")

print("Thank you for visiting")
        
