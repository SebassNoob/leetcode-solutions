class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check 3x3 + hor
        check_3x3 =[[],[],[],[],[],[],[],[],[]]
        def check_small(coord: tuple)-> int:
            i,j = coord
           
            
            if i<3:
                return 0 + j//3
            if 3<=i<6:
                return 3 + j//3
            if 6<=i<9:
                return 6 + j//3
        
        

        for i,arr in enumerate(board):
            check_hor=[]
            for j in range(len(arr)): 
                if board[i][j] not in check_hor and board[i][j] !=".":
                   check_hor.append(board[i][j])
                elif board[i][j] ==".":
                    continue
                else: return False

                if board[i][j] not in check_3x3[check_small((i,j))] and board[i][j] !=".":
                   check_3x3[check_small((i,j))].append(board[i][j])
                elif board[i][j] ==".":

                    continue
                else: 
                    
                    return False
                
        

                
                

        check_vert =[[],[],[],[],[],[],[],[],[]]
        for i,arr in enumerate(board):
            for j in range(len(arr)): 
                if board[i][j] not in check_vert[j] and board[i][j] !=".":
                   check_vert[j].append(board[i][j])
                elif board[i][j] ==".":
                    continue
                else: return False
           
        

        return True

                
                
            
