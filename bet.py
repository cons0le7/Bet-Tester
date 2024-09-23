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
    print(color_green("""
 __   ___ ___    ___  ___  __  ___  ___  __  
|__) |__   |      |  |__  /__`  |  |__  |__) 
|__) |___  |      |  |___ .__/  |  |___ |  \ 
                                             
    """))
    balance = int(input(f"{color_cyan('Enter starting balance: ')}$"))
    init_balance = balance
    start_bal = balance
    print(f"{color_cyan('Balance: ')}{color_green(f'${balance}')}")
    while True:
        try:
            initial_bet = int(input(f"{color_cyan('Enter amount to bet: ')}$"))
            if initial_bet <= 0:
                print(color_red("Please enter a positive number."))
                continue            
            num_bets = int(input(f"{color_cyan('Enter the number of bets you want to place:')} "))
            if num_bets <= 0:
                print(color_red("Please enter a positive number."))
                continue                
            loss_per = int(input(f"{color_cyan('Enter % of original bet amount to bet after losses.')}\n{color_purple('(100 = same amount, 50 = half, 200 = double):')} "))
            if loss_per <= 0:
                print(color_red("Please enter a positive number."))
                continue            
            bet_per = loss_per / 100
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
            difference = balance - next_bal
            print(f""" 
                {color_purple(f'Run: ')}{color_cyan(f'{run + 1}')}
                {color_purple(f'Initial balance: ')}{color_cyan(f'${init_balance:.2f}')}
                {color_purple(f'Start balance this run: ')}{color_cyan(f'${next_bal:.2f}')}
                {color_purple(f'Bet amount: ')}{color_cyan(f'${initial_bet:.2f}')}
                {color_purple(f'Number of bets: ')}{color_cyan(f'{bet_number + 1}')}
                {color_purple(f'% applied to bets after loss: ')}{color_cyan(f'{loss_per}%')}
                {color_purple(f'End balance ($): ')}{color_cyan(f'{balance:.2f}')}
                """)
            if difference > 0: 
                print(f"""
                {color_purple(f'Gain this run ($): ')}{color_green(f'+{difference:.2f}')}
                
                """)
            elif difference < 0: 
                print(f"""
                {color_purple(f'Loss this run ($): ')}{color_red(f'{difference:.2f}')}
                
                """)
            else: 
                print(color_cyan("""
                - IT'S A WASH! -
                """))

            next_bal = balance
            run = run + 1
        else: 
            difference = balance - init_balance
            print(f""" 
                {color_purple(f'Run: ')}{color_cyan(f'{run + 1}')}
                {color_purple(f'Initial balance: ')}{color_cyan(f'${init_balance:.2f}')}
                {color_purple(f'Bet amount: ')}{color_cyan(f'${initial_bet:.2f}')}
                {color_purple(f'Number of bets: ')}{color_cyan(f'{bet_number + 1}')}
                {color_purple(f'% applied to bets after loss: ')}{color_cyan(f'{loss_per}%')}
                {color_purple(f'End balance ($): ')}{color_cyan(f'{balance:.2f}')}
                """)
            if difference > 0: 
                print(f"""
                {color_purple(f'Gain this run ($): ')}{color_green(f'+{difference:.2f}')}
                
                """)
            else: 
                print(f"""
                {color_purple(f'Loss this run ($): ')}{color_red(f'{difference:.2f}')}
                
                """)
            next_bal = balance
            run = run + 1
        if bankrupt == False:          
            continue_betting = input("Do you want to place more bets? (yes/no): ").strip().lower()
            if continue_betting != 'yes':
                if balance > start_bal:
                    net_gain = balance - start_bal
                    print(f"""
                {color_purple(f'Total gain ($): ')}{color_green(f'+{net_gain:.2f}')}
                    """)
                elif balance < start_bal: 
                    net_loss = balance - start_bal 
                    print(f"""
                {color_purple(f'Total loss ($): ')}{color_red(f'{net_loss:.2f}')}
                    """)
                else: 
                    print(color_cyan("""
                   - IT'S A WASH! -
                    """))
                break
        elif bankrupt == True: 
            net_loss = balance - start_bal
            print(f"                {color_purple(f'Total loss ($): ')}{color_red(f'{net_loss:.2f}')}")
            print(color_red("""
                -!!!BANKRUPT!!!-
            """)) 
            break 
    
betting_test()
