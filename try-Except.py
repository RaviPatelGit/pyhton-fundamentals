# https://www.youtube.com/watch?v=NIWwJbo-9_8
# Python Tutorial: Using Try/Except Blocks for Error Handling

try:

    f = open('context--manager.py')

except FileNotFoundError as e:
    print(e)

else:
    print(f.read())
finally:
    print('text in finally')

# f = open('context--manager.py')
