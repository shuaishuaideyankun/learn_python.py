# eval()函数的使用
s='3.9+6'
print(s,type(s))
x=eval(s)
print(x,type(x))


# eval()函数经常和input()函数一起使用,用来获取用户输入的数值型
age=eval(input('请输入您的年龄：'))
print(age,type(age))


