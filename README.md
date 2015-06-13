# dart
If we choose stock market's targets like shooting darts. What will the benefit of results? Let's make a evidence to prove it.

股市中有個觀念是這樣的，如果在非常牛逼的市場下，有三組成員用各字的方法去挑選標的。

A 用技術分析

B 用基本分析

C 帶了一隻猴子，讓他去射飛標，射到哪隻就選哪隻

以結果來說，C選出來的績效，可能會高過A 和 B。當然，就像喝牛奶不用買一頭牛在家裡，我也不用真的去抓一隻猴子去教他射飛標，寫一個亂數程式，並紀錄結果，來看看會怎樣

計算方法：
每天只挑選一次，每次只挑五隻標的，使用的是Python 內建的 random 函數。
挑完後，設定為隔天的開盤價買入，收盤價賣出。
並把這損益計算出來後，寫入 (benefit.txt)

