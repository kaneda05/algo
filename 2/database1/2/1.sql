SELECT * FROM prefectures 
WHERE name in (SELECT * FROM kanto_regions);