import random

def color_blue(text): 
    BLUE = "\033[34m"
    RESET = "\033[0m" 
    return f"{BLUE}{text}{RESET}" 

def color_cyan(text): 
    CYAN = "\033[36m" 
    RESET = "\033[0m"
    return f"{CYAN}{text}{RESET}"

def color_green(text):
    GREEN = "\033[32m"
    RESET = "\033[0m"
    return f"{GREEN}{text}{RESET}"

def color_red(text):
    RED = "\033[31m"  
    RESET = "\033[0m" 
    return f"{RED}{text}{RESET}"
    


def betting_test():
    run = 0
    print("""
 __   ___ ___    ___  ___  __  ___  ___  __  
|__) |__   |      |  |__  /__`  |  |__  |__) 
|__) |___  |      |  |___ .__/  |  |___ |  \ 
                                             
    """)
    balance = int(input("Enter starting balance: $"))
    init_balance = balance
    print("Balance: $" + str(balance))
    while True:
        try:
            initial_bet = int(input("Enter amount to bet: "))
            if initial_bet <= 0:
                print(color_red("Please enter a positive number."))
                continue            
            num_bets = int(input("Enter the number of bets you want to place: "))
            if num_bets <= 0:
                print(color_red("Please enter a positive number."))
                continue                
            loss_per = int(input("Enter % to increase bet by if lost: "))
            if loss_per <= 0:
                print(color_red("Please enter a positive number."))
                continue            
            bet_per = float("1." + str(loss_per))
        except ValueError:
            print(color_red("Invalid input. Please enter a number."))
            continue
        
        current_bet = initial_bet
        bankrupt = False

        for bet_number in range(num_bets):
            if balance <= 0:
                bankrupt = True
                print(color_red("""
                -!!!BANKRUPT!!!-
                """))
                break

            print(color_blue(f"Bet {bet_number + 1}: Current balance: ${balance}"))
            print(color_cyan(f"Betting: ${current_bet}"))

            if random.choice([True, False]): 
                balance += current_bet 
                print(color_green(f"You won! New balance: ${balance}"))
                current_bet = initial_bet 
            else:
                balance -= current_bet  
                print(color_red(f"You lost! New balance: ${balance}"))
                current_bet *= bet_per  
        if run > 0: 
            print(color_cyan(f""" 
                Start balance: ${next_bal}
                Bet amount: ${initial_bet}
                Number of bets: {num_bets}
                Increase for losses {loss_per}%
                End balance: ${balance}
                """))
        else: 
            print(color_cyan(f""" 
                Initial balance: ${init_balance}
                Bet amount: ${initial_bet}
                Number of bets: {num_bets}
                Increase for losses {loss_per}%
                End balance: ${balance}
                """))
            next_bal = balance 
            run = run + 1
        if bankrupt == False:          
            continue_betting = input("Do you want to place more bets? (yes/no): ").strip().lower()
            if continue_betting != 'yes':
                print(color_cyan(f"End balance: ${balance}"))
                break
        elif bankrupt == True: 
            print(color_red("""
                -!!!BANKRUPT!!!-
            """)) 
            break 
    
betting_test()
