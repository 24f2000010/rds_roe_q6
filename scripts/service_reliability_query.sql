-- Service Reliability Analysis for payment-processor in US-EAST-1 during 2024-08
-- DuckDB SQL Query

WITH month_boundaries AS (
    -- Define the start and end of the target month (2024-08)
    SELECT 
        TIMESTAMP '2024-08-01 00:00:00' AS month_start,
        TIMESTAMP '2024-09-01 00:00:00' AS month_end
),
health_metrics AS (
    -- Calculate uptime percentage and average response time from health checks
    SELECT 
        COUNT(*) AS total_checks,
        SUM(CASE WHEN is_available = true THEN 1 ELSE 0 END) AS available_checks,
        AVG(CASE WHEN is_available = true THEN response_time_ms ELSE NULL END) AS avg_response_time
    FROM service_health, month_boundaries
    WHERE service_id = 'payment-processor'
        AND datacenter = 'US-EAST-1'
        AND check_timestamp >= month_boundaries.month_start
        AND check_timestamp < month_boundaries.month_end
),
incident_metrics AS (
    -- Calculate total incidents and downtime minutes
    -- Only count the portion of incidents that falls within the target month
    SELECT 
        COUNT(*) AS total_incidents,
        SUM(
            EXTRACT(EPOCH FROM (
                LEAST(incident_end, month_boundaries.month_end) - 
                GREATEST(incident_start, month_boundaries.month_start)
            )) / 60.0
        ) AS total_downtime_minutes
    FROM service_incidents, month_boundaries
    WHERE service_id = 'payment-processor'
        AND datacenter = 'US-EAST-1'
        AND incident_start < month_boundaries.month_end
        AND incident_end > month_boundaries.month_start
)
SELECT 
    ROUND(
        (CAST(health_metrics.available_checks AS DOUBLE) / NULLIF(health_metrics.total_checks, 0)) * 100.0,
        2
    ) AS uptime_percentage,
    ROUND(COALESCE(health_metrics.avg_response_time, 0.0), 2) AS avg_response_time,
    COALESCE(incident_metrics.total_incidents, 0) AS total_incidents,
    ROUND(COALESCE(incident_metrics.total_downtime_minutes, 0.0), 2) AS total_downtime_minutes
FROM health_metrics
CROSS JOIN incident_metrics;

