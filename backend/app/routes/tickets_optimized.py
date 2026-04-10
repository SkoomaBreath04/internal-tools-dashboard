"""Optimized ticket query — JOIN replaces N+1."""
OPTIMIZED_QUERY = """
SELECT t.*, COALESCE(c.cnt, 0) as comment_count
FROM tickets t
LEFT JOIN (
    SELECT ticket_id, COUNT(*) cnt FROM ticket_comments GROUP BY ticket_id
) c ON t.id = c.ticket_id
ORDER BY t.created_at DESC
"""
