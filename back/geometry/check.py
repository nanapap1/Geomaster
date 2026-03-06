import math


class Check:

    def __init__(self, game):
        self.field = game.fig.fig
        self.res = None
        self.func = None
        self.quan = 0
        self.find = []

    def set(self,func,quan,res):
        self.res = res
        self.func = func
        self.quan = quan
        self.find = []

    def apply(self):
        return self.func()

    def lom(self):
         self.find = []
         for one in self.res:
             self.path = []
             self.dfs(one,self.quan)
         if len(self.find) >0:
             return True
         return False


    def dfs(self, point, length):
        if len(self.path) >= length:
            return
        self.path.append(point)
        for one in self.field.polyline.connections[point]:
            if one in self.res and len(self.path) == length and one not in self.path:
                    self.find.append(self.path)
            elif one not in self.path and one in self.res:
                self.dfs(one, length)
        self.path.pop(-1)



    def lines(self):
        cnt = 0
        for x in range(0,len(self.res)):
            ls = self.res[:x] + self.res[x + 1:]
            if set(ls).issubset(self.field.polyline.connections[self.res[x]]):
                self.find.append(self.field.polyline.connections[self.res[x]])
                cnt += 1
            if cnt == self.quan:
                return True
        return False

    def point(self):
             return list(self.field.polyline.lines.keys()) != []


    def mnogo(self):
        res = self.field.polyline.search(self.quan)
        for x in range(0,len(res)):
            start = min(res[x], key=lambda p: (p.center[0], p.center[1]))
            other_points = [p for p in res[x] if p != start]
            def sort_key(p):
                dx = p.center[0] - start.center[0]
                dy = p.center[1] - start.center[1]
                angle = math.atan2(dy, dx)
                dist = dx * dx + dy * dy
                return (angle, dist)
            sorted_others = sorted(other_points, key=sort_key)
            res[x] = [start] + sorted_others
        sign = 0
        for points in res:
            cnt = list()
            for i in range(self.quan):
                p1 = points[i]
                p2 = points[(i + 1) % self.quan]
                p3 = points[(i + 2) % self.quan]

                cross = (p2.center[0] - p1.center[0]) * (p3.center[1] - p2.center[1]) - (p2.center[1] - p1.center[1]) * (p3.center[0] - p2.center[0])
                cnt.append(cross)
                if cross != 0:
                    current_sign = 1 if cross > 0 else -1
                    if sign == 0:
                        sign = current_sign
                    elif current_sign != sign:
                        return False
            if set(cnt) != {0}:
                return True
        return False







