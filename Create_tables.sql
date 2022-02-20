create table `web-project-g12`.genders
(
    gender varchar(50) default 'זכר' not null
);

create index users_genders__fk
    on `web-project-g12`.genders (gender);

create table `web-project-g12`.products
(
    product_ID  int auto_increment
        primary key,
    name        varchar(255) not null,
    description varchar(255) not null,
    price       double       null,
    picture     text         null
);

create table `web-project-g12`.reviews
(
    review_ID  int auto_increment
        primary key,
    name       varchar(50) not null,
    Comment    text        not null,
    stars_rate int         null
);

create table `web-project-g12`.service_type
(
    service_ID int auto_increment
        primary key,
    name       varchar(50) not null,
    duration   time        null,
    constraint Appointments_service_type__fk
        unique (name)
);

create table `web-project-g12`.appointments
(
    Appointment_ID int auto_increment
        primary key,
    service_type   varchar(50) not null,
    scheduled_date date        not null,
    scheduled_time time        not null,
    constraint appointments_service_type__fk
        foreign key (service_type) references `web-project-g12`.service_type (name)
);

create table `web-project-g12`.users
(
    ID           int auto_increment
        primary key,
    first_name   varchar(50)               not null,
    last_name    varchar(50)               not null,
    phone_number varchar(50)               not null,
    email        varchar(255)              not null,
    gender       varchar(50) default 'זכר' not null,
    constraint users_phone_number_uindex
        unique (phone_number),
    constraint users_genders__fk
        foreign key (gender) references `web-project-g12`.genders (gender)
);


