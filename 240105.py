# m = [1, 2, 3, 'apple', 'banana']

# for index, s in enumerate(m):
#     print(index,':',s)

#--------------split------------------
# data = "John,30,Engineer\nAlice,25,Designer\nBob,22,Artist"
# lines = data.split("\n")

# for line in lines:
#     fields = line.split(",")
#     print("Name:", fields[0], "Age:", fields[1], "Occupation:", fields[2])

#--------------join------------------
# words = ['Hello', 'world', 'this', 'is', 'a', 'test']
# sentence = ' '.join(words)
# print(sentence)

# sen = 'Geeks for Geeks'
# out = sen.split(' ')
# print(out)
# out2 = '-'.join(out)
# print(out2)

#--------------list comprehension------------------
# 별 = ['☆ '*n for n in range(1,5) if n%2==1]
# print(별)

# lis = [n**2 for n in range(1,21) if n%3==0]
# print(lis)

# inp = [i for i in range(1,6)]
# out = [inp[j]**2 for j in range(len(inp))]
# print(out)

# city = ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
# out2 = [city[i] for i in range(len(city)) if city[i][0]=='S']
# print(out2)

#--------------enumerate------------------

# fruits = ['apple','banana','cherry','strawberry']
# for index, fruit in enumerate(fruits,start=1): #index 1부터 시작
#     print('{} : {}'.format(index,fruit))

# in1 = ['a','b','c']
# for index, name in enumerate(in1):
#     print('fruit{} name is {}'.format(index,name))

# in2 = ['a','b','c']
# for i in range(len(in2)):
#     print('fruit%d name is %s'%(i,in2[i]))

#---------------zip-----------------

# names = ['John','Jane','Doe']
# ages = [25,30,35]

# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")

# d=dict(zip(names,ages))
# print(d)

# name = ['M','N','S','A']
# roll_no = [4,1,3,2]

# result = zip(name,roll_no)
# result_list = list(result)
# print(result_list)

# names = ['M', 'R', 'C']
# ages = [24, 50, 18]

# z = zip(names, ages)
# for idx, att in enumerate(z):
#     print(idx, *att)

#---------------lambda-----------------
    
# double = lambda x: x*2
# print(double(5))


# plus = lambda x,y : x+y

# print(plus(5,5))

# num1 = [4,5,6]
# num2 = [5,6,7]

# a,b,c = map(int,input().split())
# abc_list = [a,b,c]

# if (a==b | b==c | c==a):
# 	print('wrong value')
# else:
#     print(sorted(abc_list,reverse=True))
#     abc_list.sort()
    
sec = int(input())

hours = sec//3600
minutes = (sec%3600)//60
seconds = sec - 3600*hours - 60 * minutes

print('{}시 {}분 {}초'.format(hours,minutes,seconds))