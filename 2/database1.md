## データベース入門(1)
|データの表示|[1](https://github.com/kaneda05/algo/blob/main/2/database1/1/1.sql)|[2](https://github.com/kaneda05/algo/blob/main/2/database1/1/12.sql)|[3](https://github.com/kaneda05/algo/blob/main/2/database1/1/3.sql)|[4](https://github.com/kaneda05/algo/blob/main/2/database1/1/4.sql)|[5](https://github.com/kaneda05/algo/blob/main/2/database1/1/5.sql)|[6](https://github.com/kaneda05/algo/blob/main/2/database1/1/6.sql)|[7](https://github.com/kaneda05/algo/blob/main/2/database1/1/7.sql)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

|データの集計と編集|[1](https://github.com/kaneda05/algo/blob/main/2/database1/2/1.sql)|[2](https://github.com/kaneda05/algo/blob/main/2/database1/2/2.sql)|[3](https://github.com/kaneda05/algo/blob/main/2/database1/2/3.sql)|[4](https://github.com/kaneda05/algo/blob/main/2/database1/2/4.sql)|[5](https://github.com/kaneda05/algo/blob/main/2/database1/2/5.sql)|[6](https://github.com/kaneda05/algo/blob/main/2/database1/2/6.sql)|[7](https://github.com/kaneda05/algo/blob/main/2/database1/2/7.sql)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

- HAVINGについて


[【SQL】HAVING句の使い方を１分でわかりやすく解説](https://it-biz.online/it-skills/having/#toc1)


簡潔にまとめるとGROUP BYによってグループ化されたデータに対して条件を付け加えることができる。
また、合わせてグループ化する前に条件を付け加えたいならばWHEREを使えば良い。
- <strong>WHEREとHAVINGの違いについて明確に</strong>

HAVINGを使用した問題は「**データの集計と編集の6**」

|基本的な操作|[1](https://github.com/kaneda05/algo/blob/main/2/database1/3/1.sql)|[2](https://github.com/kaneda05/algo/blob/main/2/database1/3/2.sql)|[3](https://github.com/kaneda05/algo/blob/main/2/database1/3/3.sql)|[4](https://github.com/kaneda05/algo/blob/main/2/database1/3/4.sql)|[5](https://github.com/kaneda05/algo/blob/main/2/database1/3/5.sql)|[6](https://github.com/kaneda05/algo/blob/main/2/database1/3/6.sql)|[7](https://github.com/kaneda05/algo/blob/main/2/database1/3/7.sql)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

|練習問題|[1](https://github.com/kaneda05/algo/blob/main/2/database1/4/1.sql)|[2](https://github.com/kaneda05/algo/blob/main/2/database1/4/2.sql)|[3](https://github.com/kaneda05/algo/blob/main/2/database1/4/3.sql)|[4](https://github.com/kaneda05/algo/blob/main/2/database1/4/4.sql)|[5](https://github.com/kaneda05/algo/blob/main/2/database1/4/5.sql)|[6](https://github.com/kaneda05/algo/blob/main/2/database1/4/6.sql)|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

- ORVERについて
[【SQL】分析関数のOVER句を使ってデータを集計する](https://z-marketing.net/sql-over/)

分析関数と集約関数について
基本フォーマット OVER(PARTITION BY カラム名 ORDER BY カラム名)



- ROW_NUMBER()について
[【SQL】連番を振るROW_NUMBER関数を解説！一番よく使う順位付け関数をマスターしよう](https://style.potepan.com/articles/23566.html)