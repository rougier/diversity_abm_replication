import httpimport
url = "https://gist.githubusercontent.com/LukasWallrich/74df5b2ec209c34166bab9e8cb46a279/raw/56a85f6eccda9fc92f3dd73e151df8f0ec06aadf"

with httpimport.remote_repo(["HP_model"], url):
    from HP_model import HPProblem
    
import pandas as pd
import numpy as np

class GProblem(HPProblem):
    def __init__(self, n, k, l, N_agents, smoothness, seed = None, schedule = "base"):
        self.draw_G_solution(n, smoothness)
        super().__init__(n, k, l, N_agents, seed, schedule)

    def draw_solution(self, n):
        pass

    def draw_G_solution(self, n, smoothness):
        if (smoothness == 0):
            super().draw_solution(n)
        else:    
            i = 0
            solution = pd.Series(np.nan for x in range(n))
            while(i < n):
                solution[i] = self.random.uniform(0, 100)
                i += 1+self.random.randrange(2*smoothness)
            if (pd.isna(solution[n-1])):
                solution[n] = solution[0]     
            solution = solution.interpolate().tolist()    
            if (len(solution) > n):
                solution.pop()
            self.solution = solution              

