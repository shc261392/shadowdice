from random import Random
from typing import List

class Dice:
    def __init__(self,
                 count=0,
                 sides=0,
                 sides_override=None,
                 random_seed=None):
        self.count = count  # type: int
        self.sides = sides  # type: int
        self.sides_override = sides_override    # type: Dict
        self.random_seed = random_seed  # type: int
        self.result = None  # type: List[int]

    def evaluate(self) -> List[int]:
        if self.count <= 0 or self.sides <= 0:
            return []
        rand = Random(self.random_seed)
        result = [None] * self.count
        result = [rand.randint(1, self.sides) for x in result]
        
        if self.sides_override:
            for key, val in self.sides_override.items():
                result = [val if x==int(key) else x for x in result]
            
        self.result = result
        return self.result
