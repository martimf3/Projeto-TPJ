import pygame
from ui import UI

# An abstract class representing the observer
class Observer:
    def update(self, coin_count: int):
        pass

# The subject (coin counter)
class CoinCounter:
    def __init__(self):
        self.observers = []
        self.coin_count = 0

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def collect_coin(self, value):
        self.coin_count += value
        for observer in self.observers:
            observer.update(self.coin_count)

    def get_coin_count(self):
        return self.coin_count

# A concrete observer
class CoinCounterDisplay(Observer):
	def __init__(self, coin_counter: CoinCounter, screen):
		self.coin_counter = coin_counter
		self.coin_counter.add_observer(self)
		self.font = pygame.font.Font(None, 36)
		self.ui = UI(screen)

	def update(self, coin_count):
		self.coin_count = coin_count
		self.ui.show_coins(self.coin_count)
		