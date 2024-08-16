import random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())


def print_cards(user_cards, computer_cards):
  print(f"User Cards: {user_cards} = {sum(user_cards)}")
  print(f"Computer Cards: {computer_cards[0]} , X")


def result_cards(user_cards, computer_cards):
  print("\n***RESULT***\n")
  print(f"User Cards: {user_cards} = {sum(user_cards)}")
  print(f"Computer Cards: {computer_cards} = {sum(computer_cards)}")


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)


def check_winner(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw!"
  elif computer_score == 0:
    return "The computer has a blackjack! Computer wins!"
  elif user_score == 0:
    return "The user has a blackjack! User wins!"
  elif user_score > 21:
    return "The user busted! Computer wins!"
  elif computer_score > 21:
    return "The computer busted! User wins!"
  elif user_score > computer_score:
    return "User wins!"
  else:
    return "Computer wins!"


print("\n******** THE GAME STARTS ********\n")
print_cards(user_cards, computer_cards)

game_over = False

while game_over is not True:

  choice = input("\nDo you want to draw another card? (y/n): \n")

  if choice == 'y':
    user_cards.append(deal_card())
    print_cards(user_cards, computer_cards)
    calculate_score(user_cards)
    user_score = calculate_score(user_cards)

    if user_score > 21:
      result_cards(user_cards, computer_cards)
      print("\n")
      print("The user busted! Computer wins!")
      game_over = True

  if choice == 'n':

    while sum(computer_cards) <= 16:
      computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    result_cards(user_cards, computer_cards)
    result = check_winner(user_score, computer_score)
    print(result)
    game_over = True
