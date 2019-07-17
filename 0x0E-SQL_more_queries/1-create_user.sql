-- This script creates a server user with all privileges
-- It shouldn't fail if the username already exists
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO used_0d_1@localhost IDENTIFIED BY 'user_0d_pwd';
