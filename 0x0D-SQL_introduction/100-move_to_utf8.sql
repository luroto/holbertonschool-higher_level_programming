-- This script converts databases into UTF-8 encoding
-- This is pretty cool, actually
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci
ALTER TABLE hbtn_0c_0.first_table MODIFY `name` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
