# 百钱百鸡
# 公鸡：5 文钱一只；母鸡：3 文钱一只；鸡仔一文钱 3 只
# 5x + 3y + (100 - x - y) / 3 = 100

allGroup = []
def hundred_money_hundred_chicken():
  max_x = 20
  max_y = 33
  # x = 1
  # y = 1
  # z = 100 - x - y
  for x in range(0, max_x + 1):
    # x = int(x, 10)
    for y in range(0, max_y + 1):
      # y = int(y, 10)
      z = 100 - x - y
      if 5 * x + 3 * y + (100 - x - y) / 3 == 100:
        print(x, y, z)
pass

hundred_money_hundred_chicken()