# Initial datasets

The datasets considered for this study were the samples of UN General Assembly voting records for periods 1965-1980 and 2007-2023. The former is largely used as validation tool because it has historically studied voting blocs we can validate our results on.

# Overall evaluation strategy

We shall evaluate our model by comparing the original voting graph we produce on the stage of scrubbing information and initial statistics, with the post-processed graph that has edges within identified blocs removed.

To that, we shall use the period of 1965-1980 to fine-tune resolution on greedy modularity optimizing algorithm present in networkx by choosing resolution low enough to ensure that there is at most difference of 1 in detected communities between provided graphs. It will be stated as a fact that at higher resolutions, amount of communities (single node ones) detected in raw graph is significantly higher.

# Results as is

## Cold war period

After choosing a resolution of 1.55 for the algorithm we get the following divergence in communities in Cold War.

| || Processed| graph| || Raw| graph| ||
| ------------------------------|
| || Community| 1| ||
| ----------------|
| || AFGHANISTAN.| || AFGHANISTAN| ||
| || ALBANIA| || ALBANIA| ||
| || ALGERIA| || ALGERIA| ||
| || BULGARIA| || BULGARIA| ||
| || BURUNDI| || BURUNDI| ||
| || BYELORUSSIAN| SSR| || BYELORUSSIAN| SSR| ||
| || CAMBODIA| || CAMBODIA| ||
| || SRI| LANKA| || SRI| LANKA| ||
| || CHINA| || CHINA| ||
| || CONGO| || CONGO| ||
| || CUBA| || CUBA| ||
| || CYPRUS| || CYPRUS| ||
| || CZECHOSLOVAKIA| || CZECHOSLOVAKIA| ||
| || BERIN| || BERIN| ||
| || ETHIOPIA| || ETHIOPIA| ||
| || GUINEA| || GUINEA| ||
| || HUNGARY| || HUNGARY| ||
| || INDIA| || INDIA| ||
| || IRAQ| || IRAQ| ||
| || JORDAN| || JORDAN| ||
| || KENYA| || KENYA| ||
| || KUWAIT| || KUWAIT| ||
| || LEBANON| || LEBANON| ||
| || LIBYA| || LIBYA| ||
| || MALDIVE| ISLANDS| || MALDIVE| ISLANDS| ||
| || MALI| || MALI| ||
| || MAURITANIA| || MAURITANIA| ||
| || MONGOLIA| || MONGOLIA| ||
| || MOROCCO| || MOROCCO| ||
| || NIGERIA| || NIGERIA| ||
| || PAKISTAN| || PAKISTAN| ||
| || POLAND| || POLAND| ||
| || ROMANIA| || ROMANIA| ||
| || SAUDI| ARABIA| || SAUDI| ARABIA| ||
| || SENEGAL| || SENEGAL| ||
| || SOMALIA| || SOMALIA| ||
| || SUDAN| || SUDAN| ||
| || SYRIA| || SYRIA| ||
| || TUNISIA| || TUNISIA| ||
| || UGANDA| || UGANDA| ||
| || UKRAINIAN| SSR| || UKRAINIAN| SSR| ||
| || USSR| || USSR| ||
| || EGYPT| || EGYPT| ||
| || UNITED| REPUBLIC| OF| TANZANIA| || UNITED| REPUBLIC| OF| TANZANIA| ||
| || YEMEN| || YEMEN| ||
| || YUGOSLAVIA| || YUGOSLAVIA| ||
| || ZAMBIA| || ZAMBIA| ||
| || *INDONESIA*| || _| ||
| || SOUTHERN| YEMEN| || SOUTHERN| YEMEN| ||
| || EQUATORIAL| GUINEA| || EQUATORIAL| GUINEA| ||
| || GERMAN| DEMOCRATIC| REPUBLIC| || GERMAN| DEMOCRATIC| REPUBLIC| ||
| || Community| 2| ||
| ----------------|
| || ARGENTINA| || ARGENTINA| ||
| || AUSTRALIA| || AUSTRALIA| ||
| || AUSTRIA| || AUSTRIA| ||
| || BELGIUM| || BELGIUM| ||
| || BOLIVIA| || BOLIVIA| ||
| || BRAZIL| || BRAZIL| ||
| || CANADA| || CANADA| ||
| || CHILE| || CHILE| ||
| || COLOMBIA| || COLOMBIA| ||
| || COSTA| RICA| || COSTA| RICA| ||
| || DENMARK| || DENMARK| ||
| || DOMINICAN| REPUBLIC| || DOMINICAN| REPUBLIC| ||
| || EL| SALVADOR| || EL| SALVADOR| ||
| || FINLAND| || FINLAND| ||
| || FRANCE| || FRANCE| ||
| || GREECE| || GREECE| ||
| || GUATEMALA| || GUATEMALA| ||
| || HAITI| || HAITI| ||
| || HONDURAS| || HONDURAS| ||
| || ICELAND| || ICELAND| ||
| || IRELAND| || IRELAND| ||
| || ISRAEL| || ISRAEL| ||
| || ITALY| || ITALY| ||
| || IVORY| COAST| || IVORY| COAST| ||
| || JAPAN| || JAPAN| ||
| || LIBERIA| || LIBERIA| ||
| || LUXEMBOURG| || LUXEMBOURG| ||
| || MALAWI| || MALAWI| ||
| || MEXICO| || MEXICO| ||
| || NETHERLANDS| || NETHERLANDS| ||
| || NEW| ZEALAND| || NEW| ZEALAND| ||
| || NICARAGUA| || NICARAGUA| ||
| || NORWAY| || NORWAY| ||
| || PANAMA| || PANAMA| ||
| || PARAGUAY| || PARAGUAY| ||
| || PHILIPPINES| || PHILIPPINES| ||
| || PORTUGAL| || PORTUGAL| ||
| || SOUTH| AFRICA| || SOUTH| AFRICA| ||
| || SPAIN| || SPAIN| ||
| || SWEDEN| || SWEDEN| ||
| || THAILAND| || THAILAND| ||
| || TURKEY| || TURKEY| ||
| || UNITED| KINGDOM| || UNITED| KINGDOM| ||
| || UNITED| STATES| || UNITED| STATES| ||
| || URUGUAY| || URUGUAY| ||
| || VENEZUELA| || VENEZUELA| ||
| || ESWATINI| || ESWATINI| ||
| || GERMANY,| FEDERAL| REPUBLIC| OF| || GERMANY,| FEDERAL| REPUBLIC| OF| ||
| || SOLOMON| ISLANDS| || SOLOMON| ISLANDS| ||
| || Community| 3| ||
| ----------------|
| || GAMBIA| || GAMBIA| ||
| || MALTA| || MALTA| ||
| || BOTSWANA| || BOTSWANA| ||
| || _| || *GUYANA*| ||
| || LESOTHO| || LESOTHO| ||
| || MALDIVES| || MALDIVES| ||
| || MAURITIUS| || MAURITIUS| ||
| || FIJI| || FIJI| ||
| || BAHRAIN| || BAHRAIN| ||
| || BHUTAN| || BHUTAN| ||
| || OMAN| || OMAN| ||
| || QATAR| || QATAR| ||
| || UNITED| ARAB| EMIRATES| || UNITED| ARAB| EMIRATES| ||
| || BAHAMAS| || BAHAMAS| ||
| || BANGLADESH| || BANGLADESH| ||
| || GRENADA| || GRENADA| ||
| || GUINEA-BISSAU| || GUINEA-BISSAU| ||
| || BENIN| || BENIN| ||
| || CABO| VERDE| || CABO| VERDE| ||
| || COMOROS| || COMOROS| ||
| || MOZAMBIQUE| || MOZAMBIQUE| ||
| || PAPUA| NEW| GUINEA| || PAPUA| NEW| GUINEA| ||
| || SAO| TOME| AND| PRINCIPE| || SAO| TOME| AND| PRINCIPE| ||
| || SURINAME| || SURINAME| ||
| || ANGOLA| || ANGOLA| ||
| || SAMOA| || SAMOA| ||
| || SEYCHELLES| || SEYCHELLES| ||
| || DJIBOUTI| || DJIBOUTI| ||
| || VIET| NAM| || VIET| NAM| ||
| || SAINT| LUCIA| || SAINT| LUCIA| ||
| || Community| 4| ||
| ----------------|
| || _| || *CAMEROON*| ||
| || CENTRAL| AFRICAN| REPUBLIC| || CENTRAL| AFRICAN| REPUBLIC| ||
| || CHAD| || CHAD| ||
| || GABON| || GABON| ||
| || *JAMAICA*| || _| ||
| || MADAGASCAR| || MADAGASCAR| ||
| || NIGER| || NIGER| ||
| || RWANDA| || RWANDA| ||
| || SIERRA| LEONE| || SIERRA| LEONE| ||
| || TOGO| || TOGO| ||
| || UPPER| VOLTA| || UPPER| VOLTA| ||
| || Community| 5| ||
| ----------------|
| || *CONGO| (DEMOCRATIC| REPUBLIC| OF)*| || _| ||
| || *IRAN*| || _| ||
| || _| || *JAMAICA*| ||
| || _| || *LAOS*| ||
| || *MALAYSIA*| || _| ||
| || _| || *TRINIDAD| AND| TOBAGO*| ||
| || _| || *BARBADOS*| ||
| || Community| 6| ||
| ----------------|
| || *BURMA*| || _| ||
| || _| || *CONGO| (DEMOCRATIC| REPUBLIC| OF)*| ||
| || _| || *IRAN*| ||
| || _| || *MALAYSIA*| ||
| || *NEPAL*| || _| ||
| || *SINGAPORE*| || _| ||
| || _| || *INDONESIA*| ||
| || Community| 7| ||
| ----------------|
| || _| || *BURMA*| ||
| || _| || *NEPAL*| ||
| || _| || *SINGAPORE*| ||
| || *TRINIDAD| AND| TOBAGO*| || _| ||
| || *BARBADOS*| || _| ||
| || *GUYANA*| || _| ||
| || Community| 8| ||
| ----------------|
| || ECUADOR| || ECUADOR| ||
| || PERU| || PERU| ||
| || Community| 9| ||
| ----------------|
| || *CAMEROON*| || _| ||
| || GHANA| || GHANA| ||
| || Community| 10| ||
| ----------------|
| || *LAOS*| || _| ||

These results might be fairly straightforward because this period is characterized by fairly rigid political structure of the world, freed colonies and other places buried in civil wars notwithstanding. Albeit, our approach does allow one to reshuffle communities, the notable of which is separation of Malysia, 

## Modern period

At last, using the similar strategy and applying it to modern period data (resolution chosen is 1.6)

| || Processed| graph| || Raw| graph| ||
| -------------------------------|
|
| || Community| 1| ||
| ----------------|
| || *AFGHANISTAN*| || _| ||
| || *ALGERIA*| || _| ||
| || *ANGOLA*| || _| ||
| || _| || *ANTIGUA| AND| BARBUDA*| ||
| || *AZERBAIJAN*| || _| ||
| || _| || *BAHAMAS*| ||
| || *BAHRAIN*| || _| ||
| || *BANGLADESH*| || _| ||
| || _| || *BARBADOS*| ||
| || _| || *BELIZE*| ||
| || _| || *BENIN*| ||
| || BHUTAN| || BHUTAN| ||
| || *BOLIVIA*| || _| ||
| || _| || *BOTSWANA*| ||
| || *BRUNEI| DARUSSALAM*| || _| ||
| || _| || *BURKINA| FASO*| ||
| || BURUNDI| || BURUNDI| ||
| || *CAMBODIA*| || _| ||
| || _| || *CAMEROON*| ||
| || _| || *CABO| VERDE*| ||
| || _| || *CENTRAL| AFRICAN| REPUBLIC*| ||
| || CHAD| || CHAD| ||
| || *CHINA*| || _| ||
| || COMOROS| || COMOROS| ||
| || CONGO| || CONGO| ||
| || _| || *COTE| D'IVOIRE*| ||
| || *CUBA*| || _| ||
| || *DEMOCRATIC| PEOPLE'S| REPUBLIC| OF| KOREA*| || _| ||
| || DEMOCRATIC| REPUBLIC| OF| THE| CONGO| || DEMOCRATIC| REPUBLIC| OF| THE| CONGO| ||
| || *DJIBOUTI*| || _| ||
| || DOMINICA| || DOMINICA| ||
| || *ECUADOR*| || _| ||
| || *EGYPT*| || _| ||
| || _| || *EL| SALVADOR*| ||
| || EQUATORIAL| GUINEA| || EQUATORIAL| GUINEA| ||
| || *ERITREA*| || _| ||
| || *ETHIOPIA*| || _| ||
| || _| || *FIJI*| ||
| || GABON| || GABON| ||
| || GAMBIA| || GAMBIA| ||
| || _| || *GHANA*| ||
| || _| || *GRENADA*| ||
| || _| || *GUATEMALA*| ||
| || *GUINEA*| || _| ||
| || _| || *GUINEA-BISSAU*| ||
| || *GUYANA*| || _| ||
| || _| || *HAITI*| ||
| || _| || *HONDURAS*| ||
| || *INDIA*| || _| ||
| || *INDONESIA*| || _| ||
| || *IRAN| (ISLAMIC| REPUBLIC| OF)*| || _| ||
| || *IRAQ*| || _| ||
| || *JORDAN*| || _| ||
| || KENYA| || KENYA| ||
| || _| || *KIRIBATI*| ||
| || *KUWAIT*| || _| ||
| || *KYRGYZSTAN*| || _| ||
| || *LAOS*| || _| ||
| || *LEBANON*| || _| ||
| || _| || *LESOTHO*| ||
| || _| || *LIBERIA*| ||
| || *LIBYA*| || _| ||
| || _| || *MADAGASCAR*| ||
| || _| || *MALAWI*| ||
| || *MALAYSIA*| || _| ||
| || *MALDIVES*| || _| ||
| || *MALI*| || _| ||
| || *MAURITANIA*| || _| ||
| || *MAURITIUS*| || _| ||
| || *MOROCCO*| || _| ||
| || *MOZAMBIQUE*| || _| ||
| || MYANMAR| || MYANMAR| ||
| || *NAMIBIA*| || _| ||
| || _| || *NAURU*| ||
| || *NEPAL*| || _| ||
| || *NICARAGUA*| || _| ||
| || NIGER| || NIGER| ||
| || NIGERIA| || NIGERIA| ||
| || *OMAN*| || _| ||
| || *PAKISTAN*| || _| ||
| || _| || *PANAMA*| ||
| || _| || *PAPUA| NEW| GUINEA*| ||
| || _| || *PARAGUAY*| ||
| || *QATAR*| || _| ||
| || _| || *RWANDA*| ||
| || _| || *SAINT| KITTS| AND| NEVIS*| ||
| || _| || *SAINT| LUCIA*| ||
| || SAINT| VINCENT| AND| THE| GRENADINES| || SAINT| VINCENT| AND| THE| GRENADINES| ||
| || _| || *SAO| TOME| AND| PRINCIPE*| ||
| || *SAUDI| ARABIA*| || _| ||
| || *SENEGAL*| || _| ||
| || _| || *SEYCHELLES*| ||
| || SIERRA| LEONE| || SIERRA| LEONE| ||
| || *SINGAPORE*| || _| ||
| || _| || *SOLOMON| ISLANDS*| ||
| || SOMALIA| || SOMALIA| ||
| || *SOUTH| AFRICA*| || _| ||
| || *SRI| LANKA*| || _| ||
| || *SUDAN*| || _| ||
| || SURINAME| || SURINAME| ||
| || _| || *ESWATINI*| ||
| || *SYRIA*| || _| ||
| || *TAJIKISTAN*| || _| ||
| || _| || *TIMOR-LESTE*| ||
| || _| || *TOGO*| ||
| || _| || *TONGA*| ||
| || _| || *TRINIDAD| AND| TOBAGO*| ||
| || *TUNISIA*| || _| ||
| || *TURKMENISTAN*| || _| ||
| || _| || *TUVALU*| ||
| || UGANDA| || UGANDA| ||
| || *UNITED| ARAB| EMIRATES*| || _| ||
| || UNITED| REPUBLIC| OF| TANZANIA| || UNITED| REPUBLIC| OF| TANZANIA| ||
| || *UZBEKISTAN*| || _| ||
| || _| || *VANUATU*| ||
| || *VENEZUELA| (BOLIVARIAN| REPUBLIC| OF)*| || _| ||
| || *VIET| NAM*| || _| ||
| || *YEMEN*| || _| ||
| || _| || *ZAMBIA*| ||
| || *ZIMBABWE*| || _| ||
| || _| || *SOUTH| SUDAN*| ||
| || Community| 2| ||
| ----------------|
| || _| || *AFGHANISTAN*| ||
| || *ALBANIA*| || _| ||
| || _| || *ALGERIA*| ||
| || *ANDORRA*| || _| ||
| || _| || *ANGOLA*| ||
| || *AUSTRALIA*| || _| ||
| || *AUSTRIA*| || _| ||
| || _| || *AZERBAIJAN*| ||
| || _| || *BAHRAIN*| ||
| || _| || *BANGLADESH*| ||
| || _| || *BELARUS*| ||
| || *BELGIUM*| || _| ||
| || _| || *BOLIVIA*| ||
| || *BOSNIA| AND| HERZEGOVINA*| || _| ||
| || _| || *BRUNEI| DARUSSALAM*| ||
| || *BULGARIA*| || _| ||
| || _| || *CAMBODIA*| ||
| || *CANADA*| || _| ||
| || _| || *CHINA*| ||
| || *COSTA| RICA*| || _| ||
| || *CROATIA*| || _| ||
| || _| || *CUBA*| ||
| || *CYPRUS*| || _| ||
| || *CZECH| REPUBLIC*| || _| ||
| || _| || *DEMOCRATIC| PEOPLE'S| REPUBLIC| OF| KOREA*| ||
| || *DENMARK*| || _| ||
| || _| || *DJIBOUTI*| ||
| || _| || *ECUADOR*| ||
| || _| || *EGYPT*| ||
| || _| || *ERITREA*| ||
| || *ESTONIA*| || _| ||
| || _| || *ETHIOPIA*| ||
| || *FINLAND*| || _| ||
| || *FRANCE*| || _| ||
| || *GEORGIA*| || _| ||
| || *GERMANY*| || _| ||
| || *GREECE*| || _| ||
| || _| || *GUINEA*| ||
| || _| || *GUYANA*| ||
| || *HUNGARY*| || _| ||
| || *ICELAND*| || _| ||
| || _| || *INDIA*| ||
| || _| || *INDONESIA*| ||
| || _| || *IRAN| (ISLAMIC| REPUBLIC| OF)*| ||
| || _| || *IRAQ*| ||
| || *IRELAND*| || _| ||
| || *ISRAEL*| || _| ||
| || *ITALY*| || _| ||
| || *JAPAN*| || _| ||
| || _| || *JORDAN*| ||
| || _| || *KAZAKHSTAN*| ||
| || _| || *KUWAIT*| ||
| || _| || *KYRGYZSTAN*| ||
| || _| || *LAOS*| ||
| || *LATVIA*| || _| ||
| || _| || *LEBANON*| ||
| || _| || *LIBYA*| ||
| || *LIECHTENSTEIN*| || _| ||
| || *LITHUANIA*| || _| ||
| || *LUXEMBOURG*| || _| ||
| || _| || *MALAYSIA*| ||
| || _| || *MALDIVES*| ||
| || _| || *MALI*| ||
| || *MALTA*| || _| ||
| || *MARSHALL| ISLANDS*| || _| ||
| || _| || *MAURITANIA*| ||
| || _| || *MAURITIUS*| ||
| || *MICRONESIA| (FEDERATED| STATES| OF)*| || _| ||
| || *MONACO*| || _| ||
| || *MONTENEGRO*| || _| ||
| || _| || *MOROCCO*| ||
| || _| || *MOZAMBIQUE*| ||
| || _| || *NAMIBIA*| ||
| || _| || *NEPAL*| ||
| || *NETHERLANDS*| || _| ||
| || *NEW| ZEALAND*| || _| ||
| || _| || *NICARAGUA*| ||
| || *NORWAY*| || _| ||
| || _| || *OMAN*| ||
| || _| || *PAKISTAN*| ||
| || *PALAU*| || _| ||
| || *POLAND*| || _| ||
| || *PORTUGAL*| || _| ||
| || _| || *QATAR*| ||
| || *REPUBLIC| OF| KOREA*| || _| ||
| || *REPUBLIC| OF| MOLDOVA*| || _| ||
| || *ROMANIA*| || _| ||
| || *SAMOA*| || _| ||
| || *SAN| MARINO*| || _| ||
| || _| || *SAUDI| ARABIA*| ||
| || _| || *SENEGAL*| ||
| || *SERBIA*| || _| ||
| || _| || *SINGAPORE*| ||
| || *SLOVAKIA*| || _| ||
| || *SLOVENIA*| || _| ||
| || _| || *SOUTH| AFRICA*| ||
| || *SPAIN*| || _| ||
| || _| || *SRI| LANKA*| ||
| || _| || *SUDAN*| ||
| || *SWEDEN*| || _| ||
| || *SWITZERLAND*| || _| ||
| || _| || *SYRIA*| ||
| || _| || *TAJIKISTAN*| ||
| || *NORTH| MACEDONIA*| || _| ||
| || _| || *TUNISIA*| ||
| || *TURKEY*| || _| ||
| || _| || *TURKMENISTAN*| ||
| || *UKRAINE*| || _| ||
| || _| || *UNITED| ARAB| EMIRATES*| ||
| || *UNITED| KINGDOM*| || _| ||
| || *UNITED| STATES*| || _| ||
| || _| || *UZBEKISTAN*| ||
| || _| || *VENEZUELA| (BOLIVARIAN| REPUBLIC| OF)*| ||
| || _| || *VIET| NAM*| ||
| || _| || *YEMEN*| ||
| || _| || *ZIMBABWE*| ||
| || Community| 3| ||
| ----------------|
| || _| || *ALBANIA*| ||
| || _| || *ANDORRA*| ||
| || *ANTIGUA| AND| BARBUDA*| || _| ||
| || _| || *AUSTRALIA*| ||
| || _| || *AUSTRIA*| ||
| || *BAHAMAS*| || _| ||
| || *BARBADOS*| || _| ||
| || _| || *BELGIUM*| ||
| || *BELIZE*| || _| ||
| || *BENIN*| || _| ||
| || _| || *BOSNIA| AND| HERZEGOVINA*| ||
| || *BOTSWANA*| || _| ||
| || _| || *BULGARIA*| ||
| || *BURKINA| FASO*| || _| ||
| || *CAMEROON*| || _| ||
| || _| || *CANADA*| ||
| || *CABO| VERDE*| || _| ||
| || *CENTRAL| AFRICAN| REPUBLIC*| || _| ||
| || *COLOMBIA*| || _| ||
| || _| || *COSTA| RICA*| ||
| || *COTE| D'IVOIRE*| || _| ||
| || _| || *CROATIA*| ||
| || _| || *CYPRUS*| ||
| || _| || *CZECH| REPUBLIC*| ||
| || _| || *DENMARK*| ||
| || *EL| SALVADOR*| || _| ||
| || _| || *ESTONIA*| ||
| || *FIJI*| || _| ||
| || _| || *FINLAND*| ||
| || _| || *FRANCE*| ||
| || _| || *GEORGIA*| ||
| || _| || *GERMANY*| ||
| || *GHANA*| || _| ||
| || _| || *GREECE*| ||
| || *GRENADA*| || _| ||
| || *GUATEMALA*| || _| ||
| || *GUINEA-BISSAU*| || _| ||
| || *HAITI*| || _| ||
| || *HONDURAS*| || _| ||
| || _| || *HUNGARY*| ||
| || _| || *ICELAND*| ||
| || _| || *IRELAND*| ||
| || _| || *ISRAEL*| ||
| || _| || *ITALY*| ||
| || _| || *JAPAN*| ||
| || *KIRIBATI*| || _| ||
| || _| || *LATVIA*| ||
| || *LESOTHO*| || _| ||
| || *LIBERIA*| || _| ||
| || _| || *LIECHTENSTEIN*| ||
| || _| || *LITHUANIA*| ||
| || _| || *LUXEMBOURG*| ||
| || *MADAGASCAR*| || _| ||
| || *MALAWI*| || _| ||
| || _| || *MALTA*| ||
| || _| || *MARSHALL| ISLANDS*| ||
| || _| || *MICRONESIA| (FEDERATED| STATES| OF)*| ||
| || _| || *MONACO*| ||
| || _| || *MONTENEGRO*| ||
| || *NAURU*| || _| ||
| || _| || *NETHERLANDS*| ||
| || _| || *NEW| ZEALAND*| ||
| || _| || *NORWAY*| ||
| || _| || *PALAU*| ||
| || *PANAMA*| || _| ||
| || *PAPUA| NEW| GUINEA*| || _| ||
| || *PARAGUAY*| || _| ||
| || _| || *POLAND*| ||
| || _| || *PORTUGAL*| ||
| || _| || *REPUBLIC| OF| KOREA*| ||
| || _| || *REPUBLIC| OF| MOLDOVA*| ||
| || _| || *ROMANIA*| ||
| || *RWANDA*| || _| ||
| || *SAINT| KITTS| AND| NEVIS*| || _| ||
| || *SAINT| LUCIA*| || _| ||
| || _| || *SAMOA*| ||
| || _| || *SAN| MARINO*| ||
| || *SAO| TOME| AND| PRINCIPE*| || _| ||
| || _| || *SERBIA*| ||
| || *SEYCHELLES*| || _| ||
| || _| || *SLOVAKIA*| ||
| || _| || *SLOVENIA*| ||
| || *SOLOMON| ISLANDS*| || _| ||
| || _| || *SPAIN*| ||
| || *ESWATINI*| || _| ||
| || _| || *SWEDEN*| ||
| || _| || *SWITZERLAND*| ||
| || _| || *NORTH| MACEDONIA*| ||
| || *TIMOR-LESTE*| || _| ||
| || *TOGO*| || _| ||
| || *TONGA*| || _| ||
| || _| || *TURKEY*| ||
| || *TUVALU*| || _| ||
| || _| || *UKRAINE*| ||
| || _| || *UNITED| KINGDOM*| ||
| || _| || *UNITED| STATES*| ||
| || *VANUATU*| || _| ||
| || *ZAMBIA*| || _| ||
| || *SOUTH| SUDAN*| || _| ||
| || Community| 4| ||
| ----------------|
| || ARGENTINA| || ARGENTINA| ||
| || _| || *BRAZIL*| ||
| || CHILE| || CHILE| ||
| || _| || *COLOMBIA*| ||
| || DOMINICAN| REPUBLIC| || DOMINICAN| REPUBLIC| ||
| || MEXICO| || MEXICO| ||
| || PERU| || PERU| ||
| || URUGUAY| || URUGUAY| ||
| || Community| 5| ||
| ----------------|
| || *JAMAICA*| || _| ||
| || _| || *MONGOLIA*| ||
| || PHILIPPINES| || PHILIPPINES| ||
| || THAILAND| || THAILAND| ||
| || *TRINIDAD| AND| TOBAGO*| || _| ||
| || Community| 6| ||
| ----------------|
| || _| || *ARMENIA*| ||
| || *BELARUS*| || _| ||
| || *MONGOLIA*| || _| ||
| || RUSSIAN| FEDERATION| || RUSSIAN| FEDERATION| ||
| || Community| 7| ||
| ----------------|
| || *ARMENIA*| || _| ||
| || _| || *JAMAICA*| ||
| || *KAZAKHSTAN*| || _| ||
| || Community| 8| ||
| ----------------|
| || *BRAZIL*| || _| ||


One may immediately observe that  most of the reshuffling present here is caused by mix-up in communities 1,2 and 3, albeit in my opinion the fact that in processed graph we can correctly identify the Russia-Belarus block makes the few kilowatt-hours spent detecting it justified.
