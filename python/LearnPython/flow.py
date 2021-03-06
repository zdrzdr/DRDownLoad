# coding=utf-8
scroe = 20

if scroe>=80:
    print("很好")
elif scroe>=60:
    print("及格")
elif scroe>=30:
    print("不及格")
else:
    print("很差")


def add_end(L=None):
    if L is None:
        L = []
        L.append('END')
        return L


print(add_end())
print(add_end())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1,2,3]))
print(calc([1,3,5,7]))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2))
print(calc())

nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*nums))

def person1(name, age, **kw):
    print('name:',name,'age:',age, 'other:',kw)

person1('Michael',30)

person1('Bob',35,city='Beijing')
person1('Adam',45,gender='M', job='Engineer')


extra = {'city':'Beijing','job':'Engineer'}
person1('Jack',24,**extra)


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass

    print('name:',name,'age:',age,'other:',kw)



def f1(a, b, c=0, *args, **kw):
    print('a=',a, 'b=',b, 'c=',c, 'args = ',args,'kw = ',kw)


def f2(a, b, c=0, *,d, **kw):
        print('a=', a, 'b=',b, 'c =',c,'d =',d,'kw = ',kw)


print(f1(1,2))

print(f1(1,2,c=3))

print(f1(1,2,3,'a','b'))

print(f1(1,2,3, 'a', 'b', x=99))

print(f2(1,2, d=99, ext=None))

args = (1,2,3,4)

kw = {'d':99,'x':'#'}

print(f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))



def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(1))

print(fact(5))

print(fact(100))


# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return  product
    return fact_iter(num - 1,num *product)

print(fact(5))



L = ['Michael','Sarah','Tracy','Bob','Jack']


print(L[:3])
print(L[-2:])
print(L[-2:-1])


L = list(range(100))

print(L[:10])

print(L[-10:])
print(L[10:20])

print(L[:10:2])

print(L[::5])

print(L[:])

print((0,1,2,3,4,5)[:3])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k,v)

from collections import Iterable
print(isinstance('abc',Iterable))


print(isinstance([1,2,3],Iterable))


print(isinstance(123,Iterable))


for i, value in enumerate(['A','B','C']):
    print(i,value)

for x, y in [(1,1), (2,4), (3,9)]:
    print(x, y)

print([x * x for x in range(1,11)])


print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])


import os

print([d for d in os.listdir('.')])
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
    print(k, '=',v)

print([k + '=' + v for k, v in d.items()])


L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])



L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)

g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(f)


for n in fib(6):
    print(n)

g = fib(6)

while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break






def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)



o = odd()
print(next(o))
print(next(o))
print(next(o))
print(next(o))
print(next(o))







