SELECT
    country,
    COUNT(*) as total_users,
    MAX(created_at) as last_signup
FROM raw_users
GROUP BY country
ORDER BY total_users DESC