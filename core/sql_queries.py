add_person = (
    "INSERT INTO person "
    "(gender,birthdate,birthdate_estimated,dead,death_date,cause_of_death,creator,date_created,changed_by,date_changed,voided,voided_by,date_voided,void_reason,uuid,facility,state,deathdate_estimated,birthtime) "
    "VALUES (%(gender)s,%(birthdate)s,%(birthdate_estimated)s,%(dead)s,%(death_date)s,%(cause_of_death)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s,%(deathdate_estimated)s,%(birthtime)s)"
)
add_person_address = (
    "INSERT INTO person_address "
    "(person,preferred,address1,address2,city_village,state_province,postal_code,country,latitude,longitude,start_date,end_date,creator,date_created,voided,voided_by,date_voided,void_reason,county_district,address3,address4,address5,address6,date_changed,changed_by,uuid,facility,state) "
    "VALUES (%(person)s, %(preferred)s, %(address1)s, %(address2)s, %(city_village)s, %(state_province)s, %(postal_code)s, %(country)s, %(latitude)s, %(longitude)s, %(start_date)s, %(end_date)s, %(creator)s, %(date_created)s, %(voided)s, %(voided_by)s, %(date_voided)s, %(void_reason)s, %(county_district)s, %(address3)s, %(address4)s, %(address5)s, %(address6)s, %(date_changed)s, %(changed_by)s, %(uuid)s, %(facility)s, %(state)s)"
)
add_person_attribute = (
    "INSERT INTO person_attribute "
    "(person,value,person_attribute_type,creator,date_created,changed_by,date_changed,voided,voided_by,date_voided,void_reason,uuid,facility,state) "
    "VALUES (%(person)s,%(value)s,%(person_attribute_type)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s)"
)
add_person_name = (
    "INSERT INTO person_name "
    "(preferred,person,prefix,given_name,middle_name,family_name_prefix,family_name,family_name2,family_name_suffix,degree,creator,date_created,voided,voided_by,date_voided,void_reason,changed_by,date_changed,uuid,facility,state) "
    "VALUES (%(preferred)s,%(person)s,%(prefix)s,%(given_name)s,%(middle_name)s,%(family_name_prefix)s,%(family_name)s,%(family_name2)s,%(family_name_suffix)s,%(degree)s,%(creator)s,%(date_created)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(changed_by)s,%(date_changed)s,%(uuid)s,%(facility)s,%(state)s)"
)

add_patient = (
    "INSERT INTO patient "
    "(gender,birthdate,birthdate_estimated,dead,death_date,cause_of_death,creator,date_created,changed_by,date_changed,voided,voided_by,date_voided,void_reason,uuid,facility,state,deathdate_estimated,birthtime,allergy_status) "
    "VALUES (%(gender)s,%(birthdate)s,%(birthdate_estimated)s,%(dead)s,%(death_date)s,%(cause_of_death)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s,%(deathdate_estimated)s,%(birthtime)s,%(allergy_status)s)"
)

add_patient_identifier = (
    "INSERT INTO patient_identifier "
    "(patient,identifier,identifier_type,preferred,location,creator,date_created,date_changed,changed_by,voided,voided_by,date_voided,void_reason,uuid,facility,state) "
    "VALUES (%(patient)s,%(identifier)s,%(identifier_type)s,%(preferred)s,%(location)s,%(creator)s,%(date_created)s,%(date_changed)s,%(changed_by)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s)"
)
add_visit = (
    "INSERT INTO visit "
    "(patient,visit_type,start_datetime,stop_datetime,indication_concept,location,creator,date_created,changed_by,date_changed,voided,voided_by,date_voided,void_reason,uuid,facility,state) "
    "VALUES (%(patient)s,%(visit_type)s,%(start_datetime)s,%(stop_datetime)s,%(indication_concept)s,%(location)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s)"
)
add_encounter = (
    "INSERT INTO encounter "
    "(encounter_type,patient,location,form,encounter_datetime,creator,date_created,voided,voided_by,date_voided,void_reason,changed_by,date_changed,visit,uuid,facility,state) "
    "VALUES (%(encounter_type)s,%(patient)s,%(location)s,%(form)s,%(encounter_datetime)s,%(creator)s,%(date_created)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(changed_by)s,%(date_changed)s,%(visit)s,%(uuid)s,%(facility)s,%(state)s)"
)
add_obs = (
    "INSERT INTO obs "
    "(person,concept,encounter,`order`,obs_datetime,location,obs_group,accession_number,value_group,value_boolean,value_coded,value_coded_name,value_drug,value_datetime,value_numeric,value_modifier,value_text,value_complex,comments,creator,date_created,voided,voided_by,date_voided,void_reason,uuid,facility,state,previous_version) "
    "VALUES (%(person)s,%(concept)s,%(encounter)s,%(order)s,%(obs_datetime)s,%(location)s,%(obs_group)s,%(accession_number)s,%(value_group)s,%(value_boolean)s,%(value_coded)s,%(value_coded_name)s,%(value_drug)s,%(value_datetime)s,%(value_numeric)s,%(value_modifier)s,%(value_text)s,%(value_complex)s,%(comments)s,%(creator)s,%(date_created)s,%(voided)s,%(voided_by)s,%(date_voided)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s,%(previous_version)s)"
)

add_encounter_provider = (
    "INSERT INTO encounter_provider "
    "(encounter,provider,encounter_role,creator,date_created,changed_by,date_changed,voided,date_voided,voided_by,void_reason,uuid,facility,state) "
    "VALUES (%(encounter)s,%(provider)s,%(encounter_role)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(voided)s,%(date_voided)s,%(voided_by)s,%(void_reason)s,%(uuid)s,%(facility)s,%(state)s)"
)

add_metadatasharing_imported_package = (
    "INSERT INTO metadatasharing_imported_package "
    "(uuid,group_uuid,subscription_url,subscription_status,date_created,date_imported,name,description,import_config ,remote_version,version ,facility) "
    "VALUES (%(uuid)s, %(group_uuid)s, %(subscription_url)s, %(subscription_status)s, %(date_created)s, %(date_imported)s, %(name)s, %(description)s, %(import_config)s, %(remote_version)s, %(version)s, %(facility)s)"
)

add_facility = (
    "INSERT INTO facility "
    "(uuid,name) "
    "VALUES (%(uuid)s, %(name)s)"
)

add_provider = (
    "INSERT INTO provider "
    "(person,name,identifier,creator,date_created,changed_by,date_changed,retired,retired_by,date_retired,retire_reason ,uuid,provider_role,facility,state) "
    "VALUES (%(person)s,%(name)s,%(identifier)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(retired)s,%(retired_by)s,%(date_retired)s ,%(retire_reason)s,%(uuid)s,%(provider_role)s,%(facility)s,%(state)s)"
)

add_encounter_role = (
    "INSERT INTO encounter_role "
    "(name,description,creator,date_created,changed_by,date_changed,retired,retired_by,date_retired,retire_reason,uuid,facility,state) "
    "VALUES (%(name)s,%(description)s,%(creator)s,%(date_created)s,%(changed_by)s,%(date_changed)s,%(retired)s,%(retired_by)s,%(date_retired)s,%(retire_reason)s,%(uuid)s,%(facility)s,%(state)s)"
)

add_fingerprint = (
    "INSERT INTO fingerprint "
    "(patient, finger, fingerprint, date_created, facility, state) "
    "VALUES (%(patient)s, %(finger)s, %(fingerprint)s, %(date_created)s, %(facility)s, %(state)s)"
)

query_one = (
    "SELECT * FROM  %(table_name)s WHERE %(primary_column)s = %(primary_value)s"
)