ALTER TABLE book
    ADD COLUMN fk_publisher_id integer;

ALTER TABLE book
    ADD CONSTRAINT fk_book_publisher
        FOREIGN KEY (fk_publisher_id)
            REFERENCES publisher (publisher_id)