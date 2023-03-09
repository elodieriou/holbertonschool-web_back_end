-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE average_weighted FLOAT;
    SELECT SUM(score * weight) / SUM(weight) INTO average_weighted
    FROM users
    JOIN corrections ON users.id = corrections.user_id
    JOIN projects ON corrections.project_id = projects.id
    WHERE users.id = user_id;
    UPDATE users SET average_score = average_weighted WHERE id = user_id;
END$$
DELIMITER ;
