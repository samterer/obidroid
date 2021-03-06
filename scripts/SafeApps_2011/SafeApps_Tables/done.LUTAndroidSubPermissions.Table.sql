CREATE TABLE LUTAndroidSubPermissions(
    SubPermissionID int primary key,
    PermissionID int NOT NULL,
    Title varchar(500) NULL,
    Description varchar(10000) NULL,
    IsDangerous bit NULL,
    FriendlyDescription varchar(5000) NULL,
    ThreatLevelID int NULL,
    FriendlyTitle varchar(500) NULL,
    UpdatedOn timestamp NULL);