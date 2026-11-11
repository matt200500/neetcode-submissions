class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_total = 0
        bob_total = 0
        for index in range(len(colors)):
            if index == 0 or index == len(colors)-1:
                pass
            elif colors[index-1] == colors[index] and colors[index+1] == colors[index]:
                if colors[index] == "A":
                    alice_total += 1
                else:
                    bob_total += 1
        if alice_total > bob_total:
            return True
        return False



                
            

        
