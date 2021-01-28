CREATE VIEW RECLEAGUE.LEADERBOARD AS
SELECT Team_ID, Team_Name, SUM(League_Points) AS Total_Points
FROM Recleague.Teams
Natural Join Recleague.Events
Group by Team_ID, Team_Name
Order by Total_Points DESC, Team_ID;