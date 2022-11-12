import random
from time import sleep

EMPTY = 0
class player:
    rect_p = False
    init_x = 0
    init_y = 0
    rect_x = 0
    rect_y = 0
    cnt = 1
    def __init__(self):
        pass

    def move(self,B,N,cur_x,cur_y):
        
        if self.cnt > 0:
            self.fn(B, N, cur_x, cur_y)
            self.cnt = 0

        if cur_x == self.init_x and cur_y == self.init_y:
            self.fn(B, N, cur_x, cur_y)

        if self.rect_p:
            if cur_x == self.rect_x and cur_y == self.rect_y:
                self.rect_x = self.init_x
                self.rect_y = self.init_y
        
            if cur_y != self.rect_y:
                if self.rect_y < cur_y and B[cur_x][cur_y-1] == 0:
                    return (0, -1)
                elif self.rect_y > cur_y and B[cur_x][cur_y+1] == 0:
                    return (0, 1)
            elif cur_x != self.rect_x:
                if self.rect_x < cur_x and B[cur_x-1][cur_y] == 0:
                    return (-1, 0)
                elif self.rect_x > cur_x and B[cur_x+1][cur_y] == 0:
                    return (1, 0)
            
            self.rect_p = False
            self.cnt = 1

        if B[(cur_x+1)%N][cur_y] == 0:
            return (1,0)
        elif B[cur_x][(cur_y+1)%N] == 0:
            return (0,1)
        elif B[cur_x][(cur_y-1)%N] == 0:
            return (0,-1)
        elif B[(cur_x-1)%N][cur_y] == 0:
            return (-1,0)
        
        return self.closest_empty(B, N, cur_x, cur_y)

    def fn(self, B, N, cur_x, cur_y):
        self.init_x, self.init_y = cur_x, cur_y
        self.rect_p = True
        for i in range(N):
            for j in range(N):
                if B[i][j] == 2:
                    if i < cur_x-6:
                        self.rect_x = cur_x - 5
                    elif i<cur_x:
                        self.rect_x = min(N-1, cur_x+5)
                    elif i>cur_x+6:
                        self.rect_x = cur_x + 5
                    else:
                        self.rect_x = max(0, cur_x-5)
                    
                    if j < cur_y-6:
                        self.rect_y = cur_y-5
                    elif j<cur_y:
                        self.rect_y = min(N-1, cur_y+5)
                    elif j>cur_y+6:
                        self.rect_y = cur_y+5
                    else:
                        self.rect_y = max(0, cur_y-5)

    def closest_empty(self,B,N,cur_x,cur_y):
        dis=2*N+1
        best = {"x":cur_x,"y":cur_y}
        for i in range(N):
            for j in range(N):
                if B[i][j] == EMPTY:
                    dx = min ( abs(cur_x - i) , N - abs(cur_x - i) )
                    dy = min ( abs(cur_y - j) , N - abs(cur_y - j) )
                    cur_dis = dx+dy
                    if cur_dis < dis:
                        dis = cur_dis
                        best["x"] = i
                        best["y"] = j

        # Pick the direction to go in

        if best["y"] > cur_y:
            if best["y"]-cur_y < N/2:
                return (0,1)
            else:
                return (0,-1)


        if best["y"] < cur_y:
            if cur_y-best["y"] < N/2:
                return (0,-1)
            else:
                return (0,1)


        if best["x"] > cur_x:
            if best["x"]-cur_x < N/2:
                return (1,0)
            else:
                return (-1,0)

        if best["x"] < cur_x:
            if cur_x-best["x"] < N/2:
                return (-1,0)
            else:
                return (1,0)
        

        return (0,0)
    
