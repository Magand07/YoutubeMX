use YT;
drop table contenidoYT;
drop table categoryVideo;

create table contenidoYT(
    title varchar(100) primary key,
    channel varchar(100),
    category_id tinyint,
    date_upload date,
    tags varchar(500),
    views int,
    likes int,
    dislikes int,
    comments int
);

create table categoryVideo(
    category_id tinyint primary key,
    category varchar(500)
);