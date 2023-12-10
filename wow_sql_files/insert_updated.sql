INSERT INTO auth_user (username, password, email, first_name, last_name, is_superuser, is_staff, is_active, date_joined) 
VALUES
    ('ava_smith', 'CommonPass123', 'ava_smith@yahoo.com', 'Ava', 'Smith', false, false, true, NOW()),
    ('olivia_garcia', 'CommonPass123', 'olivia_garcia@gmail.com', 'Olivia', 'Garcia', false, false, true, NOW()),
    ('ava_rodriguez', 'CommonPass123', 'ava_rodriguez@gmail.com', 'Ava', 'Rodriguez', false, false, true, NOW()),
    ('mason_miller', 'CommonPass123', 'mason_miller@gmail.com', 'Mason', 'Miller', false, false, true, NOW()),
    ('emma_jones', 'CommonPass123', 'emma_jones@gmail.com', 'Emma', 'Jones', false, false, true, NOW()),
    ('logan_williams', 'CommonPass123', 'logan_williams@gmail.com', 'Logan', 'Williams', false, false, true, NOW()),
    ('sophia_martinez', 'CommonPass123', 'sophia_martinez@gmail.com', 'Sophia', 'Martinez', false, false, true, NOW()),
    ('emma_miller', 'CommonPass123', 'emma_miller@yahoo.com', 'Emma', 'Miller', false, false, true, NOW()),
    ('sophia_brown', 'CommonPass123', 'sophia_brown@gmail.com', 'Sophia', 'Brown', false, false, true, NOW()),
    ('noah_smith', 'CommonPass123', 'noah_smith@yahoo.com', 'Noah', 'Smith', false, false, true, NOW()),
    ('mason_smith', 'CommonPass123', 'mason_smith@gmail.com', 'Mason', 'Smith', false, false, true, NOW()),
    ('liam_johnson', 'CommonPass123', 'liam_johnson@gmail.com', 'Liam', 'Johnson', false, false, true, NOW()),
    ('liam_rodriguez', 'CommonPass123', 'liam_rodriguez@hotmail.com', 'Liam', 'Rodriguez', false, false, true, NOW()),
    ('elijah_davis', 'CommonPass123', 'elijah_davis@gmail.com', 'Elijah', 'Davis', false, false, true, NOW()),
    ('sophia_miller', 'CommonPass123', 'sophia_miller@hotmail.com', 'Sophia', 'Miller', false, false, true, NOW()),
    ('emma_johnson', 'CommonPass123', 'emma_johnson@gmail.com', 'Emma', 'Johnson', false, false, true, NOW()),
    ('isabella_smith', 'CommonPass123', 'isabella_smith@gmail.com', 'Isabella', 'Smith', false, false, true, NOW()),
    ('isabella_miller', 'CommonPass123', 'isabella_miller@hotmail.com', 'Isabella', 'Miller', false, false, true, NOW()),
    ('liam_davis', 'CommonPass123', 'liam_davis@gmail.com', 'Liam', 'Davis', false, false, true, NOW()),
    ('logan_martinez', 'CommonPass123', 'logan_martinez@hotmail.com', 'Logan', 'Martinez', false, false, true, NOW());

INSERT INTO wow_customer 
(user_id, address_houseno, address_street, address_city, address_state, address_zipcode, phone, cust_type)
VALUES
    (1, 154, 'Aspen Court', 'Riverside', 'NY', '43125', '5559876541', 'I'),
    (2, 217, 'Chestnut Way', 'Springfield', 'TX', '21435', '5559876542', 'I'),
    (3, 428, 'Chestnut Way', 'Madison', 'FL', '34215', '5559876543', 'I'),
    (4, 447, 'Pine Street', 'Greenwich', 'TX', '54213', '5559876544', 'I'),
    (5, 293, 'Cedar Road', 'Salem', 'CA', '12345', '5559876545', 'I'),
    (6, 935, 'Birch Lane', 'Madison', 'MI', '34215', '5559876546', 'C'),
    (7, 634, 'Walnut Avenue', 'Madison', 'NY', '12543', '5559876547', 'C'),
    (8, 671, 'Aspen Court', 'Centerville', 'GA', '43125', '5559876548', 'C'),
    (9, 833, 'Chestnut Way', 'Greenwich', 'PA', '12543', '5559876549', 'I'),
    (10, 764, 'Spruce Drive', 'Springfield', 'GA', '12453', '5559876550', 'C'),
    (11, 578, 'Aspen Court', 'Salem', 'IL', '54321', '5559876551', 'I'),
    (12, 398, 'Spruce Drive', 'Centerville', 'IL', '34215', '5559876552', 'C'),
    (13, 602, 'Birch Lane', 'Madison', 'NY', '54213', '5559876553', 'C'),
    (14, 768, 'Birch Lane', 'Madison', 'NY', '53241', '5559876554', 'C'),
    (15, 860, 'Pine Street', 'Springfield', 'CA', '54321', '5559876555', 'I'),
    (16, 373, 'Spruce Drive', 'Clinton', 'IL', '21435', '5559876556', 'I'),
    (17, 531, 'Maple Street', 'Clinton', 'NC', '43125', '5559876557', 'C'),
    (18, 302, 'Pine Street', 'Springfield', 'GA', '12543', '5559876558', 'I'),
    (19, 449, 'Chestnut Way', 'Springfield', 'PA', '54312', '5559876559', 'C'),
    (20, 896, 'Elm Street', 'Springfield', 'GA', '54213', '5559876560', 'I');

INSERT INTO wow_corpcust (customer_id, company_name, company_number, emp_id)
VALUES
    (6, 'Vandelay Industries', 'Inite123', 8100),
    (7, 'Wayne Enterprises', 'Umbr456', 1419),
    (8, 'Acme Corp', 'Wayne123', 8008),
    (10, 'Initech', 'Inite123', 5714),
    (12, 'Soylent Corp', 'Pied456', 5497),
    (13, 'Pied Piper', 'Umbr456', 9465),
    (14, 'Soylent Corp', 'Hooli123', 4087),
    (17, 'Acme Corp', 'Pied456', 1536),
    (19, 'Pied Piper', 'Comp1234', 3317);
    
INSERT INTO wow_indivcust (customer_id, license_no, insurance_co, insurance_policy_num)
VALUES
    (1, 'Lic4567890', 'StateFarm', 'Pol56789'),
    (2, 'Lic8901234', 'FarmersInsurance', 'Pol23456'),
    (3, 'Lic0123456', 'FarmersInsurance', 'Pol89012'),
    (4, 'Lic7890123', 'StateFarm', 'Pol78901'),
    (5, 'Lic7890123', 'FarmersInsurance', 'Pol01234'),
    (9, 'Lic2345678', 'Geico', 'Pol78901'),
    (11, 'Lic4567890', 'Geico', 'Pol78901'),
    (15, 'Lic3456789', 'FarmersInsurance', 'Pol01234'),
    (16, 'Lic3456789', 'Travelers', 'Pol23456'),
    (18, 'Lic4567890', 'Nationwide', 'Pol01234'),
    (20, 'Lic3456789', 'USAA', 'Pol67890');
    
INSERT INTO wow_corpdiscount
(customer_id, percentage)
VALUES
	(1, 0.11),
    (2, 0.07),
    (3, 0.21),
    (4, 0.12),
    (5, 0.15),
    (6, 0.03),
    (7, 0.2),
    (8, 0.17),
    (9, 0.05);
    
INSERT INTO wow_indivdiscount 
(customer_id, percentage, start_date, end_date)
VALUES
    (1, 0.07, '2024-11-15', '2025-03-13'),
    (2, 0.05, '2024-12-22', '2025-01-24'),
    (3, 0.13, '2024-11-11', '2024-12-25'),
    (4, 0.12, '2024-11-23', '2025-02-17'),
    (5, 0.21, '2024-06-05', '2024-09-23'),
    (6, 0.16, '2024-12-01', '2025-02-26'),
    (7, 0.8, '2024-10-16', '2024-12-12'),
    (8, 0.7, '2024-07-17', '2024-12-12'),
    (9, 0.7, '2024-01-09', '2024-05-24'),
    (10, 0.25, '2024-01-06', '2024-03-20'),
    (11, 0.1, '2024-05-26', '2024-07-18');
    
INSERT INTO wow_office 
(address_houseno, address_street, address_city, address_state, address_zipcode, phone)
VALUES
    (830, '5th Boulevard', 'Gotham', 'FL', '02101', '5553863652'),
    (119, '6th Drive', 'Midway City', 'FL', '48001', '5554924114'),
    (547, '1st Avenue', 'Midway City', 'CA', '02101', '5555105655'),
    (913, '2nd Street', 'Midway City', 'FL', '98001', '5552749851'),
    (493, '7th Terrace', 'Central City', 'NY', '60001', '5559167686'),
    (937, '4th Road', 'Coast City', 'WA', '48001', '5559230861'),
    (218, '2nd Street', 'Midway City', 'WA', '43001', '5552211343'),
    (178, '10th Parkway', 'Midway City', 'NY', '02101', '5553247342'),
    (329, '5th Boulevard', 'Gateway City', 'IL', '98001', '5559142173'),
    (317, '4th Road', 'Metropolis', 'PA', '73301', '5552841958');

INSERT INTO wow_vclass
(class_name, daily_rate, daily_mileage, overage_rate)
VALUES
	('Mid-Size Sedan', 50.00, 150, 1.50),
    ('Luxury Sedan', 100.00, 150, 3.00),
    ('SUV', 65.00, 200, 2.00),
    ('Luxury SUV', 130.00, 200, 3.00),
    ('Luxury Coupe', 110.00, 180, 2.50),
    ('Sport', 70.00, 150, 2.00),
    ('Luxury Sport', 250, 100, 5.00),
    ('Minivan', 65.00, 250, 1.50),
    ('Camper', 175.00, 500, 5.00),
    ('Pickup Truck', 50.00, 200, 1.00),
    ('Economy', 40.00, 200, 1.00),
    ('Compact', 37.50, 175, 1.50);
    
INSERT INTO wow_vehicle
(vin, make, model, year, lp_state, lp_number, vclass_id, office_id)
VALUES
	('53N7S75LGGTY7713P', 'Toyota', 'Camry', 2022, 'CA', '2ZPHVAT', 1, 5),
	('7M1L3UPFMASPA46YJ', 'Honda', 'Accord', 2017, 'NY', 'PZAZW58', 1, 1),
	('SUNT4E849BEAGMVYT', 'Nissan', 'Altima', 2021, 'PA', 'HSVWB36', 1, 10),
	('HNGGWZCK4XJNN3R4C', 'Ford', 'Fusion', 2019, 'WA', 'SGFN3Z0', 1, 10),
	('6ETMGZMRGZNHNLCTW', 'Hyundai', 'Sonata', 2019, 'OH', 'MMX6ETX', 1, 6),
	('2SE4VNPM0PSWD0JU9', 'Mercedes-Benz', 'E-Class', 2017, 'PA', 'ZBJ48SG', 2, 9),
	('GMKJPD9TJMTW0G89K', 'BMW', '5 Series', 2022, 'NY', '6ZK25M0', 2, 1),
	('90RA6YW8MA312Z09S', 'Audi', 'A6', 2019, 'IL', 'HZUKVP2', 2, 5),
	('AHL9YENKZGLWE71E9', 'Lexus', 'ES', 2018, 'CA', 'W49603V', 2, 8),
	('EAUJ92B0C4XSKSDFS', 'Jaguar', 'XF', 2022, 'WA', 'F2PV2WW', 2, 9),
	('NSTWKRNV33H1FY2NX', 'Ford', 'Explorer', 2020, 'FL', 'WFE05V7', 3, 6),
	('X23WF19ZURS2H682T', 'Chevrolet', 'Tahoe', 2019, 'CA', 'P4534MZ', 3, 8),
	('FSLEPLPASC2D5RXCU', 'Jeep', 'Grand Cherokee', 2017, 'WA', '04YNJUD', 3, 1),
	('BUXW8CUY3F5G8SSSL', 'Toyota', 'Highlander', 2019, 'FL', 'DAVH2S9', 3, 6),
	('R8C5TVM7W7MVX51SU', 'Honda', 'Pilot', 2016, 'FL', 'XNM54P9', 3, 9),
	('JJC6KFHHP5ZJ4DXGP', 'Audi', 'Q7', 2015, 'MA', 'D2S5HXF', 4, 10),
	('HR3JWPBEV4EM93507', 'BMW', 'X5', 2018, 'NY', 'S7RDAJ7', 4, 5),
	('4Y7S4EDNTZ04Z3XBZ', 'Mercedes-Benz', 'GLS', 2021, 'TX', '3V6M7B7', 4, 7),
	('58K09XHM667AWMKA7', 'Lexus', 'RX', 2018, 'MI', '8531BZC', 4, 7),
	('831RWYAC82S4DRCGE', 'Porsche', 'Cayenne', 2021, 'TX', 'FXHB51C', 4, 8),
	('5TEZU7MJ3E6C64RL3', 'BMW', '4 Series', 2021, 'MI', '63YY0E4', 5, 7),
	('ZE5J0NZNF160SWC3Z', 'Mercedes-Benz', 'C-Class Coupe', 2022, 'OH', '2LEY5DD', 5, 8),
	('XMUFTBC74C890DDVN', 'Audi', 'A5', 2017, 'WA', 'JPX8WPA', 5, 2),
	('KH736MXZ0VRKRKN5E', 'Lexus', 'RC', 2020, 'WA', 'N0PUYBW', 5, 4),
	('UH2AVGWLDCW3V2KKZ', 'Infiniti', 'Q60', 2018, 'OH', 'SP913LX', 5, 1),
	('SFC4XEWKHCV7F1LRE', 'Ford', 'Mustang', 2022, 'CA', 'P347KUG', 6, 8),
	('M7LE5S6MH3LAGL9R8', 'Chevrolet', 'Camaro', 2017, 'TX', 'X5JFA08', 6, 3),
	('8PKL8ZBK6HG2FDKH7', 'Dodge', 'Challenger', 2020, 'CA', '7NWYBVA', 6, 6),
	('5DUKL3Y7JA9W65BVE', 'Nissan', '370Z', 2022, 'MA', 'EC8G8R1', 6, 8),
	('JPG1WJECG4X9U0MTT', 'Subaru', 'BRZ', 2020, 'MI', 'HX7KF0X', 6, 1),
	('J1LK8T7ZH822A0AZR', 'Porsche', '911', 2020, 'NY', '5LEBXHH', 7, 9),
	('KBDHFYS11JEV2CURV', 'Audi', 'R8', 2022, 'CA', 'EF6KZ4N', 7, 6),
	('32Z5EDCYR4HZZ47JK', 'Lamborghini', 'Huracan', 2016, 'TX', 'MTF9B2Y', 7, 8),
	('VYZLJRESPTHKDT980', 'Ferrari', 'F8 Tributo', 2019, 'WA', 'X5EJGBH', 7, 2),
	('SLY1PX2M8C877WJ3T', 'McLaren', '570S', 2022, 'IL', 'WAXWCP2', 7, 5),
	('DF9BP657XTX7ZHFAE', 'Toyota', 'Sienna', 2015, 'CA', 'JL20TZ6', 8, 3),
	('ENNCLPU1JBV2RPGF7', 'Honda', 'Odyssey', 2015, 'FL', 'U6GEKRG', 8, 8),
	('GBBVNPHWSW3ZSFPCS', 'Chrysler', 'Pacifica', 2015, 'IL', 'WXTWYZU', 8, 2),
	('SCLGDXPMCBAHR9P3G', 'Kia', 'Sedona', 2021, 'MI', 'A7A1WZK', 8, 4),
	('6MSKC2H6GS3Z6FM3R', 'Dodge', 'Grand Caravan', 2020, 'WA', 'U8EKYS0', 8, 6),
	('6KANJ7HVU5WYE7YA1', 'Winnebago', 'Minnie Winnie', 2020, 'WA', 'NS2B7FH', 9, 4),
	('A3PVY29GN4K45XVRJ', 'Thor', 'Chateau', 2021, 'MA', '7R6GP0M', 9, 10),
	('TEJH8G22NA0F4YZC1', 'Forest River', 'Sunseeker', 2021, 'NY', 'EXKXA1M', 9, 8),
	('CX4RLPWYXNDC6FDWZ', 'Jayco', 'Redhawk', 2016, 'CA', '9APNDH3', 9, 2),
	('RJZ0JXV00TPGTEZ8M', 'Coachmen', 'Freelander', 2020, 'CA', 'C1RVVZZ', 9, 6),
	('D34C45896CANFT2WT', 'Ford', 'F-150', 2020, 'MA', 'L9GH85C', 10, 7),
	('4ESM5ZAWEYY81X6NM','Chevrolet', 'Silverado 1500', 2017, 'WA', 'R4JR17S', 10, 4),
	('A14FXXKESC21ZP3DF', 'RAM', '1500', 2022, 'OH', 'UP6EUR8', 10, 4),
	('MVHB5GCMJPFPCYNLM', 'Toyota', 'Tundra', 2016, 'CA', 'RK1B7YK', 10, 8),
	('UMCLZ9A855J47UWKD', 'GMC', 'Sierra 1500', 2019, 'MI', '88UCJT2', 10, 9),
	('3VC82ZMHRL8C5A7S2', 'Toyota', 'Yaris', 2021, 'PA', 'L5A70FP', 11, 3),
	('S5CR65N6Z4HMV03X8', 'Kia', 'Rio', 2022, 'OH', 'PSBXVSB', 11, 6),
	('VYF22H0Z74E0U78F4', 'Chevrolet', 'Spark', 2020, 'MA', 'DLNAYU4', 11, 3),
	('5DU01RN8WBYL76DBD', 'Hyundai', 'Accent', 2015, 'MA', '49GY1SC', 11, 7),
	('BT9TW1NKUVM9XVFN4', 'Honda', 'Fit', 2015, 'CA', '6YJ2ENF', 11, 3),
	('N22LA5RJWK9KHG7G1', 'Ford', 'Focus', 2022, 'OH', '9U26XW1', 12, 2),
	('GDL9LCT92XGAXZHZZ', 'Hyundai', 'Elantra', 2022, 'TX', 'LYVPDM9', 12, 9),
	('A874U4KS6ST7AYTE2', 'Kia', 'Forte', 2015, 'NY', '6R9PDYE', 12, 7),
	('HYP9JWX9B6820K8VD', 'Honda', 'Civic', 2019, 'MA', '0CCXCJ1', 12, 9);
    