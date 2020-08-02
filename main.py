
import random
import re

def roll_dice(no, sides, modifier=0):

    total = 0

    for i in range(1, no+1):
        
        val = random.randint(1, sides)
        print(f'{i} : {val}')
        total += val

    return total + modifier

if __name__=='__main__':
    
    on = True
    last = ""

    while on:

        response = input(f'> Roll:   ')

        try:
            if response != None and response != "":
                if response == "exit" or response == "quit" or response == "q":
                    on = False
                elif response == "reroll" or response == "rr":
                    if last == None or last == "":
                        print('No dice have been rolled.')
                    else:
                        di = last.split(" ")
                        print(f'{last}\n')
                    
                        for i in di:
                            
                            if "+" in i:
                                dice = re.split('[d\+]', i)
                                value = roll_dice(int(dice[0]), int(dice[1]), int(dice[2]))

                                print(f'\nTotal : {value}')
                            else:
                                dice = i.split("d")
                                value = roll_dice(int(dice[0]), int(dice[1]))

                                print(f'\nTotal : {value}')
                else:
                    last = response
                    di = response.split(" ")
                    
                    for i in di:
                        
                        if "+" in i:
                            dice = re.split('[d\+]', i)
                            value = roll_dice(int(dice[0]), int(dice[1]), int(dice[2]))

                            print(f'\nTotal : {value}')
                        else:
                            dice = i.split("d")
                            value = roll_dice(int(dice[0]), int(dice[1]))

                            print(f'\nTotal : {value}')

            else:
                print('Please enter a value.')

        except:
            print('An error occurred. Please enter valid syntax.\n\n[No. of dice to roll]d[No. sides of dice]+[Modifier]\nExample:  1d6+4')
