class Series:
    def __init__(self):
        self.series = []

    def generate_series(self, num_terms):
        n1, n2 = 0, 1
        if num_terms <= 0:
            print('Enter a positive integer')
        elif num_terms == 1:
            print(n1)
        else:
            self.series.append(n1)
            self.series.append(n2)
            for i in range(2, num_terms):
                nth = n1 + n2
                n1 = n2
                n2 = nth
                self.series.append(nth)

        return self.series

    # This approach avoids the need to store all
    # the terms in memory, especially for larger series
    # making the function memory efficient
    def generate_efficiently(self, num_terms):
        n1, n2 = 0, 1
        if num_terms <= 0:
            raise ValueError("Please enter a positive integer")
        if num_terms == 1:
            yield n1
        if num_terms > 1:
            yield n1
            yield n2
        for i in range(2,num_terms):
            nth = n1 + n2
            n1, n2 = n2, nth
            yield nth

