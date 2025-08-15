#!/usr/bin/env python3
"""
Blackjack Game - Fixed Version
Rules:
- Get as close to 21 as possible without going over
- Cards 2-10 are worth face value
- Jack, Queen, King are worth 10
- Ace is worth 11 or 1 (automatically adjusted)
- Dealer must hit if total is less than 17
"""

import random

# Card deck - Jack, Queen, King all worth 10
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck"""
    return random.choice(CARDS)

def calculate_score(cards):
    """Calculate the total score of cards, handling Aces properly"""
    score = sum(cards)
    
    # Handle Aces - convert 11 to 1 if score > 21
    ace_count = cards.count(11)
    while score > 21 and ace_count > 0:
        score -= 10  # Convert Ace from 11 to 1
        ace_count -= 1
    
    return score

def check_blackjack(cards):
    """Check if hand is blackjack (21 with 2 cards)"""
    return len(cards) == 2 and calculate_score(cards) == 21

def display_cards(user_cards, computer_cards, hide_computer=True):
    """Display current cards"""
    print(f"\nYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
    
    if hide_computer:
        print(f"Computer's first card: {computer_cards[0]}")
    else:
        print(f"Computer's cards: {computer_cards}, final score: {calculate_score(computer_cards)}")

def play_blackjack():
    """Main game function"""
    print("🃏 Welcome to Blackjack! 🃏")
    print("-" * 30)
    
    # Deal initial cards
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    game_over = False
    
    # Check for blackjack
    if check_blackjack(user_cards):
        display_cards(user_cards, computer_cards, hide_computer=False)
        if check_blackjack(computer_cards):
            print("🤝 Both have Blackjack! It's a draw!")
        else:
            print("🎉 Blackjack! You win!")
        return
    
    # User's turn
    while not game_over:
        display_cards(user_cards, computer_cards)
        
        user_score = calculate_score(user_cards)
        
        # Check if user busted
        if user_score > 21:
            game_over = True
            print("💥 You went over 21! You lose!")
            return
        
        # Ask user if they want another card
        should_continue = input("\nType 'y' to get another card, or 'n' to pass: ").lower()
        
        if should_continue == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True
    
    # Computer's turn
    computer_score = calculate_score(computer_cards)
    
    # Computer must hit if score < 17
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    # Final results
    display_cards(user_cards, computer_cards, hide_computer=False)
    user_score = calculate_score(user_cards)
    
    print("\n" + "="*40)
    print("🎯 FINAL RESULTS:")
    
    # Determine winner
    if computer_score > 21:
        print("🎉 Computer went over 21! You win!")
    elif user_score == computer_score:
        print("🤝 It's a draw!")
    elif user_score > computer_score:
        print("🎉 You win!")
    else:
        print("😔 Computer wins!")

def main():
    """Main program loop"""
    while True:
        play_blackjack()
        
        play_again = input("\n🔄 Do you want to play again? Type 'y' or 'n': ").lower()
        
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye!")
            break
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
