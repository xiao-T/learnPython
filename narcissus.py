# 寻找水仙花数

def narcissistic_number(num):
  num = str(num)
  length = len(num)
  if length != 3:
    print(num, '不是水仙花数')
  else:
    num_sum = int(num[0]) ** length + int(num[1]) ** length + int(num[2]) ** length
    if int(num) == num_sum:
      print(num, '是水仙花数')
pass

max_num = input('输入最大范围：')
max_num = int(float(max_num))

while max_num:
  max_num -= 1
  narcissistic_number(max_num)
# for num in range(0, max_num):
  # narcissistic_number(max_num)
