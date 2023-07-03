WITH rank_select AS(
    SELECT email, game_id, score FROM results
    EXCEPT
    SELECT email. game_id, score FROM optout
)

SELECT email FROM rank_select
GROUP BY email
ORDER BY SUM(score) DESC
LIMIT 10;