CREATE TABLE
applications (
    app_id SERIAL PRIMARY KEY,
    link VARCHAR(255) NOT NULL,
    company VARCHAR(255) NOT NULL,
    job_role VARCHAR(255),
    date_applied DATE,
    date_heard_back DATE,
    industry VARCHAR(255),
    location VARCHAR(255),
    app_platform VARCHAR(255)
);