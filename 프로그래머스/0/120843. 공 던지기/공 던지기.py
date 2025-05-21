def solution(numbers, k):
    answer = 0
    seq = 2*(k-1)
    if len(numbers) <= seq :
        list_len = (seq//len(numbers)) + 1
        numbers = numbers * list_len
        
    return numbers[seq]