-- Ranks country of origins by the number of non-unique fans
SELECT `band_name`,
		COALESCE(split, 2020) - formed as lifespan FROM metal_bands
FROM `metal_bands`
WHERE style LIKE '%Glam rock%';
ORDER BY `lifespan` DESC;
