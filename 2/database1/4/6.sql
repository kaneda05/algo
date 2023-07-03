WITH 
    ranking
AS(
    SELECT
        name AS '名前',
        score AS 'スコア'
    FROM
        results
    WHERE
        score = (
            SELECT MAX(score)
            FROM results AS res2
            WHERE res2.name = results.name
        )
    GROUP BY
        name
    ORDER BY 
        score DESC, id
)

SELECT
    ROW_NUMBER() OVER() AS '順位',
    *
FROM
    ranking
