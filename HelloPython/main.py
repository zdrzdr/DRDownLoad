print("Hello pyton")
print('''line1
line2
line3''')
print(r'\\\t\\')
print(10//3)
print(ord('A'))
print(chr(25991))
x = b'ABC'
print('Hello, %s' % 'world')
print('Hi, %s you have $%d.' % ('Michale', 100000))
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
classmethod = ['Michael', 'Bob', 'Tracy']
print(classmethod)
print(len(classmethod))
print(classmethod[0])
print(classmethod[-1])
classmethod.insert(1, 'Jack')
print(classmethod)
print(classmethod.pop())
print(classmethod)
print(classmethod.pop(1))
print(classmethod)
classmethod[1] = 'Sarah'
print(classmethod)

L = ['Apple', 123, True]
print(L)
s = ['python', 'java',['asp','php'],'scheme']
print(len(s))

L = []
print(len(L))


classmethod = ('Michael', 'Bob', 'Tracy')

print(classmethod)
t = (1)
print(t)

t = (1,)
print(t)

# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = ('a','b', ['A','B'])
t[2][1] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple','Google', 'Microsoft'],
    ['Java', 'Python','Ruby','PHP',
     ['Adam','Bart','Lisa']]
]

print(L[0][0])


age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if x:
    print('True')


s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

age = int(input('Input your age: '))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x

print(sum)


print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


for i in ['Bart','Lisa', 'Adam']:
    print('Hello, %s!' % i)


# while 1:
    # print(9)


names = ['Michel','Bob','Tracy']
scores = [95,75,85]

d = {'Michael': 95, 'Bob': 75}
print('Thomas' in d)

print(d.get('Thomas'))
print(d.get('Thomas',-1))

print(d.pop('Bob'))

key = [1,2,3]
# d[key] = 'a list'
# print(d)

s = set([1,2,3])
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)
print(s1 | s2)


t = [1]
print(set(t))
