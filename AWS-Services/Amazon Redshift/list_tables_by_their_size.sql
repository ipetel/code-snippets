SELECT  schema as table_schema,
        "table" as table_name,
        size as used_mb
FROM svv_table_info d
order by size desc;
