-- ==================================================
-- rag_db 初期データ
-- ==================================================

-- 文書データを追加する
INSERT INTO documents (
    title,
    file_name,
    file_type
)
VALUES (
    'PostgreSQL Guide',
    'postgresql_guide.pdf',
    'pdf'
);

-- 上で追加した文書に対応するチャンクを追加する
INSERT INTO chunks (
    document_id,
    chunk_number,
    content
)
SELECT
    document_id,
    1,
    'PostgreSQL is a relational database management system.'
FROM documents
WHERE file_name = 'postgresql_guide.pdf';

INSERT INTO chunks (
    document_id,
    chunk_number,
    content
)
SELECT
    document_id,
    2,
    'Python can connect to PostgreSQL using Psycopg.'
FROM documents
WHERE file_name = 'postgresql_guide.pdf';