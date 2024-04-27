from AIGamePlatform import OthelloPlatform
from othello.bots.MinMax import BOT

app=OthelloPlatform() # 和平台建立WebSocket連線
bot=BOT(10) # 建立隨機bot

@app.competition(competition_id='111人工智慧導論 初賽6') # 競賽ID
def _callback_(board, color): # 當需要走步會收到盤面及我方棋種
    return bot.getAction(board, color)