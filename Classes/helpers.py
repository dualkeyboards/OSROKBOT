import random
import time
class Helpers:
    @staticmethod
    def getRandomRss():
        random.seed(time.time())
        #return lambda: random.choice(["stoneicon"])
        return lambda: random.choice(["logicon", "cornicon", "stoneicon"])
