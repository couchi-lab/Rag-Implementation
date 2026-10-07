-- ==================================================
-- rag_db データベーススキーマ
-- ==================================================
--
-- documents 1 --- N chunks
--
-- 1つの文書に対して、複数のチャンクを保存する。
-- ==================================================


-- 文書全体の情報を保存するテーブル
CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(20) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- 文書を分割したテキストを保存するテーブル
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    document_id INTEGER NOT NULL,
    chunk_number INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_chunks_document
        FOREIGN KEY (document_id)
        REFERENCES documents(document_id)
        ON DELETE CASCADE,

    CONSTRAINT uq_document_chunk
        UNIQUE (document_id, chunk_number),

    CONSTRAINT chk_chunk_number
        CHECK (chunk_number >= 1)
);