CREATE TABLE AndroidAppPermissions_xref(
    AppID int NOT NULL,
    SubPermissionID int NOT NULL,
    DeveloperJustification varchar(2000) NULL,
    IsAccepted smallint NOT NULL,
    CreatedOn timestamp NULL,
    UpdatedOn timestamp NULL,
    PRIMARY KEY(AppID, SubPermissionID)
    );