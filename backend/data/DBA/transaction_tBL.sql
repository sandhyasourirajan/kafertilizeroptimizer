/*

        This table has the transaction details every time the Fertilizer Optimizer app runs the optimization logic 
        to suggest a fertilizer for a N-P-K value.

*/

drop table if exists transaction_tbl;

create table transaction_tbl (
		time_stamp timestamp default current_timestamp PRIMARY KEY,
        crop_name varchar(30) NOT NULL,
        variety varchar(50) NOT NULL,
        farmer_ID int NOT NULL,
        region_code int NOT NULL,
        irrigation_type_code char(1) NOT NULL,
        N_deficit float NOT NULL,
        P_deficit float NOT NULL,
        K_deficit float NOT NULL,
        estimated_cost float  NOT NULL 
        --fertilizer_ID char(19),
        --FOREIGN KEY(fertilizer_ID) REFERENCES fertilizer_transaction_tbl(fertilizer_ID)
);

create unique index transaction_idx on transaction_tbl(time_stamp, crop_name, variety, farmer_ID, region_code, irrigation_type_code, N_deficit, P_deficit, K_deficit, estimated_cost);
