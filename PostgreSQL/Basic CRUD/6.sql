SELECT a."number"|| ' ' || a."street" AS address, a."city_id"
FROM addresses AS a
WHERE  a."city_id">0 AND a."city_id"%2=0
ORDER BY a."city_id";