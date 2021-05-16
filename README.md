# Vocab Helper - 單字小幫手

## 動機
每次準備高中英文「克漏字單字」考試時，有許多單字散落在各式英文教材中

單字缺乏系統性的整理，準備起來相當困難

為了有效提升記憶各英文字首所對應的單字

開發了此Python Script以將單字按字首排列

## 使用方法
將考試範圍內的單字整理成一份txt檔案

指定其路徑，並執行以下指令

```bash
$ python vocab_words_helper.py <input_file_path> <output_file_path>
```

排序過後的單字會被儲存在 `<output_file_path>`


## 成果展現
詳見 [排序前的文檔](vocab_not_sorted.txt) 和 [排序後的文檔](vocab_sorted.txt)

可以看見單字以chronological order排序

大大幫助我準備克漏字考試，以後看到 `C_____` 的問題更能快速回想C開頭的單字
