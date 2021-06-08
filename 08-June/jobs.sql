drop table if exists openings;

create table openings (
       id serial primary key,
       title text,
       job_id integer,
       company_name text,
       jd_url text,
       jd_text text
);
