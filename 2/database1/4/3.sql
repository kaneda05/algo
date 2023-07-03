WITH select_rank AS (
    SELECT * FROM results
    WHERE name NOT IN (
        SELECT name FROM optout
        )
)

SELECT
    ROW_NUMBER() OVER(ORDER BY score DESC, id) AS '順位',
    name AS '名前',
    score AS 'スコア'
FROM
    select_rank
