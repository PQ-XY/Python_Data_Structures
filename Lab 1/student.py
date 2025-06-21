# Write your code below:
"""
    Yao Xu
    6/5/2025
    This is an implementation of the Student class allowing following methods:

        getScore – access a score at the given position (counting from 0)
        setScore – replace a score at the given position (counting from 0)
        getNumberOfScores – obtain the number of scores
        getHighScore – obtain the highest score
        getAverage – obtain the average score
        getName – obtain the student’s name

    I also override the __str__() so when printing a student object, it prints as following:
        Name: Ken
        Score 1: 88
        Score 2: 77
        Score 3: 100
        High score: 100
        Average: 88.333
"""
class Student:
    def __init__(self, name, num_of_scores):
        self.name = name
        self.scores = [0] * num_of_scores

    def getScore(self, index):
        return self.scores[index]

    def setScore(self, index, score):
        self.scores[index] = score

    def getNumberOfScores(self):
        return len(self.scores)

    def getHighScore(self):
        return max(self.scores)

    def getAverage(self):
        return sum(self.scores) / len(self.scores)

    def getName(self):
        return self.name

    def __str__(self):
        result = f"Name: {self.name}\n"
        count = len(self.scores)
        i = 1
        while count > 0:
            result += f"Score {i}: {self.scores[i-1]}\n"
            i = i + 1
            count = count - 1
        result += f"High score: {self.getHighScore()}\n"
        result += f"Average: {self.getAverage():.3f}\n"
        return result
