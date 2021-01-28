CREATE TABLE RECLEAGUE.EVENTS(
	EVENT_ID NUMBER(9) NOT NULL,
	TEAM_ID NUMBER(6) NOT NULL,
	SCORE VARCHAR2(15),
	PLACEMENT NUMBER(4),
	LEAGUE_POINTS NUMBER(3),
	CONSTRAINT EVENT_TEAM_FK
		FOREIGN KEY (TEAM_ID)
		REFERENCES RECLEAGUE.TEAMS(TEAM_ID),
	CONSTRAINT EVENT_INFO_FK
		FOREIGN KEY (EVENT_ID)
		REFERENCES RECLEAGUE.EVENT_INFO(EVENT_ID),		
	CONSTRAINT PK_EVENTS
		PRIMARY KEY (TEAM_ID, EVENT_ID)
);