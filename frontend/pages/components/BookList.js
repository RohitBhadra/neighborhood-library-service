export default function BookList({ borrowings }) {
  return (
    <ul>
      {borrowings.map(b => (
        <li key={b.id}>
          {b.book.title} by {b.book.author}
        </li>
      ))}
    </ul>
  );
}
