SELECT
    *
FROM
    prefectures
WHERE population > (SELECT name FROM prefectures
                    WHERE name = '東京都')/2
ORDER BY
    population DESC;