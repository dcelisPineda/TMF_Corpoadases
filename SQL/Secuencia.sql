-- Sequence: public.idfact

-- DROP SEQUENCE public.idfact;

CREATE SEQUENCE public.idfact
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.idfact
  OWNER TO postgres;
