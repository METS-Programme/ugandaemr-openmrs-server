obs_template = {
    'person': None, 'concept': None, 'encounter': None, 'order': None, 'obs_datetime': None,
    'location': None, 'obs_group': None, 'accession_number': None, 'value_group': None,
    'value_boolean': None, 'value_coded': None, 'value_coded_name': None, 'value_drug': None,
    'value_datetime': None, 'value_numeric': None, 'value_modifier': None, 'value_text': None,
    'value_complex': None, 'comments': None, 'creator': None, 'date_created': None, 'voided': None,
    'voided_by': None, 'date_voided': None, 'void_reason': None, 'uuid': None, 'facility': None,
    'state': None, 'previous_version': None, 'form_namespace_and_path': None
}
encounter_template = {
    'encounter_type': None, 'patient': None, 'location': None, 'form': None, 'encounter_datetime': None,
    'creator': None, 'date_created': None, 'voided': None, 'voided_by': None, 'date_voided': None,
    'void_reason': None, 'changed_by': None, 'date_changed': None, 'visit': None, 'uuid': None,
    'facility': None, 'state': None
}

encounter_provider_template = {
    'encounter': None, 'provider': None, 'encounter_role': None, 'creator': None, 'date_created': None,
    'changed_by': None, 'date_changed': None, 'voided': None, 'date_voided': None, 'voided_by': None,
    'void_reason': None, 'uuid': None, 'facility': None, 'state': None
}
person_template = {
    'gender': None, 'birthdate': None, 'birthdate_estimated': None, 'dead': None, 'death_date': None,
    'cause_of_death': None, 'creator': None, 'date_created': None, 'changed_by': None, 'date_changed': None,
    'voided': None, 'voided_by': None, 'date_voided': None, 'void_reason': None, 'uuid': None,
    'facility': None, 'state': None, 'deathdate_estimated': None, 'birthtime': None
}
patient_template = {
    'gender': None, 'birthdate': None, 'birthdate_estimated': None, 'dead': None, 'death_date': None,
    'cause_of_death': None, 'creator': None, 'date_created': None, 'changed_by': None, 'date_changed': None,
    'voided': None, 'voided_by': None, 'date_voided': None, 'void_reason': None, 'uuid': None,
    'facility': None, 'state': None, 'deathdate_estimated': None, 'birthtime': None, 'allergy_status': None
}
person_name_template = {
    'preferred': None, 'person': None, 'prefix': None, 'given_name': None, 'middle_name': None,
    'family_name_prefix': None, 'family_name': None, 'family_name2': None, 'family_name_suffix': None,
    'degree': None, 'creator': None, 'date_created': None, 'voided': None, 'voided_by': None,
    'date_voided': None, 'void_reason': None, 'changed_by': None, 'date_changed': None, 'uuid': None,
    'facility': None, 'state': None
}
person_attribute_template = {
    'person': None, 'value': None, 'person_attribute_type': None, 'creator': None, 'date_created': None,
    'changed_by': None, 'date_changed': None, 'voided': None, 'voided_by': None, 'date_voided': None,
    'void_reason': None, 'uuid': None, 'facility': None, 'state': None
}

patient_identifier_template = {
    'patient': None, 'identifier': None, 'identifier_type': None, 'preferred': None, 'location': None,
    'creator': None, 'date_created': None, 'date_changed': None, 'changed_by': None, 'voided': None,
    'voided_by': None, 'date_voided': None, 'void_reason': None, 'uuid': None, 'facility': None,
    'state': None
}
visit_template = {
    'patient': None, 'visit_type': None, 'start_datetime': None, 'stop_datetime': None,
    'indication_concept': None, 'location': None, 'creator': None, 'date_created': None, 'changed_by': None,
    'date_changed': None, 'voided': None, 'voided_by': None, 'date_voided': None, 'void_reason': None,
    'uuid': None, 'facility': None, 'state': None
}
person_address_template = {
    'person': None, 'preferred': None, 'address1': None, 'address2': None, 'city_village': None,
    'state_province': None, 'postal_code': None, 'country': None, 'latitude': None, 'longitude': None,
    'start_date': None, 'end_date': None, 'creator': None, 'date_created': None, 'voided': None,
    'voided_by': None, 'date_voided': None, 'void_reason': None, 'county_district': None, 'address3': None,
    'address4': None, 'address5': None, 'address6': None, 'date_changed': None, 'changed_by': None,
    'uuid': None, 'facility': None, 'state': None
}
provider_template = {
    'person': None, 'name': None, 'identifier': None, 'creator': None, 'date_created': None,
    'changed_by': None, 'date_changed': None, 'retired': None, 'retired_by': None, 'date_retired': None,
    'retire_reason': None, 'uuid': None, 'provider_role': None, 'facility': None, 'state': None
}
encounter_role_template = {
    'name': None, 'description': None, 'creator': None, 'date_created': None, 'changed_by': None,
    'date_changed': None, 'retired': None, 'retired_by': None, 'date_retired': None, 'retire_reason': None,
    'uuid': None, 'facility': None, 'state': None
}

transfered_patient_template = {
    'patient': None, 'transfered_in': None, 'transfered_in_from': None, 'transfered_in_date': None, 'transfered_out': None, 'transfered_out_from': None, 'transfered_out_date': None
}

fingerprint_template = {
    'patient': None, 'finger': None, 'fingerprint': None, 'uploaded': None, 'facility': None, 'state': None
}
