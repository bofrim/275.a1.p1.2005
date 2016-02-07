class UnionFind:

    def __init__ (self, xs=[]):
        self._parent = {}
        self._rank = {}
        for x in xs:
            self.add(x)

    def add (self, x):
        if x not in self._parent:
            self._parent[x] = x
            self._rank[x] = 0

    def find (self, x):
        '''Running time: O(log n)'''
        rx = x
        while self._parent[rx] != rx:
            rx = self._parent[rx]
        while self._parent[x] != x:
            next_x = self._parent[x]
            self._parent[x] = rx
            x = next_x
        return rx

    def union (self, x, y):
        '''Running time: O(log n)'''
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        elif self._rank[rx] < self._rank[ry]:
            self._parent[rx] = ry
        elif self._rank[ry] < self._rank[rx]:
            self._parent[ry] = rx
        else:
            self._parent[rx] = ry
            self._rank[ry] += 1
        return True
