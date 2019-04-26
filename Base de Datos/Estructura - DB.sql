


CREATE (metropolitana:Region {titulo: "Metropolitana", clima: "Cálido"})
	CREATE (ciudadGuatemala:departamento {titulo: "Ciudad de Guatemala"})
	
	CREATE
		(ciudadGuatemala)-[:pertenece_region {roles:['Departamento']}]->(metropolitana)


CREATE (norte:Region {titulo: "Altiplano", clima: "Lluvioso"})
	CREATE (altaVerapaz:departamento {titulo: "Alta Verapaz"})
	CREATE (bajaVerapaz:departamento {titulo: "Baja Verapaz"})
	
	CREATE
		(altaVerapaz)-[:pertenece_region {roles:['Departamento']}]->(norte),
		(bajaVerapaz)-[:pertenece_region {roles:['Departamento']}]->(norte)


CREATE (rpeten:Region {titulo: "Petén", clima: "Cálido"})
	CREATE (peten:departamento {titulo: "Petén"})
	
	CREATE
		(peten)-[:pertenece_region {roles:['Departamento']}]->(rpeten)
	
	
	
CREATE (norOriente:Region {titulo:"Nor-Oriente", clima: "Cálido"})
	CREATE (progreso:departamento {titulo: "El Progreso"})
	CREATE (izabal:departamento {titulo: "Izabal"})
	CREATE (zacapa:departamento {titulo: "Zacapa"})
	CREATE (chiquimula:departamento {titulo: "Chiquimula"})
	
	CREATE
		(progreso)-[:pertenece_region {roles:['Departamento']}]->(norOriente),
		(izabal)-[:pertenece_region {roles:['Departamento']}]->(norOriente),
		(zacapa)-[:pertenece_region {roles:['Departamento']}]->(norOriente),
		(chiquimula)-[:pertenece_region {roles:['Departamento']}]->(norOriente)


CREATE (surOriente:Region {titulo: "Sur-Oriente", clima: "Cálido"})
	CREATE (santaRosa:departamento {titulo: "Santa Rosa"})
	CREATE (jalapa:departamento {titulo: "Jalapa"})
	CREATE (jutiapa:departamento {titulo: "Jutiapa"})
	
	CREATE
		(santaRosa)-[:pertenece_region {roles:['Departamento']}]->(surOriente),
		(jalapa)-[:pertenece_region {roles:['Departamento']}]->(surOriente),
		(jutiapa)-[:pertenece_region {roles:['Departamento']}]->(surOriente)


CREATE (central:Region {titulo: "Central", clima: "Templado"})
	CREATE (sacatepequez:departamento {titulo: "Sacatepéquez"})
	CREATE (chimaltenango:departamento {titulo: "Chimaltenango"})
	CREATE (escuintla:departamento {titulo: "Escuintla"})
	
	CREATE
		(sacatepequez)-[:pertenece_region {roles:['Departamento']}]->(central),
		(chimaltenango)-[:pertenece_region {roles:['Departamento']}]->(central),
		(escuintla)-[:pertenece_region {roles:['Departamento']}]->(central)


CREATE (surOccidente:Region {titulo: "Sur Occidente", clima: "Frío"})
	CREATE (solola:departamento {titulo: "Sololá"})
	CREATE (totonicapan:departamento {titulo: "Totonicapán"})
	CREATE (quetzaltenango:departamento {titulo: "Quetzaltenango"})
	CREATE (suchitepequez:departamento {titulo: "Suchitepéquez"})
	CREATE (retalhuleu:departamento {titulo: "Retalhuleu"})
	CREATE (sanMarcos:departamento {titulo: "San Marcos"})
	
	CREATE
		(solola)-[:pertenece_region {roles:['Departamento']}]->(surOccidente),
		(totonicapan)-[:pertenece_region {roles:['Departamento']}]->(surOccidente),
		(quetzaltenango)-[:pertenece_region {roles:['Departamento']}]->(surOccidente),
		(suchitepequez)-[:pertenece_region {roles:['Departamento']}]->(surOccidente),
		(retalhuleu)-[:pertenece_region {roles:['Departamento']}]->(surOccidente),
		(sanMarcos)-[:pertenece_region {roles:['Departamento']}]->(surOccidente)


CREATE (norOccidente:Region {titulo: "Nor Occidente", clima: "Frío"})
	CREATE (huehue:departamento {titulo: "Huehuetenango"})
	CREATE (quiche:departamento {titulo: "Quiché"})
	
	CREATE
		(huehue)-[:pertenece_region {roles:['Departamento']}]->(norOccidente),
		(quiche)-[:pertenece_region {roles:['Departamento']}]->(norOccidente)


// Pais

create (GTM:pais {titulo:"Guatemala"})
CREATE
		 (metropolitana)-[:regiones {roles:['Regiones']}]->(GTM)
		,(norte)-[:regiones {roles:['Regiones']}]->(GTM)
		,(rpeten)-[:regiones {roles:['Regiones']}]->(GTM)
		
		,(norOriente)-[:regiones {roles:['Regiones']}]->(GTM)
		,(surOriente)-[:regiones {roles:['Regiones']}]->(GTM)
		,(surOccidente)-[:regiones {roles:['Regiones']}]->(GTM)
		,(central)-[:regiones {roles:['Regiones']}]->(GTM)
		,(norOccidente)-[:regiones {roles:['Regiones']}]->(GTM)

// Idioma

CREATE   (qeqchi:idioma {titulo:"Q'eqchi"})
		,(pocomchi:idioma {titulo:"Pocomchi"})
		,(achi:idioma {titulo:"Achí"})
		,(kiche:idioma {titulo:"K'iche'"})
		,(espaniol:idioma {titulo:"Español"})
		,(kaqchikel:idioma {titulo:"Kaqchikel"})
		,(pocoman:idioma {titulo:"Pocoman"})
		,(chorti:idioma {titulo:"Chortí"})
		,(garifuna:idioma {titulo:"Garífuna"})
		,(quekchi:idioma {titulo:"Quekchí"})
		,(mam:idioma {titulo:"Mam"})
		,(tzutujil:idioma {titulo:"Tz'utujil"})

CREATE
		 (metropolitana)-[:idioma_region {roles:['Idioma']}]->(espaniol)
	    ,(metropolitana)-[:idioma_region {roles:['Idioma']}]->(kaqchikel)
		,(metropolitana)-[:idioma_region {roles:['Idioma']}]->(pocoman)
	
		,(norte)-[:idioma_region {roles:['Idioma']}]->(qeqchi)
		,(norte)-[:idioma_region {roles:['Idioma']}]->(pocomchi)
		,(norte)-[:idioma_region {roles:['Idioma']}]->(achi)
		,(norte)-[:idioma_region {roles:['Idioma']}]->(kiche)
		,(norte)-[:idioma_region {roles:['Idioma']}]->(espaniol)
		
		,(norOriente)-[:idioma_region {roles:['Idioma']}]->(chorti)
		,(norOriente)-[:idioma_region {roles:['Idioma']}]->(garifuna)
		,(norOriente)-[:idioma_region {roles:['Idioma']}]->(quekchi)
		,(norOriente)-[:idioma_region {roles:['Idioma']}]->(espaniol)
		
		
		,(central)-[:idioma_region {roles:['Idioma']}]->(kaqchikel)
		,(central)-[:idioma_region {roles:['Idioma']}]->(espaniol)
		,(central)-[:idioma_region {roles:['Idioma']}]->(pocoman)
		
		,(surOccidente)-[:idioma_region {roles:['Idioma']}]->(kaqchikel)
		,(surOccidente)-[:idioma_region {roles:['Idioma']}]->(espaniol)
		,(surOccidente)-[:idioma_region {roles:['Idioma']}]->(mam)
		,(surOccidente)-[:idioma_region {roles:['Idioma']}]->(kiche)
		,(surOccidente)-[:idioma_region {roles:['Idioma']}]->(tzutujil)

// Lugares turisticos

//Sacatepéquez
CREATE   (sac_arco:LUGAR_TURISTICO {titulo:"Arco de Santa Catalina"})
		,(sac_cerro:LUGAR_TURISTICO {titulo:"Cerro de la Cruz"})
		,(sac_iglesiaMerced:LUGAR_TURISTICO {titulo:"Iglesia de La Merced"})
		,(sac_capuchinas:LUGAR_TURISTICO {titulo:"Iglesia y Convento de las Capuchinas"})
		,(sac_iglesiaSanFrancisco:LUGAR_TURISTICO {titulo:"Iglesia de San Francisco"})
		,(sac_catedralSanJose:LUGAR_TURISTICO {titulo:"Catedral de San José"})
		,(sac_parqueCentral:LUGAR_TURISTICO {titulo:"Parque Cenral"})
		,(sac_conventoSantoDomingo:LUGAR_TURISTICO {titulo:"Convento de Santo Domingo"})
		,(sac_conventoSantaClara:LUGAR_TURISTICO {titulo:"Convento Santa Clara"})
		,(sac_museoArteColonial:LUGAR_TURISTICO {titulo:"Museo de Arte Colonial de USAC"})
		,(sac_palacioCapitanes:LUGAR_TURISTICO {titulo:"Palacio de los Capitanes"})
		,(sac_tanqueUnion:LUGAR_TURISTICO {titulo:"Tanque de La Unión"})
		,(sac_cerroSantoDomingo:LUGAR_TURISTICO {titulo:"Santo Domingo del Cerro"})
		,(sac_mercadoArtesaniasCarmen:LUGAR_TURISTICO {titulo:"Mercado de Artesanias El Carmen"})
		,(sac_palacioAyuntamiento:LUGAR_TURISTICO {titulo:"Palacio del Ayuntamiento"})
		,(sac_conventoLaMerced:LUGAR_TURISTICO {titulo:"Convento de La Merced"})
		,(sac_florencia:LUGAR_TURISTICO {titulo:"Parque Ecológico Florencia"})


CREATE
		 (sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_arco)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_cerro)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_iglesiaMerced)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_capuchinas)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_iglesiaSanFrancisco)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_catedralSanJose)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_parqueCentral)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_conventoSantoDomingo)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_conventoSantaClara)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_museoArteColonial)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_palacioCapitanes)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_tanqueUnion)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_cerroSantoDomingo)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_mercadoArtesaniasCarmen)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_palacioAyuntamiento)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_conventoLaMerced)
		,(sacatepequez)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(sac_florencia)


// Petén
CREATE   (peten_tikal:LUGAR_TURISTICO {titulo:"Parque Tikal"})
		,(peten_lagoPetenItza:LUGAR_TURISTICO {titulo:"Lago Petén Itza"})
		,(peten_isla:LUGAR_TURISTICO {titulo:"Isla de Flores"})
		,(peten_lagunaYaxha:LUGAR_TURISTICO {titulo:"Laguna Yaxhá"})
		,(peten_petencito:LUGAR_TURISTICO {titulo:"Petencito"})
		,(peten_actunKan:LUGAR_TURISTICO {titulo:"Parque Actún Kan"})
		,(peten_craterAzul:LUGAR_TURISTICO {titulo:"Cráter Azul"})
		,(peten_biotopoTigre:LUGAR_TURISTICO {titulo:"Biotopo Laguna del Tigre"})
		,(peten_parqueMirador:LUGAR_TURISTICO {titulo:"Parque Nacional El Mirador"})
		,(peten_biotopoNaachtun:LUGAR_TURISTICO {titulo:"Biotopo Naachtún - Dos Lagunas"})
		,(peten_biosferaMaya:LUGAR_TURISTICO {titulo:"Reserva de Biosfera Maya"})
		,(peten_parqueLacandon:LUGAR_TURISTICO {titulo:"Parque Nacional Sierra Del Lacandón"})
		,(peten_reservaMachaquila:LUGAR_TURISTICO {titulo:"Reserva Machaquila"})

CREATE
		 (peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_tikal)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_lagoPetenItza)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_isla)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_lagunaYaxha)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_petencito)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_actunKan)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_craterAzul)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_biotopoTigre)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_parqueMirador)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_biotopoNaachtun)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_biosferaMaya)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_parqueLacandon)
		,(peten)-[:lugares_turisticos {roles:['Lugares Turisticos']}]->(peten_reservaMachaquila)
		
