drop table if exists gp_taluka_xref_tbl;

create table gp_taluka_xref_tbl(
		gp_code int PRIMARY KEY,
		gp_name varchar(80) NOT NULL,
		taluka_code int
);

create unique index gp_taluka_xref_idx on gp_taluka_xref_tbl(gp_code,taluka_code);


INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (201,'B M Sugur',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (202,'Balkundi',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (203,'Byrapura',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (204,'Baggur',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (205,'H Hosahalli',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (206,'Halekote',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (207,'Hacchohalli',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (208,'K Belegal',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (209,'Kenchanagudda',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (210,'K Sugur',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (211,'Kududrahal',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (212,'Kuruvalli',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (213,'M Sugur',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (214,'Nadavi',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (215,'Raravi',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (216,'Ravihal',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (217,'Shanvaspura',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (218,'Sirigeri',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (219,'Talur',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (220,'Uttanur',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (101,'Alagwadi',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (102,'Belehar',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (103,'Bhadrapura',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (104,'Gudisagara',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (105,'Gummagola',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (106,'Hallekusugal',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (107,'Hallikeri',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (108,'Hebbal',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (109,'Ibrahimpur',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (110,'Kalwadi',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (111,'Morab',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (112,'Navalli',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (113,'Nayaknur',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (114,'Saswihalli',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (115,'Shalwadi',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (116,'Shirakol',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (117,'Shirur',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (118,'Shishwinahalli',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (119,'Tadahal',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (120,'Yamanur',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (121001,'Belavatagi',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (122001,'Javoor',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (123001,'Nelwadi',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (124001,'Tirlapur',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (125001,'Tuppadakuratti',1);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (226001,'Konchigere',2);
INSERT INTO gp_taluka_xref_tbl (gp_code,gp_name,taluka_code) VALUES (224001,'Deshanuru',2);
