CREATE TABLE LUTOperatingSystem(
    OperatingSystemID int primary key,
    Name varchar(500) NULL,
    Description varchar(1000) NULL,
    CreatedOn timestamp NULL,
    CreatedBy varchar(500) NULL,
    UpdatedBy varchar(500) NULL,
    UpdatedOn timestamp NULL);