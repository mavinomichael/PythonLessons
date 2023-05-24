from BeginnerLessons.Fibonacci.generate import Series

fibonacci = Series()

# non-efficient generator
def generate_v1(num_terms):
    print(fibonacci.generate_series(num_terms))

# more efficient generator
def generate_v2(num_terms):
    generator = fibonacci.generate_efficiently(num_terms)
    for value in generator:
        print(value)