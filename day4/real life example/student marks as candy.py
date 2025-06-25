ratings = [20, 90, 80, 70, 60]


class Nishant:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)





output =[1, 2, 3, 2, 1] → 1 + 2 + 3 + 2 + 1 = 9


















