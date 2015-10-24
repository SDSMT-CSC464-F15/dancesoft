CREATE TABLE Address(
    Address_id INT NOT NULL,
    Street varchar(150) NOT NULL,
    City varchar(150) NOT NULL,
    State varchar(50) NOT NULL,
    Zipcode INT NOT NULL,
    PRIMARY KEY (Address_id)
)

CREATE TABLE Guardian(
	Guardian_id INT NOT NULL,
    Guardian_address INT NOT NULL,
	Guardian_name varchar(150) NOT NULL,
    Guardian_home_phone varchar(15) NOT NULL,
    Guardian_cell_phone varchar(15),
    Guardian_work_phone varchar(15),
    Guardian_email varchar(100),
	PRIMARY KEY (Guardian_id),
    FOREIGN KEY (Guardian_address) REFERENCES Address(Address_id)
)


CREATE TABLE Teacher(
    Teacher_id INT NOT NULL,
	Teacher_name varchar(150) NOT NULL,
    Teacher_home_phone varchar(15) Not Null,
    Teacher_cell_phone varchar(15),
    Teacher_work_phone varchar(15),
    Teacher_address INT NOT NULL,
    Teacher_email varchar(100),
    Teacher_sex char(1) NOT NULL,
    Teacher_SSN INT NOT NULL 
    Teacher_pay_rate numeric(15,2)
    Teacher_medical_information varchar(MAX)
	PRIMARY KEY (Teacher_id)
    FOREIGN KEY (Teacher_address) REFERENCES Address(Address_id)
)

CREATE TABLE Class(
    Class_id INT NOT NULL.
    Class_name varchar(100) NOT NULL,
    Class_Cost numeric(15,2),
    Class_time time(6)
    Class_day varchar(15)
    Class_location varchar(100),
    Class_cap INT,
    Class_clothing varchar(200),
    Class_description varchar(MAX),
    Class_start_date date,
    Class_end_date date,
    Class_age INT,
    Class_age_end INT,
    PRIMARY KEY (Class_id)
)

CREATE TABLE Student(
    Student_id INT NOT NULL,
    Guardian_primary INT,
    Guardian_secondary INT,
    Student_address INT,
    Student_name varchar(150) NOT NULL
    Student_sex char(1) NOT NULL,
    Student_email varchar(150),
    Student_date_of_birth date NOT NULL,
    Student_home_phone varchar(15),
    Student_cell_phone varchar(15),
    Student_Emergency_contact varchar(100),
    Emergency_contact_phone varchar(15),
    Student_medical_information varchar(MAX),
    Tuition numeric(15,2)
    PRIMARY KEY (Student_id)
    FOREIGN KEY (Guardian_primary) REFERENCES Guardian(Guardian_id)
    FOREIGN KEY (Guardian_secondary) REFERENCES Guardian(Guardian_id)
    FOREIGN KEY (Student_address) REFERENCES Address(Address_id)
)

CREATE TABLE Teacher_Class(
    Teacher_id INT NOT NULL,
    Class_id INT NOT NULL,
    PRIMARY KEY (Class_id, Teacher_id),
    FOREIGN KEY (Class_id) REFERENCES Class(Class_id),
    FOREIGN KEY (Teacher_id) REFERENCES Teacher(Teacher_id)
)

CREATE TABLE Student_Class(
    Student_id INT NOT NULL,
    Class_id INT NOT NULL,
    Class_finished bit DEFAULT 0
    Class_aproval INT DEFAULT 0,
    Student_date_taken date,
    PRIMARY KEY (Student_id, Class_id),
    FOREIGN KEY (Class_id) REFERENCES Class(Class_id)
    FOREIGN KEY (Student_id) REFERENCES Student(Student_id)
)

CREATE TABLE Admin(
    Admin_id INT NOT NULL,
	Admin_name varchar(150) NOT NULL,
    Admin_home_phone varchar(15) Not Null,
    Admin_cell_phone varchar(15),
    Admin_work_phone varchar(15),
    Admin_address INT NOT NULL,
    Admin_email varchar(100),
    Admin_sex char(1) NOT NULL,
    Admin_SSN INT NOT NULL 
    Admin_pay_rate numeric(15,2)
    Admin_medical_information varchar(MAX)
	PRIMARY KEY (Admin_id)
    FOREIGN KEY (Admin_address) REFERENCES Address(Address_id)

CREATE TABLE Account(
	User_id INT NOT NULL,
    User_name varchar(30) NOT NULL,
    User_password varchar(MAX) NOT NULL,
    Access_level INT NOT NULL,
    Student_id INT,
    Teacher_id INT,
    Admin_id INT,
    PRIMARY KEY(User_id)
    FOREIGN KEY(Student_id) REFERENCES Student(Student_id)
    FOREIGN KEY(Teacher_id) REFERENCES Teacher(Teacher_id)
    FOREIGN KEY(Admin_id) REFERENCES Admin(Admin_id)
)


