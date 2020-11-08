#Runtime: 1916 ms, faster than 21.16% of Python3 online submissions for Escape a Large Maze.
#Memory Usage: 26.5 MB, less than 5.29% of Python3 online submissions for Escape a Large Maze.
#LC Hard
#In a 1 million by 1 million grid, the coordinates of each grid square are (x, y).

#We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

#Return true if and only if it is possible to reach the target square through a sequence of moves.

 

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], src: List[int], target: List[int]) -> bool:
        ##BFS
        if src == None or target == None:
            return False
        if len(blocked) == 0:
            return True
       
        visited = {(src[0],src[1]):True}
        visit_queue = [(src[0],src[1],0)]
        blocked_dict = {(x,y):True for x,y in blocked}
        
        #check if all squares around the target are blocks
        x,y = target[0],target[1]
        if (x-1,y) in blocked_dict and (x+1,y) in blocked_dict and (x,y-1) in blocked_dict and (x,y+1) in blocked_dict:
            return False
        
        while len(visit_queue) > 0:
            current = visit_queue.pop(0)
            #d = distance from source block
            #if we get past 200 blocked squares, we have a guarenteed escape
            x,y,d = current
            if d >= 200:
                return True
            adjacents = []
            
            #check if all possible moves are valid
            if (x-1 > 0): 
                adjacents.append((x-1,y))
            if (x+1 < 1000000):
                adjacents.append((x+1,y))
            if (y-1 > 0):
                adjacents.append((x,y-1))
            if (y+1 < 1000000):
                adjacents.append((x,y+1))
          
            for adj in adjacents:
                if adj[0] == target[0] and adj[1]== target[1]:
                    return True
              
                #check if we have visited adj square before 
                if adj not in visited:
                    #if the adj square is not in the blocked_dict
                    if adj not in blocked_dict:
                        visit_queue.append((adj[0],adj[1],d+1))
                        visited[adj] = True

        return False
    

        
