'''
http://strategywincraps.blogspot.com/2008/12/craps.html
http://www.lagoon-casino.com/chinese/craps.html
如第一次掷骰，两粒骰子的总点数为七或十一，博彩者赢，
如出现二、三或十二任一点数，则输；
但如出现四、五、六、八、九或十的点数，博彩者须继续掷骰，
直至再次掷得四、五、六、八、九或十则为赢，但如掷出七则为输。
'''

import random

play_time = input('你需要玩几次：')
play_time = int(float(play_time))

w_time = l_time = 0
winner = []
loser = []

sum1 = sum2 = 0

def sum_craps():
  return random.randrange(1, 7) + random.randrange(1, 7)

def again():
  global l_time
  global w_time
  global sum1
  global sum2
  global winner
  global loser
  global play_time
  sum2 = sum_craps()
  if sum2 == 7:
    l_time += 1
    loser.append(play_time)
    play_time -= 1
    return False
  elif sum2 == sum1:
    w_time += 1
    winner.append(play_time)
    play_time -= 1
    return True
  else:
    again()

def play():
  global l_time
  global w_time
  global sum1
  global winner
  global loser
  global play_time
  sum1 = sum_craps()
  if sum1 == 7 or sum1 == 11:
    w_time += 1
    winner.append(play_time)
    play_time -= 1
    return True
  elif sum1 == 2 or sum1 == 3 or sum1 == 12:
    l_time += 1
    loser.append(play_time)
    play_time -= 1
    return False
  else:
    again()

if __name__ == '__main__':
  while play_time > 0:
    play()

print('w_time: %d, winner: %s' % (w_time, winner))
print('l_time: %d, loser: %s' % (l_time, loser))
  