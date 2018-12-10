class Solution:
    
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        
        def findWords(self, board, words):
            result=[]
            final_output=[]
            letter=0
            index_adj = [[0,1],[1,0],[0,-1],[-1,0]]
            
            def look_adj(i,j,letter):
                for row, col in index_adj:
                    try:
                        if word[letter]==board[i+row][j+col]:
                            result.append(word[letter])

                            if len(result)==len(word): 
                                str1 = ''.join(result)
                                final_output.append(str1)
                            else:
                                look_adj(i+row, j+col, letter+1)

                    except:
                        continue

            for word in words:
                result=[]
                for i in range(0,len(board)):
                    for j in range(0, len(board[i])):

                        letter=0
                        if board[i][j]==word[0]:
                            if word[0] not in result:
                                result.append(word[0])
                                if len(result)==len(word): 
                                    str1 = ''.join(result)
                                    final_output.append(str1)
                            letter = letter+1
                            look_adj(i,j,letter)


            return final_output
       
         
                
    

    
