#############################################################
#                                                           #
#  M O D U L E     I M P O R T S        (B E G I N N I N G) #
#                                                           #
#############################################################

import mariadb
import sys

#################################################
#                                               #
#  M O D U L E     I M P O R T S        (E N D) #
#                                               #
#################################################


#############################################################################
#                                                                           #
# E S T A B L I S H I N G       C O N N E C T I O N     (B E G I N N I N G) #
#                                                                           #   
#############################################################################

# Connect to MariaDB Platform - Try Clause
try:
    conn = mariadb.connect(
        user = "root",
        password = "",
        host = "127.0.0.1",
        port = 3306,
        database = "cse_2213"
    )

# Connect to MariaDB Platform - Execption Handling
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor - Used to execute queries
cur = conn.cursor()

#################################################################
#                                                               #
# E S T A B L I S H I N G       C O N N E C T I O N     (E N D) #
#                                                               #   
#################################################################


# Execute Query
cur.execute(
    "SELECT * FROM books"
)

# Print Result-set
for (ISBN, Title, Author, Year, Genre) in cur:
    print(f"ISBN: {Title}, Title: {Title}, Author: {Author}, Year: {Year}, Genre: {Genre}")


##################################################################
#                                                                #
# C L O S I N G      C O N N E C T I O N     (B E G I N N I N G) #
#                                                                #   
##################################################################

# Close Connection
conn.close()
sys.exit(0)

######################################################
#                                                    #
# C L O S I N G      C O N N E C T I O N     (E N D) #
#                                                    #   
######################################################
# CSE_2213_Group_Project_Spring_2022
# CSE_2213_Group_Project_Spring_2022
