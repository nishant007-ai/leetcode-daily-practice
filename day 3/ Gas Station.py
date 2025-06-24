
134. Gas Station






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


