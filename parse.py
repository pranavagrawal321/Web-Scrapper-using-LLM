from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import scraper

# Initialize the model
model = OllamaLLM(model='llama3.1')

# Define the prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse(chunks, description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_result = []

    for i, chunk in enumerate(chunks, start=1):
        try:
            # Invoke the model for each chunk
            response = chain.invoke({
                "dom_content": chunk,
                "parse_description": description,
            })

            # Append the response to the results
            parsed_result.append(response)

        except Exception as e:
            print(f"An error occurred while processing chunk {i}: {e}")
            parsed_result.append('')  # Append empty string in case of error

    # Join all responses into a single string
    return "\n".join(parsed_result)

# Example usage
if __name__ == '__main__':
    text = """
    Trends
Trends
Home
Home
Explore
Explore
Trending now
Trending now
maps
India
Afghanistan
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antigua & Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bosnia & Herzegovina
Botswana
Brazil
British Indian Ocean Territory
British Virgin Islands
Brunei
Bulgaria
Burkina Faso
Burundi
Cambodia
Cameroon
Canada
Cape Verde
Caribbean Netherlands
Cayman Islands
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo - Brazzaville
Congo - Kinshasa
Cook Islands
Costa Rica
Côte d’Ivoire
Croatia
Cuba
Curaçao
Cyprus
Czechia
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
Falkland Islands (Islas Malvinas)
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
Gabon
Gambia
Georgia
Germany
Ghana
Gibraltar
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guinea
Guinea-Bissau
Guyana
Haiti
Honduras
Hong Kong
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macao
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar (Burma)
Namibia
Nauru
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
North Korea
North Macedonia
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Palestine
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Puerto Rico
Qatar
Réunion
Romania
Russia
Rwanda
Samoa
San Marino
São Tomé & Príncipe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Maarten
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Korea
South Sudan
Spain
Sri Lanka
St. Barthélemy
St. Helena
St. Kitts & Nevis
St. Lucia
St. Martin
St. Pierre & Miquelon
St. Vincent & Grenadines
Sudan
Suriname
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad & Tobago
Tunisia
Türkiye
Turkmenistan
Turks & Caicos Islands
Tuvalu
U.S. Virgin Islands
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Uruguay
Uzbekistan
Vanuatu
Vatican City
Venezuela
Vietnam
Wallis & Futuna
Yemen
Zambia
Zimbabwe
Sign in
home
Home
search
Explore
trending_up
Trending now
calendar_month
Year in Search
notifications
Subscriptions
help_outline
Help
sms_failed
Send feedback
location_on
India   ▾
Trend location
search
my_location
My location (India)
Albania
Algeria
Angola
check_indeterminate_small
Argentina
All regions
Autonomous City of Buenos Aires
Buenos Aires Province
Catamarca Province
Chaco Province
Chubut Province
Cordoba
Corrientes Province
Entre Rios
Formosa Province
Jujuy
La Pampa Province
La Rioja Province
Mendoza Province
Misiones Province
Neuquen
Río Negro
Salta Province
San Juan Province
San Luis Province
Santa Cruz Province
Santa Fe Province
Santiago del Estero Province
Tierra del Fuego Province
Tucumán
Armenia
check_indeterminate_small
Australia
All regions
Australian Capital Territory
New South Wales
Northern Territory
Queensland
South Australia
Tasmania
Victoria
Western Australia
check_indeterminate_small
Austria
All regions
Burgenland
Carinthia
Lower Austria
Salzburg
Styria
Tyrol
Upper Austria
Vienna
Vorarlberg
Azerbaijan
Bahrain
Bangladesh
Belarus
check_indeterminate_small
Belgium
All regions
Brussels Capital Region
Flanders
Walloon Region
Benin
Bolivia
Bosnia & Herzegovina
check_indeterminate_small
Brazil
All regions
Federal District
State of Acre
State of Alagoas
State of Amapá
State of Amazonas
State of Bahia
State of Ceará
State of Espírito Santo
State of Goiás
State of Maranhão
State of Mato Grosso
State of Mato Grosso do Sul
State of Minas Gerais
State of Pará
State of Paraíba
State of Paraná
State of Pernambuco
State of Piauí
State of Rio de Janeiro
State of Rio Grande do Norte
State of Rio Grande do Sul
State of Rondônia
State of Roraima
State of Santa Catarina
State of São Paulo
State of Sergipe
State of Tocantins
Bulgaria
Burkina Faso
Cambodia
Cameroon
check_indeterminate_small
Canada
All regions
Alberta
British Columbia
Manitoba
New Brunswick
Newfoundland and Labrador
Northwest Territories
Nova Scotia
Nunavut
Ontario
Prince Edward Island
Québec
Saskatchewan
Yukon Territory
check_indeterminate_small
Chile
All regions
Antofagasta Region
Araucania
Arica y Parinacota Region
Atacama Region
Bío Bío Region
Coquimbo Region
Los Lagos Region
Los Ríos Region
Magallanes y la Antártica Chilena Region
Maule Region
O'Higgins Region
Santiago Metropolitan Region
Tarapacá Region
Valparaiso Region
XI Región
check_indeterminate_small
Colombia
All regions
Amazonas Department
Antioquia
Arauca
Atlantico
Bogota
Bolivar
Boyaca
Caldas
Caquetá
Casanare
Cauca Department
Cesar
Choco
Cordoba
Cundinamarca
Guainia
Guaviare
Huila
La Guajira
Magdalena
Meta
Narino
North Santander
Putumayo
Quindio
Risaralda
San Andrés and Providencia
Santander Department
Sucre
Tolima
Valle del Cauca
Vaupes
Vichada
Congo - Kinshasa
Costa Rica
Côte d’Ivoire
Croatia
Cuba
Cyprus
Czechia
check_indeterminate_small
Denmark
All regions
Capital Region of Denmark
Central Denmark Region
North Denmark Region
Region Syddanmark
Region Zealand
Dominican Republic
check_indeterminate_small
Ecuador
All regions
Azuay
Bolívar Province
Cañar Province
Carchi Province
Chimborazo Province
Cotopaxi Province
El Oro
Esmeraldas Province
Galápagos Islands
Guayas
Imbabura Province
Loja
Los Ríos Province
Manabí Province
Morona-Santiago Province
Orellana Province
Pastaza Province
Pichincha
Provincia de Napo
Santa Elena Province
Santo Domingo de los Tsáchilas Province
Sucumbíos Province
Tungurahua
Zamora-Chinchipe Province
check_indeterminate_small
Egypt
All regions
Al Qalyubia Governorate
Al Uqsur
Alexandria Governorate
Ash Sharqia Governorate
Assiut Governorate
Aswan Governorate
Beni Suef Governorate
Cairo Governorate
Dakahlia Governorate
Damietta Governorate
El Beheira Governorate
Faiyum Governorate
Gharbia Governorate
Giza Governorate
Ismailia Governorate
Kafr El Sheikh Governorate
Matrouh Governorate
Menia Governorate
Menofia Governorate
New Valley Governorate
North Sinai Governorate
Port Said Governorate
Qena Governorate
Red Sea Governorate
Sohag Governorate
South Sinai Governorate
Suez Governorate
El Salvador
Estonia
Ethiopia
Finland
check_indeterminate_small
France
By region
By department
All regions
Alsace
Aquitaine
Auvergne
Brittany
Burgundy
Centre-Val de Loire
Champagne-Ardenne
Corsica
Franche-Comté
Île-de-France
Languedoc-Roussillon
Limousin
Lorraine
Lower Normandy
Midi-Pyrénées
Nord-Pas-de-Calais
Pays de la Loire
Picardy
Poitou-Charentes
Provence-Alpes-Côte d'Azur
Rhone-Alpes
Upper Normandy
Ain
Aisne
Allier
Alpes-Maritimes
Alpes-de-Haute-Provence
Ardeche
Ardennes
Ariege
Aube
Aude
Aveyron
Bas-Rhin
Bouches-du-Rhone
Calvados
Cantal
Charente
Charente-Maritime
Cher
Correze
Corse-du-Sud
Cotes-d'Armor
Creuse
Côte-d'Or
Deux-Sevres
Dordogne
Doubs
Drôme
Essonne
Eure
Eure-et-Loir
Finistere
Gard
Gers
Gironde
Haut-Rhin
Haute-Corse
Haute-Garonne
Haute-Loire
Haute-Marne
Haute-Savoie
Haute-Saône
Haute-Vienne
Hautes-Alpes
Hautes-Pyrénées
Hauts-de-Seine
Hérault
Ille-et-Vilaine
Indre
Indre-et-Loire
Isere
Jura
Landes
Loir-et-Cher
Loire
Loire-Atlantique
Loiret
Lot
Lot-et-Garonne
Lozère
Maine-et-Loire
Manche
Marne
Mayenne
Meurthe-et-Moselle
Meuse
Morbihan
Moselle
Nievre
Nord
Oise
Orne
Pas-de-Calais
Puy-de-Dome
Pyrénées-Atlantiques
Pyrénées-Orientales
Rhône
Sarthe
Savoie
Saône-et-Loire
Seine-Maritime
Seine-Saint-Denis
Seine-et-Marne
Somme
Tarn
Tarn-et-Garonne
Territoire de Belfort
Val-d'Oise
Val-de-Marne
Var
Vaucluse
Vendee
Vienne
Ville de Paris
Vosges
Yonne
Yvelines
Georgia
check_indeterminate_small
Germany
All regions
Baden-Württemberg
Bavaria
Berlin
Brandenburg
Bremen
Hamburg
Hesse
Lower Saxony
Mecklenburg-Vorpommern
North Rhine-Westphalia
Rhineland-Palatinate
Saarland
Saxony
Saxony-Anhalt
Schleswig-Holstein
Thuringia
Ghana
Greece
Guatemala
Haiti
Honduras
Hong Kong
Hungary
check
India
check
All regions
Andaman and Nicobar Islands
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chandigarh
Chhattisgarh
Dadra and Nagar Haveli
Daman and Diu
Delhi
Goa
Gujarat
Haryana
Himachal Pradesh
Jammu and Kashmir
Jharkhand
Karnataka
Kerala
Lakshadweep
Madhya Pradesh
Maharashtra
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
Puducherry
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
check_indeterminate_small
Indonesia
All regions
Aceh
Bali
Bangka Belitung
Banten
Bengkulu
Central Java
Central Kalimantan
Central Sulawesi
East Java
East Kalimantan
East Nusa Tenggara
Gorontalo
Jambi
Lampung
Maluku
North Kalimantan
North Maluku
North Sulawesi
North Sumatra
Papua
Riau
Riau Islands
South East Sulawesi
South Kalimantan
South Sulawesi
South Sumatra
Special Capital Region of Jakarta
Special Region of Yogyakarta
West Java
West Kalimantan
West Nusa Tenggara
West Papua
West Sulawesi
West Sumatra
Iran
Iraq
Ireland
check_indeterminate_small
Israel
All regions
Center District
Ha Zafon
Hefa
Jerusalem District
South District
Tel-Aviv
check_indeterminate_small
Italy
All regions
Abruzzo
Aosta
Apulia
Basilicata
Calabria
Campania
Emilia-Romagna
Friuli-Venezia Giulia
Lazio
Liguria
Lombardy
Marche
Molise
Piedmont
Sardinia
Sicily
Trentino-Alto Adige/South Tyrol
Tuscany
Umbria
Veneto
Jamaica
check_indeterminate_small
Japan
All regions
Aichi Prefecture
Akita Prefecture
Aomori Prefecture
Chiba Prefecture
Ehime Prefecture
Fukui Prefecture
Fukuoka Prefecture
Fukushima Prefecture
Gifu Prefecture
Gunma Prefecture
Hiroshima Prefecture
Hokkaido Prefecture
Hyogo Prefecture
Ibaraki Prefecture
Ishikawa Prefecture
Iwate Prefecture
Kagawa Prefecture
Kagoshima Prefecture
Kanagawa Prefecture
Kochi Prefecture
Kumamoto Prefecture
Kyoto Prefecture
Mie Prefecture
Miyagi Prefecture
Miyazaki Prefecture
Nagano Prefecture
Nagasaki Prefecture
Nara Prefecture
Niigata Prefecture
Oita Prefecture
Okayama Prefecture
Okinawa Prefecture
Osaka Prefecture
Saga Prefecture
Saitama Prefecture
Shiga Prefecture
Shimane Prefecture
Shizuoka Prefecture
Tochigi Prefecture
Tokushima Prefecture
Tokyo
Tottori Prefecture
Toyama Prefecture
Wakayama Prefecture
Yamagata Prefecture
Yamaguchi Prefecture
Yamanashi Prefecture
Jordan
Kazakhstan
Kenya
Kuwait
Kyrgyzstan
Latvia
Lebanon
Libya
Lithuania
check_indeterminate_small
Malaysia
All regions
Federal Territory of Kuala Lumpur
Johor
Kedah
Kelantan
Labuan Federal Territory
Malacca
Negeri Sembilan
Pahang
Penang
Perak
Perlis
Putrajaya
Sabah
Sarawak
Selangor
Terengganu
Mali
check_indeterminate_small
Mexico
All regions
Aguascalientes
Baja California
Baja California Sur
Campeche
Chiapas
Chihuahua
Coahuila
Colima
Durango
Guanajuato
Guerrero
Hidalgo
Jalisco
Mexico City
Michoacán
Morelos
Nayarit
Nuevo Leon
Oaxaca
Puebla
Queretaro de Arteaga
Quintana Roo
San Luis Potosi
Sinaloa
Sonora
State of Mexico
Tabasco
Tamaulipas
Tlaxcala
Veracruz
Yucatan
Zacatecas
Moldova
Morocco
Mozambique
Myanmar (Burma)
Nepal
check_indeterminate_small
Netherlands
All regions
Drenthe
Flevoland
Friesland
Gelderland
Groningen
Limburg
North Brabant
North Holland
Overijssel
South Holland
Utrecht
Zeeland
check_indeterminate_small
New Zealand
All regions
Auckland
Bay Of Plenty
Canterbury
Gisborne
Hawke's Bay
Manawatu Wanganui
Marlborough District
Nelson City
Northland
Otago
Southland
Taranaki
Tasman
Waikato
Wellington
West Coast
Nicaragua
check_indeterminate_small
Nigeria
All regions
Abia
Adamawa
Akwa Ibom
Anambra
Bauchi
Bayelsa
Benue
Borno
Cross River
Delta
Ebonyi
Edo
Ekiti
Enugu
Federal Capital Territory
Gombe
Imo
Jigawa
Kaduna
Kano
Katsina
Kebbi
Kogi
Kwara
Lagos
Nasarawa
Niger
Ogun State
Ondo
Osun
Oyo
Plateau
Rivers
Sokoto
Taraba
Yobe
Zamfara
North Macedonia
Norway
Oman
check_indeterminate_small
Pakistan
All regions
Azad Jammu and Kashmir
Balochistan
Federally Administered Tribal Areas
Gilgit-Baltistan
Islamabad Capital Territory
Khyber Pakhtunkhwa
Punjab
Sindh
Palestine
Panama
Paraguay
check_indeterminate_small
Peru
All regions
Amazonas
Ancash
Apurimac
Arequipa
Ayacucho
Cajamarca
Callao
Cusco
Huancavelica
Huanuco
Ica
Junin
La Libertad
Lambayeque
Lima Region
Loreto
Madre de Dios
Moquegua
Pasco
Piura
Puno
San Martin
Tacna
Tumbes
Ucayali
check_indeterminate_small
Philippines
All regions
Autonomous Region in Muslim Mindanao
Bicol
Cagayan Valley
Calabarzon
Caraga
Central Luzons
Central Visayas
Cordillera Administrative Region
Davao Region
Eastern Visayas
Ilocos Region
Metro Manila
MIMAROPA
Northern Mindanao
Region XII
Western Visayas
Zamboanga Peninsula
check_indeterminate_small
Poland
All regions
Greater Poland Voivodeship
Kuyavian-Pomeranian Voivodeship
Lesser Poland Voivodeship
Łódź Voivodeship
Lower Silesian Voivodeship
Lublin Voivodeship
Lubusz Voivodeship
Masovian Voivodeship
Opole Voivodeship
Podkarpackie Voivodeship
Podlaskie Voivodeship
Pomeranian Voivodeship
Silesian Voivodeship
Swietokrzyskie
Warmian-Masurian Voivodeship
West Pomeranian Voivodeship
check_indeterminate_small
Portugal
All regions
Aveiro District
Azores
Beja District
Braga
Bragança District
Castelo Branco District
Coimbra District
Évora District
Faro District
Guarda District
Leiria District
Lisbon
Madeira
Portalegre District
Porto District
Santarém District
Setubal
Viana do Castelo District
Vila Real District
Viseu District
Puerto Rico
Qatar
Romania
check_indeterminate_small
Russia
All regions
Adygea
Altai Krai
Altai Republic
Amur Oblast
Arkhangelsk Oblast
Astrakhan Oblast
Belgorod Oblast
Bryansk Oblast
Buryatia
Chechnya
Chelyabinsk Oblast
Chukotka Autonomous Okrug
Chuvashia Republic
Dagestan Republic
Ingushetia
Irkutsk Oblast
Ivanovo Oblast
Jewish Autonomous Oblast
Kabardino-Balkaria
Kaliningrad Oblast
Kalmykia
Kaluga Oblast
Kamchatka Krai
Karachay-Cherkessia
Kemerovo Oblast
Khabarovsk Krai
Khanty-Mansi Autonomous Okrug
Kirov Oblast
Komi Republic
Kostroma Oblast
Krasnodar Krai
Krasnoyarsk Krai
Kurgan Oblast
Kursk Oblast
Leningrad Oblast
Lipetsk Oblast
Magadan Oblast
Mari El Republic
Mordovia
Moscow
Moscow Oblast
Murmansk Oblast
Nenets Autonomous Okrug
Nizhny Novgorod Oblast
North Ossetia–Alania
Novgorod Oblast
Novosibirsk Oblast
Omsk Oblast
Orenburg Oblast
Oryol Oblast
Penza Oblast
Perm Krai
Primorsky Krai
Pskov Oblast
Republic of Bashkortostan
Republic of Karelia
Republic of Khakassia
Rostov Oblast
Ryazan Oblast
Saint Petersburg
Sakha Republic
Sakhalin Oblast
Samara Oblast
Saratov Oblast
Smolensk Oblast
Stavropol Krai
Sverdlovsk Oblast
Tambov Oblast
Tatarstan
Tomsk Oblast
Tula Oblast
Tuva
Tver Oblast
Tyumen Oblast
Udmurt Republic
Ulyanovsk Oblast
Vladimir Oblast
Volgograd Oblast
Vologda Oblast
Voronezh Oblast
Yamalo-Nenets Autonomous Okrug
Yaroslavl Oblast
Zabaykalsky Krai
check_indeterminate_small
Saudi Arabia
All regions
Al Bahah Province
Al Jowf
Al Madinah Province
Al Qassim
Aseer Province
Eastern Province
Hail Province
Jazan
Makkah Province
Najran
Northern Borders Province
Riyadh Province
Tabuk Province
Senegal
Serbia
Singapore
Slovakia
Slovenia
check_indeterminate_small
South Africa
All regions
Gauteng
KwaZulu Natal
Limpopo
Mpumalanga
Noord-Wes
Northern Cape
Oos-Kaap
Vrystaat
Wes-Kaap
check_indeterminate_small
South Korea
All regions
Busan
Chungbuk
Chungnam
Daegu
Daejeon
Gangwon-do
Gwangju
Gyeongbuk
Gyeonggi-do
Gyeongnam
Incheon
Jeju-do
Jeonbuk
Jeonnam
Seoul
Ulsan
check_indeterminate_small
Spain
All regions
Andalusia
Aragon
Asturias
Balearic Islands
Basque Country
Canary Islands
Cantabria
Castile and León
Castile-La Mancha
Catalonia
Ceuta
Community of Madrid
Extremadura
Galicia
La Rioja
Melilla
Navarre
Region of Murcia
Valencian Community
Sri Lanka
check_indeterminate_small
Sweden
All regions
Blekinge County
Dalarna County
Gavleborg County
Gotland County
Halland County
Jamtland County
Jonkoping County
Kalmar County
Kronoberg County
Norrbotten County
Örebro County
Östergötland County
Skåne County
Södermanland County
Stockholm County
Uppsala County
Varmland County
Västerbotten County
Västernorrland County
Västmanland County
Västra Götaland County
check_indeterminate_small
Switzerland
All regions
Aargau
Appenzell Innerrhoden
Appenzell Outer Rhodes
Basel-Landschaft
Basel-Stadt
Canton of Bern
Canton of Fribourg
Canton of Glarus
Canton of Jura
Canton of Neuchâtel
Canton of Obwalden
Canton of Schaffhausen
Canton of Schwyz
Canton of Solothurn
Canton of Uri
Canton of Zug
Geneva
Grisons
Lucerne
Nidwalden
St. Gallen
Thurgau
Ticino
Valais
Vaud
Zurich
Syria
check_indeterminate_small
Taiwan
All regions
Kaohsiung City
New Taipei City
Taichung City
Tainan City
Taipei City
Taoyuan City
Tanzania
Thailand
Trinidad & Tobago
Tunisia
check_indeterminate_small
Türkiye
All regions
Adana
Adiyaman
Afyonkarahisar Province
Agri
Aksaray
Amasya Province
Ankara
Antalya
Ardahan Province
Artvin
Aydin
Balikesir
Bartın Province
Batman
Bayburt
Bilecik
Bingöl Province
Bitlis
Bolu
Burdur Province
Bursa
Çanakkale Province
Çankiri
Çorum Province
Denizli
Diyarbakir
Düzce Province
Edirne
Elazig
Erzincan
Erzurum
Eskisehir
Gaziantep
Giresun
Gümüshane
Hakkâri
Hatay
Igdir
Isparta Province
İstanbul
İzmir
Kahramanmaras
Karabuk
Karaman
Kars
Kastamonu
Kayseri Province
Kilis
Kirikkale
Kirklareli
Kirsehir
Kocaeli
Konya
Kütahya
Malatya
Manisa
Mardin
Mersin Province
Mugla
Mus
Nevsehir
Nigde
Ordu
Osmaniye
Rize
Sakarya
Samsun
Sanliurfa
Siirt Province
Sinop Province
Sivas
Şırnak
Tekirdag
Tokat
Trabzon
Tunceli
Usak
Van
Yalova Province
Yozgat
Zonguldak
Turkmenistan
Uganda
check_indeterminate_small
Ukraine
All regions
Cherkas'ka
Chernihivs'ka oblast
Chernivets'ka oblast
Dnipropetrovs'ka
Donetsk Oblast
Ivano-Frankivs'ka
Kharkivs'ka
Khersons'ka
Khmel'nyts'ka
Kirovohrads'ka
Kyïv
Kyïvs'ka
L'vivs'ka
Luhans'ka
Mykolaïvs'ka
Odes'ka
Poltavs'ka
Respublika Krym
Rivnens'ka
Sevastopol'
Sums'ka
Ternopil's'ka
Vinnyts'ka
Volyns'ka
Zakarpats'ka
Zaporiz'ka
Zhytomyrs'ka
check_indeterminate_small
United Arab Emirates
All regions
Abu Dhabi
Ajman
Dubai
Fujairah
Ras al Khaimah
Sharjah
Umm Al Quwain
check_indeterminate_small
United Kingdom
All regions
England
Northern Ireland
Scotland
Wales
check_indeterminate_small
United States
By state
By DMA
All regions
Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
District of Columbia
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming
Abilene-Sweetwater TX
Albany GA
Albany-Schenectady-Troy NY
Albuquerque-Santa Fe NM
Alexandria LA
Alpena MI
Amarillo TX
Anchorage AK
Atlanta GA
Augusta GA
Austin TX
Bakersfield CA
Baltimore MD
Bangor ME
Baton Rouge LA
Beaumont-Port Arthur TX
Bend OR
Billings, MT
Biloxi-Gulfport MS
Binghamton NY
Birmingham AL
Bluefield-Beckley-Oak Hill WV
Boise ID
Boston MA-Manchester NH
Bowling Green KY
Buffalo NY
Burlington VT-Plattsburgh NY
Butte-Bozeman MT
Casper-Riverton WY
Cedar Rapids-Waterloo-Iowa City & Dubuque IA
Champaign & Springfield-Decatur IL
Charleston SC
Charleston-Huntington WV
Charlotte NC
Charlottesville VA
Chattanooga TN
Cheyenne WY-Scottsbluff NE
Chicago IL
Chico-Redding CA
Cincinnati OH
Clarksburg-Weston WV
Cleveland-Akron (Canton) OH
Colorado Springs-Pueblo CO
Columbia SC
Columbia-Jefferson City MO
Columbus GA
Columbus OH
Columbus-Tupelo-West Point MS
Corpus Christi TX
Dallas-Ft. Worth TX
Davenport IA-Rock Island-Moline IL
Dayton OH
Denver CO
Des Moines-Ames IA
Detroit MI
Dothan AL
Duluth MN-Superior WI
El Paso TX
Elmira NY
Erie PA
Eugene OR
Eureka CA
Evansville IN
Fairbanks AK
Fargo-Valley City ND
Flint-Saginaw-Bay City MI
Florence-Myrtle Beach SC
Fresno-Visalia CA
Ft. Myers-Naples FL
Ft. Smith-Fayetteville-Springdale-Rogers AR
Ft. Wayne IN
Gainesville FL
Glendive MT
Grand Junction-Montrose CO
Grand Rapids-Kalamazoo-Battle Creek MI
Great Falls MT
Green Bay-Appleton WI
Greensboro-High Point-Winston Salem NC
Greenville-New Bern-Washington NC
Greenville-Spartanburg SC-Asheville NC-Anderson SC
Greenwood-Greenville MS
Harlingen-Weslaco-Brownsville-McAllen TX
Harrisburg-Lancaster-Lebanon-York PA
Harrisonburg VA
Hartford & New Haven CT
Hattiesburg-Laurel MS
Helena MT
Honolulu HI
Houston TX
Huntsville-Decatur (Florence) AL
Idaho Falls-Pocatello ID
Indianapolis IN
Jackson MS
Jackson TN
Jacksonville FL
Johnstown-Altoona PA
Jonesboro AR
Joplin MO-Pittsburg KS
Juneau AK
Kansas City MO
Knoxville TN
La Crosse-Eau Claire WI
Lafayette IN
Lafayette LA
Lake Charles LA
Lansing MI
Laredo TX
Las Vegas NV
Lexington KY
Lima OH
Lincoln & Hastings-Kearney NE
Little Rock-Pine Bluff AR
Los Angeles CA
Louisville KY
Lubbock TX
Macon GA
Madison WI
Mankato MN
Marquette MI
Medford-Klamath Falls OR
Memphis TN
Meridian MS
Miami-Ft. Lauderdale FL
Milwaukee WI
Minneapolis-St. Paul MN
Minot-Bismarck-Dickinson(Williston) ND
Missoula MT
Mobile AL-Pensacola (Ft. Walton Beach) FL
Monroe LA-El Dorado AR
Monterey-Salinas CA
Montgomery (Selma) AL
Nashville TN
New Orleans LA
New York NY
Norfolk-Portsmouth-Newport News VA
North Platte NE
Odessa-Midland TX
Oklahoma City OK
Omaha NE
Orlando-Daytona Beach-Melbourne FL
Ottumwa IA-Kirksville MO
Paducah KY-Cape Girardeau MO-Harrisburg-Mount Vernon IL
Palm Springs CA
Panama City FL
Parkersburg WV
Peoria-Bloomington IL
Philadelphia PA
Phoenix AZ
Pittsburgh PA
Portland OR
Portland-Auburn ME
Presque Isle ME
Providence RI-New Bedford MA
Quincy IL-Hannibal MO-Keokuk IA
Raleigh-Durham (Fayetteville) NC
Rapid City SD
Reno NV
Richmond-Petersburg VA
Roanoke-Lynchburg VA
Rochester MN-Mason City IA-Austin MN
Rochester NY
Rockford IL
Sacramento-Stockton-Modesto CA
Salisbury MD
Salt Lake City UT
San Angelo TX
San Antonio TX
San Diego CA
San Francisco-Oakland-San Jose CA
Santa Barbara-Santa Maria-San Luis Obispo CA
Savannah GA
Seattle-Tacoma WA
Sherman TX-Ada OK
Shreveport LA
Sioux City IA
Sioux Falls(Mitchell) SD
South Bend-Elkhart IN
Spokane WA
Springfield MO
Springfield-Holyoke MA
St. Joseph MO
St. Louis MO
Syracuse NY
Tallahassee FL-Thomasville GA
Tampa-St. Petersburg (Sarasota) FL
Terre Haute IN
Toledo OH
Topeka KS
Traverse City-Cadillac MI
Tri-Cities TN-VA
Tucson (Sierra Vista) AZ
Tulsa OK
Twin Falls ID
Tyler-Longview(Lufkin & Nacogdoches) TX
Utica NY
Victoria TX
Waco-Temple-Bryan TX
Washington DC (Hagerstown MD)
Watertown NY
Wausau-Rhinelander WI
West Palm Beach-Ft. Pierce FL
Wheeling WV-Steubenville OH
Wichita Falls TX & Lawton OK
Wichita-Hutchinson KS
Wilkes Barre-Scranton PA
Wilmington NC
Yakima-Pasco-Richland-Kennewick WA
Youngstown OH
Yuma AZ-El Centro CA
Zanesville OH
check_indeterminate_small
Uruguay
All regions
Artigas Department
Canelones Department
Cerro Largo Department
Colonia
Durazno Department
Flores Department
Florida Department
Lavalleja Department
Maldonado Department
Montevideo Department
Paysandú Department
Río Negro Department
Rivera Department
Rocha Department
Salto
San José Department
Soriano Department
Tacuarembó Department
Treinta y Tres Department
Uzbekistan
Venezuela
check_indeterminate_small
Vietnam
All regions
An Giang Province
Ba Ria - Vung Tau
Bac Can
Bac Giang
Bac Lieu
Bac Ninh Province
Ben Tre
Binh Dinh Province
Binh Duong
Binh Phuoc
Binh Thuan
Ca Mau
Can Tho
Cao Bang
Da Nang
Đắk Lắk Province
Dak Nong
Dien Bien
Dong Nai
Đồng Tháp Province
Gia Lai Province
Ha Giang
Hà Nam Province
Ha Tinh Province
Hai Duong
Haiphong
Hanoi
Hau Giang
Ho Chi Minh
Hoa Binh
Hung Yen Province
Khanh Hoa Province
Kien Giang
Kon Tum Province
Lai Chau
Lâm Đồng
Lang Son Province
Lao Cai
Long An Province
Nam Dinh
Nghe An
Ninh Bình Province
Ninh Thuan Province
Phu Tho Province
Phú Yên Province
Quang Binh Province
Quang Nam Province
Quang Ngai
Quảng Ninh Province
Quảng Trị Province
Soc Trang
Son La
Tây Ninh Province
Thai Binh
Thai Nguyen
Thanh Hoa
Thua Thien Hue
Tien Giang
Tra Vinh
Tuyên Quang Province
Vinh Long
Vinh Phuc Province
Yen Bai Province
Yemen
Zambia
Zimbabwe
calendar_month
Past 24 hours   ▾
Started trending
Past 4 hours
Past 24 hours
Past 48 hours
Past 7 days
grid_3x3
All trends   ▾
Trend status
Show active trends only
sort
By relevance   ▾
Sort by
Title
Search volume
Recency
Relevance
Significant and recent trends
arrow_back_ios_new
arrow_forward_ios
ios_share
Export
csv
Download CSV
content_copy
Copy to clipboard
rss_feed
RSS feed
ios_share
Export   ▾
csv
Download CSV
content_copy
Copy to clipboard
rss_feed
RSS feed
Trends
Sort by title
Trends
(Updated Sep 15, 12:15 AM)
Search volume
Sort by search volume
Started
Sort by recency
info_outline
Trend status
trending_up
Active:
These search queries are still being searched more than usual.
timelapse
Lasted:
These queries were searched more than usual sometime in the selected timeframe and are now back to their typical search volume.
Tip:
Click on the trend time to toggle between elapsed time and start time. All times are displayed in your local time zone.
Trend breakdown
info_outline
Trend breakdown
A trend may consist of multiple queries that are variants of the same search or considered to be related. Trend breakdown details these queries.
Past 24 hours
maharashtra
100K+ searches
·
trending_up
Active
·
11h ago
100K+
arrow_upward
1,000%
11 hours ago
trending_up
Active
maharashtra government eid holiday
maharashtra government eid holiday
Search term
query_stats
Explore
eid e milad
eid e milad
Search term
query_stats
Explore
+ 2 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
southampton vs man united
200K+ searches
·
trending_up
Active
·
8h ago
200K+
arrow_upward
1,000%
8 hours ago
trending_up
Active
manchester united
manchester united
Search term
query_stats
Explore
+ 21 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
man city vs brentford
100K+ searches
·
trending_up
Active
·
5h ago
100K+
arrow_upward
1,000%
5 hours ago
trending_up
Active
manchester city
manchester city
Search term
query_stats
Explore
erling haaland
erling haaland
Search term
query_stats
Explore
man city
man city
Search term
query_stats
Explore
+ 14 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
real sociedad vs real madrid
20K+ searches
·
trending_up
Active
·
1h ago
20K+
arrow_upward
1,000%
1 hour ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
bengaluru vs east bengal
50K+ searches
·
trending_up
Active
·
5h ago
50K+
arrow_upward
1,000%
5 hours ago
trending_up
Active
bengaluru fc vs east bengal fc lineups
bengaluru fc vs east bengal fc lineups
Search term
query_stats
Explore
east bengal
east bengal
Search term
query_stats
Explore
+ 12 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
liverpool vs nottm forest
100K+ searches
·
trending_up
Active
·
5h ago
100K+
arrow_upward
1,000%
5 hours ago
trending_up
Active
liverpool fc
liverpool fc
Search term
query_stats
Explore
+ 14 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
norfolk southern ceo alan shaw
20K+ searches
·
trending_up
Active
·
22h ago
20K+
arrow_upward
1,000%
22 hours ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
holstein kiel vs bayern
20K+ searches
·
trending_up
Active
·
2h ago
20K+
arrow_upward
1,000%
2 hours ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
radhika merchant
50K+ searches
·
trending_up
Active
·
21h ago
50K+
arrow_upward
1,000%
21 hours ago
trending_up
Active
mumbai lalbaugcha raja
mumbai lalbaugcha raja
Search term
query_stats
Explore
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
odisha vs chennaiyin
50K+ searches
·
trending_up
Active
·
8h ago
50K+
arrow_upward
1,000%
8 hours ago
trending_up
Active
farukh choudhary
farukh choudhary
Search term
query_stats
Explore
+ 8 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
england women vs ireland women
50K+ searches
·
trending_up
Active
·
5h ago
50K+
arrow_upward
1,000%
5 hours ago
trending_up
Active
bryony smith
bryony smith
Search term
query_stats
Explore
eng w vs ire w
eng w vs ire w
Search term
query_stats
Explore
+ 8 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
aston villa vs everton
10K+ searches
·
trending_up
Active
·
3h ago
10K+
arrow_upward
1,000%
3 hours ago
trending_up
Active
aston villa vs everton f.c. lineups
aston villa vs everton f.c. lineups
Search term
query_stats
Explore
aston villa
aston villa
Search term
query_stats
Explore
+ 2 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
ind vs pak hockey
50K+ searches
·
trending_up
Active
·
11h ago
50K+
arrow_upward
800%
11 hours ago
trending_up
Active
india vs pakistan hockey
india vs pakistan hockey
Search term
query_stats
Explore
+ 24 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
thangalaan
50K+ searches
·
trending_up
Active
·
19h ago
50K+
arrow_upward
100%
19 hours ago
trending_up
Active
thangalaan ott release
thangalaan ott release
Search term
query_stats
Explore
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
al-riyadh vs al-hilal
5K+ searches
·
trending_up
Active
·
1h ago
5K+
arrow_upward
1,000%
1 hour ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
bournemouth vs chelsea
10K+ searches
·
trending_up
Active
·
40m ago
10K+
arrow_upward
1,000%
40 minutes ago
trending_up
Active
premier league games
premier league games
Search term
query_stats
Explore
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
diamond league
10K+ searches
·
trending_up
Active
·
2h ago
10K+
arrow_upward
600%
2 hours ago
trending_up
Active
diamond league 2024
diamond league 2024
Search term
query_stats
Explore
neeraj chopra match
neeraj chopra match
Search term
query_stats
Explore
+ 6 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
onam wishes
10K+ searches
·
trending_up
Active
·
17h ago
10K+
arrow_upward
200%
17 hours ago
trending_up
Active
thiruvonam 2024
thiruvonam 2024
Search term
query_stats
Explore
onam festival 2024
onam festival 2024
Search term
query_stats
Explore
+ 1 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
asteroid hitting earth 2024
20K+ searches
·
trending_up
Active
·
13h ago
20K+
arrow_upward
200%
13 hours ago
trending_up
Active
nasa 15 september 2024
nasa 15 september 2024
Search term
query_stats
Explore
+ 6 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
thangalaan ott
10K+ searches
·
trending_up
Active
·
23h ago
10K+
arrow_upward
300%
23 hours ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
kanpur superstars vs meerut mavericks
10K+ searches
·
trending_up
Active
·
4h ago
10K+
arrow_upward
600%
4 hours ago
trending_up
Active
up t20 live
up t20 live
Search term
query_stats
Explore
uttar pradesh t20 league
uttar pradesh t20 league
Search term
query_stats
Explore
+ 1 more
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
revised orop pensions
10K+ searches
·
trending_up
Active
·
14h ago
10K+
arrow_upward
300%
14 hours ago
trending_up
Active
orop pension
orop pension
Search term
query_stats
Explore
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
west bengal mamata banerjee
20K+ searches
·
trending_up
Active
·
10h ago
20K+
arrow_upward
900%
10 hours ago
trending_up
Active
mamata banerjee doctors
mamata banerjee doctors
Search term
query_stats
Explore
doctor
doctor
Search term
query_stats
Explore
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
hoffenheim vs leverkusen
10K+ searches
·
trending_up
Active
·
6h ago
10K+
arrow_upward
1,000%
6 hours ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
crystal palace vs leicester city
10K+ searches
·
trending_up
Active
·
5h ago
10K+
arrow_upward
700%
5 hours ago
trending_up
Active
more_vert
More actions
checklist
Select
query_stats
Explore
Search it
Rows per page
25
15
25
50
1–25 of 271
Go to first page
Go to previous page
Go to next page
Go to last page
Privacy
Terms
Send feedback
About
help
Help
language
English (United States)‎
Afrikaans
Bahasa Indonesia
Bahasa Melayu
bosanski
català
Čeština
Dansk
Deutsch
eesti
English (Australia)‎
English (United Kingdom)‎
English (United States)‎
Español (España)‎
Español (Latinoamérica)‎
Filipino
Français (France)‎
Hrvatski
Italiano
latviešu
lietuvių
magyar
Nederlands
norsk
polski
Português (Brasil)‎
Português (Portugal)‎
română
Slovenčina
slovenščina
Suomi
Svenska
Tiếng Việt
Türkçe
Ελληνικά
български
Русский
српски (ћирилица)‎
Українська
עברית
اردو
العربية
فارسی
मराठी
हिन्दी
বাংলা
ਪੰਜਾਬੀ
ગુજરાતી
தமிழ்
తెలుగు
മലയാളം
ไทย
한국어
中文 (香港)‎
中文（简体)‎
中文（繁體)‎
日本語
Search
Clear search
Close search
Main menu
Google apps
    """

    chunks = scraper.create_chunks(text)
    description = "Specific information you want to extract"

    result = parse(chunks, description)
    print(result)
