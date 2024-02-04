class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        result = self.current
        self.current += 2
        return result

class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        result = self.current
        self.current += 2
        return result

def print_from_stream(n, stream):
    stream.__init__()  # Reset the stream to its initial state
    for _ in range(n):
        print(stream.get_next())

# Number of queries
q = int(input())

# Process each query
for _ in range(q):
    stream_name, n = input().split()
    n = int(n)

    if stream_name == "even":
        print_from_stream(n, EvenStream())
    elif stream_name == "odd":
        print_from_stream(n, OddStream())
