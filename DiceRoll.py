#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  num_rolls = 10000
  for r in range(num_rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    
  #find the sum total of the two dice
    total = dice1 + dice2
    rolls[total - 2] = rolls[total-2] + 1
  #print statictics for dice rolls
  print("Sum", "Count", "Percentage")
  for index in range(11):
      sum_value = index + 2
      count = rolls[index]
      percentage = (count / num_rolls)* 100
      rounded_percent = round(percentage, 2)

      print(sum_value,":", count, rounded_percent, "%") 
    

if __name__ == '__main__':
  main()
