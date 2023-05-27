from heroes_data import HeroesData
import numpy as np

class TeamRolesProblem:
    def solve(self, pick):
        keys = []
        h = HeroesData()
        for hero in pick:
            keys.append(h.searchByName(hero))
        self.values = h.getTeamPositionValues(keys)

        while not self.solved():
            self.setPos(*self.maxValueSearch())
        
        for i in range(1, 5):
            for j in range(i):
                if self.values[i][j] == 1:
                    pick[i], pick[j] = pick[j], pick[i]
    
    def maxValueSearch(self):
        max = -float("inf")
        i, j = -1, -1
        for row in range(5):
            for column in range(5):
                if self.values[row][column] > max and self.values[row][column] != 1:
                    max = self.values[row][column]
                    i, j = row, column
        return i, j

    def setPos(self, hero, pos):
        for i in range(5):
            self.values[hero][i] = 0
            self.values[i][pos] = 0
        self.values[hero][pos] = 1

        for row in self.values:
            summ = sum(row)
            for i in range(5):
                row[i] /= summ
    
    def solved(self):
        for i in range(5):
            for j in range(5):
                if self.values[i][j] != 1 and self.values[i][j] != 0:
                    return False
        return True