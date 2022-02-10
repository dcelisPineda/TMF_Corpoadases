-- Table: public."TBL_PALABRAS_CLAVE"

-- DROP TABLE public."TBL_PALABRAS_CLAVE";

CREATE TABLE public."TBL_PALABRAS_CLAVE"
(
  id integer,
  key_word character varying(100),
  "Dimension" character varying(100)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."TBL_PALABRAS_CLAVE"
  OWNER TO postgres;
