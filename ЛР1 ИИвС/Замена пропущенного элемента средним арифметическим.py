numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count_number = len(numbers)
numbers[4] = 0
numbers[4] = sum(numbers) / count_number

print("Измененный список:", numbers)
