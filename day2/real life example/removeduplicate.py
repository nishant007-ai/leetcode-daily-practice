
# Example usage
reviews = [
    "Great product!",
    "Great product!",
    "Great product!",
    "Could be better",
    "Could be better",
    "Could be better",
    "Excellent!",
    "Excellent!"
]

class ReviewFilter:
    def filter_reviews(self, reviews):
        if len(reviews) < 2:
            return reviews

        k = 2
        for i in range(2, len(reviews)):
            if reviews[i] != reviews[k - 2]:
                reviews[k] = reviews[i]
                k += 1

        return reviews[:k]
    
    

    Filtered Reviews:
['Great product!', 'Great product!', 'Could be better', 'Could be better', 'Excellent!', 'Excellent!']
