-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE average_weighted FLOAT;
    DECLARE i INT DEFAULT 0;

    WHILE i < (SELECT COUNT(*) FROM users) DO
        SET @user_id = (SELECT id FROM users ORDER BY id ASC LIMIT 1 OFFSET i);
        SET @score = (SELECT score FROM corrections
            WHERE user_id = @user_id LIMIT 1 OFFSET i);
        SET @weight = (SELECT weight FROM projects
            JOIN corrections ON corrections.project_id = projects.id
            WHERE user_id = @user_id LIMIT 1 OFFSET i);

        IF @score IS NOT NULL AND @weight IS NOT NULL THEN
            SET average_weighted = SUM(@score * @weight) / SUM(@weight);
            UPDATE users SET average_score = average_weighted WHERE id = @user_id;
        END IF;

        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;

