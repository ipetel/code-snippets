-- This script create a trigger for function that will run on each insert operation on each record
-- and perform an upsert operation --> it will insert records as is if the record is not existed, else it will accumulate the old value with the new one

CREATE TABLE IF NOT EXISTS table_1 (
   id bigint,
   metric_value float(8) NOT NULL,
   PRIMARY KEY (id)
);



CREATE OR REPLACE FUNCTION table_1_upsert() RETURNS trigger AS $table_1_upsert$
declare existing record;    
	BEGIN
        -- check if record is existed
        if (select EXISTS(select 1 from table_1 where alert_id = NEW.id)) then
        	
            -- get "metric_value" value for existing record
        	select metric_value into strict existing from table_1 where id = NEW.id;

            -- update the relevant record
            UPDATE table_1 SET
                metric_value = new.metric_value+existing.metric_value
                WHERE alert_id = NEW.id

            return null;
        END if;
        
        -- if rrecord not existed, return record as is
        return NEW;
    END;
$table_1_upsert$ LANGUAGE plpgsql;



CREATE TRIGGER table_1_upsert 
	BEFORE INSERT ON table_1 
	FOR EACH ROW EXECUTE PROCEDURE table_1_upsert();
