import React from "react";

const Article = ({ id, publication_date, title, content, image }) => {
  return (
    <div className="row justify-content-center">
      <div className="card col-sm-10 mt-4 shadow p-0" title={title}>
        <div className="row g-0">
          <div className="col-md-4">
            <a href={`/articles/${id}`}>
              <div
                className="card-img"
                style={{
                  backgroundImage: `url(${image})`,
                  height: "15rem",
                  backgroundSize: "cover",
                  backgroundPosition: "center",
                }}
              ></div>
            </a>
          </div>
          <div className="col-md-8">
            <div className="d-flex flex-column" style={{ height: "100%" }}>
              <div className="card-body flex-grow-1">
                <h5 className="card-title">
                  <a href="" className="text-decoration-none dark-blue">
                    {title}
                  </a>
                </h5>
                <p className="card-text">{content}</p>
              </div>
              <div className="mt-auto me-1">
                <div className="text-end text-muted small">
                  Le {publication_date.substring(0, 10)} à {publication_date.substring(11, 16)}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Article;
