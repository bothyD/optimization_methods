class Edge:
    def __init__(self, a: int, b: int, cost: int, flow: int = 0):
        self.a=a
        self.b=b
        self.cost=cost
        self.flow=flow