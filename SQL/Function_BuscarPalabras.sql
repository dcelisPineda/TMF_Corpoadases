-- Function: public.validarllave(text, text)

-- DROP FUNCTION public.validarllave(text, text);

CREATE OR REPLACE FUNCTION public.validarllave(
    key text,
    dim text)
  RETURNS text AS
$BODY$
declare 
    pa text;
BEGIN	
     SELECT MAX(key_word) key_word  into pa
	FROM public."TBL_PALABRAS_CLAVE" TB
	WHERE similarity(key_word_inicial, translate(key,'áéíóúÁÉÍÓÚäëïöüÄËÏÖÜ','aeiouAEIOUaeiouAEIOU'))>= 0.7 and "Dimension"=dim
	GROUP BY key_word
	LIMIT 1;
      return pa;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;
ALTER FUNCTION public.validarllave(text, text)
  OWNER TO postgres;
