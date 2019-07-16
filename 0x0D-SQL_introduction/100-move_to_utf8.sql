-- This script converts databases into UTF-8 encoding
-- This is pretty cool, actually
USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE first_table MODIFY name VARCHAR (256) CHARACTER SET utf8 COLLATE utf8_general_ci;
