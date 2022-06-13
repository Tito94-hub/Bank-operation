
#Data Generation Exercise

import random

print("Generating 3 random integer number between 100 and 999 divisible by 5")
for num in range(3):
    print(random.randrange(100, 999, 5), end=', ')


#Random Lottery pick

import random

lottery_tickets_list = []
print(" Create  100 random lottery tickets")
# to get 100 tickets
for i in range(100):
    # ticket must be 10 digit (1000000000, 9999999999) 
    "lottery_ticket_list".append(random.randrange(1000000000, 000000000))  
# pick 2 luck tickets
winners = random.sample("lottery_ticket_list", 2)
print("Lucky 2 lottery tickets are", winners)


#Generate 6 digit random secure OTP

import secrets

#Getting systemRandom class instance out of secets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("Secure random OTP is ", otp)

#random.choice

import random

number_list = [111, 222, 333, 444, 555]
# random item from list
print(random.choice(number_list))
