WITH
    ranking
AS(
    SELECT
        ROW_NUMBER() OVER(ORDER BY score DESC, id) AS '順位',
        name AS '名前',
        score AS 'スコア'
    FROM
        results
)

SELECT * FROM ranking
WHERE `順位` IN (1, 2, 3, 10)