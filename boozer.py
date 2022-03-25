# Карточная игра "Пьяница"
from random import shuffle

class Card():
    suits = ["пикей", "червей", "бубей", "треф"]
    values = [None, None, "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "валет", "дама", "король", "туз"]

    def __init__(self, value, suit):
        '''value, suit - целые числа'''
        self.value = value
        self.suit = suit

    def __lt__(self, card2):
        '''переопределение медота сравнения (less than), учитывает масти карт'''
        if self.value < card2.value:
            return True
        if self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, card2):
        '''переопределение медота сравнения (greater than), учитывает масти карт'''
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        '''переопределение метода строкового представления объекта'''
        v = self.values[self.value] + " " + self.suits[self.suit]
        return v

class Deck():
    def __init__(self):
        '''создание колоды карт и перемешивание в случайном порядке'''
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    
    def remove_card(self):
        '''изъятие карты из колоды, при отсутствии карт возвращает None'''
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0

class Game():
    def __init__(self):
        name1 = input("Имя первого игрока: ")
        name2 = input("Имя второго игрока: ")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)
    
    def wins(self, winner):
        '''вывод победившего в раунде игрока'''
        print("{} забирает карты".format(winner))

    def draw(self, player1, card1, player2, card2):
        '''вытягивание карт в раунде'''
        print("{} вытягивает {}, а {} вытягивает {}".format(player1, card1, player2, card2))

    def play_game(self):
        '''имитация игры'''
        cards = self.deck.cards
        print("Начинаем!")
        while len(cards) >= 2:
            response = input("Нажмите 'X' для выхода или любую другую клавишу для продолжения")
            if response == 'X' or response == 'Х':
                break
            player1_card = self.deck.remove_card()
            player2_card = self.deck.remove_card()
            self.draw(self.player1.name, player1_card, self.player2.name, player2_card)
            if player1_card > player2_card:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name)
            
        win = self.winner(self.player1, self.player2)
        if(win != "Ничья!"):
            print("Игра окончена, победил {}! Счет: {} на {}".format(win, self.player1.wins, self.player2.wins))
        else:
            print("У нас Ничья!")

    def winner(self, player1, player2):
        '''определение победителя по итогам всех раундов'''
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "Ничья!"

game = Game()
game.play_game()    
