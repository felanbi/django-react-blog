import React, { useEffect, useState } from "react";
import Article from "../components/Article/Article";

const Articles = ({ jwtToken }) => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch("/api/articles/", {
          method: "GET",
          headers: {
            Authorization: `Bearer ${jwtToken}`,
          },
          credentials: "include",
        });
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setArticles(data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchArticles();
  }, []);

  return <>
  {articles.map((article) => <Article key={article.id} {...article} />)}
  <div className="mb-4"></div>
  </>
};

export default Articles;
