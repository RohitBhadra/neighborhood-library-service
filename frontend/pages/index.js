import { useEffect, useState } from "react";

export default function Home() {
  const [borrowings, setBorrowings] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/members/1/borrowings")
      .then(res => res.json())
      .then(data => setBorrowings(data));
  }, []);

  return (
    <div>
      <h1>Borrowed Books</h1>
      <ul>
        {borrowings.map(b => (
          <li key={b.id}>{b.book.title} by {b.book.author}</li>
        ))}
      </ul>
    </div>
  );
}
