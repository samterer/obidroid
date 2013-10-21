CREATE TABLE LUTDevice(
    DeviceID int primary key,
    Name varchar(500) NULL,
    Description varchar(1000) NULL,
    CreatedBy varchar(500) NULL,
    CreatedOn timestamp NULL,
    UpdatedBy varchar(500) NULL,
    UpdatedOn timestamp NULL,
    ManufacturerID int NULL,
    OperatingSystemID int NULL,
    ModelNo varchar(100) NULL,
    DeviceTypeID int NULL
    );