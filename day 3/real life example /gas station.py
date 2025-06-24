Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]




class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total += gain
            tank += gain

            if tank < 0:
                start = i + 1
                tank = 0
                

        return start if total >= 0 else -1


 
output = 3