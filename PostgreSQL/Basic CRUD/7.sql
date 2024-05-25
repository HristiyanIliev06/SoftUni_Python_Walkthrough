SELECT a."id", a."number"|| ' ' || a."street" AS address, a."city_id"
FROM addresses AS a
WHERE a."id">=20;