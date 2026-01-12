data_cruda = """
* Abjasia - Sujumi
* Acrotiri y Dhekelia - Episkopí
* Afganistán - Kabul
* Albania - Tirana
* Alemania - Berlín
* Andorra - Andorra la Vieja
* Angola - Luanda
* Anguila - El Valle
* Antigua y Barbuda - Saint John
* Arabia Saudita - Riad
* Argelia - Argel
* Argentina - Buenos Aires
* Armenia - Ereván
* Aruba - Oranjestad
* Australia - Canberra
* Austria - Viena
* Azerbaiyán - Bakú
* Bahamas - Nasáu
* Bangladés - Daca
* Barbados - Bridgetown
* Baréin - Manama
* Bélgica - Bruselas
* Belice - Belmopán
* Benín - Porto Novo (constitucional), Cotonú (sede del gobierno)
* Bermudas - Hamilton
* Bielorrusia - Minsk
* Birmania (Myanmar) - Naipyidó
* Bután - Timbu
* Bolivia - Sucre (constitucional y judicial), La Paz (sede del gobierno y legislativo)
* Bosnia y Herzegovina - Sarajevo
* Botsuana - Gaborone
* Brasil - Brasilia
* Brunéi - Bandar Seri Begawan
* Bulgaria - Sofía
* Burkina Faso - Uagadugú
* Burundi - Guitega (oficial), Buyumbura (sede de los poderes del Estado)
* Cabo Verde - Praia
* Islas Caimán - George Town
* Camboya - Nom Pen
* Camerún - Yaundé
* Canadá - Ottawa
* Catar - Doha
* Chad - Yamena
* Chile - Santiago (oficial), Valparaíso (sede legislativa)
* China - Pekín
* Chipre - Nicosia, Nicosia del Norte
* Islas Cocos - West Island
* Colombia - Bogotá
* Comoras - Moroni
* República Democrática del Congo - Kinsasa
* República del Congo - Brazzaville
* Islas Cook - Avarua
* Corea del Norte - Pionyang
* Corea del Sur - Seúl
* Croacia - Zagreb
* Costa de Marfil - Yamusukro (oficial), Abiyán (sede de los poderes del Estado)
* Costa Rica - San José
* Cuba - La Habana
* Curazao - Willemstad
* Dinamarca - Copenhague
* Dominica - Roseau
* Ecuador - Quito
* Egipto - El Cairo
* El Salvador - San Salvador
* Emiratos Árabes Unidos - Abu Dabi
* Eritrea - Asmara
* Eslovaquia - Bratislava
        * Eslovenia - Liubliana
        * España - Madrid
        * Estados Unidos - Washington D. C.
        * Estonia - Tallin
        * Etiopía - Adís Abeba
        * Islas Feroe - Tórshavn
        * Filipinas - Manila
        * Finlandia - Helsinki
        * Fiyi - Suva
        * Francia - París
        * Gabón - Libreville
        * Gambia - Banjul
        * Georgia - Tiflis
        * Ghana - Acra
        * Gibraltar - Gibraltar
        * Granada - Saint George
        * Grecia - Atenas
        * Groenlandia - Nuuk
        * Guam - Agaña
        * Guatemala - Ciudad de Guatemala
        * Guernsey - Saint Peter Port
        * Guinea - Conakri
        * Guinea-Bisáu - Bisáu
        * Guinea Ecuatorial - Malabo
        * Guyana - Georgetown
        * Haití - Puerto Príncipe
        * Honduras - Tegucigalpa
        * Hungría - Budapest
        * India - Nueva Delhi
        * Indonesia - Yakarta
        * Irak - Bagdad
        * Irán - Teherán
        * Irlanda - Dublín
        * Islandia - Reikiavik
        * Israel - Jerusalén (constitucional)
        * Italia - Roma
        * Jamaica - Kingston
        * Japón - Tokio
        * Jersey - Saint Helier
        * Jordania - Amán
        * Kazajistán - Astaná
        * Kenia - Nairobi
        * Kirguistán - Biskek
        * Kiribati - Tarawa
        * Kosovo - Pristina
        * Kuwait - Ciudad de Kuwait
        * Laos - Vientián
        * Lesoto - Maseru
        * Letonia - Riga
        * Líbano - Beirut
        * Liberia - Monrovia
        * Libia - Trípoli
        * Liechtenstein - Vaduz
        * Lituania - Vilna
        * Luxemburgo - Ciudad de Luxemburgo
        * Macedonia del Norte - Skopie
        * Madagascar - Antananarivo
        * Malasia - Kuala Lumpur (constitucional), Putrajaya (sede del gobierno)
        * Malaui - Lilongüe
        * Maldivas - Malé
        * Mali - Bamako
        * Malta - La Valeta
        * Islas Malvinas - Puerto Argentino/Stanley
        * Isla de Man - Douglas
        * Islas Marianas del Norte - Saipán
        * Marruecos - Rabat
        * Islas Marshall - Majuro
        * Mauritania - Nuakchot
        * Mauricio - Port Louis
        * México - Ciudad de México
        * Micronesia - Palikir
        * Moldavia - Chisináu
        * Mónaco - Mónaco
        * Mongolia - Ulán Bator
        * Montenegro - Podgorica (constitucional), Cetiña (sede de la jefatura del Estado)
        * Montserrat - Brades
        * Mozambique - Maputo
        * Namibia - Windhoek
        * Nauru - Yaren (de facto)
        * Isla de Navidad - Flying Fish Cove
        * Nepal - Katmandú
        * Nicaragua - Managua
        * Níger - Niamey
        * Nigeria - Abuya
        * Niue - Alofi
        * Isla Norfolk - Kingston
        * Noruega - Oslo
        * Nueva Caledonia - Numea
        * Nueva Zelanda - Wellington
        * Omán - Mascate
        * Osetia del Sur - Tsjinval
        * Países Bajos - Ámsterdam (constitucional), La Haya (sede de los poderes del Estado)
        * Pakistán - Islamabad
        * Palaos - Ngerulmud (oficial)
        * Palestina - Jerusalén Este (proclamada), Ramala (administrativa)
        * Panamá - Ciudad de Panamá
        * Papúa Nueva Guinea - Puerto Moresby
        * Paraguay - Asunción
        * Perú - Lima
        * Islas Pitcairn - Adamstown
        * Polinesia Francesa - Papeete
        * Polonia - Varsovia
        * Portugal - Lisboa
        * Puerto Rico - San Juan
        * Reino Unido - Londres
        * República Centroafricana - Bangui
        * República Checa - Praga (constitucional), Brno (judicial)
        * República Dominicana - Santo Domingo
        * República Árabe Saharaui Democrática - El Aaiún (proclamada), Tifariti (de facto)
        * Ruanda - Kigali
        * Rumania - Bucarest
        * Rusia - Moscú
        * Islas Salomón - Honiara
        * Samoa - Apia
        * Samoa Americana - Pago Pago
        * San Bartolomé - Gustavia
        * San Cristóbal y Nieves - Basseterre
        * San Marino - Ciudad de San Marino
        * San Martín - Marigot, Philipsburg
        * San Pedro y Miquelón - San Pedro
        * Santa Elena, Ascensión y Tristán de Acuña - Jamestown
        * Santa Lucía - Castries
        * Santo Tomé y Príncipe - Santo Tomé
        * San Vicente y las Granadinas - Kingstown
        * Senegal - Dakar
        * Serbia - Belgrado
        * Seychelles - Victoria
        * Sierra Leona - Freetown
        * Singapur - Ciudad de Singapur
        * Siria - Damasco
        * Somalia - Mogadiscio
        * Somalilandia - Hargeisa
        * Sri Lanka - Colombo (sede del gobierno), Sri Jayawardenapura Kotte (oficial)
        * Suazilandia - Lobamba (sede legislativa y real), Mbabane (sede del Gobierno)
        * Sudáfrica - Pretoria (sede ejecutiva), Ciudad del Cabo (sede legislativa), Bloemfontein (sede judicial)
        * Sudán - Jartum
        * Sudán del Sur - Yuba
        * Suecia - Estocolmo
        * Suiza - Berna
        * Surinam - Paramaribo
        * Svalbard - Longyearbyen
        * Tailandia - Bangkok
        * Taiwán - Taipéi
        * Tanzania - Dodoma
        * Tayikistán - Dusambé
        * Timor Oriental - Dili
        * Togo - Lomé
        * Tokelau - Sin capital definida
        * Tonga - Nukualofa
        * Transnistria - Tiráspol
        * Trinidad y Tobago - Puerto España
        * Túnez - Ciudad de Túnez
        * Islas Turcas y Caicos - Cockburn Town
        * Turkmenistán - Asjabad
        * Turquía - Ankara
        * Tuvalu - Funafuti
        * Ucrania - Kiev
        * Uganda - Kampala
        * Uruguay - Montevideo
        * Uzbekistán - Taskent
        * Vanuatu - Port Vila
        * Ciudad del Vaticano - Ciudad del Vaticano
        * Venezuela - Caracas
        * Vietnam - Hanói
        * Islas Vírgenes Británicas - Road Town
        * Islas Vírgenes de los Estados Unidos - Charlotte Amalie
        * Wallis y Futuna - Mata-Utu
        * Yemen - Saná
        * Yibuti - Ciudad de Yibuti
        * Zambia - Lusaka
        * Zimbabue - Harare
        """