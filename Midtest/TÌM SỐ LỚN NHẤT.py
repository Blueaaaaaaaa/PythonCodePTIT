def find_largest_number_in_string(test_cases):
    results = []
    for test in test_cases:
        max_num = 0
        current_num = 0
        for char in test:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                max_num = max(max_num, current_num)
            else:
                current_num = 0
        results.append(max_num)
    return results

# Test cases from the user's example
test_cases = ["12ab29cd19", "ab123gh456cd"]
find_largest_number_in_string(test_cases)

def initation

for i in range(5):
    