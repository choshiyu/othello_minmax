from othello.OthelloGame import OthelloGame
from othello.bots import MinMax
import time

start = time.time()

game = OthelloGame(10)
game.play(MinMax.BOT(10),MinMax.BOT(10))

end = time.time()
print("執行時間：%f 秒" % (end - start))