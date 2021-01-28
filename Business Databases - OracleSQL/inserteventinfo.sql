INSERT INTO RECLEAGUE.EVENT_INFO(Event_ID, Description, Category, Start_Time)
VALUES(event_seq.NEXTVAL, '3v3 basketball game with two 10-minute halves', 'Basketball', 
TO_DATE('2020/01/04 12:00:00', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO RECLEAGUE.EVENT_INFO(Event_ID, Description, Category, Start_Time)
VALUES(event_seq.NEXTVAL, '3v3 basketball game with two 10-minute halves', 'Basketball', 
TO_DATE('2020/01/04 12:30:00', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO RECLEAGUE.EVENT_INFO(Event_ID, Description, Category, Start_Time)
VALUES(event_seq.NEXTVAL, '3v3 basketball game with two 10-minute halves', 'Basketball', 
TO_DATE('2020/01/04 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO RECLEAGUE.EVENT_INFO(Event_ID, Description, Category, Start_Time)
VALUES(event_seq.NEXTVAL, '100m dash', 'Track and Field', 
TO_DATE('2020/01/05 12:00:00', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO RECLEAGUE.EVENT_INFO(Event_ID, Description, Category, Start_Time)
VALUES(event_seq.NEXTVAL, 'Long Jump', 'Track and Field', 
TO_DATE('2020/01/05 12:30:00', 'yyyy/mm/dd hh24:mi:ss'));
INSERT INTO RECLEAGUE.EVENT_INFO(Event_ID, Description, Category, Start_Time)
VALUES(event_seq.NEXTVAL, '50m hurdles', 'Track and Field', 
TO_DATE('2020/01/05 13:00:00', 'yyyy/mm/dd hh24:mi:ss'));
commit;