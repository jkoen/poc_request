POC_Status = (
    ('OPEN UNALLOCATED', 'Open Unallocated'),
    ('OPEN ALLOCATED', 'Open Allocated'),
    ('SUCCESSFUL', 'Successful'),
    ('UNSUCCESSFUL', 'Unsuccessful'),
    ('CANCELLED', 'Cancelled'),
)

POC_Countries = (
    ('Afghanistan','Afghanistan'),
    ('Albania','Albania'),
    ('Algeria','Algeria'),
    ('Andorra','Andorra'),
    ('Angola','Angola'),
    ('Austria','Austria'),
    ('Bahrain','Bahrain'),
    ('Belgium','Belgium'),
    ('Bolivia','Bolivia'),
    ('Botswana','Botswana'),
    ('Burundi','Burundi'),
    ('Croatia','Croatia'),
    ('Cyprus','Cyprus'),
    ('Czech Republic','Czech Republic'),
    ('Denmark','Denmark'),
    ('Djibouti','Djibouti'),
    ('Egypt','Egypt'),
    ('Ethiopia','Ethiopia'),
    ('Finland','Finland'),
    ('France','France'),
    ('Gabon','Gabon'),
    ('United Kingdom','United Kingdom'),
    ('Gambia','Gambia'),
    ('Georgia','Georgia'),
    ('Germany','Germany'),
    ('Ghana','Ghana'),
    ('Greece','Greece'),
    ('Guinea','Guinea'),
    ('Hungary','Hungary'),
    ('Iceland','Iceland'),
    ('Ireland','Ireland'),
    ('Israel','Israel'),
    ('Isle of','Isle of'),
    ('Italy','Italy'),
    ('Jordan','Jordan'),
    ('Kenya','Kenya'),
    ('Kuwait','Kuwait'),
    ('Lebanon','Lebanon'),
    ('Lesotho','Lesotho'),
    ('Liberia','Liberia'),
    ('Liechtenstein','Liechtenstein'),
    ('Lithuania','Lithuania'),
    ('Luxembourg','Luxembourg'),
    ('Macao','Macao'),
    ('Madagascar','Madagascar'),
    ('Malawi','Malawi'),
    ('Malaysia','Malaysia'),
    ('Maldives','Maldives'),
    ('Mali','Mali'),
    ('Malta','Malta'),
    ('Martinique','Martinique'),
    ('Mauritania','Mauritania'),
    ('Mauritius','Mauritius'),
    ('Mayotte','Mayotte'),
    ('Morocco','Morocco'),
    ('Mozambique','Mozambique'),
    ('Namibia','Namibia'),
    ('Nauru','Nauru'),
    ('Nepal','Nepal'),
    ('Netherlands','Netherlands'),
    ('Nicaragua','Nicaragua'),
    ('Niger','Niger'),
    ('Nigeria','Nigeria'),
    ('Norway','Norway'),
    ('Oman','Oman'),
    ('Pakistan','Pakistan'),
    ('Philippines','Philippines'),
    ('Poland','Poland'),
    ('Portugal','Portugal'),
    ('Puerto Rico','Puerto Rico'),
    ('Qatar','Qatar'),
    ('Reunion','Reunion'),
    ('Romania','Romania'),
    ('Rwanda','Rwanda'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Senegal','Senegal'),
    ('Serbia','Serbia'),
    ('Russia','Russia'),
    ('Seychelles','Seychelles'),
    ('Sierra Leone','Sierra Leone'),
    ('Slovakia','Slovakia'),
    ('Slovenia','Slovenia'),
    ('Somalia','Somalia'),
    ('South Africa','South Africa'),
    ('Spain','Spain'),
    ('Sri Lanka','Sri Lanka'),
    ('Sudan','Sudan'),
    ('Swaziland','Swaziland'),
    ('Sweden','Sweden'),
    ('Switzerland','Switzerland'),
    ('Tonga','Tonga'),
    ('Tunisia','Tunisia'),
    ('Turkey','Turkey'),
    ('Uganda','Uganda'),
    ('Ukraine','Ukraine'),
    ('United Arab','United Arab'),
    ('Yemen','Yemen'),
    ('Zambia','Zambia'),
    ('Zimbabwe','Zimbabwe'),
)

POC_location = (
	('EDC', 'EDC Zaltbommel'),
	('CUSTOMER', 'Customer Premises'),
)

POC_Primary_Catagory = (
	('UCP-VMWARE', 'UCP for VMware'),
	('UCP-HYPERV', 'UCP for HyperV'),
	('UCP-ORACLE', 'UCP for Oracle'),
	('UCP-SAP', 'UCP for SAP HANA'),
	('STORAGE', 'Storage'),
	('COMPUTE', 'Compute'),
    ('FILE', 'File'),
    ('CONTENT', 'Content'),
	('DATA-PROTECTION', 'Data Protection '),
)

POC_Secondary_Catagory_VMWARE = (
    ('UCP-4000-E', 'UCP 4000e'),
    ('UCP-4000', 'UCP 4000'),
    ('UCP-2000', 'UCP 2000'),
    ('UCP-HC', 'UCP HC'),
)

POC_Secondary_Catagory_HYPERV = (
    ('UCP-4000-E', 'UCP 4000e'),
    ('UCP-4000', 'UCP 4000'),
    ('UCP-2000', 'UCP 2000'),
)

POC_Secondary_Catagory_ORACLE = (
    ('UCP-6000', 'UCP 6000'),
    ('UCP-6000-TDI', 'UCP 6000 TDI'),
)

POC_Secondary_Catagory_HANA = (
    ('UCP-6000', 'UCP 6000'),
    ('UCP-6000-TDI', 'UCP 6000 TDI'),
)

POC_Secondary_Catagory_STORAGE = (
    ('STORAGE-MANAGEMENT', 'Storage Management'),
    ('PERFORMANCE', 'Performance'),
    ('GLOBAL-ACTIVE-DEVICE', 'Global-Active-Device'),
)

POC_Secondary_Catagory_COMPUTE = (
    ('QUANTAGRID', 'Quantagrid'),
    ('COMPUTE-BLADE-500', 'Compute Blade 500'),
    ('COMPUTE-BLADE-2500', 'Compute Blade 2500'),
)

POC_Secondary_Catagory_FILE = (
    ('HITACHI-NAS-4000', 'Hitachi NAS 4000'),
    ('HITACHI-DATA-INGESTOR', 'Hitachi Data Ingestor'),
)

POC_Secondary_Catagory_CONTENT = (
    ('HITACHI-COMPUTE-PLATFORM', 'Hitachi Compute Platform'),
    ('HCP-ANYWHERE', 'HCP Anywhere'),
)

POC_Secondary_Catagory_DATA_PROTECTION = (
    ('HITACHI-DATA-INSTANCE-DIRECTOR', 'Hitachi Data Instance Director'),
    ('HITACHI-DATA-PROTECTION-SUITE', 'Hitachi Data Protection Suite'),
)

POC_Gss_Services_required = (
	('YES', 'Yes'),
	('NO', 'No'),
)