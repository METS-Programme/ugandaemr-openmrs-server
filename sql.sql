DROP  TABLE IF EXISTS facility;

CREATE TABLE `facility` (
  `id`                 INT(11)    NOT NULL AUTO_INCREMENT,
  `uuid`               CHAR(38)   NOT NULL,
  `name`              TEXT,
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS encounter;

CREATE TABLE `encounter` (
  `id`                 INT(11)    NOT NULL AUTO_INCREMENT,
  `encounter_type`     CHAR(38)    NOT NULL,
  `patient`         CHAR(38)    NOT NULL,
  `location`        CHAR(38)             DEFAULT NULL,
  `form`            CHAR(38)             DEFAULT NULL,
  `encounter_datetime` DATETIME   NOT NULL,
  `creator`            CHAR(38)    NOT NULL,
  `date_created`       DATETIME   NOT NULL,
  `voided`             TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`          CHAR(38)             DEFAULT NULL,
  `date_voided`        DATETIME            DEFAULT NULL,
  `void_reason`        VARCHAR(255)        DEFAULT NULL,
  `changed_by`         CHAR(38)             DEFAULT NULL,
  `date_changed`       DATETIME            DEFAULT NULL,
  `visit`           CHAR(38)             DEFAULT NULL,
  `uuid`               CHAR(38)   NOT NULL,
  `facility`           CHAR(38),
  `state`              CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS obs;

CREATE TABLE `obs` (
  `id`                  INT(11)    NOT NULL AUTO_INCREMENT,
  `person`           CHAR(38)    NOT NULL,
  `concept`          CHAR(38)    NOT NULL,
  `encounter`        CHAR(38)             DEFAULT NULL,
  `order`            CHAR(38)             DEFAULT NULL,
  `obs_datetime`        DATETIME   NOT NULL,
  `location`         CHAR(38)             DEFAULT NULL,
  `obs_group`        CHAR(38)             DEFAULT NULL,
  `accession_number`    VARCHAR(255)        DEFAULT NULL,
  `value_group`      CHAR(38)             DEFAULT NULL,
  `value_boolean`       TINYINT(1)          DEFAULT NULL,
  `value_coded`         CHAR(38)             DEFAULT NULL,
  `value_coded_name` CHAR(38)             DEFAULT NULL,
  `value_drug`          CHAR(38)             DEFAULT NULL,
  `value_datetime`      DATETIME            DEFAULT NULL,
  `value_numeric`       DOUBLE              DEFAULT NULL,
  `value_modifier`      VARCHAR(2)          DEFAULT NULL,
  `value_text`          TEXT,
  `value_complex`       VARCHAR(255)        DEFAULT NULL,
  `comments`            VARCHAR(255)        DEFAULT NULL,
  `creator`             CHAR(38)    NOT NULL DEFAULT '0',
  `date_created`        DATETIME   NOT NULL,
  `voided`              TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`           CHAR(38)             DEFAULT NULL,
  `date_voided`         DATETIME            DEFAULT NULL,
  `void_reason`         VARCHAR(255)        DEFAULT NULL,
  `uuid`                CHAR(38)   NOT NULL,
  `facility`            CHAR(38),
  `state`               CHAR(12),
  `previous_version`    INT(11)             DEFAULT NULL,
  `form_namespace_and_path` varchar(255),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS patient;

CREATE TABLE `patient` (
  `id`                  INT(11)    NOT NULL AUTO_INCREMENT,
  `gender`              VARCHAR(50)         DEFAULT '',
  `birthdate`           DATE                DEFAULT NULL,
  `birthdate_estimated` TINYINT(1) NOT NULL DEFAULT '0',
  `dead`                TINYINT(1) NOT NULL DEFAULT '0',
  `death_date`          DATETIME            DEFAULT NULL,
  `cause_of_death`      CHAR(38)             DEFAULT NULL,
  `creator`             CHAR(38)             DEFAULT NULL,
  `date_created`        DATETIME   NOT NULL,
  `changed_by`          CHAR(38)             DEFAULT NULL,
  `date_changed`        DATETIME            DEFAULT NULL,
  `voided`              TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`           CHAR(38)             DEFAULT NULL,
  `date_voided`         DATETIME            DEFAULT NULL,
  `void_reason`         VARCHAR(255)        DEFAULT NULL,
  `uuid`                CHAR(38)   NOT NULL,
  `facility`            CHAR(38),
  `state`               CHAR(12),
  `deathdate_estimated` TINYINT(1) NOT NULL DEFAULT '0',
  `birthtime`           TIME                DEFAULT NULL,
  `allergy_status` VARCHAR(50)  DEFAULT 'Unknown',
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS patient_identifier;

CREATE TABLE `patient_identifier` (
  `id`                    INT(11)     NOT NULL AUTO_INCREMENT,
  `patient`            CHAR(38)     NOT NULL,
  `identifier`            VARCHAR(50) NOT NULL DEFAULT '',
  `identifier_type`       CHAR(38)     NOT NULL ,
  `preferred`             TINYINT(1)  NOT NULL DEFAULT '0',
  `location`           CHAR(38)              ,
  `creator`               CHAR(38)     NOT NULL,
  `date_created`          DATETIME    NOT NULL,
  `date_changed`          DATETIME             DEFAULT NULL,
  `changed_by`            CHAR(38)              DEFAULT NULL,
  `voided`                TINYINT(1)  NOT NULL DEFAULT '0',
  `voided_by`             CHAR(38)              DEFAULT NULL,
  `date_voided`           DATETIME             DEFAULT NULL,
  `void_reason`           VARCHAR(255)         DEFAULT NULL,
  `uuid`                  CHAR(38)    NOT NULL,
  `facility`              CHAR(38),
  `state`                 CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS patient_program;


CREATE TABLE `patient_program` (
  `id`                 INT(11)    NOT NULL AUTO_INCREMENT,
  `patient`         CHAR(38)    NOT NULL,
  `program`         CHAR(38)    NOT NULL,
  `date_enrolled`      DATETIME            DEFAULT NULL,
  `date_completed`     DATETIME            DEFAULT NULL,
  `location`        CHAR(38)             DEFAULT NULL,
  `outcome_concept` CHAR(38)             DEFAULT NULL,
  `creator`            CHAR(38)    NOT NULL,
  `date_created`       DATETIME   NOT NULL,
  `changed_by`         CHAR(38)             DEFAULT NULL,
  `date_changed`       DATETIME            DEFAULT NULL,
  `voided`             TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`          CHAR(38)             DEFAULT NULL,
  `date_voided`        DATETIME            DEFAULT NULL,
  `void_reason`        VARCHAR(255)        DEFAULT NULL,
  `uuid`               CHAR(38)   NOT NULL,
  `facility`           CHAR(38),
  `state`              CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS patient_state;

CREATE TABLE `patient_state` (
  `id`                 INT(11)    NOT NULL AUTO_INCREMENT,
  `patient_state`   CHAR(38)    NOT NULL,
  `patient_program` CHAR(38)    NOT NULL,
  `start_date`         DATE                DEFAULT NULL,
  `end_date`           DATE                DEFAULT NULL,
  `creator`            CHAR(38)    NOT NULL DEFAULT '0',
  `date_created`       DATETIME   NOT NULL,
  `changed_by`         CHAR(38)             DEFAULT NULL,
  `date_changed`       DATETIME            DEFAULT NULL,
  `voided`             TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`          CHAR(38)             DEFAULT NULL,
  `date_voided`        DATETIME            DEFAULT NULL,
  `void_reason`        VARCHAR(255)        DEFAULT NULL,
  `uuid`               CHAR(38)   NOT NULL,
  `facility`           CHAR(38),
  `state`              CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS person;

CREATE TABLE `person` (
  `id`                  INT(11)    NOT NULL AUTO_INCREMENT,
  `gender`              VARCHAR(50)         DEFAULT '',
  `birthdate`           DATE                DEFAULT NULL,
  `birthdate_estimated` TINYINT(1) NOT NULL DEFAULT '0',
  `dead`                TINYINT(1) NOT NULL DEFAULT '0',
  `death_date`          DATETIME            DEFAULT NULL,
  `cause_of_death`      CHAR(38)             DEFAULT NULL,
  `creator`             CHAR(38)             DEFAULT NULL,
  `date_created`        DATETIME   NOT NULL,
  `changed_by`          CHAR(38)             DEFAULT NULL,
  `date_changed`        DATETIME            DEFAULT NULL,
  `voided`              TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`           CHAR(38)             DEFAULT NULL,
  `date_voided`         DATETIME            DEFAULT NULL,
  `void_reason`         VARCHAR(255)        DEFAULT NULL,
  `uuid`                CHAR(38)   NOT NULL,
  `facility`            CHAR(38),
  `state`               CHAR(12),
  `deathdate_estimated` TINYINT(1) NOT NULL DEFAULT '0',
  `birthtime`           TIME                DEFAULT NULL,
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS person_address;

CREATE TABLE `person_address` (
  `id`                INT(11)    NOT NULL AUTO_INCREMENT,
  `person`         CHAR(38)             DEFAULT NULL,
  `preferred`         TINYINT(1) NOT NULL DEFAULT '0',
  `address1`          VARCHAR(255)        DEFAULT NULL,
  `address2`          VARCHAR(255)        DEFAULT NULL,
  `city_village`      VARCHAR(255)        DEFAULT NULL,
  `state_province`    VARCHAR(255)        DEFAULT NULL,
  `postal_code`       VARCHAR(50)         DEFAULT NULL,
  `country`           VARCHAR(50)         DEFAULT NULL,
  `latitude`          VARCHAR(50)         DEFAULT NULL,
  `longitude`         VARCHAR(50)         DEFAULT NULL,
  `start_date`        DATETIME            DEFAULT NULL,
  `end_date`          DATETIME            DEFAULT NULL,
  `creator`           CHAR(38)    NOT NULL,
  `date_created`      DATETIME   NOT NULL,
  `voided`            TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`         CHAR(38)             DEFAULT NULL,
  `date_voided`       DATETIME            DEFAULT NULL,
  `void_reason`       VARCHAR(255)        DEFAULT NULL,
  `county_district`   VARCHAR(255)        DEFAULT NULL,
  `address3`          VARCHAR(255)        DEFAULT NULL,
  `address4`          VARCHAR(255)        DEFAULT NULL,
  `address5`          VARCHAR(255)        DEFAULT NULL,
  `address6`          VARCHAR(255)        DEFAULT NULL,
  `date_changed`      DATETIME            DEFAULT NULL,
  `changed_by`        CHAR(38)             DEFAULT NULL,
  `uuid`              CHAR(38)   NOT NULL,
  `facility`          CHAR(38),
  `state`             CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS person_attribute;

CREATE TABLE `person_attribute` (
  `id`                       INT(11)     NOT NULL AUTO_INCREMENT,
  `person`                CHAR(38)     NOT NULL,
  `value`                    VARCHAR(2500) NOT NULL DEFAULT '',
  `person_attribute_type` CHAR(38)     NOT NULL,
  `creator`                  CHAR(38)     NOT NULL,
  `date_created`             DATETIME    NOT NULL,
  `changed_by`               CHAR(38)              DEFAULT NULL,
  `date_changed`             DATETIME             DEFAULT NULL,
  `voided`                   TINYINT(1)  NOT NULL DEFAULT '0',
  `voided_by`                CHAR(38)              DEFAULT NULL,
  `date_voided`              DATETIME             DEFAULT NULL,
  `void_reason`              VARCHAR(255)         DEFAULT NULL,
  `uuid`                     CHAR(38)    NOT NULL,
  `facility`                 CHAR(38),
  `state`                    CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS person_name;


CREATE TABLE `person_name` (
  `id`                 INT(11)    NOT NULL AUTO_INCREMENT,
  `preferred`          TINYINT(1) NOT NULL DEFAULT '0',
  `person`          CHAR(38)    NOT NULL,
  `prefix`             VARCHAR(50)         DEFAULT NULL,
  `given_name`         VARCHAR(50)         DEFAULT NULL,
  `middle_name`        VARCHAR(50)         DEFAULT NULL,
  `family_name_prefix` VARCHAR(50)         DEFAULT NULL,
  `family_name`        VARCHAR(50)         DEFAULT NULL,
  `family_name2`       VARCHAR(50)         DEFAULT NULL,
  `family_name_suffix` VARCHAR(50)         DEFAULT NULL,
  `degree`             VARCHAR(50)         DEFAULT NULL,
  `creator`            CHAR(38)    NOT NULL,
  `date_created`       DATETIME   NOT NULL,
  `voided`             TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`          CHAR(38)             DEFAULT NULL,
  `date_voided`        DATETIME            DEFAULT NULL,
  `void_reason`        VARCHAR(255)        DEFAULT NULL,
  `changed_by`         CHAR(38)             DEFAULT NULL,
  `date_changed`       DATETIME            DEFAULT NULL,
  `uuid`               CHAR(38)   NOT NULL,
  `facility`           CHAR(38),
  `state`              CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS relationship;

CREATE TABLE `relationship` (
  `id`              INT(11)    NOT NULL AUTO_INCREMENT,
  `person_a`        CHAR(38)    NOT NULL,
  `relationship`    CHAR(38)    NOT NULL,
  `person_b`        CHAR(38)    NOT NULL,
  `start_date`      DATETIME            DEFAULT NULL,
  `end_date`        DATETIME            DEFAULT NULL,
  `creator`         CHAR(38)    NOT NULL,
  `date_created`    DATETIME   NOT NULL,
  `date_changed`    DATETIME            DEFAULT NULL,
  `changed_by`      CHAR(38)             DEFAULT NULL,
  `voided`          TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`       CHAR(38)             DEFAULT NULL,
  `date_voided`     DATETIME            DEFAULT NULL,
  `void_reason`     VARCHAR(255)        DEFAULT NULL,
  `uuid`            CHAR(38)   NOT NULL,
  `facility`        CHAR(38),
  `state`           CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

DROP  TABLE IF EXISTS visit;

CREATE TABLE `visit` (
  `id`                    INT(11)    NOT NULL AUTO_INCREMENT,
  `patient`            CHAR(38)    NOT NULL,
  `visit_type`         CHAR(38)    NOT NULL,
  `start_datetime`          DATETIME   NOT NULL,
  `stop_datetime`          DATETIME            DEFAULT NULL,
  `indication_concept` CHAR(38)             DEFAULT NULL,
  `location`           CHAR(38)             DEFAULT NULL,
  `creator`               CHAR(38)    NOT NULL,
  `date_created`          DATETIME   NOT NULL,
  `changed_by`            CHAR(38)             DEFAULT NULL,
  `date_changed`          DATETIME            DEFAULT NULL,
  `voided`                TINYINT(1) NOT NULL DEFAULT '0',
  `voided_by`             CHAR(38)             DEFAULT NULL,
  `date_voided`           DATETIME            DEFAULT NULL,
  `void_reason`           VARCHAR(255)        DEFAULT NULL,
  `uuid`                  CHAR(38)   NOT NULL,
  `facility`              CHAR(38),
  `state`                 CHAR(12),
  PRIMARY KEY (`id`)
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

  DROP TABLE IF EXISTS encounter_provider;

  CREATE TABLE `encounter_provider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encounter` CHAR(38) NOT NULL,
  `provider` CHAR(38) NOT NULL,
  `encounter_role` CHAR(38) NOT NULL,
  `creator` CHAR(38),
  `date_created` datetime NOT NULL,
  `changed_by` CHAR(38) DEFAULT NULL,
  `date_changed` datetime DEFAULT NULL,
  `voided` tinyint(1)  DEFAULT '0',
  `date_voided` datetime DEFAULT NULL,
  `voided_by` CHAR(38) DEFAULT NULL,
  `void_reason` varchar(255) DEFAULT NULL,
  `uuid` char(38) NOT NULL,
  `facility`              CHAR(38),
  `state`                 CHAR(12),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS provider;

CREATE TABLE `provider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person` CHAR(38) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `identifier` varchar(255) DEFAULT NULL,
  `creator` CHAR(38) NOT NULL,
  `date_created` datetime NOT NULL,
  `changed_by` CHAR(38) DEFAULT NULL,
  `date_changed` datetime DEFAULT NULL,
  `retired` tinyint(1) NOT NULL DEFAULT '0',
  `retired_by` CHAR(38) DEFAULT NULL,
  `date_retired` datetime DEFAULT NULL,
  `retire_reason` varchar(255) DEFAULT NULL,
  `uuid` char(38) NOT NULL,
  `provider_role` CHAR(38) DEFAULT NULL,
  `facility`              CHAR(38),
  `state`                 CHAR(12),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS encounter_role;


CREATE TABLE `encounter_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `creator` char(38) NOT NULL,
  `date_created` datetime NOT NULL,
  `changed_by` char(38) DEFAULT NULL,
  `date_changed` datetime DEFAULT NULL,
  `retired` tinyint(1) NOT NULL DEFAULT '0',
  `retired_by` char(38) DEFAULT NULL,
  `date_retired` datetime DEFAULT NULL,
  `retire_reason` varchar(255) DEFAULT NULL,
  `uuid` char(38) NOT NULL,
  `facility`              CHAR(38),
  `state`                 CHAR(12),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS fingerprint;


CREATE TABLE `fingerprint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `patient` varchar(38) NOT NULL,
  `finger` int(1) DEFAULT NULL,
  `fingerprint` TEXT NOT NULL,
  `uploaded` int DEFAULT 0,
  `facility`    CHAR(38),
  `state`       CHAR(12),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;