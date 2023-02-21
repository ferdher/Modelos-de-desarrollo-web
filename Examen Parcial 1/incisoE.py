from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
 
router = APIRouter()



class CountryAttributes(BaseModel):
    Id:int
    Code:str
    Country:str
    Surface_area:int
    Population:int
    Life_expectancy:str
    Local_name:str
    Government_form:str
    Head_of_state:str

    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
CountryAttributes_list= [CountryAttributes(	Id=1,	Code="AFG",	Country="Afghanistan",	Surface_area=652090,	Population=22720000,	Life_expectancy="45.9",	Local_name="Afganistan/Afqanestan",	Government_form="Islamic Emirate",	Head_of_state="Mohammad Omar"),
                         CountryAttributes(	Id=2,	Code="ALB",	Country="Albania",	Surface_area=28748,	Population=3401200,	Life_expectancy="71.6",	Local_name="Shqiperia",	Government_form="Republic",	Head_of_state="Rexhep Mejdani"),
                         CountryAttributes(	Id=3,	Code="DZA",	Country="Algeria",	Surface_area=2381741,	Population=31471000,	Life_expectancy="69.7",	Local_name="Al-Jazair/Algerie",	Government_form="Republic",	Head_of_state="Abdelaziz Bouteflika"),
                         CountryAttributes(	Id=4,	Code="ASM",	Country="American Samoa",	Surface_area=199,	Population=68000,	Life_expectancy="75.1",	Local_name="Amerika Samoa",	Government_form="uS Territory",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=5,	Code="AND",	Country="Andorra",	Surface_area=468,	Population=78000,	Life_expectancy="83.5",	Local_name="Andorra",	Government_form="Parliamentary Coprincipality",	Head_of_state="---"),
                         CountryAttributes(	Id=6,	Code="AGO",	Country="Angola",	Surface_area=1246700,	Population=12878000,	Life_expectancy="38.3",	Local_name="Angola",	Government_form="Republic",	Head_of_state="Jose Eduardo dos Santos"),
                         CountryAttributes(	Id=7,	Code="AIA",	Country="Anguilla",	Surface_area=96,	Population=8000,	Life_expectancy="76.1",	Local_name="Anguilla",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=8,	Code="ATA",	Country="Antarctica",	Surface_area=13120000,	Population=0,	Life_expectancy="NuLL",	Local_name="N/A",	Government_form="Co-administrated",	Head_of_state="---"),
                         CountryAttributes(	Id=9,	Code="ATG",	Country="Antigua and Barbuda",	Surface_area=442,	Population=68000,	Life_expectancy="70.5",	Local_name="Antigua and Barbuda",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=10,	Code="ARG",	Country="Argentina",	Surface_area=2780400,	Population=37032000,	Life_expectancy="75.1",	Local_name="Argentina",	Government_form="Federal Republic",	Head_of_state="Fernando de la Rua"),
                         CountryAttributes(	Id=11,	Code="ARM",	Country="Armenia",	Surface_area=29800,	Population=3520000,	Life_expectancy="66.4",	Local_name="Hajastan",	Government_form="Republic",	Head_of_state="Robert KotSarjan"),
                         CountryAttributes(	Id=12,	Code="ABW",	Country="Aruba",	Surface_area=193,	Population=103000,	Life_expectancy="78.4",	Local_name="Aruba",	Government_form="Nonmetropolitan Territory of The Netherlands",	Head_of_state="Willem-Alexander"),
                         CountryAttributes(	Id=13,	Code="AuS",	Country="Australia",	Surface_area=7741220,	Population=18886000,	Life_expectancy="79.8",	Local_name="Australia",	Government_form="Constitutional Monarchy, Federation",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=14,	Code="AuT",	Country="Austria",	Surface_area=83859,	Population=8091800,	Life_expectancy="77.7",	Local_name="osterreich",	Government_form="Federal Republic",	Head_of_state="Thomas Klestil"),
                         CountryAttributes(	Id=15,	Code="AZE",	Country="Azerbaijan",	Surface_area=86600,	Population=7734000,	Life_expectancy="62.9",	Local_name="Azarbaycan",	Government_form="Federal Republic",	Head_of_state="Heydar aliyev"),
                         CountryAttributes(	Id=16,	Code="BHS",	Country="Bahamas",	Surface_area=13878,	Population=307000,	Life_expectancy="71.1",	Local_name="The Bahamas",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=17,	Code="BHR",	Country="Bahrain",	Surface_area=694,	Population=617000,	Life_expectancy="73",	Local_name="Al-Bahrayn",	Government_form="Monarchy (Emirate)",	Head_of_state="Hamad ibn Isa al-Khalifa"),
                         CountryAttributes(	Id=18,	Code="BGD",	Country="Bangladesh",	Surface_area=143998,	Population=129155000,	Life_expectancy="60.2",	Local_name="Bangladesh",	Government_form="Republic",	Head_of_state="Shahabuddin Ahmad"),
                         CountryAttributes(	Id=19,	Code="BRB",	Country="Barbados",	Surface_area=430,	Population=270000,	Life_expectancy="73",	Local_name="Barbados",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=20,	Code="BLR",	Country="Belarus",	Surface_area=207600,	Population=10236000,	Life_expectancy="68",	Local_name="Belarus",	Government_form="Republic",	Head_of_state="Aljaksandr LukaSenka"),
                         CountryAttributes(	Id=21,	Code="BEL",	Country="Belgium",	Surface_area=30518,	Population=10239000,	Life_expectancy="77.8",	Local_name="Belgie/Belgique",	Government_form="Constitutional Monarchy, Federation",	Head_of_state="Albert II"),
                         CountryAttributes(	Id=22,	Code="BLZ",	Country="Belize",	Surface_area=22696,	Population=241000,	Life_expectancy="70.9",	Local_name="Belize",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=23,	Code="BEN",	Country="Benin",	Surface_area=112622,	Population=6097000,	Life_expectancy="50.2",	Local_name="Benin",	Government_form="Republic",	Head_of_state="Mathieu Kerekou"),
                         CountryAttributes(	Id=24,	Code="BMu",	Country="Bermuda",	Surface_area=53,	Population=65000,	Life_expectancy="76.9",	Local_name="Bermuda",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=25,	Code="BTN",	Country="Bhutan",	Surface_area=47000,	Population=2124000,	Life_expectancy="52.4",	Local_name="Druk-Yul",	Government_form="Monarchy",	Head_of_state="Jigme Singye Wangchuk"),
                         CountryAttributes(	Id=26,	Code="BOL",	Country="Bolivia",	Surface_area=1098581,	Population=8329000,	Life_expectancy="63.7",	Local_name="Bolivia",	Government_form="Republic",	Head_of_state="Hugo Banzer Suarez"),
                         CountryAttributes(	Id=27,	Code="BIH",	Country="Bosnia and Herzegovina",	Surface_area=51197,	Population=3972000,	Life_expectancy="71.5",	Local_name="Bosna i Hercegovina",	Government_form="Federal Republic",	Head_of_state="Ante Jelavic"),
                         CountryAttributes(	Id=28,	Code="BWA",	Country="Botswana",	Surface_area=581730,	Population=1622000,	Life_expectancy="39.3",	Local_name="Botswana",	Government_form="Republic",	Head_of_state="Festus G. Mogae"),
                         CountryAttributes(	Id=29,	Code="BVT",	Country="Bouvet Island",	Surface_area=59,	Population=0,	Life_expectancy="NuLL",	Local_name="Bouvetoya",	Government_form="Dependent Territory of Norway",	Head_of_state="Harald V"),
                         CountryAttributes(	Id=30,	Code="BRA",	Country="Brazil",	Surface_area=8547403,	Population=170115000,	Life_expectancy="62.9",	Local_name="Brasil",	Government_form="Federal Republic",	Head_of_state="Fernando Henrique Cardoso"),
                         CountryAttributes(	Id=31,	Code="IOT",	Country="British Indian Ocean Territory",	Surface_area=78,	Population=0,	Life_expectancy="NuLL",	Local_name="British Indian Ocean Territory",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=32,	Code="BRN",	Country="Brunei",	Surface_area=5765,	Population=328000,	Life_expectancy="73.6",	Local_name="Brunei Darussalam",	Government_form="Monarchy (Sultanate)",	Head_of_state="Haji Hassan al-Bolkiah"),
                         CountryAttributes(	Id=33,	Code="BGR",	Country="Bulgaria",	Surface_area=110994,	Population=8190900,	Life_expectancy="70.9",	Local_name="Balgarija",	Government_form="Republic",	Head_of_state="Petar Stojanov"),
                         CountryAttributes(	Id=34,	Code="BFA",	Country="Burkina Faso",	Surface_area=274000,	Population=11937000,	Life_expectancy="46.7",	Local_name="Burkina Faso",	Government_form="Republic",	Head_of_state="Blaise Compaore"),
                         CountryAttributes(	Id=35,	Code="BDI",	Country="Burundi",	Surface_area=27834,	Population=6695000,	Life_expectancy="46.2",	Local_name="Burundi/uburundi",	Government_form="Republic",	Head_of_state="Pierre Buyoya"),
                         CountryAttributes(	Id=36,	Code="KHM",	Country="Cambodia",	Surface_area=181035,	Population=11168000,	Life_expectancy="56.5",	Local_name="Kampuchea",	Government_form="Constitutional Monarchy",	Head_of_state="Norodom Sihanouk"),
                         CountryAttributes(	Id=37,	Code="CMR",	Country="Cameroon",	Surface_area=475442,	Population=15085000,	Life_expectancy="54.8",	Local_name="Cameroun/Cameroon",	Government_form="Republic",	Head_of_state="Paul Biya"),
                         CountryAttributes(	Id=38,	Code="CAN",	Country="Canada",	Surface_area=9970610,	Population=31147000,	Life_expectancy="79.4",	Local_name="Canada",	Government_form="Constitutional Monarchy, Federation",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=39,	Code="CPV",	Country="Cape Verde",	Surface_area=4033,	Population=428000,	Life_expectancy="68.9",	Local_name="Cabo Verde",	Government_form="Republic",	Head_of_state="Antonio Mascarenhas Monteiro"),
                         CountryAttributes(	Id=40,	Code="CYM",	Country="Cayman Islands",	Surface_area=264,	Population=38000,	Life_expectancy="78.9",	Local_name="Cayman Islands",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=41,	Code="CAF",	Country="Central African Republic",	Surface_area=622984,	Population=3615000,	Life_expectancy="44",	Local_name="Centrafrique/Be-Afrika",	Government_form="Republic",	Head_of_state="Ange-Felix Patasse"),
                         CountryAttributes(	Id=42,	Code="TCD",	Country="Chad",	Surface_area=1284000,	Population=7651000,	Life_expectancy="50.5",	Local_name="Tchad/Tshad",	Government_form="Republic",	Head_of_state="Idriss Deby"),
                         CountryAttributes(	Id=43,	Code="CHL",	Country="Chile",	Surface_area=756626,	Population=15211000,	Life_expectancy="75.7",	Local_name="Chile",	Government_form="Republic",	Head_of_state="Ricardo Lagos Escobar"),
                         CountryAttributes(	Id=44,	Code="CHN",	Country="China",	Surface_area=9572900,	Population=1277558000,	Life_expectancy="71.4",	Local_name="Zhongquo",	Government_form="People'sRepublic",	Head_of_state="Jiang Zemin"),
                         CountryAttributes(	Id=45,	Code="CXR",	Country="Christmas Island",	Surface_area=135,	Population=2500,	Life_expectancy="NuLL",	Local_name="Christmas Island",	Government_form="Territory of Australia",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=46,	Code="CCK",	Country="Cocos (Keeling) Islands",	Surface_area=14,	Population=600,	Life_expectancy="NuLL",	Local_name="Cocos (Keeling) Islands",	Government_form="Territory of Australia",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=47,	Code="COL",	Country="Colombia",	Surface_area=1138914,	Population=42321000,	Life_expectancy="70.3",	Local_name="Colombia",	Government_form="Republic",	Head_of_state="Andres Pastrana Arango"),
                         CountryAttributes(	Id=48,	Code="COM",	Country="Comoros",	Surface_area=1862,	Population=578000,	Life_expectancy="60",	Local_name="Komori/Comores",	Government_form="Republic",	Head_of_state="Azali Assoumani"),
                         CountryAttributes(	Id=49,	Code="COG",	Country="Congo",	Surface_area=342000,	Population=2943000,	Life_expectancy="47.4",	Local_name="Congo",	Government_form="Republic",	Head_of_state="Denis Sassou-Nguesso"),
                         CountryAttributes(	Id=50,	Code="COD",	Country="Congo, The Democratic Republic of the",	Surface_area=2344858,	Population=51654000,	Life_expectancy="48.8",	Local_name="Republique Democratique du Congo",	Government_form="Republic",	Head_of_state="Joseph Kabila"),
                         CountryAttributes(	Id=51,	Code="COK",	Country="Cook Islands",	Surface_area=236,	Population=20000,	Life_expectancy="71.1",	Local_name="The Cook Islands",	Government_form="Nonmetropolitan Territory of New Zealand",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=52,	Code="CRI",	Country="Costa Rica",	Surface_area=51100,	Population=4023000,	Life_expectancy="75.8",	Local_name="Costa Rica",	Government_form="Republic",	Head_of_state="Miguel angel RodrIguez EcheverrIa"),
                         CountryAttributes(	Id=53,	Code="CIV",	Country="Cote dIvoire",	Surface_area=322463,	Population=14786000,	Life_expectancy="45.2",	Local_name="Cote dIvoire",	Government_form="Republic",	Head_of_state="Laurent Gbagbo"),
                         CountryAttributes(	Id=54,	Code="HRV",	Country="Croatia",	Surface_area=56538,	Population=4473000,	Life_expectancy="73.7",	Local_name="Hrvatska",	Government_form="Republic",	Head_of_state="Stipe Mesic"),
                         CountryAttributes(	Id=55,	Code="CuB",	Country="Cuba",	Surface_area=110861,	Population=11201000,	Life_expectancy="76.2",	Local_name="Cuba",	Government_form="Socialistic Republic",	Head_of_state="Fidel Castro Ruz"),
                         CountryAttributes(	Id=56,	Code="CYP",	Country="Cyprus",	Surface_area=9251,	Population=754700,	Life_expectancy="76.7",	Local_name="Kypros/Kibris",	Government_form="Republic",	Head_of_state="Glafkos Klerides"),
                         CountryAttributes(	Id=57,	Code="CZE",	Country="Czech Republic",	Surface_area=78866,	Population=10278100,	Life_expectancy="74.5",	Local_name="esko",	Government_form="Republic",	Head_of_state="Vaclav Havel"),
                         CountryAttributes(	Id=58,	Code="DNK",	Country="Denmark",	Surface_area=43094,	Population=5330000,	Life_expectancy="76.5",	Local_name="Danmark",	Government_form="Constitutional Monarchy",	Head_of_state="Margrethe II"),
                         CountryAttributes(	Id=59,	Code="DJI",	Country="Djibouti",	Surface_area=23200,	Population=638000,	Life_expectancy="50.8",	Local_name="Djibouti/Jibuti",	Government_form="Republic",	Head_of_state="Ismail Omar Guelleh"),
                         CountryAttributes(	Id=60,	Code="DMA",	Country="Dominica",	Surface_area=751,	Population=71000,	Life_expectancy="73.4",	Local_name="Dominica",	Government_form="Republic",	Head_of_state="Vernon Shaw"),
                         CountryAttributes(	Id=61,	Code="DOM",	Country="Dominican Republic",	Surface_area=48511,	Population=8495000,	Life_expectancy="73.2",	Local_name="Republica Dominicana",	Government_form="Republic",	Head_of_state="Hipolito MejIa DomInguez"),
                         CountryAttributes(	Id=62,	Code="TMP",	Country="East Timor",	Surface_area=14874,	Population=885000,	Life_expectancy="46",	Local_name="Timor Timur",	Government_form="Administrated by the uN",	Head_of_state="Jose Alexandre Gusmao"),
                         CountryAttributes(	Id=63,	Code="ECu",	Country="Ecuador",	Surface_area=283561,	Population=12646000,	Life_expectancy="71.1",	Local_name="Ecuador",	Government_form="Republic",	Head_of_state="Gustavo Noboa Bejarano"),
                         CountryAttributes(	Id=64,	Code="EGY",	Country="Egypt",	Surface_area=1001449,	Population=68470000,	Life_expectancy="63.3",	Local_name="Misr",	Government_form="Republic",	Head_of_state="Hosni Mubarak"),
                         CountryAttributes(	Id=65,	Code="SLV",	Country="El Salvador",	Surface_area=21041,	Population=6276000,	Life_expectancy="69.7",	Local_name="El Salvador",	Government_form="Republic",	Head_of_state="Francisco Guillermo Flores Perez"),
                         CountryAttributes(	Id=66,	Code="GNQ",	Country="Equatorial Guinea",	Surface_area=28051,	Population=453000,	Life_expectancy="53.6",	Local_name="Guinea Ecuatorial",	Government_form="Republic",	Head_of_state="Teodoro Obiang Nguema Mbasogo"),
                         CountryAttributes(	Id=67,	Code="ERI",	Country="Eritrea",	Surface_area=117600,	Population=3850000,	Life_expectancy="55.8",	Local_name="Ertra",	Government_form="Republic",	Head_of_state="Isayas Afewerki [Isaias Afwerki]"),
                         CountryAttributes(	Id=68,	Code="EST",	Country="Estonia",	Surface_area=45227,	Population=1439200,	Life_expectancy="69.5",	Local_name="Eesti",	Government_form="Republic",	Head_of_state="Lennart Meri"),
                         CountryAttributes(	Id=69,	Code="ETH",	Country="Ethiopia",	Surface_area=1104300,	Population=62565000,	Life_expectancy="45.2",	Local_name="YeItyop iya",	Government_form="Republic",	Head_of_state="Negasso Gidada"),
                         CountryAttributes(	Id=70,	Code="FLK",	Country="Falkland Islands",	Surface_area=12173,	Population=2000,	Life_expectancy="NuLL",	Local_name="Falkland Islands",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=71,	Code="FRO",	Country="Faroe Islands",	Surface_area=1399,	Population=43000,	Life_expectancy="78.4",	Local_name="Foroyar",	Government_form="Part of Denmark",	Head_of_state="Margrethe II"),
                         CountryAttributes(	Id=72,	Code="FJI",	Country="Fiji Islands",	Surface_area=18274,	Population=817000,	Life_expectancy="67.9",	Local_name="Fiji Islands",	Government_form="Republic",	Head_of_state="Josefa Iloilo"),
                         CountryAttributes(	Id=73,	Code="FIN",	Country="Finland",	Surface_area=338145,	Population=5171300,	Life_expectancy="77.4",	Local_name="Suomi",	Government_form="Republic",	Head_of_state="Tarja Halonen"),
                         CountryAttributes(	Id=74,	Code="FRA",	Country="France",	Surface_area=551500,	Population=59225700,	Life_expectancy="78.8",	Local_name="France",	Government_form="Republic",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=75,	Code="GuF",	Country="French Guiana",	Surface_area=90000,	Population=181000,	Life_expectancy="76.1",	Local_name="Guyane francaise",	Government_form="Overseas Department of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=76,	Code="PYF",	Country="French Polynesia",	Surface_area=4000,	Population=235000,	Life_expectancy="74.8",	Local_name="Polynesie francaise",	Government_form="Nonmetropolitan Territory of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=77,	Code="ATF",	Country="French Southern territories",	Surface_area=7780,	Population=0,	Life_expectancy="NuLL",	Local_name="Terres australes francaises",	Government_form="Nonmetropolitan Territory of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=78,	Code="GAB",	Country="Gabon",	Surface_area=267668,	Population=1226000,	Life_expectancy="50.1",	Local_name="Le Gabon",	Government_form="Republic",	Head_of_state="Omar Bongo"),
                         CountryAttributes(	Id=79,	Code="GMB",	Country="Gambia",	Surface_area=11295,	Population=1305000,	Life_expectancy="53.2",	Local_name="The Gambia",	Government_form="Republic",	Head_of_state="Yahya Jammeh"),
                         CountryAttributes(	Id=80,	Code="GEO",	Country="Georgia",	Surface_area=69700,	Population=4968000,	Life_expectancy="64.5",	Local_name="Sakartvelo",	Government_form="Republic",	Head_of_state="Eduard Sevardnadze"),
                         CountryAttributes(	Id=81,	Code="DEu",	Country="Germany",	Surface_area=357022,	Population=82164700,	Life_expectancy="77.4",	Local_name="Deutschland",	Government_form="Federal Republic",	Head_of_state="Johannes Rau"),
                         CountryAttributes(	Id=82,	Code="GHA",	Country="Ghana",	Surface_area=238533,	Population=20212000,	Life_expectancy="57.4",	Local_name="Ghana",	Government_form="Republic",	Head_of_state="John Kufuor"),
                         CountryAttributes(	Id=83,	Code="GIB",	Country="Gibraltar",	Surface_area=6,	Population=25000,	Life_expectancy="79",	Local_name="Gibraltar",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=84,	Code="GRC",	Country="Greece",	Surface_area=131626,	Population=10545700,	Life_expectancy="78.4",	Local_name="Ellada",	Government_form="Republic",	Head_of_state="Kostis Stefanopoulos"),
                         CountryAttributes(	Id=85,	Code="GRL",	Country="Greenland",	Surface_area=2166090,	Population=56000,	Life_expectancy="68.1",	Local_name="Kalaallit Nunaat/Gronland",	Government_form="Part of Denmark",	Head_of_state="Margrethe II"),
                         CountryAttributes(	Id=86,	Code="GRD",	Country="Grenada",	Surface_area=344,	Population=94000,	Life_expectancy="64.5",	Local_name="Grenada",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=87,	Code="GLP",	Country="Guadeloupe",	Surface_area=1705,	Population=456000,	Life_expectancy="77",	Local_name="Guadeloupe",	Government_form="Overseas Department of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=88,	Code="GuM",	Country="Guam",	Surface_area=549,	Population=168000,	Life_expectancy="77.8",	Local_name="Guam",	Government_form="uS Territory",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=89,	Code="GTM",	Country="Guatemala",	Surface_area=108889,	Population=11385000,	Life_expectancy="66.2",	Local_name="Guatemala",	Government_form="Republic",	Head_of_state="Alfonso Portillo Cabrera"),
                         CountryAttributes(	Id=90,	Code="GIN",	Country="Guinea",	Surface_area=245857,	Population=7430000,	Life_expectancy="45.6",	Local_name="Guinee",	Government_form="Republic",	Head_of_state="Lansana Conte"),
                         CountryAttributes(	Id=91,	Code="GNB",	Country="Guinea-Bissau",	Surface_area=36125,	Population=1213000,	Life_expectancy="49",	Local_name="Guine-Bissau",	Government_form="Republic",	Head_of_state="Kumba Iala"),
                         CountryAttributes(	Id=92,	Code="GuY",	Country="Guyana",	Surface_area=214969,	Population=861000,	Life_expectancy="64",	Local_name="Guyana",	Government_form="Republic",	Head_of_state="Bharrat Jagdeo"),
                         CountryAttributes(	Id=93,	Code="HTI",	Country="Haiti",	Surface_area=27750,	Population=8222000,	Life_expectancy="49.2",	Local_name="Haiti/Dayti",	Government_form="Republic",	Head_of_state="Jean-Bertrand Aristide"),
                         CountryAttributes(	Id=94,	Code="HMD",	Country="Heard Island and McDonald Islands",	Surface_area=359,	Population=0,	Life_expectancy="NuLL",	Local_name="Heard and McDonald Islands",	Government_form="Territory of Australia",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=95,	Code="VAT",	Country="Holy See (Vatican City State)",	Surface_area=0.4,	Population=1000,	Life_expectancy="NuLL",	Local_name="Santa Sede/Citta del Vaticano",	Government_form="Independent Church State",	Head_of_state="Johannes Paavali II"),
                         CountryAttributes(	Id=96,	Code="HND",	Country="Honduras",	Surface_area=112088,	Population=6485000,	Life_expectancy="69.9",	Local_name="Honduras",	Government_form="Republic",	Head_of_state="Carlos Roberto Flores Facusse"),
                         CountryAttributes(	Id=97,	Code="HKG",	Country="Hong Kong",	Surface_area=1075,	Population=6782000,	Life_expectancy="79.5",	Local_name="Xianggang/Hong Kong",	Government_form="Special Administrative Region of China",	Head_of_state="Jiang Zemin"),
                         CountryAttributes(	Id=98,	Code="HuN",	Country="Hungary",	Surface_area=93030,	Population=10043200,	Life_expectancy="71.4",	Local_name="Magyarorszag",	Government_form="Republic",	Head_of_state="Ferenc Madl"),
                         CountryAttributes(	Id=99,	Code="ISL",	Country="Iceland",	Surface_area=103000,	Population=279000,	Life_expectancy="79.4",	Local_name="Island",	Government_form="Republic",	Head_of_state="olafur Ragnar GrImsson"),
                         CountryAttributes(	Id=100,	Code="IND",	Country="India",	Surface_area=3287263,	Population=1013662000,	Life_expectancy="62.5",	Local_name="Bharat/India",	Government_form="Federal Republic",	Head_of_state="Kocheril Raman Narayanan"),
                         CountryAttributes(	Id=101,	Code="IDN",	Country="Indonesia",	Surface_area=1904569,	Population=212107000,	Life_expectancy="68",	Local_name="Indonesia",	Government_form="Republic",	Head_of_state="Abdurrahman Wahid"),
                         CountryAttributes(	Id=102,	Code="IRN",	Country="Iran",	Surface_area=1648195,	Population=67702000,	Life_expectancy="69.7",	Local_name="Iran",	Government_form="Islamic Republic",	Head_of_state="Ali Mohammad Khatami-Ardakani"),
                         CountryAttributes(	Id=103,	Code="IRQ",	Country="Iraq",	Surface_area=438317,	Population=23115000,	Life_expectancy="66.5",	Local_name="Al- Iraq",	Government_form="Republic",	Head_of_state="Saddam Hussein al-Takriti"),
                         CountryAttributes(	Id=104,	Code="IRL",	Country="Ireland",	Surface_area=70273,	Population=3775100,	Life_expectancy="76.8",	Local_name="Ireland/eire",	Government_form="Republic",	Head_of_state="Mary McAleese"),
                         CountryAttributes(	Id=105,	Code="ISR",	Country="Israel",	Surface_area=21056,	Population=6217000,	Life_expectancy="78.6",	Local_name="Yisrael/Israil",	Government_form="Republic",	Head_of_state="Moshe Katzav"),
                         CountryAttributes(	Id=106,	Code="ITA",	Country="Italy",	Surface_area=301316,	Population=57680000,	Life_expectancy="79",	Local_name="Italia",	Government_form="Republic",	Head_of_state="Carlo Azeglio Ciampi"),
                         CountryAttributes(	Id=107,	Code="JAM",	Country="Jamaica",	Surface_area=10990,	Population=2583000,	Life_expectancy="75.2",	Local_name="Jamaica",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=108,	Code="JPN",	Country="Japan",	Surface_area=377829,	Population=126714000,	Life_expectancy="80.7",	Local_name="Nihon/Nippon",	Government_form="Constitutional Monarchy",	Head_of_state="Akihito"),
                         CountryAttributes(	Id=109,	Code="JOR",	Country="Jordan",	Surface_area=88946,	Population=5083000,	Life_expectancy="77.4",	Local_name="Al-urdunn",	Government_form="Constitutional Monarchy",	Head_of_state="Abdullah II"),
                         CountryAttributes(	Id=110,	Code="KAZ",	Country="Kazakstan",	Surface_area=2724900,	Population=16223000,	Life_expectancy="63.2",	Local_name="Qazaqstan",	Government_form="Republic",	Head_of_state="Nursultan Nazarbajev"),
                         CountryAttributes(	Id=111,	Code="KEN",	Country="Kenya",	Surface_area=580367,	Population=30080000,	Life_expectancy="48",	Local_name="Kenya",	Government_form="Republic",	Head_of_state="Daniel arap Moi"),
                         CountryAttributes(	Id=112,	Code="KIR",	Country="Kiribati",	Surface_area=726,	Population=83000,	Life_expectancy="59.8",	Local_name="Kiribati",	Government_form="Republic",	Head_of_state="Teburoro Tito"),
                         CountryAttributes(	Id=113,	Code="KWT",	Country="Kuwait",	Surface_area=17818,	Population=1972000,	Life_expectancy="76.1",	Local_name="Al-Kuwayt",	Government_form="Constitutional Monarchy (Emirate)",	Head_of_state="Jabir al-Ahmad al-Jabir al-Sabah"),
                         CountryAttributes(	Id=114,	Code="KGZ",	Country="Kyrgyzstan",	Surface_area=199900,	Population=4699000,	Life_expectancy="63.4",	Local_name="Kyrgyzstan",	Government_form="Republic",	Head_of_state="Askar Akajev"),
                         CountryAttributes(	Id=115,	Code="LAO",	Country="Laos",	Surface_area=236800,	Population=5433000,	Life_expectancy="53.1",	Local_name="Lao",	Government_form="Republic",	Head_of_state="Khamtay Siphandone"),
                         CountryAttributes(	Id=116,	Code="LVA",	Country="Latvia",	Surface_area=64589,	Population=2424200,	Life_expectancy="68.4",	Local_name="Latvija",	Government_form="Republic",	Head_of_state="Vaira Vike-Freiberga"),
                         CountryAttributes(	Id=117,	Code="LBN",	Country="Lebanon",	Surface_area=10400,	Population=3282000,	Life_expectancy="71.3",	Local_name="Lubnan",	Government_form="Republic",	Head_of_state="emile Lahoud"),
                         CountryAttributes(	Id=118,	Code="LSO",	Country="Lesotho",	Surface_area=30355,	Population=2153000,	Life_expectancy="50.8",	Local_name="Lesotho",	Government_form="Constitutional Monarchy",	Head_of_state="Letsie III"),
                         CountryAttributes(	Id=119,	Code="LBR",	Country="Liberia",	Surface_area=111369,	Population=3154000,	Life_expectancy="51",	Local_name="Liberia",	Government_form="Republic",	Head_of_state="Charles Taylor"),
                         CountryAttributes(	Id=120,	Code="LBY",	Country="Libyan Arab Jamahiriya",	Surface_area=1759540,	Population=5605000,	Life_expectancy="75.5",	Local_name="Libiya",	Government_form="Socialistic State",	Head_of_state="Muammar al-Qadhafi"),
                         CountryAttributes(	Id=121,	Code="LIE",	Country="Liechtenstein",	Surface_area=160,	Population=32300,	Life_expectancy="78.8",	Local_name="Liechtenstein",	Government_form="Constitutional Monarchy",	Head_of_state="Hans-Adam II"),
                         CountryAttributes(	Id=122,	Code="LTu",	Country="Lithuania",	Surface_area=65301,	Population=3698500,	Life_expectancy="69.1",	Local_name="Lietuva",	Government_form="Republic",	Head_of_state="Valdas Adamkus"),
                         CountryAttributes(	Id=123,	Code="LuX",	Country="Luxembourg",	Surface_area=2586,	Population=435700,	Life_expectancy="77.1",	Local_name="Luxembourg/Letzebuerg",	Government_form="Constitutional Monarchy",	Head_of_state="Henri"),
                         CountryAttributes(	Id=124,	Code="MAC",	Country="Macao",	Surface_area=18,	Population=473000,	Life_expectancy="81.6",	Local_name="Macau/Aomen",	Government_form="Special Administrative Region of China",	Head_of_state="Jiang Zemin"),
                         CountryAttributes(	Id=125,	Code="MKD",	Country="Macedonia",	Surface_area=25713,	Population=2024000,	Life_expectancy="73.8",	Local_name="Makedonija",	Government_form="Republic",	Head_of_state="Boris Trajkovski"),
                         CountryAttributes(	Id=126,	Code="MDG",	Country="Madagascar",	Surface_area=587041,	Population=15942000,	Life_expectancy="55",	Local_name="Madagasikara/Madagascar",	Government_form="Federal Republic",	Head_of_state="Didier Ratsiraka"),
                         CountryAttributes(	Id=127,	Code="MWI",	Country="Malawi",	Surface_area=118484,	Population=10925000,	Life_expectancy="37.6",	Local_name="Malawi",	Government_form="Republic",	Head_of_state="Bakili Muluzi"),
                         CountryAttributes(	Id=128,	Code="MYS",	Country="Malaysia",	Surface_area=329758,	Population=22244000,	Life_expectancy="70.8",	Local_name="Malaysia",	Government_form="Constitutional Monarchy, Federation",	Head_of_state="Salahuddin Abdul Aziz Shah Alhaj"),
                         CountryAttributes(	Id=129,	Code="MDV",	Country="Maldives",	Surface_area=298,	Population=286000,	Life_expectancy="62.2",	Local_name="Dhivehi Raajje/Maldives",	Government_form="Republic",	Head_of_state="Maumoon Abdul Gayoom"),
                         CountryAttributes(	Id=130,	Code="MLI",	Country="Mali",	Surface_area=1240192,	Population=11234000,	Life_expectancy="46.7",	Local_name="Mali",	Government_form="Republic",	Head_of_state="Alpha Oumar Konare"),
                         CountryAttributes(	Id=131,	Code="MLT",	Country="Malta",	Surface_area=316,	Population=380200,	Life_expectancy="77.9",	Local_name="Malta",	Government_form="Republic",	Head_of_state="Guido de Marco"),
                         CountryAttributes(	Id=132,	Code="MHL",	Country="Marshall Islands",	Surface_area=181,	Population=64000,	Life_expectancy="65.5",	Local_name="Marshall Islands/Majol",	Government_form="Republic",	Head_of_state="Kessai Note"),
                         CountryAttributes(	Id=133,	Code="MTQ",	Country="Martinique",	Surface_area=1102,	Population=395000,	Life_expectancy="78.3",	Local_name="Martinique",	Government_form="Overseas Department of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=134,	Code="MRT",	Country="Mauritania",	Surface_area=1025520,	Population=2670000,	Life_expectancy="50.8",	Local_name="Muritaniya/Mauritanie",	Government_form="Republic",	Head_of_state="Maaouiya Ould Sid Ahmad Taya"),
                         CountryAttributes(	Id=135,	Code="MuS",	Country="Mauritius",	Surface_area=2040,	Population=1158000,	Life_expectancy="71",	Local_name="Mauritius",	Government_form="Republic",	Head_of_state="Cassam uteem"),
                         CountryAttributes(	Id=136,	Code="MYT",	Country="Mayotte",	Surface_area=373,	Population=149000,	Life_expectancy="59.5",	Local_name="Mayotte",	Government_form="Territorial Collectivity of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=137,	Code="MEX",	Country="Mexico",	Surface_area=1958201,	Population=98881000,	Life_expectancy="71.5",	Local_name="Mexico",	Government_form="Federal Republic",	Head_of_state="Vicente Fox Quesada"),
                         CountryAttributes(	Id=138,	Code="FSM",	Country="Micronesia, Federated States of",	Surface_area=702,	Population=119000,	Life_expectancy="68.6",	Local_name="Micronesia",	Government_form="Federal Republic",	Head_of_state="Leo A. Falcam"),
                         CountryAttributes(	Id=139,	Code="MDA",	Country="Moldova",	Surface_area=33851,	Population=4380000,	Life_expectancy="64.5",	Local_name="Moldova",	Government_form="Republic",	Head_of_state="Vladimir Voronin"),
                         CountryAttributes(	Id=140,	Code="MCO",	Country="Monaco",	Surface_area=1.5,	Population=34000,	Life_expectancy="78.8",	Local_name="Monaco",	Government_form="Constitutional Monarchy",	Head_of_state="Rainier III"),
                         CountryAttributes(	Id=141,	Code="MNG",	Country="Mongolia",	Surface_area=1566500,	Population=2662000,	Life_expectancy="67.3",	Local_name="Mongol uls",	Government_form="Republic",	Head_of_state="Natsagiin Bagabandi"),
                         CountryAttributes(	Id=142,	Code="MSR",	Country="Montserrat",	Surface_area=102,	Population=11000,	Life_expectancy="78",	Local_name="Montserrat",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=143,	Code="MAR",	Country="Morocco",	Surface_area=446550,	Population=28351000,	Life_expectancy="69.1",	Local_name="Al-Maghrib",	Government_form="Constitutional Monarchy",	Head_of_state="Mohammed VI"),
                         CountryAttributes(	Id=144,	Code="MOZ",	Country="Mozambique",	Surface_area=801590,	Population=19680000,	Life_expectancy="37.5",	Local_name="Mocambique",	Government_form="Republic",	Head_of_state="JoaquIm A. Chissano"),
                         CountryAttributes(	Id=145,	Code="MMR",	Country="Myanmar",	Surface_area=676578,	Population=45611000,	Life_expectancy="54.9",	Local_name="Myanma Pye",	Government_form="Republic",	Head_of_state="kenraali Than Shwe"),
                         CountryAttributes(	Id=146,	Code="NAM",	Country="Namibia",	Surface_area=824292,	Population=1726000,	Life_expectancy="42.5",	Local_name="Namibia",	Government_form="Republic",	Head_of_state="Sam Nujoma"),
                         CountryAttributes(	Id=147,	Code="NRu",	Country="Nauru",	Surface_area=21,	Population=12000,	Life_expectancy="60.8",	Local_name="Naoero/Nauru",	Government_form="Republic",	Head_of_state="Bernard Dowiyogo"),
                         CountryAttributes(	Id=148,	Code="NPL",	Country="Nepal",	Surface_area=147181,	Population=23930000,	Life_expectancy="57.8",	Local_name="Nepal",	Government_form="Constitutional Monarchy",	Head_of_state="Gyanendra Bir Bikram"),
                         CountryAttributes(	Id=149,	Code="NLD",	Country="Netherlands",	Surface_area=41526,	Population=15864000,	Life_expectancy="78.3",	Local_name="Nederland",	Government_form="Constitutional Monarchy",	Head_of_state="Willem-Alexander"),
                         CountryAttributes(	Id=150,	Code="ANT",	Country="Netherlands Antilles",	Surface_area=800,	Population=217000,	Life_expectancy="74.7",	Local_name="Nederlandse Antillen",	Government_form="Nonmetropolitan Territory of The Netherlands",	Head_of_state="Willem-Alexander"),
                         CountryAttributes(	Id=151,	Code="NCL",	Country="New Caledonia",	Surface_area=18575,	Population=214000,	Life_expectancy="72.8",	Local_name="Nouvelle-Caledonie",	Government_form="Nonmetropolitan Territory of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=152,	Code="NZL",	Country="New Zealand",	Surface_area=270534,	Population=3862000,	Life_expectancy="77.8",	Local_name="New Zealand/Aotearoa",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=153,	Code="NIC",	Country="Nicaragua",	Surface_area=130000,	Population=5074000,	Life_expectancy="68.7",	Local_name="Nicaragua",	Government_form="Republic",	Head_of_state="Arnoldo Aleman Lacayo"),
                         CountryAttributes(	Id=154,	Code="NER",	Country="Niger",	Surface_area=1267000,	Population=10730000,	Life_expectancy="41.3",	Local_name="Niger",	Government_form="Republic",	Head_of_state="Mamadou Tandja"),
                         CountryAttributes(	Id=155,	Code="NGA",	Country="Nigeria",	Surface_area=923768,	Population=111506000,	Life_expectancy="51.6",	Local_name="Nigeria",	Government_form="Federal Republic",	Head_of_state="Olusegun Obasanjo"),
                         CountryAttributes(	Id=156,	Code="NIu",	Country="Niue",	Surface_area=260,	Population=2000,	Life_expectancy="NuLL",	Local_name="Niue",	Government_form="Nonmetropolitan Territory of New Zealand",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=157,	Code="NFK",	Country="Norfolk Island",	Surface_area=36,	Population=2000,	Life_expectancy="NuLL",	Local_name="Norfolk Island",	Government_form="Territory of Australia",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=158,	Code="PRK",	Country="North Korea",	Surface_area=120538,	Population=24039000,	Life_expectancy="70.7",	Local_name="Choson Minjujuui In min Konghwaguk (Bukhan)",	Government_form="Socialistic Republic",	Head_of_state="Kim Jong-il"),
                         CountryAttributes(	Id=159,	Code="MNP",	Country="Northern Mariana Islands",	Surface_area=464,	Population=78000,	Life_expectancy="75.5",	Local_name="Northern Mariana Islands",	Government_form="Commonwealth of the uS",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=160,	Code="NOR",	Country="Norway",	Surface_area=323877,	Population=4478500,	Life_expectancy="78.7",	Local_name="Norge",	Government_form="Constitutional Monarchy",	Head_of_state="Harald V"),
                         CountryAttributes(	Id=161,	Code="OMN",	Country="Oman",	Surface_area=309500,	Population=2542000,	Life_expectancy="71.8",	Local_name="uman",	Government_form="Monarchy (Sultanate)",	Head_of_state="Qabus ibn Sa id"),
                         CountryAttributes(	Id=162,	Code="PAK",	Country="Pakistan",	Surface_area=796095,	Population=156483000,	Life_expectancy="61.1",	Local_name="Pakistan",	Government_form="Republic",	Head_of_state="Mohammad Rafiq Tarar"),
                         CountryAttributes(	Id=163,	Code="PLW",	Country="Palau",	Surface_area=459,	Population=19000,	Life_expectancy="68.6",	Local_name="Belau/Palau",	Government_form="Republic",	Head_of_state="Kuniwo Nakamura"),
                         CountryAttributes(	Id=164,	Code="PSE",	Country="Palestine",	Surface_area=6257,	Population=3101000,	Life_expectancy="71.4",	Local_name="Filastin",	Government_form="Autonomous Area",	Head_of_state="Yasser (Yasir) Arafat"),
                         CountryAttributes(	Id=165,	Code="PAN",	Country="Panama",	Surface_area=75517,	Population=2856000,	Life_expectancy="75.5",	Local_name="Panama",	Government_form="Republic",	Head_of_state="Mireya Elisa Moscoso RodrIguez"),
                         CountryAttributes(	Id=166,	Code="PNG",	Country="Papua New Guinea",	Surface_area=462840,	Population=4807000,	Life_expectancy="63.1",	Local_name="Papua New Guinea/Papua Niugini",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=167,	Code="PRY",	Country="Paraguay",	Surface_area=406752,	Population=5496000,	Life_expectancy="73.7",	Local_name="Paraguay",	Government_form="Republic",	Head_of_state="Luis angel Gonzalez Macchi"),
                         CountryAttributes(	Id=168,	Code="PER",	Country="Peru",	Surface_area=1285216,	Population=25662000,	Life_expectancy="70",	Local_name="Peru/Piruw",	Government_form="Republic",	Head_of_state="Valentin Paniagua Corazao"),
                         CountryAttributes(	Id=169,	Code="PHL",	Country="Philippines",	Surface_area=300000,	Population=75967000,	Life_expectancy="67.5",	Local_name="Pilipinas",	Government_form="Republic",	Head_of_state="Gloria Macapagal-Arroyo"),
                         CountryAttributes(	Id=170,	Code="PCN",	Country="Pitcairn",	Surface_area=49,	Population=50,	Life_expectancy="NuLL",	Local_name="Pitcairn",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=171,	Code="POL",	Country="Poland",	Surface_area=323250,	Population=38653600,	Life_expectancy="73.2",	Local_name="Polska",	Government_form="Republic",	Head_of_state="Aleksander Kwasniewski"),
                         CountryAttributes(	Id=172,	Code="PRT",	Country="Portugal",	Surface_area=91982,	Population=9997600,	Life_expectancy="75.8",	Local_name="Portugal",	Government_form="Republic",	Head_of_state="Jorge Sampaio"),
                         CountryAttributes(	Id=173,	Code="PRI",	Country="Puerto Rico",	Surface_area=8875,	Population=3869000,	Life_expectancy="75.6",	Local_name="Puerto Rico",	Government_form="Commonwealth of the uS",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=174,	Code="QAT",	Country="Qatar",	Surface_area=11000,	Population=599000,	Life_expectancy="72.4",	Local_name="Qatar",	Government_form="Monarchy",	Head_of_state="Hamad ibn Khalifa al-Thani"),
                         CountryAttributes(	Id=175,	Code="REu",	Country="Reunion",	Surface_area=2510,	Population=699000,	Life_expectancy="72.7",	Local_name="Reunion",	Government_form="Overseas Department of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=176,	Code="ROM",	Country="Romania",	Surface_area=238391,	Population=22455500,	Life_expectancy="69.9",	Local_name="Romania",	Government_form="Republic",	Head_of_state="Ion Iliescu"),
                         CountryAttributes(	Id=177,	Code="RuS",	Country="Russian Federation",	Surface_area=17075400,	Population=146934000,	Life_expectancy="67.2",	Local_name="Rossija",	Government_form="Federal Republic",	Head_of_state="Vladimir Putin"),
                         CountryAttributes(	Id=178,	Code="RWA",	Country="Rwanda",	Surface_area=26338,	Population=7733000,	Life_expectancy="39.3",	Local_name="Rwanda/urwanda",	Government_form="Republic",	Head_of_state="Paul Kagame"),
                         CountryAttributes(	Id=179,	Code="SHN",	Country="Saint Helena",	Surface_area=314,	Population=6000,	Life_expectancy="76.8",	Local_name="Saint Helena",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=180,	Code="KNA",	Country="Saint Kitts and Nevis",	Surface_area=261,	Population=38000,	Life_expectancy="70.7",	Local_name="Saint Kitts and Nevis",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=181,	Code="LCA",	Country="Saint Lucia",	Surface_area=622,	Population=154000,	Life_expectancy="72.3",	Local_name="Saint Lucia",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=182,	Code="SPM",	Country="Saint Pierre and Miquelon",	Surface_area=242,	Population=7000,	Life_expectancy="77.6",	Local_name="Saint-Pierre-et-Miquelon",	Government_form="Territorial Collectivity of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=183,	Code="VCT",	Country="Saint Vincent and the Grenadines",	Surface_area=388,	Population=114000,	Life_expectancy="72.3",	Local_name="Saint Vincent and the Grenadines",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=184,	Code="WSM",	Country="Samoa",	Surface_area=2831,	Population=180000,	Life_expectancy="69.2",	Local_name="Samoa",	Government_form="Parlementary Monarchy",	Head_of_state="Malietoa Tanumafili II"),
                         CountryAttributes(	Id=185,	Code="SMR",	Country="San Marino",	Surface_area=61,	Population=27000,	Life_expectancy="81.1",	Local_name="San Marino",	Government_form="Republic",	Head_of_state="NuLL"),
                         CountryAttributes(	Id=186,	Code="STP",	Country="Sao Tome and Principe",	Surface_area=964,	Population=147000,	Life_expectancy="65.3",	Local_name="Sao Tome e PrIncipe",	Government_form="Republic",	Head_of_state="Miguel Trovoada"),
                         CountryAttributes(	Id=187,	Code="SAu",	Country="Saudi Arabia",	Surface_area=2149690,	Population=21607000,	Life_expectancy="67.8",	Local_name="Al- Arabiya as-Sa udiya",	Government_form="Monarchy",	Head_of_state="Fahd ibn Abdul-Aziz al-Sa ud"),
                         CountryAttributes(	Id=188,	Code="SEN",	Country="Senegal",	Surface_area=196722,	Population=9481000,	Life_expectancy="62.2",	Local_name="Senegal/Sounougal",	Government_form="Republic",	Head_of_state="Abdoulaye Wade"),
                         CountryAttributes(	Id=189,	Code="SYC",	Country="Seychelles",	Surface_area=455,	Population=77000,	Life_expectancy="70.4",	Local_name="Sesel/Seychelles",	Government_form="Republic",	Head_of_state="France-Albert Rene"),
                         CountryAttributes(	Id=190,	Code="SLE",	Country="Sierra Leone",	Surface_area=71740,	Population=4854000,	Life_expectancy="45.3",	Local_name="Sierra Leone",	Government_form="Republic",	Head_of_state="Ahmed Tejan Kabbah"),
                         CountryAttributes(	Id=191,	Code="SGP",	Country="Singapore",	Surface_area=618,	Population=3567000,	Life_expectancy="80.1",	Local_name="Singapore/Singapura/Xinjiapo/Singapur",	Government_form="Republic",	Head_of_state="Sellapan Rama Nathan"),
                         CountryAttributes(	Id=192,	Code="SVK",	Country="Slovakia",	Surface_area=49012,	Population=5398700,	Life_expectancy="73.7",	Local_name="Slovensko",	Government_form="Republic",	Head_of_state="Rudolf Schuster"),
                         CountryAttributes(	Id=193,	Code="SVN",	Country="Slovenia",	Surface_area=20256,	Population=1987800,	Life_expectancy="74.9",	Local_name="Slovenija",	Government_form="Republic",	Head_of_state="Milan Kucan"),
                         CountryAttributes(	Id=194,	Code="SLB",	Country="Solomon Islands",	Surface_area=28896,	Population=444000,	Life_expectancy="71.3",	Local_name="Solomon Islands",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=195,	Code="SOM",	Country="Somalia",	Surface_area=637657,	Population=10097000,	Life_expectancy="46.2",	Local_name="Soomaaliya",	Government_form="Republic",	Head_of_state="Abdiqassim Salad Hassan"),
                         CountryAttributes(	Id=196,	Code="ZAF",	Country="South Africa",	Surface_area=1221037,	Population=40377000,	Life_expectancy="51.1",	Local_name="South Africa",	Government_form="Republic",	Head_of_state="Thabo Mbeki"),
                         CountryAttributes(	Id=197,	Code="SGS",	Country="South Georgia and the South Sandwich Islands",	Surface_area=3903,	Population=0,	Life_expectancy="NuLL",	Local_name="South Georgia and the South Sandwich Islands",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=198,	Code="KOR",	Country="South Korea",	Surface_area=99434,	Population=46844000,	Life_expectancy="74.4",	Local_name="Taehan Minguk (Namhan)",	Government_form="Republic",	Head_of_state="Kim Dae-jung"),
                         CountryAttributes(	Id=199,	Code="ESP",	Country="Spain",	Surface_area=505992,	Population=39441700,	Life_expectancy="78.8",	Local_name="Espana",	Government_form="Constitutional Monarchy",	Head_of_state="Juan Carlos I"),
                         CountryAttributes(	Id=200,	Code="LKA",	Country="Sri Lanka",	Surface_area=65610,	Population=18827000,	Life_expectancy="71.8",	Local_name="Sri Lanka/Ilankai",	Government_form="Republic",	Head_of_state="Chandrika Kumaratunga"),
                         CountryAttributes(	Id=201,	Code="SDN",	Country="Sudan",	Surface_area=2505813,	Population=29490000,	Life_expectancy="56.6",	Local_name="As-Sudan",	Government_form="Islamic Republic",	Head_of_state="Omar Hassan Ahmad al-Bashir"),
                         CountryAttributes(	Id=202,	Code="SuR",	Country="Suriname",	Surface_area=163265,	Population=417000,	Life_expectancy="71.4",	Local_name="Suriname",	Government_form="Republic",	Head_of_state="Ronald Venetiaan"),
                         CountryAttributes(	Id=203,	Code="SJM",	Country="Svalbard and Jan Mayen",	Surface_area=62422,	Population=3200,	Life_expectancy="NuLL",	Local_name="Svalbard og Jan Mayen",	Government_form="Dependent Territory of Norway",	Head_of_state="Harald V"),
                         CountryAttributes(	Id=204,	Code="SWZ",	Country="Swaziland",	Surface_area=17364,	Population=1008000,	Life_expectancy="40.4",	Local_name="kaNgwane",	Government_form="Monarchy",	Head_of_state="Mswati III"),
                         CountryAttributes(	Id=205,	Code="SWE",	Country="Sweden",	Surface_area=449964,	Population=8861400,	Life_expectancy="79.6",	Local_name="Sverige",	Government_form="Constitutional Monarchy",	Head_of_state="Carl XVI Gustaf"),
                         CountryAttributes(	Id=206,	Code="CHE",	Country="Switzerland",	Surface_area=41284,	Population=7160400,	Life_expectancy="79.6",	Local_name="Schweiz/Suisse/Svizzera/Svizra",	Government_form="Federation",	Head_of_state="Adolf Ogi"),
                         CountryAttributes(	Id=207,	Code="SYR",	Country="Syria",	Surface_area=185180,	Population=16125000,	Life_expectancy="68.5",	Local_name="Suriya",	Government_form="Republic",	Head_of_state="Bashar al-Assad"),
                         CountryAttributes(	Id=208,	Code="TWN",	Country="Taiwan",	Surface_area=36188,	Population=22256000,	Life_expectancy="76.4",	Local_name="Tai-wan",	Government_form="Republic",	Head_of_state="Chen Shui-bian"),
                         CountryAttributes(	Id=209,	Code="TJK",	Country="Tajikistan",	Surface_area=143100,	Population=6188000,	Life_expectancy="64.1",	Local_name="Tocikiston",	Government_form="Republic",	Head_of_state="Emomali Rahmonov"),
                         CountryAttributes(	Id=210,	Code="TZA",	Country="Tanzania",	Surface_area=883749,	Population=33517000,	Life_expectancy="52.3",	Local_name="Tanzania",	Government_form="Republic",	Head_of_state="Benjamin William Mkapa"),
                         CountryAttributes(	Id=211,	Code="THA",	Country="Thailand",	Surface_area=513115,	Population=61399000,	Life_expectancy="68.6",	Local_name="Prathet Thai",	Government_form="Constitutional Monarchy",	Head_of_state="Bhumibol Adulyadej"),
                         CountryAttributes(	Id=212,	Code="TGO",	Country="Togo",	Surface_area=56785,	Population=4629000,	Life_expectancy="54.7",	Local_name="Togo",	Government_form="Republic",	Head_of_state="Gnassingbe Eyadema"),
                         CountryAttributes(	Id=213,	Code="TKL",	Country="Tokelau",	Surface_area=12,	Population=2000,	Life_expectancy="NuLL",	Local_name="Tokelau",	Government_form="Nonmetropolitan Territory of New Zealand",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=214,	Code="TON",	Country="Tonga",	Surface_area=650,	Population=99000,	Life_expectancy="67.9",	Local_name="Tonga",	Government_form="Monarchy",	Head_of_state="Taufa'ahau Tupou IV"),
                         CountryAttributes(	Id=215,	Code="TTO",	Country="Trinidad and Tobago",	Surface_area=5130,	Population=1295000,	Life_expectancy="68",	Local_name="Trinidad and Tobago",	Government_form="Republic",	Head_of_state="Arthur N. R. Robinson"),
                         CountryAttributes(	Id=216,	Code="TuN",	Country="Tunisia",	Surface_area=163610,	Population=9586000,	Life_expectancy="73.7",	Local_name="Tunis/Tunisie",	Government_form="Republic",	Head_of_state="Zine al-Abidine Ben Ali"),
                         CountryAttributes(	Id=217,	Code="TuR",	Country="Turkey",	Surface_area=774815,	Population=66591000,	Life_expectancy="71",	Local_name="Turkiye",	Government_form="Republic",	Head_of_state="Ahmet Necdet Sezer"),
                         CountryAttributes(	Id=218,	Code="TKM",	Country="Turkmenistan",	Surface_area=488100,	Population=4459000,	Life_expectancy="60.9",	Local_name="Turkmenostan",	Government_form="Republic",	Head_of_state="Saparmurad Nijazov"),
                         CountryAttributes(	Id=219,	Code="TCA",	Country="Turks and Caicos Islands",	Surface_area=430,	Population=17000,	Life_expectancy="73.3",	Local_name="The Turks and Caicos Islands",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=220,	Code="TuV",	Country="Tuvalu",	Surface_area=26,	Population=12000,	Life_expectancy="66.3",	Local_name="Tuvalu",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=221,	Code="uGA",	Country="uganda",	Surface_area=241038,	Population=21778000,	Life_expectancy="42.9",	Local_name="uganda",	Government_form="Republic",	Head_of_state="Yoweri Museveni"),
                         CountryAttributes(	Id=222,	Code="uKR",	Country="ukraine",	Surface_area=603700,	Population=50456000,	Life_expectancy="66",	Local_name="ukrajina",	Government_form="Republic",	Head_of_state="Leonid KutSma"),
                         CountryAttributes(	Id=223,	Code="ARE",	Country="united Arab Emirates",	Surface_area=83600,	Population=2441000,	Life_expectancy="74.1",	Local_name="Al-Imarat al- Arabiya al-Muttahida",	Government_form="Emirate Federation",	Head_of_state="Zayid bin Sultan al-Nahayan"),
                         CountryAttributes(	Id=224,	Code="GBR",	Country="united Kingdom",	Surface_area=242900,	Population=59623400,	Life_expectancy="77.7",	Local_name="united Kingdom",	Government_form="Constitutional Monarchy",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=225,	Code="uSA",	Country="united States",	Surface_area=9363520,	Population=278357000,	Life_expectancy="77.1",	Local_name="united States",	Government_form="Federal Republic",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=226,	Code="uMI",	Country="united States Minor Outlying Islands",	Surface_area=16,	Population=0,	Life_expectancy="NuLL",	Local_name="united States Minor Outlying Islands",	Government_form="Dependent Territory of the uS",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=227,	Code="uRY",	Country="uruguay",	Surface_area=175016,	Population=3337000,	Life_expectancy="75.2",	Local_name="uruguay",	Government_form="Republic",	Head_of_state="Jorge Batlle Ibanez"),
                         CountryAttributes(	Id=228,	Code="uZB",	Country="uzbekistan",	Surface_area=447400,	Population=24318000,	Life_expectancy="63.7",	Local_name="uzbekiston",	Government_form="Republic",	Head_of_state="Islam Karimov"),
                         CountryAttributes(	Id=229,	Code="VuT",	Country="Vanuatu",	Surface_area=12189,	Population=190000,	Life_expectancy="60.6",	Local_name="Vanuatu",	Government_form="Republic",	Head_of_state="John Bani"),
                         CountryAttributes(	Id=230,	Code="VEN",	Country="Venezuela",	Surface_area=912050,	Population=24170000,	Life_expectancy="73.1",	Local_name="Venezuela",	Government_form="Federal Republic",	Head_of_state="Hugo Chavez FrIas"),
                         CountryAttributes(	Id=231,	Code="VNM",	Country="Vietnam",	Surface_area=331689,	Population=79832000,	Life_expectancy="69.3",	Local_name="Viet Nam",	Government_form="Socialistic Republic",	Head_of_state="Tran Duc Luong"),
                         CountryAttributes(	Id=232,	Code="VGB",	Country="Virgin Islands, British",	Surface_area=151,	Population=21000,	Life_expectancy="75.4",	Local_name="British Virgin Islands",	Government_form="Dependent Territory of the uK",	Head_of_state="Elisabeth II"),
                         CountryAttributes(	Id=233,	Code="VIR",	Country="Virgin Islands, u.S.",	Surface_area=347,	Population=93000,	Life_expectancy="78.1",	Local_name="Virgin Islands of the united States",	Government_form="uS Territory",	Head_of_state="George W. Bush"),
                         CountryAttributes(	Id=234,	Code="WLF",	Country="Wallis and Futuna",	Surface_area=200,	Population=15000,	Life_expectancy="NuLL",	Local_name="Wallis-et-Futuna",	Government_form="Nonmetropolitan Territory of France",	Head_of_state="Jacques Chirac"),
                         CountryAttributes(	Id=235,	Code="ESH",	Country="Western Sahara",	Surface_area=266000,	Population=293000,	Life_expectancy="49.8",	Local_name="As-Sahrawiya",	Government_form="Occupied by Marocco",	Head_of_state="Mohammed Abdel Aziz"),
                         CountryAttributes(	Id=236,	Code="YEM",	Country="Yemen",	Surface_area=527968,	Population=18112000,	Life_expectancy="59.8",	Local_name="Al-Yaman",	Government_form="Republic",	Head_of_state="Ali Abdallah Salih"),
                         CountryAttributes(	Id=237,	Code="YuG",	Country="Yugoslavia",	Surface_area=102173,	Population=10640000,	Life_expectancy="72.4",	Local_name="Jugoslavija",	Government_form="Federal Republic",	Head_of_state="Vojislav KoStunica"),
                         CountryAttributes(	Id=238,	Code="ZMB",	Country="Zambia",	Surface_area=752618,	Population=9169000,	Life_expectancy="37.2",	Local_name="Zambia",	Government_form="Republic",	Head_of_state="Frederick Chiluba"),
                         CountryAttributes(	Id=239,	Code="ZWE",	Country="Zimbabwe",	Surface_area=390757,	Population=11669000,	Life_expectancy="37.8",	Local_name="Zimbabwe",	Government_form="Republic",	Head_of_state="Robert G. Mugabe")]


@router.get("/continent/region/country/" , status_code= status.HTTP_200_OK)
async def usersclass():
    return (CountryAttributes_list)
   
#***Get con Filtro Path
@router.get("/continent/region/country/{id}", status_code = status.HTTP_200_OK)
async def usersclass(id:int):
    users=filter (lambda user: user.Id == id, CountryAttributes_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="El pais no fue encontrado")


@router.post("/continent/region/country/",  response_model=CountryAttributes, status_code=status.HTTP_201_CREATED)
async def usersclass(user:CountryAttributes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(CountryAttributes_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="El pais ya existe")
    else:
        CountryAttributes_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/continent/region/country/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryAttributes):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(CountryAttributes_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           CountryAttributes_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe el pais que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/continent/region/country/{id}", status_code= status.HTTP_200_OK)
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(CountryAttributes_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del CountryAttributes_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="El pais se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar el pais")
    