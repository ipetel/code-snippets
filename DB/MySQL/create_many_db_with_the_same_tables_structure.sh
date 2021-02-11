'''
    This bash script is for creating several DB in MySQL with the same structure.
    assume you have SQL script with creation of tables (script.sql), now you want to create 3 identical structure
'''

HOST="localhost"
PASSWORD="<DB-PASSWORD>"
USER="<DB-USER>"

COMPS=('db_1' 'db2' 'db3')
for comp in $COMPS
do
mysql --host=$HOST --password=$PASSWORD --user=$USER -e"CREATE SCHEMA $comp CHARACTER SET utf8 COLLATE utf8_general_ci;";
mysql --host=$HOST --password=$PASSWORD --user=$USER --database="$comp"<./script.sql >./reports/restore_$comp.log;
done

''' example of "script.sql"

DROP TABLE IF EXISTS `table_1`;
CREATE TABLE `table_1` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(50) DEFAULT NULL,

  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `table_2`;
CREATE TABLE `table_2` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(50) DEFAULT NULL,

  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

'''
