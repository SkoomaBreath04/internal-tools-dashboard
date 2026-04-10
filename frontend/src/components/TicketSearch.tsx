import React, { useState, useEffect } from 'react';
export const TicketSearch: React.FC = () => {
  const [q, setQ] = useState('');
  const [dateFrom, setDateFrom] = useState(''); // backend ignores this
  const [tickets, setTickets] = useState<any[]>([]);
  useEffect(() => {
    fetch(`/api/v1/tickets?q=${q}&date_from=${dateFrom}`).then(r=>r.json()).then(d=>setTickets(d.tickets||[]));
  }, [q, dateFrom]);
  return (<div>
    <input placeholder="Search..." value={q} onChange={e=>setQ(e.target.value)} />
    <input type="date" value={dateFrom} onChange={e=>setDateFrom(e.target.value)} />
    <table><tbody>{tickets.map((t:any)=><tr key={t.id}><td>{t.title}</td><td>{t.status}</td></tr>)}</tbody></table>
  </div>);
};
