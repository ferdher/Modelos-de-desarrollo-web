from fastapi import *
from pydantic import BaseModel
 
router = APIRouter()
class CountryTable(BaseModel):
    Id:int
    Region:str
    Country:str
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
region_list= [  CountryTable(	Id=1,	        Region="Antarctica",	                    Country="Antarctica"),
                CountryTable(	Id=2,	        Region="Antarctica",	                    Country="French Southern territories"),
                CountryTable(	Id=3,	        Region="Antarctica",	                    Country="Bouvet Island"),
                CountryTable(	Id=4,	        Region="Antarctica",	                    Country="Heard Island and McDonald Islands"),
                CountryTable(	Id=5,	        Region="Antarctica",	                    Country="South Georgia and the South Sandwich Islands"),
                CountryTable(	Id=6,	        Region="Australia and New Zealand",	        Country="Australia"),
                CountryTable(	Id=7,	        Region="Australia and New Zealand",	        Country="Cocos (Keeling) Islands"),
                CountryTable(	Id=8,	        Region="Australia and New Zealand",	        Country="Christmas Island"),
                CountryTable(	Id=9,	        Region="Australia and New Zealand",	        Country="Norfolk Island"),
                CountryTable(	Id=10,	        Region="Australia and New Zealand",	        Country="New Zealand"),
                CountryTable(	Id=11,	        Region="Baltic Countries",	                Country="Estonia"),
                CountryTable(	Id=12,	        Region="Baltic Countries",	                Country="Lithuania"),
                CountryTable(	Id=13,	        Region="Baltic Countries",	                Country="Latvia"),
                CountryTable(	Id=14,	        Region="British Islands",	                Country="united Kingdom"),
                CountryTable(	Id=15,	        Region="British Islands",	                Country="Ireland"),
                CountryTable(	Id=16,	        Region="Caribbean",	                        Country="Anguilla"),
                CountryTable(	Id=17,	        Region="Caribbean",	                        Country="Netherlands Antilles"),
                CountryTable(	Id=18,	        Region="Caribbean",	                        Country="Aruba"),
                CountryTable(	Id=19,	        Region="Caribbean",	                        Country="Antigua and Barbuda"),
                CountryTable(	Id=20,	        Region="Caribbean",	                        Country="Bahamas"),
                CountryTable(	Id=21,	        Region="Caribbean",	                        Country="Barbados"),
                CountryTable(	Id=22,	        Region="Caribbean",	                        Country="Cuba"),
                CountryTable(	Id=23,	        Region="Caribbean",	                        Country="Cayman Islands"),
                CountryTable(	Id=24,	        Region="Caribbean",	                        Country="Dominica"),
                CountryTable(	Id=25,	        Region="Caribbean",	                        Country="Dominican Republic"),
                CountryTable(	Id=26,	        Region="Caribbean",	                        Country="Guadeloupe"),
                CountryTable(	Id=27,	        Region="Caribbean",	                        Country="Grenada"),
                CountryTable(	Id=28,	        Region="Caribbean",	                        Country="Haiti"),
                CountryTable(	Id=29,	        Region="Caribbean",	                        Country="Jamaica"),
                CountryTable(	Id=30,	        Region="Caribbean",	                        Country="Saint Kitts and Nevis"),
                CountryTable(	Id=31,	        Region="Caribbean",	                        Country="Saint Lucia"),
                CountryTable(	Id=32,	        Region="Caribbean",	                        Country="Montserrat"),
                CountryTable(	Id=33,	        Region="Caribbean",	                        Country="Martinique"),
                CountryTable(	Id=34,	        Region="Caribbean",	                        Country="Puerto Rico"),
                CountryTable(	Id=35,	        Region="Caribbean",	                        Country="Turks and Caicos Islands"),
                CountryTable(	Id=36,	        Region="Caribbean",	                        Country="Trinidad and Tobago"),
                CountryTable(	Id=37,	        Region="Caribbean",	                        Country="Saint Vincent and the Grenadines"),
                CountryTable(	Id=38,	        Region="Caribbean",	                        Country="Virgin Islands, British"),
                CountryTable(	Id=39,	        Region="Caribbean",	                        Country="Virgin Islands, u.S."),
                CountryTable(	Id=40,	        Region="Central Africa",	                Country="Angola"),
                CountryTable(	Id=41,	        Region="Central Africa",	                Country="Central African Republic"),
                CountryTable(	Id=42,	        Region="Central Africa",	                Country="Cameroon"),
                CountryTable(	Id=43,	        Region="Central Africa",	                Country="Congo, The Democratic Republic of the"),
                CountryTable(	Id=44,	        Region="Central Africa",	                Country="Congo"),
                CountryTable(	Id=45,	        Region="Central Africa",	                Country="Gabon"),
                CountryTable(	Id=46,	        Region="Central Africa",	                Country="Equatorial Guinea"),
                CountryTable(	Id=47,	        Region="Central Africa",	                Country="Sao Tome and Principe"),
                CountryTable(	Id=48,	        Region="Central Africa",	                Country="Chad"),
                CountryTable(	Id=49,	        Region="Central America",	                Country="Belize"),
                CountryTable(	Id=50,	        Region="Central America",	                Country="Costa Rica"),
                CountryTable(	Id=51,	        Region="Central America",	                Country="Guatemala"),
                CountryTable(	Id=52,	        Region="Central America",	                Country="Honduras"),
                CountryTable(	Id=53,	        Region="Central America",	                Country="Mexico"),
                CountryTable(	Id=54,	        Region="Central America",	                Country="Nicaragua"),
                CountryTable(	Id=55,	        Region="Central America",	                Country="Panama"),
                CountryTable(	Id=56,	        Region="Central America",	                Country="El Salvador"),
                CountryTable(	Id=57,	        Region="Eastern Africa",	                Country="Burundi"),
                CountryTable(	Id=58,	        Region="Eastern Africa",	                Country="Comoros"),
                CountryTable(	Id=59,	        Region="Eastern Africa",	                Country="Djibouti"),
                CountryTable(	Id=60,	        Region="Eastern Africa",	                Country="Eritrea"),
                CountryTable(	Id=61,	        Region="Eastern Africa",	                Country="Ethiopia"),
                CountryTable(	Id=62,	        Region="Eastern Africa",	                Country="British Indian Ocean Territory"),
                CountryTable(	Id=63,	        Region="Eastern Africa",	                Country="Kenya"),
                CountryTable(	Id=64,	        Region="Eastern Africa",	                Country="Madagascar"),
                CountryTable(	Id=65,	        Region="Eastern Africa",	                Country="Mozambique"),
                CountryTable(	Id=66,	        Region="Eastern Africa",	                Country="Mauritius"),
                CountryTable(	Id=67,	        Region="Eastern Africa",	                Country="Malawi"),
                CountryTable(	Id=68,	        Region="Eastern Africa",	                Country="Mayotte"),
                CountryTable(	Id=69,	        Region="Eastern Africa",	                Country="Reunion"),
                CountryTable(	Id=70,	        Region="Eastern Africa",	                Country="Rwanda"),
                CountryTable(	Id=71,	        Region="Eastern Africa",	                Country="Somalia"),
                CountryTable(	Id=72,	        Region="Eastern Africa",	                Country="Seychelles"),
                CountryTable(	Id=73,	        Region="Eastern Africa",	                Country="Tanzania"),
                CountryTable(	Id=74,	        Region="Eastern Africa",	                Country="uganda"),
                CountryTable(	Id=75,	        Region="Eastern Africa",	                Country="Zambia"),
                CountryTable(	Id=76,	        Region="Eastern Africa",	                Country="Zimbabwe"),
                CountryTable(	Id=77,	        Region="Eastern Asia",	                    Country="China"),
                CountryTable(	Id=78,	        Region="Eastern Asia",	                    Country="Hong Kong"),
                CountryTable(	Id=79,	        Region="Eastern Asia",	                    Country="Japan"),
                CountryTable(	Id=80,	        Region="Eastern Asia",	                    Country="South Korea"),
                CountryTable(	Id=81,	        Region="Eastern Asia",	                    Country="Macao"),
                CountryTable(	Id=82,	        Region="Eastern Asia",	                    Country="Mongolia"),
                CountryTable(	Id=83,	        Region="Eastern Asia",	                    Country="North Korea"),
                CountryTable(	Id=84,	        Region="Eastern Asia",	                    Country="Taiwan"),
                CountryTable(	Id=85,	        Region="Eastern Europe",	                Country="Bulgaria"),
                CountryTable(	Id=86,	        Region="Eastern Europe",	                Country="Belarus"),
                CountryTable(	Id=87,	        Region="Eastern Europe",	                Country="Czech Republic"),
                CountryTable(	Id=88,	        Region="Eastern Europe",	                Country="Hungary"),
                CountryTable(	Id=89,	        Region="Eastern Europe",	                Country="Moldova"),
                CountryTable(	Id=90,	        Region="Eastern Europe",	                Country="Poland"),
                CountryTable(	Id=91,	        Region="Eastern Europe",	                Country="Romania"),
                CountryTable(	Id=92,	        Region="Eastern Europe",	                Country="Russian Federation"),
                CountryTable(	Id=93,	        Region="Eastern Europe",	                Country="Slovakia"),
                CountryTable(	Id=94,	        Region="Eastern Europe",	                Country="ukraine"),
                CountryTable(	Id=95,	        Region="Melanesia",	                        Country="Fiji Islands"),
                CountryTable(	Id=96,	        Region="Melanesia",	                        Country="New Caledonia"),
                CountryTable(	Id=97,	        Region="Melanesia",	                        Country="Papua New Guinea"),
                CountryTable(	Id=98,	        Region="Melanesia",	                        Country="Solomon Islands"),
                CountryTable(	Id=99,	        Region="Melanesia",	                        Country="Vanuatu"),
                CountryTable(	Id=100,	        Region="Micronesia",	                    Country="Micronesia, Federated States of"),
                CountryTable(	Id=101,	        Region="Micronesia",	                    Country="Guam"),
                CountryTable(	Id=102,	        Region="Micronesia",	                    Country="Kiribati"),
                CountryTable(	Id=103,	        Region="Micronesia",	                    Country="Marshall Islands"),
                CountryTable(	Id=104,	        Region="Micronesia",	                    Country="Northern Mariana Islands"),
                CountryTable(	Id=105,	        Region="Micronesia",	                    Country="Nauru"),
                CountryTable(	Id=106,	        Region="Micronesia",	                    Country="Palau"),
                CountryTable(	Id=107,	        Region="Micronesia/Caribbean",	            Country="united States Minor Outlying Islands"),
                CountryTable(	Id=108,	        Region="Middle East",	                    Country="Armenia"),
                CountryTable(	Id=109,	        Region="Middle East",	                    Country="Azerbaijan"),
                CountryTable(	Id=110,	        Region="Middle East",	                    Country="Bahrain"),
                CountryTable(	Id=111,	        Region="Middle East",	                    Country="united Arab Emirates"),
                CountryTable(	Id=112,	        Region="Middle East",	                    Country="Cyprus"),
                CountryTable(	Id=113,	        Region="Middle East",	                    Country="Georgia"),
                CountryTable(	Id=114,	        Region="Middle East",	                    Country="Iraq"),
                CountryTable(	Id=115,	        Region="Middle East",	                    Country="Israel"),
                CountryTable(	Id=116,	        Region="Middle East",	                    Country="Jordan"),
                CountryTable(	Id=117,	        Region="Middle East",	                    Country="Kuwait"),
                CountryTable(	Id=118,	        Region="Middle East",	                    Country="Lebanon"),
                CountryTable(	Id=119,	        Region="Middle East",	                    Country="Oman"),
                CountryTable(	Id=120,	        Region="Middle East",	                    Country="Palestine"),
                CountryTable(	Id=121,	        Region="Middle East",	                    Country="Qatar"),
                CountryTable(	Id=122,	        Region="Middle East",	                    Country="Saudi Arabia"),
                CountryTable(	Id=123,	        Region="Middle East",	                    Country="Syria"),
                CountryTable(	Id=124,	        Region="Middle East",	                    Country="Turkey"),
                CountryTable(	Id=125,	        Region="Middle East",	                    Country="Yemen"),
                CountryTable(	Id=126,	        Region="Nordic Countries",	                Country="Denmark"),
                CountryTable(	Id=127,	        Region="Nordic Countries",	                Country="Finland"),
                CountryTable(	Id=128,	        Region="Nordic Countries",	                Country="Faroe Islands"),
                CountryTable(	Id=129,	        Region="Nordic Countries",	                Country="Iceland"),
                CountryTable(	Id=130,	        Region="Nordic Countries",	                Country="Norway"),
                CountryTable(	Id=131,	        Region="Nordic Countries",	                Country="Svalbard and Jan Mayen"),
                CountryTable(	Id=132,	        Region="Nordic Countries",	                Country="Sweden"),
                CountryTable(	Id=133,	        Region="North America",	                    Country="Bermuda"),
                CountryTable(	Id=134,	        Region="North America",	                    Country="Canada"),
                CountryTable(	Id=135,	        Region="North America",	                    Country="Greenland"),
                CountryTable(	Id=136,	        Region="North America",	                    Country="Saint Pierre and Miquelon"),
                CountryTable(	Id=137,	        Region="North America",	                    Country="united States"),
                CountryTable(	Id=138,	        Region="Northern Africa",	                Country="Algeria"),
                CountryTable(	Id=139,	        Region="Northern Africa",	                Country="Egypt"),
                CountryTable(	Id=140,	        Region="Northern Africa",	                Country="Western Sahara"),
                CountryTable(	Id=141,	        Region="Northern Africa",	                Country="Libyan Arab Jamahiriya"),
                CountryTable(	Id=142,	        Region="Northern Africa",	                Country="Morocco"),
                CountryTable(	Id=143,	        Region="Northern Africa",	                Country="Sudan"),
                CountryTable(	Id=144,	        Region="Northern Africa",	                Country="Tunisia"),
                CountryTable(	Id=145,	        Region="Polynesia",	                        Country="American Samoa"),
                CountryTable(	Id=146,	        Region="Polynesia",	                        Country="Cook Islands"),
                CountryTable(	Id=147,	        Region="Polynesia",	                        Country="Niue"),
                CountryTable(	Id=148,	        Region="Polynesia",	                        Country="Pitcairn"),
                CountryTable(	Id=149,	        Region="Polynesia",	                        Country="French Polynesia"),
                CountryTable(	Id=150,	        Region="Polynesia",	                        Country="Tokelau"),
                CountryTable(	Id=151,	        Region="Polynesia",	                        Country="Tonga"),
                CountryTable(	Id=152,	        Region="Polynesia",	                        Country="Tuvalu"),
                CountryTable(	Id=153,	        Region="Polynesia",	                        Country="Wallis and Futuna"),
                CountryTable(	Id=154,	        Region="Polynesia",	                        Country="Samoa"),
                CountryTable(	Id=155,	        Region="South America",	                    Country="Bolivia"),
                CountryTable(	Id=156,	        Region="South America",	                    Country="Brazil"),
                CountryTable(	Id=157,	        Region="South America",	                    Country="Chile"),
                CountryTable(	Id=158,	        Region="South America",	                    Country="Colombia"),
                CountryTable(	Id=159,	        Region="South America",	                    Country="Argentina"),
                CountryTable(	Id=160,	        Region="South America",	                    Country="Ecuador"),
                CountryTable(	Id=161,	        Region="South America",	                    Country="Falkland Islands"),
                CountryTable(	Id=162,	        Region="South America",	                    Country="French Guiana"),
                CountryTable(	Id=163,	        Region="South America",	                    Country="Guyana"),
                CountryTable(	Id=164,	        Region="South America",	                    Country="Peru"),
                CountryTable(	Id=165,	        Region="South America",	                    Country="Paraguay"),
                CountryTable(	Id=166,	        Region="South America",	                    Country="Suriname"),
                CountryTable(	Id=167,	        Region="South America",	                    Country="uruguay"),
                CountryTable(	Id=168,	        Region="South America",	                    Country="Venezuela"),
                CountryTable(	Id=169,	        Region="Southeast Asia",	                Country="Brunei"),
                CountryTable(	Id=170,	        Region="Southeast Asia",	                Country="Indonesia"),
                CountryTable(	Id=171,	        Region="Southeast Asia",	                Country="Cambodia"),
                CountryTable(	Id=172,	        Region="Southeast Asia",	                Country="Laos"),
                CountryTable(	Id=173,	        Region="Southeast Asia",	                Country="Myanmar"),
                CountryTable(	Id=174,	        Region="Southeast Asia",	                Country="Malaysia"),
                CountryTable(	Id=175,	        Region="Southeast Asia",	                Country="Philippines"),
                CountryTable(	Id=176,	        Region="Southeast Asia",	                Country="Singapore"),
                CountryTable(	Id=177,	        Region="Southeast Asia",	                Country="Thailand"),
                CountryTable(	Id=178,	        Region="Southeast Asia",	                Country="East Timor"),
                CountryTable(	Id=179,	        Region="Southeast Asia",	                Country="Vietnam"),
                CountryTable(	Id=180,	        Region="Southern Africa",	                Country="Botswana"),
                CountryTable(	Id=181,	        Region="Southern Africa",	                Country="Lesotho"),
                CountryTable(	Id=182,	        Region="Southern Africa",	                Country="Namibia"),
                CountryTable(	Id=183,	        Region="Southern Africa",	                Country="Swaziland"),
                CountryTable(	Id=184,	        Region="Southern Africa",	                Country="South Africa"),
                CountryTable(	Id=185,	        Region="Southern and Central Asia",	        Country="Bangladesh"),
                CountryTable(	Id=186,	        Region="Southern and Central Asia",	        Country="Bhutan"),
                CountryTable(	Id=187,	        Region="Southern and Central Asia",	        Country="Afghanistan"),
                CountryTable(	Id=188,	        Region="Southern and Central Asia",	        Country="India"),
                CountryTable(	Id=189,	        Region="Southern and Central Asia",	        Country="Iran"),
                CountryTable(	Id=190,	        Region="Southern and Central Asia",	        Country="Kazakstan"),
                CountryTable(	Id=191,	        Region="Southern and Central Asia",	        Country="Kyrgyzstan"),
                CountryTable(	Id=192,	        Region="Southern and Central Asia",	        Country="Sri Lanka"),
                CountryTable(	Id=193,	        Region="Southern and Central Asia",	        Country="Maldives"),
                CountryTable(	Id=194,	        Region="Southern and Central Asia",	        Country="Nepal"),
                CountryTable(	Id=195,	        Region="Southern and Central Asia",	        Country="Pakistan"),
                CountryTable(	Id=196,	        Region="Southern and Central Asia",	        Country="Tajikistan"),
                CountryTable(	Id=197,	        Region="Southern and Central Asia",	        Country="Turkmenistan"),
                CountryTable(	Id=198,	        Region="Southern and Central Asia",	        Country="uzbekistan"),
                CountryTable(	Id=199,	        Region="Southern Europe",	                Country="Andorra"),
                CountryTable(	Id=200,	        Region="Southern Europe",	                Country="Bosnia and Herzegovina"),
                CountryTable(	Id=201,	        Region="Southern Europe",	                Country="Spain"),
                CountryTable(	Id=202,	        Region="Southern Europe",	                Country="Albania"),
                CountryTable(	Id=203,	        Region="Southern Europe",	                Country="Gibraltar"),
                CountryTable(	Id=204,	        Region="Southern Europe",	                Country="Greece"),
                CountryTable(	Id=205,	        Region="Southern Europe",	                Country="Croatia"),
                CountryTable(	Id=206,	        Region="Southern Europe",	                Country="Italy"),
                CountryTable(	Id=207,	        Region="Southern Europe",	                Country="Macedonia"),
                CountryTable(	Id=208,	        Region="Southern Europe",	                Country="Malta"),
                CountryTable(	Id=209,	        Region="Southern Europe",	                Country="Portugal"),
                CountryTable(	Id=210,	        Region="Southern Europe",	                Country="San Marino"),
                CountryTable(	Id=211,	        Region="Southern Europe",	                Country="Slovenia"),
                CountryTable(	Id=212,	        Region="Southern Europe",	                Country="Holy See (Vatican City State)"),
                CountryTable(	Id=213,	        Region="Southern Europe",	                Country="Yugoslavia"),
                CountryTable(	Id=214,	        Region="Western Africa",	                Country="Burkina Faso"),
                CountryTable(	Id=215,	        Region="Western Africa",	                Country="Cote dIvoire"),
                CountryTable(	Id=216,	        Region="Western Africa",	                Country="Cape Verde"),
                CountryTable(	Id=217,	        Region="Western Africa",	                Country="Benin"),
                CountryTable(	Id=218,	        Region="Western Africa",	                Country="Ghana"),
                CountryTable(	Id=219,	        Region="Western Africa",	                Country="Guinea"),
                CountryTable(	Id=220,	        Region="Western Africa",	                Country="Gambia"),
                CountryTable(	Id=221,	        Region="Western Africa",	                Country="Guinea-Bissau"),
                CountryTable(	Id=222,	        Region="Western Africa",	                Country="Liberia"),
                CountryTable(	Id=223,	        Region="Western Africa",	                Country="Mali"),
                CountryTable(	Id=224,	        Region="Western Africa",	                Country="Mauritania"),
                CountryTable(	Id=225,	        Region="Western Africa",	                Country="Niger"),
                CountryTable(	Id=226,	        Region="Western Africa",	                Country="Nigeria"),
                CountryTable(	Id=227,	        Region="Western Africa",	                Country="Senegal"),
                CountryTable(	Id=228,	        Region="Western Africa",	                Country="Saint Helena"),
                CountryTable(	Id=229,	        Region="Western Africa",	                Country="Sierra Leone"),
                CountryTable(	Id=230,	        Region="Western Africa",	                Country="Togo"),
                CountryTable(	Id=231,	        Region="Western Europe",	                Country="Belgium"),
                CountryTable(	Id=232,	        Region="Western Europe",	                Country="Switzerland"),
                CountryTable(	Id=233,	        Region="Western Europe",	                Country="Germany"),
                CountryTable(	Id=234,	        Region="Western Europe",	                Country="France"),
                CountryTable(	Id=235,	        Region="Western Europe",	                Country="Liechtenstein"),
                CountryTable(	Id=236,	        Region="Western Europe",	                Country="Luxembourg"),
                CountryTable(	Id=237,	        Region="Western Europe",	                Country="Monaco"),
                CountryTable(	Id=238,	        Region="Western Europe",	                Country="Netherlands"),
                CountryTable(	Id=239,	        Region="Western Europe",	                Country="Austria"),]






#***Get con Filtro Path
@router.get("/{region}/{id}", status_code = status.HTTP_200_OK)
async def usersclass(region:str,id:int):
    filter (lambda user: user.Region == region, region_list)  #Función de orden superior
    ids=filter (lambda user: user.Id == id, region_list)  #Función de orden superior     
    try:
        return list(ids)[0]
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region no encontrada")
  
#***Get con Filtro Path
@router.get("/{region}/", status_code = status.HTTP_200_OK)
async def usersclass(region:str):
    users=filter (lambda user: user.Region == region, region_list)  #Función de orden superior
    try:
        return list(users)
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="Region no encontrada")


@router.post("/{region}/",  response_model=CountryTable, status_code=status.HTTP_201_CREATED)
async def usersclass(region:str, user:CountryTable):
    users=filter (lambda user: user.Region == region, region_list)  #Función de orden superior
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(region_list):
        if saved_user.Id == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="La region ya existe")
    else:
        region_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/

@router.put("/{region}/", status_code= status.HTTP_202_ACCEPTED)
async def usersclass(user:CountryTable, region:str):
    filter (lambda user: user.Region == region, region_list)  #Función de orden superior
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(region_list):
        if saved_user.Id   == user.Id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           region_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
           found=True
           
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No existe la region que quieres actualizar")
    else:
        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
@router.delete("/{region}/{id}", status_code= status.HTTP_200_OK)
async def usersclass(region:str, id:int):
    users=filter (lambda user: user.Region == region, region_list)  #Función de orden superior
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(region_list):
        if saved_user.Id == id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del region_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code= status.HTTP_200_OK, detail="La region se ha eliminado")
         
       
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se pudo eliminar la region")
    
    #http://127.0.0.1:8000/usersclass/1