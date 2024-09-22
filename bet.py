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
    
def color_purple(text): 
    PURPLE = "\033[35m"
    RESET = "\033[0m" 
    return f"{PURPLE}{text}{RESET}"

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
            initial_bet = int(input("Enter amount to bet: $"))
            if initial_bet <= 0:
                print(color_red("Please enter a positive number."))
                continue            
            num_bets = int(input("Enter the number of bets you want to place: "))
            if num_bets <= 0:
                print(color_red("Please enter a positive number."))
                continue                
            loss_per = int(input("Enter % of original bet amount to bet after losses. \n(100 = same amount, 50 = half, 200 = double): "))
            if loss_per <= 0:
                print(color_red("Please enter a positive number."))
                continue            
            bet_per = loss_per / 100
        except ValueError:
            print(color_red("Invalid input. Please enter a number."))
            continue
        
        start_bal = balance
        current_bet = initial_bet
        bankrupt = False

        for bet_number in range(num_bets):
            if balance <= 0:
                bankrupt = True
                print(color_red("""
                -!!!BANKRUPT!!!-
                """))
                break

            print(f"{color_blue(f'Bet {bet_number + 1}:')}{color_cyan(f' ${current_bet:.2f}')}")

            if random.choice([True, False]): 
                balance += current_bet 
                print(color_green(f"You won! New balance: ${balance:.2f}"))
                current_bet = initial_bet 
            else:
                balance -= current_bet  
                print(color_red(f"You lost! New balance: ${balance:.2f}"))
                current_bet *= bet_per  
        if run > 0: 
            print(f""" 
                {color_purple(f'Run: ')}{color_cyan(f'{run + 1}')}
                {color_purple(f'Initial balance: ')}{color_cyan(f'${init_balance:.2f}')}
                {color_purple(f'Start balance this run: ')}{color_cyan(f'${next_bal:.2f}')}
                {color_purple(f'Bet amount: ')}{color_cyan(f'${initial_bet:.2f}')}
                {color_purple(f'Number of bets: ')}{color_cyan(f'{bet_number}')}
                {color_purple(f'% applied after lost bets: ')}{color_cyan(f'{loss_per}%')}
                {color_purple(f'End balance: ')}{color_cyan(f'${balance:.2f}')}
                """)
            next_bal = balance
            run = run + 1
        else: 
            print(f""" 
                {color_purple(f'Run: ')}{color_cyan(f'{run + 1}')}
                {color_purple(f'Initial balance: ')}{color_cyan(f'${init_balance:.2f}')}
                {color_purple(f'Bet amount: ')}{color_cyan(f'${initial_bet:.2f}')}
                {color_purple(f'Number of bets: ')}{color_cyan(f'{bet_number}')}
                {color_purple(f'% applied after lost bets: ')}{color_cyan(f'{loss_per}%')}
                {color_purple(f'End balance: ')}{color_cyan(f'${balance:.2f}')}
                """)
            next_bal = balance
            run = run + 1
        if bankrupt == False:          
            continue_betting = input("Do you want to place more bets? (yes/no): ").strip().lower()
            if continue_betting != 'yes':
                net = balance - start_bal
                if net > 0: 
                    print(f"                {color_purple(f'Net gain ($): ')}{color_cyan(f'+{net:.2f}')}")
                else: 
                    print(f"                {color_purple(f'Net loss ($): ')}{color_cyan(f'{net:.2f}')}")
                break
        elif bankrupt == True: 
            print(color_red("""
                -!!!BANKRUPT!!!-
            """)) 
            break 
    
betting_test()
