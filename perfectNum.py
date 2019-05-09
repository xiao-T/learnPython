# 寻找完全数

max_num = input('请输入最大范围: ')
max_num = int(float(max_num))

def perfect_num(num):
  if num == 1:
    return False
  else:
    num_sum = 0
    for i in range(1, num + 1):
      if num % i == 0 and i != num:
        num_sum += i
    if num_sum == num:
      print('%d 是完全数' % num)
pass

while max_num:
  perfect_num(max_num)
  max_num -= 1
  pass
