CREATE TABLE LUTAndroidPermissions(
    PermissionID int primary key,
    Title varchar(500) NULL,
    Description varchar(5000) NULL,
    FriendlyDescription varchar(5000) NULL,
    ThreatLevelID int NULL,
    CreatedBy varchar(100) NULL,
    CreatedOn timestamp NULL,
    UpdatedBy varchar(100) NULL,
    UpdatedOn timestamp NULL,
    FriendlyTitle varchar(500) NULL);