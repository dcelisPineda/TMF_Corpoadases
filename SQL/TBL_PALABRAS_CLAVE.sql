	
	INSERT INTO public."TBL_PALABRAS_CLAVE"(
            id, key_word, "Dimension",key_word_inicial)
    VALUES 
    ((SELECT MAX(ID) + 1 FROM public."TBL_PALABRAS_CLAVE"),
   	'', 
	'TIEMPOSANCION',
	'MESES'
	);
	INSERT INTO public."TBL_PALABRAS_CLAVE"(
            id, key_word, "Dimension",key_word_inicial)
    VALUES 
    ((SELECT MAX(ID) + 1 FROM public."TBL_PALABRAS_CLAVE"),
   	',', 
	'TIEMPOSANCION',
	'Y'
	);
	INSERT INTO public."TBL_PALABRAS_CLAVE"(
            id, key_word, "Dimension",key_word_inicial)
    VALUES 
    ((SELECT MAX(ID) + 1 FROM public."TBL_PALABRAS_CLAVE"),
   	'', 
	'TIEMPOSANCION',
	'DIAS'
	);
	INSERT INTO public."TBL_PALABRAS_CLAVE"(
            id, key_word, "Dimension",key_word_inicial)
    VALUES 
    ((SELECT MAX(ID) + 1 FROM public."TBL_PALABRAS_CLAVE"),
   	'', 
	'TIEMPOSANCION',
	'DÍA'
	);
	INSERT INTO public."TBL_PALABRAS_CLAVE"(
            id, key_word, "Dimension",key_word_inicial)
    VALUES 
    ((SELECT MAX(ID) + 1 FROM public."TBL_PALABRAS_CLAVE"),
   	'', 
	'TIEMPOSANCION',
	'DÍAS'
	);