""" to generate large strings/list/methods using multiple methods """


large_list = [i for i in range(1000000)]  # 1 million integers

large_list = list(range(1000000))  # 1 million integers

small_list = [1, 2, 3, 4, 5]
large_list = small_list * 200000  # Repeat small list 200,000 times to get 1 million elements

# Test with a list of 1 million repeated integers
large_list2 = [1] * 1000000