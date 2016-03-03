怎麼在readme 裡面畫流程圖?

# darts 2.0

init_funding = 1000000 #一百萬 JPY 為起始資金

rand_choose_darts_quantity = Y/N #是否以亂數決定買的數量?
rand_quantity_range_min = (int) #如果以亂數決定買的數量，設定範圍(下限)
rand_quantity_range_max = (int) #如果以亂數決定買的數量，設定範圍(上限)

not_rand_quantity = (int) #如果不是用亂數決定買的數量，那一次會買幾支?
buy_for_every_dart = (int) #每個標的用多少金額購買

duration = 0 or 1 #設定起始點，如果是0，則表示程式從末開始，是第一次射飛標，或許這個名稱不用設

不確定要更新什麼

可能要連續開三個不同的核心飛鏢

1.5darts (預設，射5支飛標)
2.Ndarts (自定射幾支飛標)
3.Random (輸入亂數範圍)

但pandas的格式怎樣能被random吃?

這要研究一下

-----------------------------------以下是舊的版本-------------------------------------------------
# dart
If we choose stock market's targets like shooting darts. What will the benefit of results? Let's make a evidence to prove it.

Execute shoot_dart.py, it will pick up 5 targets randomly.

只要執行 shoot_dart.py 他就會從目標來源隨機挑出五個標的。

股市中有個觀念是這樣的，如果在牛市的市場下，有三組成員用各字的方法去挑選標的。

A 用技術分析

B 用基本分析

C 帶了一隻猴子，讓他去射飛標，射到哪隻就選哪隻

以結果來說，C選出來的績效，可能會高過A 和 B。當然，就像喝牛奶不用買一頭牛在家裡，我也不用真的去抓一隻猴子去教他射飛標，寫一個亂數程式，並紀錄結果，來看看會怎樣

計算方法：
每天只挑選一次，每次只挑五隻標的，使用的是Python 內建的 random 函數。
挑完後，設定為隔天的開盤價買入，收盤價賣出。
並把這損益計算出來後，寫入 (benefit.txt)

