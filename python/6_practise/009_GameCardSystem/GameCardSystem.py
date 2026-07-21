class GameCard:
    def __init__(self, card_id, game_name, balance, is_active):
        self.card_id = card_id
        self.game_name = game_name
        self.balance = balance
        self.is_active = True
    
    def display_card_info(self):
        print(f"Card ID: {self.card_id}")
        print(f"Game Name: {self.game_name}")
        print(f"Balance: {self.balance}")
        print(f"Active Status: {self.is_active}")

    def add_balance(self, amount):
        self.balance += amount
        print(f"Added {amount} to balance. New balance: {self.balance}")

    def deduct_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Deducted {amount} from balance. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

class Player:
    def __init__(self, player_id, name, card):
        self.player_id = player_id
        self.name = name
        self.card = card
    def display_player_info(self):
        print(f"Player ID: {self.player_id}")
        print(f"Name: {self.name}")
        print(f"Card Info: {self.card}")


        

class GameCenter:
    def __init__(self):
        self.players = []
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        print(f"Card {card.card_id} added to the game center.")

    def add_player(self, player):
        self.players.append(player)
        print(f"Player {player.name} added to the game center.")

    def find_card(self, card_id):
        for card in self.cards:
            if card.card_id == card_id:
                return card
        print("Card not found.")
        return None
    
    def remove_card(self, card):
        self.cards.remove(card)
        print(f"Card {card.card_id} removed from the game center.")

    def display_cards(self):
        for card in self.cards:
            card.display_card_info()

    def active_cards(self, is_active=True):
        active_cards = []
        for card in self.cards:
            if card.is_active == is_active:
                active_cards.append(card)
        return active_cards
   
    def play_game(self, card_id, cost):
        card = self.find_card(card_id)
        if card:
            if card.is_active:
                card.deduct_balance(cost)
            else:
                print("Card is not active.")

    def recharge_card(self, card_id, amount):
        card = self.find_card(card_id)
        if card:
            card.add_balance(amount)
            print(f"Card {card.card_id} recharged with {amount}. New balance: {card.balance}")  

Game_Centre = GameCenter()
gamecard1 = GameCard(1, "Game A", 100, True)
gamecard2 = GameCard(2, "Game B", 150, True)
Player1 = Player(1, "Alice", gamecard1)
Player2 = Player(2, "Bob", gamecard2)
Game_Centre.add_player(Player1)
Game_Centre.add_player(Player2)
Game_Centre.add_card(gamecard1)
Game_Centre.add_card(gamecard2)
Game_Centre.display_cards()
Game_Centre.recharge_card(1, 50)
Game_Centre.play_game(1, 30)
Game_Centre.play_game(2, 30)
Game_Centre.find_card(1).display_card_info()
Game_Centre.remove_card(gamecard1)
Game_Centre.display_cards()

