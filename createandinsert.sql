CREATE TABLE testdb.classroom (
rollno INT PRIMARY KEY,
namestd VARCHAR(50) NOT NULL,
house VARCHAR(50) NOT NULL,
grade CHAR(1)
);

INSERT INTO testdb.classroom 
(rollno,namestd,house,grade)
VALUES
(1,'Sam','Akash','B'),
(2,'Ram','Agni','A'),
(3,'Shyam','Jal','B'),
(4,'Sundar','Agni','A'),
(5,'Ram','Vayu','B');