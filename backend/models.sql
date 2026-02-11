CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  published_year INT,
  isbn VARCHAR(20) UNIQUE,
  available BOOLEAN DEFAULT TRUE
);

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone VARCHAR(20),
  address TEXT
);

CREATE TABLE borrowings (
  id SERIAL PRIMARY KEY,
  book_id INT REFERENCES books(id),
  member_id INT REFERENCES members(id),
  borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  due_date TIMESTAMP,
  returned_at TIMESTAMP
);
