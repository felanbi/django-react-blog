import React, { useEffect, useState } from "react";
import Event from "../components/Event/Event";

const Events = ({ jwtToken }) => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await fetch("/api/events/");
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setEvents(data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchEvents();
  }, []);

  return events.map((event) => <Event key={event.id} {...event} />);
};

export default Events;
