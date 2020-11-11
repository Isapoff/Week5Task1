# import json
# task 1
# with open('task1.txt') as f:
#     marks_sum = 0
#     marks_count = 0
#     for i in f.readlines():
#         i = i.rstrip('\n')
#         marks_count += 1
#         mark = int(i[-1])
#         marks_sum += mark
#         if mark < 3:
#             print("Student whose grade less than 3: ", i[:-1])
# print("Avarage grade in the class: ", marks_sum / marks_count)

# f.close()


# task 2
# file = open('test.txt', mode = 'w')
# while True:
#     s = input()
#     if s == '':
#         break
#     f = file.write(s +'\n')
# file.close()

# task 3
#1
# file = open('test.txt', 'r')
# print(len(set(open('test.txt').read().split())))  # кол-во слов
# print(len(file.read()))                           # кол-во символов
# print(sum(1 for line in open('test.txt')))        # кол-во строк 
# file.close()

#2
# lines = 0
# words = 0
# char = 0
# file = open('test.txt', 'r')
# for i in file:
#     wrd = i.split()
#     lines += 1
#     words += len(wrd)
#     chars += len(i)
# print(lines)
# print(words)
# print(char)

# task 4
# with open('nums.txt') as file:
#     s = file.readline()
# s = list(map(int, s.split()))
# print(sum(s))
# file.close()


# task 5
# with open('nums.txt') as file:
#     s = file.readline()
# s = list(map(int, s.split()))
# with open('output.txt', mode = 'w+') as f:
#     f.write(str(s))
# print(sum(s*2))


# task 6
# file1 = open('nums.txt')
# s = file1.readline()
# s = list(map(int, s.split()))
# print(min(s), max(s))
# file2 = open('output.txt', 'w')
# file2.write(file1.read())    

# file1.close()
# file2.close()


# task 7
# file1 = open('input.txt')
# s = file1.read().split()
# s2 = sorted(s, key = lambda x: x[::1])
# file1.close
# file2 = open('output.txt', mode = 'w')
# for i in s2:
#     file2.write(i+' ')
# file2.close()


# task 8
# with open('task8.txt') as file:
#     for i in file:
#         i = input()
#         if i == 'Hello':
#             print(file.read())
#             a = input('Введите жалобу: ')
# file2 = input('Куда отправить жалобу: ')
# f = open(file2, 'w')
# f.write(file2)

# task 8
# user = '{"name": "John", "age": 30, "city": "New York"}'
# a = json.loads(user)
# print(a['age'])


# task 9
# user = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
#     }

# json_obj = json.dumps(user)
# print(json_obj)






