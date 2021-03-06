USE [SafeApps]
GO
/****** Object:  Table [dbo].[DeveloperNotification]    Script Date: 09/28/2013 03:28:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DeveloperNotification](
	[NotificationID] [int] IDENTITY(1,1) NOT NULL,
	[AppId] [int] NOT NULL,
	[IsSent] [bit] NOT NULL,
	[DeveloperEmail] [nvarchar](500) NULL,
 CONSTRAINT [PK_DeveloperNotification] PRIMARY KEY CLUSTERED 
(
	[NotificationID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[DeveloperNotification]  WITH CHECK ADD  CONSTRAINT [FK_DeveloperNotification_App] FOREIGN KEY([AppId])
REFERENCES [dbo].[App] ([AppID])
GO
ALTER TABLE [dbo].[DeveloperNotification] CHECK CONSTRAINT [FK_DeveloperNotification_App]
GO
