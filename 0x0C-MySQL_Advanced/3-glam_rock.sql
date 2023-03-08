-- Lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, COALESCE(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE BINARY style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
