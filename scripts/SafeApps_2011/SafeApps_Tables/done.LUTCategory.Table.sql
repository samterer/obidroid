CREATE TABLE LUTCategory(
    CategoryID int primary key,
    Name varchar(500) NULL,
    Description varchar(1000) NULL,
    OperatingSystemID int NOT NULL,
    ParentCategoryID int NULL,
    CreatedOn timestamp NULL,
    CreatedBy varchar(500) NULL,
    UpdatedOn timestamp NULL,
    UpdatedBy varchar(500) NULL);