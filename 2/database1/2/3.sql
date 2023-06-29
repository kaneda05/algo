-- データの更新
UPDATE prefectures SET name = '茨城県' WHERE name = '茨木県';
UPDATE prefectures SET name = '鳥取県' WHERE name = '取鳥県';
-- テーブルの情報を表示
SELECT * FROM prefectures;