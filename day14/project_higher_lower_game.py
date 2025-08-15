# Higher Lower Game
# The player guesses which option has a higher value

import random

logo = """
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                
"""


vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""



def higher_lower():
    print("🎮 Welcome to the Higher Lower Game! 🎮")
    print(logo)

    print("I'll show you two numbers, guess which one is higher!")
    print("Choose 'A' for the first number or 'B' for the second number")
    print("-" * 50)
    print(vs)
    score = 0
    game_continues = True
    
    while game_continues:
        # Generate two random numbers
        choice_A = random.randint(1, 100)
        choice_B = random.randint(1, 100)
        
        # Make sure the numbers are different
        while choice_A == choice_B:
            choice_B = random.randint(1, 100)
        
        # Display the choices
        print(f"\nA: {choice_A}")
        print(f"B: {choice_B}")
        
        # Get user input
        user_input = input("\nWhich number is higher? (A/B): ").upper().strip()
        
        # Validate input
        while user_input not in ['A', 'B']:
            user_input = input("Please enter 'A' or 'B': ").upper().strip()
        
        # Check if the guess is correct
        if (choice_A > choice_B and user_input == "A") or (choice_B > choice_A and user_input == "B"):
            score += 1
            print(f"✅ Correct! Your score: {score}")
            
            # Ask if they want to continue
            continue_game = input("\nDo you want to continue? (y/n): ").lower().strip()
            if continue_game != 'y':
                game_continues = False
        else:
            print(f"❌ Wrong! The correct answer was {'A' if choice_A > choice_B else 'B'}")
            print(f"💀 Game Over! Your final score: {score}")
            game_continues = False
    
    print(f"\n🏆 Thanks for playing! Final Score: {score}")

# Start the game
if __name__ == "__main__":
    higher_lower()