
file = open('example.txt', 'r')
try:
    file = open('example.txt', 'r')
    print(file.read())
except FileNotFoundError as f:
    print(f)
finally:
    if file and not file.closed:
        file.close()

with open('example.txt', 'r') as file:
    print(file.read())


# class ContextManager:
#     def __init__(self):
#         print('Init method called')
#
#     def __enter__(self):
#         print('Entering method')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exiting method')
#
#
# with ContextManager() as file:
#     print('With block statement')




# class ContextManager2:
#     def __init__(self, file, mode='r'):
#         self.file = file
#         self.mode = mode
#
#     def __enter__(self):
#         print('Entering context manager')
#         self.file = open(self.file, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exiting context manager')
#         if self.file and not self.file.closed:
#             self.file.close()


# with OpenContextManager('example.txt', 'w') as file:
#     file.write('Hello World 1\n')
#     file.write('Hello Guys 2\n')
#     file.write('Hello Student 3')
#     file.write('Hello Person 4')