"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish and bears that die of old age."""
        keep_fish: list[Fish] = []
        for i in self.fish:
            if i.age <= 3:
                keep_fish.append(i)
        self.fish = keep_fish

        keep_bears: list[Bear] = []
        for j in self.bears:
            if j.age <= 5:
                keep_bears.append(j)
        self.bears = keep_bears

    def bears_eating(self):
        if len(self.fish) >= 5:
            for i in self.bears:
                i.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        keep_bears: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                keep_bears.append(i)
        self.bears = keep_bears
        
    def repopulate_fish(self):
        for i in range(((len(self.fish))//2) * 4):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        for i in range(len(self.bears)//2):
            self.bears.append(Bear())
    
    def view_river(self):
        print(f"~~~ Day {self.day} ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")

    def one_river_week(self):
        for i in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        for i in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()