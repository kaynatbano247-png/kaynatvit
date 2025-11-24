# This is the number guessing game till four digits
import random
print("welcome to  number guessing game")
while True:
  print("select how many digits of number you want to guess ")
  i=int(input("click 1 for one digit,"
            "2 for two digit,"
            "3 for three digit,"
            "4 for four digit"))

  if(i==1):
    number = random.randint(0, 10)
    print("you get 3 chance to guess the number right")
    j=1
    while (j<=3):

        num=int(input("enter the number"))
        if(num>=0 and num<10):
         if (num==number):
            print("congratulations that's a right guess")
            break
         elif(num>number):
            print("too high, try again")
         else:
            print("too low, try again")
         j=j+1
         if (j==4 and num!=number):
             print("you lost the chance the correct guess is", number)
        else:
            print("the no. of digits are wrong")
  elif(i==2):
         number=random.randint(10,100)
         print("you get 6 chance to guess the number right")
         j=1
         while (j<=6):
             num=int(input("enter the number"))
             if (num >= 10 and num < 100):
              if (num==number):
                 print("congratulations that's a right guess")
                 break
              elif(num>number):
                 print("too high, try again")
              else:
                 print("too low, try again")
              j=j+1
              if (j == 7 and num != number):
                  print("you lost the chance the correct guess is", number)
             else:
                 print("the no. of digits are wrong")
  elif(i==3):
    print("you get 9 chance to guess the number right")
    number = random.randint(100, 1000)
    j = 1
    while (j <= 9):
        num = int(input("enter the number"))
        if (num >= 100 and num <1000):
         if (num == number):
            print("congratulations that's a right guess")
            break
         elif (num > number):
            print("too high, try again")
         else:
            print("too low, try again")
         j = j + 1
         if (j==10 and num!=number):
             print("you lost the chance the correct guess is", number)
        else:
            print("the no. of digits are wrong")
  elif(i==4):
    print("you get 12 chance to guess the number right")
    number = random.randint(1000, 10000)
    j = 1
    while (j <= 12):
        num = int(input("enter the number"))
        if (num >= 1000 and num < 10000):
         if (num == number):
            print("congratulations that's a right guess")
            break
         elif (num > number):
            print("too high, try again")
         else:
            print("too low, try again")
         j = j + 1
         if (j==13 and num!=number):
             print("you lost the chance the correct guess is", number)
        else:
            print("the no. of digits are wrong")
  else:
    print("invalid input")
  user_input=int(input("do you want to play again? press 1 for yes or 0 for no"))
  if user_input==1:
     continue
  else:
     break










