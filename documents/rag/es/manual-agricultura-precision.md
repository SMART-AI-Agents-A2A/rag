---
title: Manual de Agricultura de Precisión
source: Manualagricultura.pdf
year: 2014
crop: agriculture
region: cono-sur
topic: agricultura-precision
document_type: technical_manual
language: es
scope: Manual em espanhol sobre diagnóstico, integração de informações, tomada de decisão e implementação de agricultura de precisão no Cone Sul.
reference: IICA/PROCISUR, Manual de agricultura de precisión, Montevideo, 2014, ISBN 978-92-9248-545-0.
review_status: approved
---

# Manual de Agricultura de Precisión

## Resumo

Documento aprovado para ingestão no RAG a partir da conversão automática melhorada do PDF bruto. Usar com atenção ao escopo, idioma e referência original.

## Escopo e limitações

Manual em espanhol sobre diagnóstico, integração de informações, tomada de decisão e implementação de agricultura de precisão no Cone Sul.

Este documento está em `review_status: approved` e faz parte do corpus RAG documental.

## Conteúdo técnico convertido

### Página 3

MANUAL

DE AGRICULTURA DE

PRECISIÓN

Editores:

Evandro Chartuni Mantovani

Empresa Brasileira de Pesquisa

Agropecuaria (EMBRAPA)

Carlos Magdalena

Instituto Nacional de Tecnología

Agropecuaria (INTA)

Programa Cooperativo para el Desarrollo Tecnológico

Agroalimentario y Agroindustrial del Cono Sur

### Página 4

Instituto Interamericano de Cooperación para la Agricultura (IICA), 2014.

Manual de agricultura de precisión por IICA se encuentra bajo una Licencia Creative Commons Reconocimiento-Compartir igual 3.0 IGO (CC-BY-SA 3.0 IGO) (http://creativecommons.org/licenses/by-sa/3.0/igo/) Creado a partir de la obra en www.iica.int El Instituto promueve el uso justo de este documento. Se solicita que sea citado apropiadamente cuando corresponda.

Esta publicación también está disponible en formato electrónico (PDF) en el sitio Web institucional en http://www.iica.int

Coordinación editorial: Evandro Chartuni Mantovani y Carlos Magdalena

Corrección de estilo: Virginia Rodríguez, Valentina Chiocchi y Malvina Galván

Adaptación al español: Virginia Rodríguez y Valentina Chiocchi

Ilustración de tapa y portada de capítulos: Gonzalo Rocha

Diseño de tapa: Esteban Grille

Diagramación: Esteban Grille

Impresión: Imprenta Boscana

Manual de agricultura de precisión / IICA, PROCISUR - Montevideo: IICA, 2014

176 p.; 20 cm X 20 cm

ISBN: 978-92-9248-545-0

1. Agricultura de precisión 2. Sistemas de posicionamiento global 3. Sistemas de información geográfica 4. Instrumentos de medición 5. Análisis de datos 6. Tecnología 7. Cambio tecnológico 8. Argentina 9. Bolivia 10. Brasil 11. Chile 12. Paraguay 13. Uruguay I. IICA II. PROCISUR III. Título AGRIS DEWEY E14 338.16

### Página 5

CONTENIDO

PRESENTACIÓN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

INTRODUCCIÓN.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

PARTE 1

Abordaje y herramientas para el diagnóstico

de áreas de producción

1.1. Uso del Sistema de Posicionamiento Global

en la caracterización de áreas agrícolas

Darly Geraldo Sena Junior y Francisco de Assis

de Carvalho Pinto.. ................................................................................................ 14

1.2. Uso de Sistema de Informaciones Geográficas para

espacialización de datos del área de producción agrícola

Elena Charlotte Landau, Daniel Pereira Guimarães

y André Hirsch....................................................................................................... 24

1.3. Monitores de rendimiento y mapeo

Ricardo Melchiori, Kemerer, Alejandra C. e Albarenque, Susana M.. ............................... 32

1.4. Adquisición remota y agricultura de precisión

Carlos Alberto Vettorazzi y Stanley Best................................................................... 38

1.5. Muestreo para mapeo y manejo de la fertilidad del suelo

Álvaro V. Resende y Antonio M. Coelho.................................................................... 49

1.6. Técnicas avanzadas de análisis para los cultivos a tiempo real

Rodrigo Quintana. ................................................................................................. 60

### Página 6

PARTE 2

Integración de informaciones y toma

de decisiones

2.1. Creación de mapas de manejo con datos espaciales

Elena Charlotte Landau, Ziany Neiva Brandão, Carla

Moreira de Faria.................................................................................................... 76

2.2. Uso de la geoestadística y los sistemas de información

geográfica en agricultura

Dario E. Fernández y Manel Ribes i Dasi. ................................................................ 86

2.3. Interpretación de informaciones espacializadas y definición

de unidades de manejo

Ricardo Melchiori, Alejandra Kemerer y Susana Albarenque.. ................................... 93

2.4. Aspectos económicos: análisis de viabilidad de adopción

de intervenciones en los sistemas de producción

Marc Vanacht........................................................................................................ 99

2.5. Monitoreo temporal de los sistemas de producción para

la toma de decisiones y mejora

Evandro Chartuni Mantovani y Gisela de Avellar..................................................... 110

PARTE 3

Implementación de la agricultura de precisión

3.1 Tecnología de precisión para gestión de nutrientes

Harold Reetz.. ..................................................................................................... 122

3.2. Sistemas de guía por satélite, automatización agrícola

y controladores electrónicos

Stanley Best........................................................................................................ 133

3.3. Sensores de nitrógeno para la medición y aplicación

en el cultivo en tiempo real

Lorenzo León.. .................................................................................................... 148

3.4. Monitoreo de desempeño y retorno de las prácticas de

la agricultura de precisión

Andrés Méndez, Fernando Scaramuzza, Juan Pablo Vélez

y Diego Villarroel.. ............................................................................................... 160

ANEXO. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

BIBLIOGRAFÍA. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173

### Página 7

PRÓLOGO

El Programa Cooperativo para el Desarrollo las tecnologías de las comunicaciones, el sensoTecnológico Agroalimentario y Agroindustrial del ramiento remoto, la inteligencia computacional Cono Sur (PROCISUR), creado en 1980 con el apo- y minería de datos, entre otras, han permitido el yo del Banco Interamericano de Desarrollo (BID), desarrollo de equipos y sistemas altamente especonstituye una iniciativa conjunta de los Institutos cializados, con una capacidad enorme para adquiNacionales de Investigación Agropecuaria –INIA– de rir, procesar y analizar información de todo tipo.

Argentina, Bolivia, Brasil, Chile, Paraguay y Uruguay, Esto está cambiando profundamente la forma de y el Instituto Interamericano de Cooperación para la gestionar y la toma de decisiones en los procesos Agricultura (IICA). productivos, en los diferentes niveles y escalas en En el año 2006 PROCISUR publicó el primer que se desenvuelve la nueva agricultura. En ese libro regional sobre agricultura de precisión, que sentido el concepto inicial de la agricultura de predescribió los aspectos conceptuales como tam- cisión, que se centraba en el conocimiento y mabién los primeros avances que esta tecnología nejo de la variabilidad espacial y temporal de los emergente estaba plasmando en algunos paí- suelos, ha ido evolucionando a la integración de ses de la región. Los autores de “Agricultura de tecnologías más amplias en distintas etapas de los Precisión: Integrando conocimientos para una procesos productivos, donde el acceso y manejo agricultura moderna y sustentable” fueron investi- de la información de todo tipo es fundamental para gadores pioneros, que con el apoyo de los INIA y la gestión integral y competitividad de las empreorganizaciones de productores, daban inicio a una sas, cualquiera sea su escala. revolución tecnológica en la agricultura regional. Sin embargo, este impresionante desarrollo Han pasado más de ocho años y el avance tec- tecnológico requiere también de una importante nológico ha continuado con un desarrollo cada vez adecuación institucional, motivada principalmente más sorprendente. Los avances en la electrónica, por la naturaleza y la alta especialización de es-

5

### Página 8

tas nuevas tecnologías. El desarrollo de recursos

humanos, la capacidad para trabajar en forma

interdisciplinaria e interinstitucional, nuevos enfoques para la difusión y capacitación, son requisitos indispensables para innovar en la forma de como estas nuevas tecnologías puedan efectivamente impactar a gran escala en la agricultura.

La contribución que hace PROCISUR con este

segundo libro “Manual de agricultura de precisión”

es poner en un contexto simple los conocimientos

y avances que hay en este conjunto de nuevas tecnologías emergentes. La publicación fue pensada con el objetivo de facilitar el acceso a información, entrenamiento y capacitación de profesionales extensionistas que tienen que enfrentar estos nuevos desafíos que presenta la agricultura de precisión y que sin duda serán de uso cada vez más amplio en el futuro.

Emilio Ruz

Secretario Ejecutivo PROCISUR

6

### Página 9

INTRODUCCIÓN

Existen evidencias de que se vive un cambio de bros del Programa Cooperativo para el Desarrollo época, la era industrial está en crisis y se comienza Tecnológico Agroalimentario y Agroindustrial del a transitar lo que algunos autores llaman post-in- Cono Sur (PROCISUR), poseen recursos hudustrialismo o era del conocimiento. La proble- manos altamente especializados en tecnología mática global del industrialismo está provocando agropecuaria, pero tienen escasas capacidades problemas ambientales, energéticos, alimentarios, de difusión en estas nuevas tecnologías. Si bien sociales, económicos y financieros que han gene- es cierto que los niveles de conocimiento e inforrado una profunda crisis mundial que afecta a las mación requieren de integración interinstitucional, principales economías y que tiene consecuencias sería necesaria la incorporación de estos perfiles, hasta el momento impredecibles. para facilitar la articulación con el sector privado y Actualmente se observan profundos cambios con otros actores públicos como organizaciones tecnológicos: el desarrollo de la electrónica y de de investigación y universidades. las tecnologías de la información y comunica- Son pilares fundamentales para llevar adelante ción ha favorecido la difusión de la agricultura de este objetivo la capacitación y el desarrollo del coprecisión. Si bien este concepto está vinculado nocimiento a través de una red de universidades, al manejo de la variabilidad espacial y temporal institutos tecnológicos y sistemas de extensión, en la producción agropecuaria, en muchos ca- se debería poner foco en el fortalecimiento de los sos se asocia a la aplicación de la tecnología del recursos humanos especializados en las nuevas post- industrialismo. tecnologías, además de promover la articulación La aplicación virtuosa del concepto de agri- e integración institucional, con el convencimiento cultura de precisión está asociada a una visión de que en la nueva época que se transita no habrá sistémica e interdisciplinaria. Los institutos nacio- innovación sin interdisciplina y sin interinstitucionales de investigación agropecuaria (INIA), miem- nalidad. En síntesis, sería pertinente y necesario

7

### Página 10

promover los conceptos y herramientas de la agri- sis en el desarrollo de los sistemas guiados por cultura de precisión a través de un programa piloto satélites, automatización agrícola y controladode extensión. res electrónicos. Se desarrolla la temática de aplicación de insumos a tasa variable basada Contenidos del manual en mapas de aplicación y en tiempo real. Se analiza el desempeño y retorno de las prácticas El Manual fue dividido en tres partes para facide agricultura de precisión. litar su utilización:

• La primera parte desarrolla el abordaje y las

herramientas para el diagnóstico de áreas de Objetivo de este manual

producción, donde se describen los procedi- El presente manual fue elaborado con una vimientos básicos para la adquisición de datos sión simple y práctica y con el objetivo de facilitar y construcción de mapas georreferenciados. el entrenamiento de profesionales extensionistas Dentro de los puntos tratados en esta primera para la aplicación de la agricultura de precisión en parte, se destaca la utilización de: sistema de diferentes escalas de producción en los países del posicionamiento global, sistemas de informa- Cono Sur. ción geográficos, monitores de productividad, Seguramente, los capítulos podrían tener un adquisición remota de información, muesdesarrollo más extenso y detallado de los temas treo de mapeo y análisis de suelo entre otras temáticas. propuestos, no obstante se optó por un trabajo con lineamientos básicos e integrados de profe-

• La segunda parte aborda el manejo integrado

sionales de los distintos países de la región que

de la información para la toma de decisiones,

cumplirán roles docentes durante los entrenaeste capítulo es de gran importancia considemientos que se desarrollaran por indicación de rando que el objetivo de la agricultura de prelos INIA. Con certeza los entrenamientos dejacisión es la transformación de datos en información organizada para la toma de decisiones. rán una serie de aprendizajes que permitirán la Se apunta al fortalecimiento de los conocimien- edición de un manual más completo en donde tos que faciliten la generación de mapas de se rescaten ejemplos sobre las experiencias manejo con datos espaciales, geoestadística, prácticas de los participantes de los cursos de interpretación de la información y definición de entrenamiento. unidades de manejo, aspectos económicos y Los fines de la agricultura de precisión traen viabilidad de adopción, monitoreo para la toma consigo objetivos implícitos a este manual, que de decisiones y mejora permanente. apuntan a fortalecer la sostenibilidad social, am-

• Por último, la tercera parte analiza la implemen- biental y económica de los productores de nuestación de la agricultura de precisión, con énfa- tra región.

8

### Página 11

Ventajas del uso de la agricultura La agricultura de precisión en tanto se transde precisión en comparación con la forma en una metodología de trabajo permite a los agricultura tradicional pequeños productores a ser menos dependiente de insumos externos a la explotación, mejoranLa agricultura tradicional consideraba a los do la sostenibilidad de los pequeños productores campos agrícolas como homogéneos y la aplicafamiliares. ción de insumos no incluía la variabilidad espacial y temporal de la producción ni el análisis de las causas de esa variabilidad. Visión sistémica de la gestión económica De modo que la agricultura de precisión es del sistema de producción la aplicación de tecnologías y principios para El concepto de gerenciamiento de sistemas el manejo de la variabilidad espacial y temporal de producción ha demostrado ser la forma más asociada a todos los aspectos de la producción adecuada para la utilización de la agricultura de agrícola con el propósito de mejorar la produc- precisión. El análisis de la estructura de costos, tividad del cultivo y la calidad ambiental. (Pierce permite evaluar el impacto de las tareas sugeridas y Nowak, 1999). o de nuevas técnicas empleadas sobre el costo Con este enfoque, las ventajas de la agricul- total de producción e inferir en los retornos económicos esperados. tura de precisión sobre la tradicional son claras y contundentes debido a la posibilidad de utilizar De modo que el Manual ha sido estructurado los insumos de forma cada vez más criteriosa con para analizar el proceso de producción agrícola, dosis adecuadas y de acuerdo a la real necesi- con una visión sistémica, integrando todas las fadad del cultivo. Este manejo del ambiente permite ses del sistema de producción, al mismo tiempo la aplicación de insumos solo en las áreas en las que se realiza la gestión económica del sistema de que resulta necesario y en donde la respuesta de producción. esta intervención tendrá un claro beneficio económico. Se identifica además una ventaja sobre la sostenibilidad ambiental de la producción, ya que se evita la aplicación de insumos en general y de agroquímicos en particular en las áreas en que no son necesarios o se requieren en cantidades inferiores. Esto que permite una disminución del impacto sobre el medio ambiente y una significativa reducción de los recursos energéticos, lo que seguramente aportará a la mitigación del cambio climático global.

9

### Página 13

PARTE 1

ABORDAJE Y HERRAMIENTAS

PARA EL DIAGNÓSTICO DE ÁREAS

DE PRODUCCIÓN

### Página 14

1.1. Uso del Sistema de do con las distancias en relación a los satélites, se

determina el posicionamiento del usuario sobre la

Posicionamiento Global en la superficie terrestre. caracterización de áreas agrícolas Darly Geraldo Sena Junior y Francisco de Assis de ¿Por qué utilizar satélites para el mapeo?

Carvalho Pinto

• No es necesario que exista visión entre las posiciones que se desea relevar, como en la topoDarly Geraldo Sena Junior grafía convencional con el uso del teodolito o estación total. Solo se necesita de una apertura Ingeniero Agrónomo, doctor en Ingeniería Agrícola, profesor al cielo. Esto quiere decir que no puede haber de la Universidad de Federal de Goiás, Campus Jataí -Curso impedimento físico entre la antena del receptor de Agronomía, Jataí, GO, Brasil. y los satélites, como por ejemplo: copas de árdarly.sena@ufg.br boles, construcciones, etc.

• Cuando los satélites operan apropiadamente,

Francisco de Assis de Carvalho Pinto permiten la captura de una ubicación precisa y Ingeniero Agrícola, doctor en Ingeniería Agrícola, profesor rápida, incluso con el receptor en movimiento. de la Universidad de Federal de Viçosa, Departamento de • La información ya se encuentra en forma diIngeniería Agrícola, Viçosa MG, Brasil gital, lo que permite una integración más fácil facpinto@ufv.br con sistemas de informaciones geográficas, de mapeo y computadores de a bordo y controladores de máquinas.

Introducción

• Permite trabajar en cualquier condición de

Dentro de las diferentes propuestas de tectiempo, de día o de noche. nologías para el posicionamiento en el campo, Se puede afirmar que a partir de la disposición los sistemas globales de navegación por satélites del Sistema de Posicionamiento Global (GPS, por (GNSS, por sus siglas en inglés) son actualmente sus siglas en inglés) por parte del Departamento los más populares. Desarrollados para el uso mili- de Defensa de Estados Unidos para el uso civil tar, la disposición de su uso para la comunidad civil al inicio de la década de 1990, se comenzaron a revolucionó la navegación y la medición de áreas georreferenciar los problemas y soluciones para la y distancias, especialmente en el medio rural. Su agricultura. funcionamiento es análogo al método utilizado por Además del GPS, otros ejemplos de GNSS los antiguos navegantes, que determinaban su son: el sistema ruso (GLONASS) iniciado en la ubicación basándose en las estrellas, planetas y Unión Soviética y que se encuentra en pleno funsatélites naturales. Los sistemas actuales utilizan cionamiento, el sistema europeo (GALILEO), chino satélites especialmente desarrollados para ese fin, (COMPASS), indio (IRNSS) y japonés (QZSS), que con órbitas perfectamente conocidas y, de acuer- se encuentran en desarrollo, además de los siste-

12

### Página 15

mas regionales. La expectativa es que en el futuro proyectada para que por lo menos cuatro satélites cercano haya una integración entre los sistemas y estén en el campo de la comunicación de cualse mejore la cobertura y la precisión de las medi- quier receptor, en cualquier lugar del planeta y a ciones. Ya existen en el mercado receptores que cualquier hora del día, en caso de que no haya utilizan simultáneamente GPS y/o GLONASS.1 ningún impedimento físico o de calidad de señal El presente apartado presenta el principio de emitida por el satélite. funcionamiento del GPS, por tratarse del sistema más difundido, en pleno funcionamiento y disponi- Segmento de control ble en todo el mundo. El funcionamiento de los de- El segmento de control monitorea los mensajes más sistemas es muy parecido al GPS. Asimismo, de navegación de los satélites y envía los ajustes se analizarán los diferentes tipos de receptores que sean necesarios. Este segmento opera a parde GPS, conceptos básicos de cartografía para tir de la Base Falcon de la Fuerza Aérea Americana el uso del GPS y ejemplos de su utilización en la en Colorado Springs, Estados Unidos, y también agricultura. contiene cuatro estaciones de monitoreo y tres estaciones de carga distribuidas alrededor del munSegmentos del sistema de do. Las estaciones envían a la Base Falcon inforposicionamiento global maciones para el cálculo de las órbitas de cada satélite, y actualiza esa información en el sistema Este sistema está basado en tres componen- de señales. tes o segmentos:

Segmento de usuario

Segmento espacial

Este segmento está compuesto por los recepPara que el sistema funcione en cualquier lugar tores y antenas que reciben y procesan las señales del planeta, 24 horas al día y sobre cualquier conde los satélites para determinar su ubicación en la dición climática, el segmento espacial está constitierra, en el aire o en el mar. Dentro de la aplicación tuido de por lo menos 24 satélites funcionales. El civil, se pueden citar: relevamiento de datos para número de satélites fluctúa debido a los satélites sistemas georeferrenciados, navegación marítima que son desconectados y a los que son lanzados y terrestre, topografía, servicios de emergencia, para entrar en funcionamiento o permanecer como aviación, posicionamiento preciso, agricultura, foreservas. Los satélites orbitan aproximadamente togrametría, etc.

20 200 km por encima de la superficie terrestre

con tiempo de revolución de aproximadamente 12

horas, en seis planos orbitales con cuatro satéli- Funcionamiento del sistema de tes cada plano. La constelación de satélites fue posicionamiento global Entender cómo el sistema GPS establece la

1 Por siglas en ingles: Global naya Navigatsionnaya Sputnikovaya Sistema

(GLONASS),Indian Regional Navigational Satellite System (IRNSS) y Sistema ubicación ayuda a tomar decisiones correctas por Satélite Quasi-Zenith (QZSS). para la determinación de coordenadas, medición

13 PARTE 1

### Página 16

de áreas y distancias. Aunque se pueda utilizar Medición de distancias

el sistema sin las explicaciones presentadas a Las distancias (d) hasta los satélites son calcucontinuación –y así lo hacen la mayoría de los ladas conociendo la velocidad de desplazamiento usuarios–, la información es de fundamental im- de la señal, que es igual a la velocidad de la luz (v) portancia en la práctica para reducir errores en el y midiendo el intervalo de tiempo (t) necesario para relevamiento de datos. que la señal sea emitida por el satélite y llegue al receptor, o sea:

Posicionamiento

d=v*t

Al conocer la posición de varios satélites y la

Para medir el tiempo de viaje de la señal del

distancia hacia ellos, el receptor GPS puede calGPS, el receptor compara la diferencia entre la secular una posición precisa, para lo cual el sistema ñal generada por el satélite y la generada por él utiliza el concepto de triangulación y la información mismo. Esto se realiza utilizando un código de ruide la velocidad de propagación de la señal. do pseudo-aleatorio (PRN por su sigla en inglés), Una posición se calcula mediante el conoci- único para cada satélite, que es generado al mismiento de la posición de por lo menos cuatro saté- mo tiempo en el receptor y en el satélite después lites y de la distancia del receptor a esos satélites. de la sincronización de los relojes. El tiempo se Cada satélite tiene sus códigos específicos emidetermina de acuerdo con la diferencia entre los tidos constantemente, en dos ondas portadoras puntos semejantes de esos dos códigos.

L1 (1 575,42 MHz) y L2 (1 227,60 MHz). Sobre

las ondas portadoras se modulan los códigos: C/A

en la portadora L1, de uso civil y sobre las porta- Relojes precisos

dores L1 y L2 el código P, de uso militar. Además El cronometraje es importante ya que los códide los códigos, se transmiten diversos mensajes gos del receptor y del satélite deben estar sincrosobre los satélites en funcionamiento (almanaque), nizados. Los satélites tienen relojes atómicos que correcciones de los relojes, calidad de las señales son precisos hasta los nanosegundos (10-9 s), no y otras informaciones del sistema. obstante, son inviables en los receptores. Esos reEl posicionamiento con GPS puede ser reali- ceptores usan relojes convencionales y utilizan la zado con dos tipos de mediciones y receptores: medición de un cuarto satélite para resolver errocon base en el código o con base en las ondas res de reloj. portadoras.

El posicionamiento por el código es el más di- Triangulación

fundido y utilizado en los receptores más baratos, Con la triangulación utilizada por los antiguos los llamados GPS de navegación. El posiciona- navegantes para posicionarse, se puede determiento basado en las ondas portadoras es el utili- minar la posición de un determinado objeto (en el zado en equipos más caros y precisos destinados caso del receptor del GPS), midiendo las distana levantamientos geodésicos. cias de este objeto a tres puntos de coordenadas

14

### Página 17

conocidas (satélites GPS), conforme descripto C) Tercera medición

más abajo y representado en la Figura 1. Al recibir la señal de un tercer satélite, se deA) Primera medición termina una tercera esfera y así se crean dos circunferencias que se interceptan en dos puntos.

En cuanto el receptor capta la señal de un satéTeóricamente, con esas tres mediciones, el receplite, se calcula la distancia hasta éste, por ejemplo

19 000 km, esto significa que el receptor se loca- tor sería capaz de determinar la posición correcta liza en cualquier punto sobre una esfera con este porque uno de los puntos presenta un valor abradio, con el satélite en el centro. surdo y podría ser eliminado por procedimientos matemáticos. Sin embargo, esta posición está deB) Segunda medición terminada en 2D (posición planimétrica).

Al recibir la señal de un segundo satélite, se

calcula la distancia, por ejemplo 20 000 km entre D) Cuarta medición

el satélite y el receptor, y se determina otra esfera. Una cuarta medición decide entre las dos posiComo el área de intersección se da entre dos es- ciones y de esta manera determina la posición del feras y una circunferencia, la posición del receptor receptor en 3D (posición planialtimétrica). El cuarto puede ser cualquier punto sobre el perímetro de satélite también se utiliza para minimizar los erroesa circunferencia. res de sincronización entre los relojes del receptor del satélite (Figura 2).

Figura 1. Medición de la distancia hasta tres satélites para Figura 2. Seguimiento de la señal de 4 satélites para la obtención de localización del punto posición 3D

15 PARTE 1

### Página 18

Tipos de receptores utilizados en la Métodos de posicionamiento

agricultura a. Autónomo: Sin corrección, menor precisión. Al

registrar posiciones en cualquier receptor GPS,

Precisión del sistema ocurrirá un error de hasta 10 m, rastreando por

A continuación se listan algunas variables invo- lo menos cuatro satélites. Son los receptores lucradas en la precisión del GPS: más baratos y más difundidos. a. Tipo de receptor: Los receptores de tipo topo- b. Diferencial: Se aplican correcciones diferengráfico tienen precisión submétrica mientras ciales. La corrección diferencial es el proceso que los receptores de navegación poseen pre- de utilizar datos del satélite, recogidos por un cisión entre 5 y 10 m. Los receptores geodési- receptor localizado en una posición conocida, cos tienen precisión en centímetros. para ajustar las posiciones registradas por receptores móviles. b. Tiempo de relevamiento de una posición geográfica: En general, cuanto mayor es el número c. Autónomo con corrección por algoritmo: No de posiciones (lecturas) relevadas en un lugar, se utiliza corrección diferencial, pero algoritmos mayor es la precisión.2 internos permiten obtener errores por debajo de 1 m. El costo de estos receptores es mayor c. Posición relativa de los satélites: Generalmente, que el de los receptores de navegación. ocurren menos errores cuando se utiliza una constelación de satélites con gran distancia d. Posicionamiento según la fase de la portadora: entre ellos. Por esta razón, las posiciones más Se realiza corrección diferencial con procesaprecisas se obtienen cuando gran parte del cielo está visible. d. Configuración del receptor: La precisión puede depender del nivel de tolerancia establecida en la configuración.3

2 Nota: Actualmente, incluso los receptores de navegación disponen de

una función para calcular la media de las lecturas en una misma posición

para aumentar la precisión de las coordenadas.

3 Nota: Cuando la precisión del receptor es de 5 metros, por ejemplo,

significa que la coordenada proporcionada por el dispositivo varía a cada

instante dentro de una circunferencia de 5 m de radio. Como esa coordenada varía aleatoriamente, el error cambia constantemente, algunas veces cercano a los 5 m y otras cercano a cero, como en el caso del ejemplo que se presenta en la Figura 3. Ese es el motivo principal por el cual, si se observan las coordenadas proporcionadas por un receptor detenido en un Figura 3. Coordenadas proporcionadas por un receptor con precisión punto, se verificará que las coordenadas van a cambiar a cada instante. de 5 m

16

### Página 19

miento de la fase (o portadora). Los receptores de corrección emitida por ejemplo por las radios de precisión submétrica pueden obtener pre- de los faroles de la Marina esparcidos a lo largo de cisiones de hasta 10 cm con el procesamiento la costa brasilera. de la fase. Utilizando una base propia, la estación base envía señal de corrección para el móvil vía radio, Corrección diferencial denominada RTK (del inglés: real time kinematic).

Es necesario utilizar dos receptores para corre- La estación base es colocada bastante cerca del gir los datos diferencialmente. Uno de esos recep- móvil por la dificultad –especialmente en topogratores debe ser instalado sobre un punto de coor- fía accidentada–, para la comunicación entre redenada conocida y configurado como base, mien- ceptores por radio. La otra opción, bastante utitras que otro operará como móvil, para realizar el lizada en la agricultura, es la adquisición de señal registro propiamente dicho. El principio utilizado de corrección de empresas especializadas, que considera que como están siendo rastreados los con estaciones base y satélites de baja órbita, mismos satélites, con una diferencia relativamente proporcionan la señal de corrección para el usuapequeña entre los receptores, el error obtenido en rio. Por un lado, esta opción tiene la ventaja de la base es el mismo obtenido en el móvil, lo cual permitir al usuario la adquisición de un solo receppermite utilizar este error para corregir la coorde- tor, al contrario de la corrección vía link de radio, nada obtenida por el receptor móvil. En este caso, que requiere tener dos receptores. Por otro lado, los receptores son de tipo DGPS (GPS diferencial). los errores obtenidos con la “compra” de la señal Para precisiones submétricas, la mayoría de los fa- de corrección son mayores que con la corrección bricantes de receptores recomienda distancias de RTK, donde el error en la mayor parte de los casos hasta 300 km entre la base y el móvil y precisiones es de alrededor de 5 cm. decimétricas de hasta 60 km. En general, cuanto menor es la distancia base-móvil, menores errores Posicionamiento según la fase de la portadora ocurren. Una vez que las longitudes de onda de las La corrección diferencial puede ser realizada en portadoras L1 y L2 son conocidas, otra forma de post-proceso, donde los datos de la base y del medir el tiempo de desplazamiento de la señal es móvil son almacenados durante el levantamiento por medio de la diferencia de fase entre la onda y al final se descargan en una computadora para emitida por el satélite y su reproducción por el rerealizar la corrección. Es la llamada corrección ceptor. Este tipo de medición garantiza errores de post-proceso, bastante utilizada en mediciones 1 a 2 mm. Para realizar esa medición es necesario topográficas. conocer la cantidad total de longitudes de onda En determinadas situaciones, como direccio- entre el satélite y el receptor, denominada de resonamiento de máquinas (piloto automático) es ne- lución de ambigüedad del sistema. El movimiento cesario que la corrección sea realizada en tiempo del satélite (efecto doppler) permite contar el núreal. Se puede usar una base propia, corrección mero de ciclos entre las dos posiciones del satélite vía satélite ofrecida por empresas, o utilizar la señal que indica la variación de la distancia. De todas

17 PARTE 1

### Página 20

maneras, también se debe conocer el número de rregirse, por lo que la única opción es adquirir un ciclos inicial; para eso, cuanto mayor es el tiempo receptor de buena calidad. en que los dos receptores permanecen en el punto, más precisa será la resolución de ambigüedad.

Conceptos básicos de cartografía

Este tipo de relevamiento, más tardío y preciso,

es utilizado en el georreferenciamiento de propie- El uso correcto del GPS, así como la interpredades rurales en Brasil. tación de la información obtenida, depende de los conocimientos básicos de cartografía que tenga el usuario. Por esta razón, seguidamente se presenFuentes de error tan algunos conceptos importantes para la configuración y operación de receptores GPS.

Retardo atmosférico

Las señales GPS sufren retrasos cuando atra- Datum

viesan la ionosfera y la troposfera, con lo cual, el La superficie del planeta terrestre presenta una tiempo que la señal necesita para alcanzar la tierra serie de elevaciones y depresiones, denominada es mayor, interfiriendo en la posición calculada. superficie topográfica. El objetivo de la cartografía El retardo atmosférico es mayor en las horas es representar esa superficie irregular en una sumás cálidas del día, cuando la ionosfera y la tro- perficie plana, una hoja de papel o, actualmente, posfera se encuentran en su período de mayor en la pantalla de la computadora. Para eso, se utiactividad4. liza una técnica denominada de “proyección”, con la cual se representa la superficie real por medio Multitrayectoria de proyección ortogonal sobre una superficie regular, esférica o elipsoidal.

La multitrayectoria ocurre cuando la señal GPS

es reflejada en un objeto antes de alcanzar la ante- En general, la superficie topográfica se proyecna. El error de multitrayectoria depende de varios ta sobre una superficie con forma matemática coparámetros atmosféricos y ocurren sin ningún avi- nocida, un elipsoide o una esfera. El uso de una so previo. Los errores graves de multitrayectoria superficie esférica es más simple, mientras que el pueden ser visualmente reconocibles en la confec- elipsoide, generado por la revolución de una elipse ción de mapas. sobre su eje menor, se aproxima más a la forma real del globo terrestre, que presenta mayor diámetro en el Ecuador que entre los Polos Sur y Norte.

Ruido del receptor

Una superficie muy importante en la cartograCasi todos los aparatos electrónicos generan fía es el geoide, una superficie de altitud igual a ruidos. El ruido electrónico de un receptor puede interferir en la señal GPS. Este error no puede co- cero, pero que no es utilizada para proyecciones pues es ondulada y no presenta forma matemá-

4 Nota: el GPS funciona en cualquier condición climática, que respete las tica o geométrica definida. El geoide se determitemperaturas mínimas y máximas de los componentes electrónicos. na por medidas gravimétricas y su diferencia en

18

### Página 21

relación al elipsoide varía de un lugar a otro en el considerables en las coordenadas para un misglobo terrestre. El geoide no puede ser utilizado mo lugar pueden observarse al utilizarlas con otro para proyección de la superficie topográfica, pero Datum. De este modo, es fundamental verificar la es bastante utilizado como una superficie de refe- configuración del receptor y la especificación del rencia de nivel. Datum utilizado al informar una coordenada o elaVarios elipsoides son utilizados para un mejor borar una base de datos, para evitar errores graajuste al geoide en diversas partes del mundo. El ves en el futuro. ajuste del geoide al elipsoide da origen a otro tér- En la Tabla 1 se ejemplifica la diferencia en mino bastante común cuando se utiliza el GPS, el las coordenadas del Departamento de Ingeniería Datum, que es el punto de coincidencia entre el Agrícola de la Universidad Federal de Viçosa (UFV), geoide y el elipsoide. Cada región del planeta utili- Minas Gerais, Brasil, con el cambio de Datum. za el Datum que más se ajusta a la superficie física El GPS proporciona co ordenadas globalmente de la tierra. Pueden utilizarse Datum topocéntricos georreferenciadas y las dos más utilizadas para las o geocéntricos. ciencias agrarias son las coordenadas geográficas En un Datum topocéntrico, existe un punto en la y las coordenadas UTM (cartesianas). superficie terrestre donde el elipsoide coincide con la superficie topográfica. Con la llegada del GPS, surgió la posibilidad de utilizar Datum geocéntri- Tabla 1. Coordenadas UTM del Marco del DEA – UFV en el Datum SAD 69 y WGS 84. co, donde la referencia pasa a ser el centro de la Tierra. El GPS utiliza el Datum WGS 84 (del inglés: Datum Este (X) Norte (Y) Altura (Z) world geodetic system 1984), que busca un ajuste SAD-69 721564,498 7701820,194 675,316 al globo y no a regiones específicas.5 WGS-84 721520,710 7701775,634 672,938 En el caso de América del Sur, el más utiliza- Diferencia 43,788 44,560 2,378 do actualmente es el Datum topocéntrico SAD

69 (del inglés: south american Datum 1969), que

está siendo sustituído por el Datum geocéntrico

SIRGAS (sistema de referencia geocéntrico de

América del Sur). Antes del SAD 69, en Brasil se Coordenadas geográficas

utilizaba el Datum Córrego Alegre y todavía se en- Las coordenadas geográficas se utilizan para cuentran muchos mapas y bases de datos elabo- posicionar un punto sobre el elipsoide. Para eso, rados con éste. se definieron líneas imaginarias: los meridianos y El conocimiento del Datum que está siendo uti- los paralelos. lizado por el receptor GPS y en las bases de datos Los meridianos son líneas en el sentido norya existentes es muy importante, pues diferencias te-sur, conectando un polo con otro. Se forman por la intersección de planos que pasan por los

5 La presentación de las coordenadas en la pantalla del receptor puede

ser en cualquier Datum; basta que el usuario defina en la configuración del polos y por el centro de la Tierra con la superficie receptor las opciones de Datum disponibles. del elipsoide. El origen de los meridianos fue defi-

19 PARTE 1

### Página 22

nido arbitrariamente como el meridiano que pasa

por Greenwich, Inglaterra. Los meridianos sirven

para definir las longitudes, o sea, el ángulo formado entre el meridiano de Greenwich, el centro de la Tierra y otro meridiano que pasa por el punto de interés. Las longitudes varían de 0 a 180° en la dirección este (E), considerada positiva, y de

0 a -180° en la dirección oeste (W). Pueden ser

presentadas como signos o en valores absolutos

seguidos por las siglas E (este) o W (oeste).

Los paralelos son líneas imaginarias, en el

sentido este-oeste, creadas por la intersección

Figura 4. Punto de coordenada 80° de longitud (L) y 40° de latitud (N) de planos paralelos entre sí con la superficie del elipsoide. En cuanto un plano para por el centro de la Tierra se da origen al Ecuador. De la misma manera, las latitudes son ángulos formados entre en la superficie de la Tierra que en el mismo ángulo el Ecuador (origen), el centro de la Tierra y otro cercano a los polos, por ejemplo. paralelo que pasa por el punto de interés. Así, las latitudes son referenciadas a partir del Ecuador, de Coordenadas rectangulares

0 a 90° en el hemisferio norte y de 0 a -90° en el

Es un sistema de coordenadas donde la posihemisferio sur. También pueden ser presentadas ción de un punto se define por una abscisa (X) y en valores absolutos, e indicar su hemisferio, N o una ordenada (Y) creada a partir de la proyección S. En la Figura 4 se ilustra cómo es la localización de un punto al utilizar coordenadas geográficas. de dos puntos.

El sistema de coordenadas geográficas es El sistema de proyección es utilizado para ampliamente conocido y bastante utilizado para “transformar” la superficie terrestre considerada indicar la localización de puntos sobre el plane- esférica (o elipsoidal) en un mapa, que es una suta terrestre. Sin embargo, en ciencias agrarias el perficie plana. Para eso es necesario proyectar los GPS es generalmente utilizado para la medición puntos de la superficie de referencia en el plano, de distancias y áreas. En este caso, aunque los dejando claro que toda proyección implica deforreceptores presenten los resultados de manera mación. Existen varios sistemas de proyección que confiable (de acuerdo con la precisión del recep- pueden utilizarse, con mayor o menor deformación, tor), las coordenadas geográficas muchas veces de acuerdo con el área a ser proyectada, región del dificultan cálculos e interpretación de resultados. globo y finalidad del mapa. Cuando se trata del uso Esto ocurre debido a que son ángulos. Así, por la del GPS para ciencias agrarias en el continente suforma de la Tierra, un ángulo de 1° de longitud en ramericano, el sistema más utilizado es la proyecel Ecuador representa una distancia mucho mayor ción Universal Transversa de Mercator (UTM).

20

### Página 23

En el sistema UTM, la proyección del elipsoide

de referencia se realiza sobre un cilindro secante

con la superficie. El eje del cilindro se localiza en

el plano del Ecuador y en el área de proyección

abarca solo una parte de la superficie, los denominados husos o zonas. Los husos son creados porque el cilindro presenta un diámetro menor que la superficie de referencia. Cada huso o zona es representado por el número del huso o por la longitud de su meridiano central.

En la proyección UTM, el globo terrestre se

divide en 60 zonas, a cada 6° de longitud y nuFigura 5. Coordenadas UTM de la ciudad de Jataí – GO, Brasil meradas de 1 a 60 a partir del anti-meridiano de Greenwich para el este. Las deformaciones son escasas, pues la proyección es realizada plano a plano. Otra característica del sistema UTM es que nada en cuál huso o zona se está trabajando, pues utiliza como unidad al metro, lo cual facilita mulas coordenadas se repiten en cada zona. cho el cálculo de áreas y distancias utilizando sus coordenadas. La principal ventaja de utilizar el sistema UTM es que permite representar grandes áreas de suEn cada zona UTM la línea del Ecuador y el meperficie terrestre con pocas deformaciones, sobre ridiano central son representados por líneas rectas, un plano con coordenadas rectangulares y de madefinido el eje X e Y, respectivamente. El Ecuador nera relativamente simple. Otra ventaja, menciorepresenta el cero para el hemisferio norte y el vanada anteriormente, es que utiliza como unidad al lor de 10 millones de m para el hemisferio sur. En metro (m), lo cual facilita los cálculos de áreas y el caso del hemisferio sur, el Ecuador es llamado distancias a partir de las coordenadas. falso norte, y el valor de la coordenada Y va disminuyendo en dirección hacia el Polo Sur. En el caso del hemisferio norte, el valor de la coordenada Y Ejemplos de aplicación en la agricultura aumenta en dirección al Polo Norte. El meridiano Una vez entendida la funcionalidad del GPS, se central recibe el valor de 500 mil m, con el valor pueden imaginar diversas aplicaciones en diferende X aumentando para el este (hacia la derecha) tes sectores de las actividades económicas. En la y disminuyendo para el oeste (hacia la izquierda). agricultura, se pueden destacar las siguientes:

Ver Figura 5. a. Relevamiento planialtimétrico: Debido a su faciEn cuanto todo el meridiano central recibe el va- lidad operacional, el GPS ha sido bastante utilor de 500 mil m y la proyección se realiza zona a lizado para delimitar áreas en el establecimienzona, es fundamental que siempre se indique cuan- to rural. Incluso los aparatos menos precisos, do se utiliza el sistema UTM, además de la coorde- como los de navegación, son utilizados para

21 PARTE 1

### Página 24

ese fin. Sin embargo, debido a los errores que 1.2. Uso de Sistema de

presentan este tipo de aparatos, los mapas

planialtimétricos que realizan deben utilizarse

Informaciones Geográficas para

en forma restringida a decisiones administrati- espacialización de datos del área vas de la propiedad rural como, por ejemplo, de producción agrícola estimar la cantidad de insumos a ser transpor- Elena Charlotte Landau, Daniel Pereira Guimarães y tados para una determinada área. Para su uso André Hirsch fuera del contexto administrativo de la propiedad rural, se deben utilizar aparatos de mayor precisión que sigan las legislaciones pertinenElena Charlotte Landau tes de cada país.

Embrapa Maíz y Sorgo

b. Dirección de máquinas agrícolas: Es conocido charlotte.landau@embrapa.br

el uso del GPS para auxilio de la dirección de

máquinas agrícolas en el momento de la distri- Daniel Pereira Guimarães

bución de insumos en área (dirección con auxi- Embrapa Maíz y Sorgo

lio de barras de luces), o incluso en la completa daniel.guimaraes@embrapa.br

automatización de esta operación (pilotos automáticos). Estos sistemas han permitido una André Hirsch mayor eficiencia en dicha distribución, ya que Universidad Federal de São João del-Rei, Minas Gerais, Brasil. pueden evitar superposición o falla de bandas hirsch_andre@ufsj.edu.br tratadas. Otra ventaja es la posibilidad de trabajar de noche, lo cual aumenta la capacidad Introducción operacional de las máquinas y permite realizar aplicaciones de insumos en horas técnicamen- Actualmente, las principales herramientas que te más adecuadas. posibilitan la aplicación de la agricultura de precisión son: los sistemas de navegación global por c. Georreferenciamiento de parámetros de suesatélites (GNSS) y los sistemas de información lo y planta: Con la disponibilidad del uso del geográfica (SIG) (MAPA, Brasil, 2013).

GPS a partir de la década de 1990, se inició

una revolución en el manejo de la producción Como ya fue presentado, los GNSS (popularagrícola, comparando la eficiencia del uso de mente conocidos como GPS) constituyen receplos insumos en las prácticas de manejo por el tores de señales satelitales que proporcionan al rendimiento promedio con el manejo por am- usuario datos sobre su posición geográfica y albiente (sitio-específico). De esta manera, se titud, además de permitirle planificar mejor la ruta proponen diversas técnicas donde se realizan a seguir para efectuar las demostraciones y lueintervenciones en la agricultura, basadas en go estimar la extensión de trayectos recorridos. el georreferenciamiento de las propiedades fí- Cuando se conecta el receptor a la maquinaria sico-químicas del suelo, de la nutrición de la agrícola utilizada para la cosecha o en un lugar planta y de ataques de plagas y enfermedades. definido por el usuario, se puede registrar informa-

22

### Página 25

ción sobre la localización geográfica de los datos adquisición remota (teledetección), que es un conmuestreados, facilitando el georreferenciamiento y junto de técnicas para obtener información sobre el posterior mapeo de la información relevada en un objeto, área o fenómeno de la superficie terresel campo. tre, sin estar en contacto directo con ellos. A traLos SIG son softwares compuestos por varios vés de la detección, el registro y el análisis del flujo módulos dedicados al almacenamiento y procesa- de energía radiante reflejado o emitido por ellos, miento de datos con localización geográfica cono- las técnicas de teledetección permiten la diferencida (geoprocesamiento) que posibilita el análisis ciación de propiedades de los objetivos naturales, de patrones, integración y modelos espaciales, posibilitando la identificación de características monitoreo, simulación de precisiones y presenta- ambientales como: propiedades del suelo, morción de gran cantidad de información en forma de fología del terreno, patrones de cobertura vegetal mapas, gráficos, figuras y sistemas multimedia. No y uso del suelo, etc. A través de los satélites se hay consenso sobre la definición de un SIG, pero produce una adquisición continua de datos para todo el mundo, que cubre una misma área perióes reconocida su importancia en la organización e dicamente, en intervalos de tiempo que varían de integración espacial de informaciones de diferenhoras a semanas. Fotografías aéreas, imágenes tes naturalezas, tornando posible relacionar con satelitales e imágenes de radar son productos obgran practicidad y relativa precisión una inmensa tenidos a través de la adquisición remota. Cada cantidad de datos, realizar cambios de escala y una presenta ventajas específicas, comparándose de proyección cartográfica, y relacionar bases de sus escalas originales, los diferentes intervalos del datos multidisciplinarios, lo cual facilita la solución espectro electromagnético de los sensores utilizade problemas reales y concretos, así como la gesdos y la frecuencia temporal con que las imágetión adecuada del espacio geográfico (adaptado nes son obtenidas. La forma como los patrones de Jones, 1997 y Landau, 2003). se encuentran representados en las imágenes La aplicación de técnicas de geoprocesamien- puede variar de acuerdo con el sensor, la fecha to para el mapeo de la variabilidad espacial de y el horario de adquisilas áreas de producción agrícola representa una ción de la imagen, su herramienta potente para el gerenciamiento de resolución, la escala, los Mayor información sobre el los sistemas de producción, ya que contribuyen parámetros climáticos y uso de la adquisición remota a la toma de decisiones para la intervención futura las bandas espectrales. será abordada en el Capítulo en áreas de baja productividad (como por ejem- Utilizando las téc- 1.4. Adquisición remota y plo elegir el cultivo que se adapte más, mejorar nicas de geoprocesa- agricultura de precisión las condiciones físicas del suelo para reducir su miento (procesamiento compactación, recomendar determinadas dosis informatizado de datos de aplicación de fertilizantes, etc.) (Adaptado de referenciados geográficamente), la información soMantovani et al. 2004). bre cada lugar puede ser georreferenciada, lo que Otra valiosa fuente de datos al utilizar sistemas permite representar cartográficamente la variación de información geográfica está representada por la espacial y/o temporal de las variables conside-

23 PARTE 1

### Página 26

radas, así como la integración espacial de infor- cubriendo todas las capas la misma área geográmación georreferenciada proveniente de diversas fica y considerando, preferencialmente, el mismo fuentes como: datos recolectados en el campo sistema de proyección cartográfica (Figura 1). con coordenadas geográficas conocidas, mapas Los mapas constituyen representaciones cartemáticos diversos, mapas topográficos, imáge- tográficas simplificadas de la realidad. Los mapas nes georreferenciadas obtenidas mediante adqui- sobre un determinado tema o aspecto de la reasición remota, modelos espaciales y simulación de lidad son denominados mapas temáticos. En los escenarios, geoestadística, etc. Datos asociados sistemas de información geográfica, los mapas tea diferentes mapas temáticos pueden ser super- máticos pueden estar representados por archivos puestos espacialmente y comparados o integra- en formato vectorial (vector files) o matricial (raster dos en diferentes secuencias, según los objetivos files o raster datasets) (Figura 2). de cada trabajo.

Formato vectorial (vector file): es el formato en

La representación espacial de datos sobre el

el cual la localización geográfica de los aspectos

área de producción ha contribuido significativamapeados es almacenada y representada por mente para la toma de decisiones y esfuerzos para vértices definidos por un único par de coordemanejar adecuadamente esas áreas, ya que apunnadas geográficas (punto), por varios pares de ta a producir y obtener información que favorezca coordenadas geográficas (línea) o por varios pael gerenciamiento adecuado de insumos y busca res de coordenadas geográficas si el último par es la forma de solucionar o mitigar conjuntamente coincidente con el primer par (polígono) (Figura 2). cuestiones de tipo ambiental, social y económico.

Como ejemplos de mapas de puntos cabe citar el

En este sentido, la aplicación de técnicas de geoprocesamiento utilizando sistemas de información mapeo de la localización geográfica de áreas de geográfica se ha transformado en una alternativa recolección de muestras en el campo, de bebedeesencial para la integración espacial de los datos ros de animales, de estaciones meteorológicas, de multidisciplinarios a ser considerados. registros de crecimiento de una determinada especie, de focos de incendios, de postes de energía eléctrica, entre muchos otros. Los trazos que Organización de datos con Sistemas de pueden representarse por líneas son: arroyos, ríos Información Geográfica de margen simple, caminos captados vía recepUna de las principales ventajas de los SIG es tores GNSS, carreteras, autopistas, filas de cultipoder integrar datos de diversas áreas de cono- vos agrícolas, canales de riego, líneas de transcimiento con diferentes niveles de detalle, lo que misión, desplazamiento de animales o materiales, permite un enfoque holístico o multidisciplinario en etc. Características que pueden representarse a el estudio del área geográfica de interés. Para que través de polígonos son: lagunas, represas, límiesto sea posible, es necesario que toda la infor- tes municipales, estatales o de países, propiedamación esté organizada en capas o coberturas de des rurales, haciendas, parcelas plantadas, subinformación (layers), cada capa representada por divisiones de áreas de producción agrícola, etc. un conjunto de archivos digitales diferentes, pero Algunas características pueden ser representadas

24

### Página 27

por más de un trazo, pero esto depende de la es- Formato matricial (raster file o raster dataset): cala o del nivel de detalle del mapa. Por ejemplo, Es aquel formato en el cual el área geográfica es en un mapa que abarca todo el estado de Minas representada por una matriz M (i,j), compuesta por Gerais (Brasil), una estancia situada en el Estado i columnas y j líneas, que definen celdas regulares, podrá ser representada por un punto, indicando la cuadradas o rectangulares, denominadas pixels localización geográfica de ésta. En un mapa que (picture elements) (Figura 2). Cada píxel, además muestre informaciones sobre la distribución de tra- de un par de coordenadas geográficas, tiene asobajos de mejoras y cultivos dentro de ese mismo ciado un valor referente al atributo representado, establecimiento rural, él área del establecimiento como por ejemplo: los valores de reflectancia de será representada por un polígono referente a su una imagen satelital, las clases de cobertura vecontorno. getal, los tipos de uso del suelo, la aptitud agrícola para un determinado cultivo, la cantidad de En la mayoría de los SIG, cada trazo geográfico fertilizante utilizada, la productividad por hectárea, mapeado tiene asociado, además de un par de entre muchos otros. coordenadas, un campo o número de indexación o registro y otro campo con el tipo de trazo (punto, Archivos con extensiones GeoTIFF, IMG, JPEG, JPEG2000, MrSID (formato mucho más comprilínea o polígono). De acuerdo al interés, también mido leído por diversos programas SIG), DEM y pueden crearse campos adicionales, a los cuales SDTS son ejemplos de archivos digitales en forpueden asociarse atributos descriptivos espaciamato matricial6. les (altitud, longitud, área, perímetro, pendiente) y no espaciales (cultivo, número de matrícula, año El píxel es la menor unidad física de representade catastro, fecha del cultivo, estado de desarrollo ción de la información en una pantalla, en un prodel cultivo, nombre del responsable, link para fo- yector, o en un televisor digital de pantalla plana, smartphone o tablet. En cualquier archivo matricial tografía digital, observaciones). Los atributos deso raster dataset, como imágenes satelitales, fotocriptivos pueden estar representados por variables grafías aéreas digitalizadas, mapas escaneados a cuantitativas o cualitativas. Todos los atributos son partir del papel y fotografías digitales comunes de organizados en una tabla de atributos (ATT por su personas, objetos o paisajes, el píxel puede ser sigla en inglés) o base de datos relacional (DBF considerado la menor celda de direccionamienpor su sigla en inglés) asociada intrínsecamento de coordenadas geográficas y de un atributo, te al archivo digital del mapa. Las consultas a la como los valores de reflectancia de una imagen base de datos relacional asociada al mapa per- satelital, las clases de suelo en un mapa temátimiten responder cuestiones como: ¿qué existe en co digital, o los colores de una fotografía digital. El un determinado lugar? y ¿cuáles son los lugares tamaño del píxel define la resolución espacial y la que tienen una o más características de interés?

Archivos con extensiones SHP (shapefiles), DXF 6 Por siglas en ingles: GeoTIFF (geocoded tagged image file format), IMG (drawing exchange format), DGN (design) y KML (image raster dataset), JPEG (joint photographic experts group), JPEG2000 (joint photographic experts group 2000), MrSID (multi-resolution seamless (keyhole markup language) son ejemplos de ma- image database), DEM (digital elevation model) y SDTS (spatial data transfer pas digitales en formato vectorial. standard).

25 PARTE 1

### Página 28

escala de mejor visualización de una imagen digi- las mismas operaciones si el mapa estuviese en tal, como por ejemplo, 90 m en un archivo SRTM formato matricial. (escala de 1:340.200), 30 m en una imagen de sa- Los programas de SIG deben ser capaces de télite Landsat (escala de 1:113.400), 10 m en una convertir archivos de formato vectorial para matriimagen de satélite SPOT (escala de 1:37.800), o 1 cial y viceversa.Siempre es preferible realizar este m en una imagen de satélite IKONOS (escala de proceso en el sentido vectorial-matricial y no en 1:3.780). Cuanto mayor el tamaño del píxel, menor el sentido matricial-vectorial, porque en este últila resolución espacial o el nivel de nitidez y detalle mo caso, generalmente, pueden ocurrir pérdidas de la información representada. de datos ya que en el momento de convertir un En términos comparativos, cabe mencionar punto para un píxel, por menor que sea el tamaque cada tipo de formato presenta ventajas y ño del píxel resultante, se pierde una característica desventajas. En general, los archivos vectoriales puntual. Lo mismo ocurre con datos anteriormenson fácilmente manejados por el procesador de te representados por líneas finas. Considerando como ejemplo un mapa de líneas en que las líneas las computadoras, principalmente porque ocurepresentan arroyos con un ancho de 3 m; al conpan poco espacio en la memoria durante la reavertir una línea vectorial para formato matricial con lización de los cálculos y ocupan poco espacio píxel de 5 m de lado, por ejemplo, la línea que reen el disco duro (HD por su sigla en inglés) para su grabado. Además, la nitidez es independiente del zoom aplicado en el monitor de la computadora, porque al aumentar o disminuir el zoom, un punto siempre continúa siendo un punto y una línea continúa siendo una línea. Por otro lado, los archivos matriciales exigen mayor procesamiento por el hecho de que la representación de la información está asociada a una matriz cuadrada o rectangular de pixeles alrededor del trazo en sí, o sea, incluso pixeles que poseen valor 0 (cero) o valor inexistente (missing value) forman parte del archivo y exigen tiempo de procesamiento, ocupan memoria y necesitan espacio en el disco duro. Además, la visualización está comprometida por el zoom aplicado en la pantalla. En el caso de archivos vectoriales con gran cantidad de datos, el tamaño de los archivos y el tiempo de procesamiento pueden exceder significativamente el Figura 1. Ejemplo de organización de datos en SIG, que posibilita la integración espacial y/o temporal de información multidisciplinaria tiempo necesario para la realización de cálculos, representada en mapas temáticos o layers (Fuente: Environmental Systems Research Institute, ESRI) al comparar con el tiempo necesario para realizar

26

### Página 29

presenta el arroyo pasará a tener el mismo ancho Escala geográfica de mapeo

correspondiente al tamaño del píxel, o sea, 5 m de En cartografía, la escala de mapeo indica la reancho, lo que no corresponde a la realidad (Figura lación matemática existente entre las dimensiones 2). Diversos programas de SIG trabajan con los de los elementos representados en un mapa, una dos formatos de archivos. carta, un plano, una imagen satelital o una fotografía aérea y sus dimensiones reales en el terreno, o sea, en cuántas veces el tamaño real fue dividido o reducido en el mapa. Por ejemplo, 1:100.000, se lee “escala de uno a 100 000”, y significa que la superficie terrestre representada en el mapa fue reducida 100 mil veces.

La escala constituye uno de los elementos

esenciales de un mapa, juntamente con la leyenda, la orientación con relación al Norte, la localización geográfica del área representada y la fuente de la base cartográfica. Cuanto mayor sea la escala geográfica, menor será el área abarcada por el mapa y, consecuentemente, mayor la cantidad de detalles presentados en el mapa. En un producto cartográfico pueden aparecer dos tipos de escala:

Escala métrica o numérica: Es representada

por una proporción en la cual el numerador indica

la distancia en el mapa (d) y el denominador, la

distancia correspondiente en el terreno (D), como

“d : N” o “1 : N”.

Escala gráfica: Esta escala representa las distancias en el terreno sobre una regla graduada.

Figura 2. Ejemplos de trazos puntuales, lineales y poligonales Normalmente, la parte de la izquierda está dividirepresentados en los sistemas vectoriales (izquierda) y matricial (derecha) da en décimos, facilitando la medición de distancias con mayor precisión. La escala gráfica debe aparecer obligatoriamente en el mapa generado, para mantener la relación entre el layout del mapa presentado y el tamaño real. Esto garantiza que la escala será mantenida en el caso de ampliaciones para proyecciones utilizando multimedia o reducciones para ajuste al tamaño de la página de algún trabajo en que los mapas sean presentados.

27 PARTE 1

### Página 30

Además de la escala de representación del Tomando como referencia la superficie de promapa, es importante especificar la escala de yección, las proyecciones cartográficas se clasifila(s) fuente(s) cartográfica(s) considerada(s), lo can en tres grandes grupos (Figura 3): cual permite que no se representen cartográfi- • Proyecciones planas o acimutales: la superficie camente datos en una escala mayor que la rela- de proyección es un plano, por ejemplo: procionada con la resolución espacial de los datos yección plana polar. presentados.

• Proyecciones cónicas: la superficie de proyecProyecciones cartográficas ción es un cono, como por ejemplo la proyección cónica de Albers.

Aunque la Tierra no sea una esfera perfecta,

se considera que un globo geográfico representa • Proyecciones cilíndricas: la superficie de proaproximadamente su formato. Pero la represen- yección es un cilindro, por ejemplo: proyección tación cartográfica de una superficie curva en un de Mercator, proyección cilíndrica de Peters. plano de dos dimensiones (hoja de papel, panta- Todas las proyecciones cartográficas presentan lla), teniendo que mantener ángulos rectos en el distorsiones, mayores o menores, en función de cruzamiento entre meridianos y paralelos, requiere tres variables: área, distancia y/o dirección (Figura la adopción de proyecciones cartográficas. Así, la 3). Considerando propiedades relacionadas con la importancia de las proyecciones cartográficas de- deformación de la superficie terrestre en cuanto a riva de la necesidad de proyectar una superficie las áreas, las distancias y las direcciones (o ánesférica y tridimensional (la Tierra) en una super- gulos), las proyecciones cartográficas son además ficie plana bidimensional, manteniendo ángulos clasificadas en tres grandes grupos: rectos en el cruzamiento de los meridianos con los • Proyecciones conformes: También conociparalelos, lo cual es imposible sin hacer extensio- das como ortomórficas, pues poseen la prones y/o contracciones. piedad de no deformar los ángulos. En estas Las proyecciones cartográficas posibilitan la proyecciones, los paralelos y meridianos se representación del globo terrestre, continentes o cruzan en ángulos rectos y la escala alrededor áreas geográficas de menor tamaño en una su- de un punto se mantiene para cualquier direcperficie plana, generalmente en una hoja de papel ción. Son por ejemplo: la Proyección Universal o pantalla, permitiendo su trazado en forma de Transversa de Mercator (UTM) y la Proyección mapas, cartas y planos que representan propor- Cónica Conforme de Lambert; ambas utilizacionalmente su dimensión, forma y ángulos de das en el mapeo sistemático de Brasil. la manera más próxima posible de la realidad. • Proyecciones equidistantes: Son las proyeccioExisten centenas de proyecciones cartográfi- nes que no presentan deformaciones lineales, o cas, cada una adecuada para representar todo sea, las distancias son representadas en una esel mundo, determinado continente, país o región cala uniforme. Sin embargo, esta condición solo geográfica. se alcanza en determinada dirección, y puede ser

28

### Página 31

Figura 3. Tipos de proyecciones cartográficas adoptados para el mapeo de datos geográficos en dos dimensiones (hoja de papel, pantalla de computadora) (Fuente: Peter H. Dana, 20/set/1994)

clasificada además en: meridiana, transversal y iguales o menores de 6° de longitud. En Brasil, los azimutal u ortodrómica. Es menos utilizada que mapas en escalas de 1:250.000 y mayores, elaboralas proyecciones conformes o equivalentes por- dos por el Instituto Brasilero de Geografía y Estadística que raramente se precisa un mapa con distan- (IBGE) y la Dirección de Servicio Geográfico (DSG), cias medidas considerando una única dirección. se encuentran en la proyección UTM.

Por ejemplo: proyección equidistante cónica. Además de la proyección cartográfica, asocia-

• Proyecciones equivalentes: Estas proyeccio- do a cada mapa también deben ser especificados nes no deforman áreas y conservan una rela- el “Datum” y el sistema de coordenadas geográfición constante com la superfície terrestre, en cas considerados (ya presentados en el apartado términos de área. Debido a sus deformaciones anterior 1.1.Uso del Sistema de Posicionamiento no son adecuadas para la cartografía básica, Global en la caracterización de áreas agrícolas. pero son de mucho interés para la cartografía Los sistemas de información geográfica permiten temática. Ejemplo: proyección de Miller, pro- fácilmente realizar conversiones entre proyeccioyección de Berhmann, proyección de Albers. nes cartográficas, “Data” y/o sistemas de coordeLa proyección universal transversa de Mercator nadas, posibilitando la estandarización e integra- (UTM) es frecuentemente utilizada para el mapeo de ción de información multidisciplinaria, subsidiando áreas con poca extensión en el sentido este-oeste, la toma de decisiones.

29 PARTE 1

### Página 32

1.3. Monitores de rendimiento y largo plazo. Aumentar el número de años utilizados para estudiar la variabilidad espacio-temporal mapeo y definir zonas de manejo, puede ser una solución Ricardo Melchiori, Alejandra Kemerer y Susana para este problema. Datos de rendimiento de vaAlbarenque rios años, permiten identificar patrones de rendimiento y separar las causas naturales de la variación de aquellas debidas al manejo o errores de Ricardo Melchiori medición (Kleinjan et al., 2007).

Grupo Recursos Naturales y Factores Abióticos. Estación La variación debida al manejo incluye errores Experimental Agropecuaria Paraná del INTA. Ruta 11 km12.5, que típicamente se observan en parches pequeños, Oro Verde, Argentina. como las fallas de siembra, fallas en el establecimelchiori.ricardo@inta.gob.ar miento del cultivo, fertilización desuniforme, daños Alejandra Kemerer de herbicidas, daños de enfermedades, entre otros.

Los errores de medición incluyen errores de sensoGrupo Recursos Naturales y Factores Abióticos. Estación res de flujo y humedad de granos, errores debidos a Experimental Agropecuaria Paraná del INTA. Ruta 11 km12.5, la georreferenciación y al movimiento de la cosechaOro Verde, Argentina. dora, errores debido al operario de la maquinaria, y kemerer.alejandra@inta.gob.ar errores del procesamiento de los datos. Un requisito Susana Albarenque indispensable previo a la utilización de un monitor de rendimiento es su correcta calibración, lo cual permiGrupo Recursos Naturales y Factores Abióticos. Estación te evitar algunos de los errores mencionados. Para Experimental Agropecuaria Paraná del INTA.Ruta 11 km12.5, que los mapas de rendimientos puedan utilizarse Oro Verde, Argentina. para caracterizar la variabilidad del rendimiento de albarenque.susana@inta.gob.ar los cultivos de manera adecuada deben removerse los errores que se generan, aun con un monitor calibrado (Albarenque y Vélez, 2011).

Introducción

La disponibilidad de sistemas de posicionamiento ¿Qué es un mapa de rendimiento? global precisos y relativamente económicos, combi- Es una representación espacial de datos de nados con los monitores de rendimiento, proveen la rendimiento registrados durante la cosecha de un oportunidad de registrar y mapear instantáneamente cultivo. Comúnmente la representación espacial los rendimientos de los cultivos durante la cosecha. se realiza utilizando un formato vectorial de puntos Aunque el mapa de rendimiento de un año es y coordenadas (x, y, z) asociadas a un sistema de útil para interpretaciones de posibles causas de la proyección (latitud y longitud, WGS84) que refevariación del rendimiento, resulta de valor limita- rencia geográficamente los puntos (Figura 1). do para la toma de decisiones de estrategias de La cantidad de información que se obtiene en manejo sitio-específico en períodos de mediano o cada punto del mapa de rendimiento depende del

30

### Página 33

Figura 1. Mapa de rendimiento y detalle de puntos

monitor que se utilice; estos pueden ser: altura de res que permiten calcular la cantidad de grano cocabezal, ancho de cosecha, distancia recorrida, sechado por unidad de superficie. La información velocidad de avance, flujo de granos, humedad de obtenida por los sensores y el GPS, es centralizada granos, pérdidas de cosecha, entre otros. y almacenada en una consola (Figura 2b) que sirve de interfaz con el usuario (Bragachini et al., 2006). ¿Cómo se obtiene un mapa de rendimiento? Sensores del monitor de rendimiento Los mapas de rendimiento se obtienen a par- El sistema de sensores que integran el monitor tir de los datos recolectados por una cosechadora de rendimiento es el siguiente: que incluye un sistema de posicionamiento global • Sensor de flujo de grano: se ubica en la no- (GPS, Figura 2a) junto con un sistema de senso- ria de la cosechadora (Figura2c) y determina

31 PARTE 1

### Página 34

Figura 2. Cosechadora equipada con monitor de rendimiento. Ubicación del sistema de posicionamiento global y sensores

la cantidad de grano que ingresa a la tolva. • Sensor de posición del cabezal: cuando el caExisten diferentes tipos de sensores, los que bezal está en posición de cosecha el sensor utilizan una placa de impacto en el camino del activa el registro de datos, cuando se levanta flujo de grano y mediante una celda de carga el cabezal el sensor detiene el registro de datos transforman la fuerza del impacto en una señal (Figura 2f). eléctrica. Otros sensores operan sobre un prin- El área cosechada se determina con la velocicipio volumétrico y constan de una rueda con dad de avance y el ancho de cabezal, que debe paletas de volumen conocido, el rendimiento ser definido por el operario de la cosechadora en de grano es medido mediante la cantidad de caso de que el cabezal sea menor al ancho total veces que las ruedas descargan las paletas. de labor. La velocidad de avance de la cosecha-

• Sensor de humedad de grano: normalmente se dora también puede determinarse usando el GPS. ubica en el elevador de grano. Es un sensor de capacitancia que mide las propiedades dieléc- Calibración del monitor tricas del grano que fluye entre placas metáli- La calibración se realiza para garantizar que los cas (Figura 2d). datos registrados sean precisos y representen de

• Sensor de velocidad de avance: puede medir- manera confiable las variaciones del rendimiento se mediante un sensor magnético que mide las del cultivo. vueltas de las ruedas delanteras de la cosecha- • Calibraciones previas a la cosecha: incluye las dora o usando un radar (Figura 2e). calibraciones por vibración y distancia. Deben

32

### Página 35

realizarse una vez al inicio de la campaña y registro de datos de rendimiento, cuando el cacada vez que se repare o modifique la máqui- bezal baja el equipo comienza a registrar datos. na, cuando se cambia el rodado o las condicio- Si se avanza con el cabezal bajo, aun cuando nes de piso varían bruscamente. no se está cosechando se generan puntos sin

• Calibración del sensor de altura del cabezal: debe datos de rendimiento que luego se visualizan realizarse al iniciar la cosecha de un nuevo culti- en el mapa como rendimiento cero (Figura 3). vo de acuerdo con su altura normal de cosecha. • Retardos en el inicio y fin de registro de datos:

• Calibración de humedad de grano: se realiza este error se manifiesta en el mapa como puncomparando la humedad medida con un hu- tos faltantes en el inicio de una franja de cosemedímetro y la determinada por el sensor de cha y puntos adicionales en el fin de la franja humedad. (Figura 4, círculos punteados y llenos, respectivamente). El error de inicio se debe a que existe

• Calibración del peso del grano: debe realizarse

un retraso desde que comienza la cosecha, los

luego de la calibración de humedad, compagranos pasan por el sistema de trilla, separación rando el peso medido mediante una tolva con y limpieza, llegan a la placa de impacto y se rebalanza y el peso determinado con el monitor. gistra el dato. Esto genera un desfasaje entre la La calibración debe realizarse para cada cultivo posición de cosecha y la posición de registro del o ante cambios predecibles en las condiciones de dato. El error de fin de cosecha en una pasada cosecha (por ejemplo: variaciones en el peso hec- se debe a que el monitor de rendimiento sigue tolítrico y la humedad). registrando datos con un flujo de granos decreSegún el monitor de rendimiento las calibracio- ciente a partir de que finaliza la cosecha de una nes se realizan introduciendo un factor de correc- pasada y dejan de ingresar granos al sistema de ción o el dato medido con otro dispositivo de medi- trilla. Algunos monitores de rendimiento realizan ción (Tolva balanza, humedímetro, etc.). En el caso del peso del grano, la calibración puede requerir más de una pesada, obtenida mediante condiciones de cosecha que generen flujos de grano diferentes (es decir cosechas a diferentes velocidades).

Errores más frecuentes en los mapas de

rendimiento

Los datos del monitor de rendimiento comúnmente contienen valores que son erróneos debidos a diferentes causas. Los errores más frecuentes son:

• Errores de registro por altura de cabezal:

Cuando se levanta el cabezal de la cosechado- Figura 3. Errores de registro por altura de cabezal. Efecto comúnmente visible en la cabecera (puntos en color rojo) ra, el sensor de altura de cabezal suspende el

33 PARTE 1

### Página 36

Figura 4. Retrasos al inicio (círculos punteados) y al final Figura 5.Franja de cosecha con rendimiento bajo, evidencia de (círculos llenos) de la franja de cosecha error en la configuración del ancho de cabezal

correcciones que permiten al operador estimar se consideran de interés agronómico debido a el retraso de tiempo desde el inicio de corte has- que no representan la variabilidad característita que el grano llega a la placa de impacto. ca del sitio por lo que se recomienda remover

• Valores fuera de rango: corresponden a datos los valores extremos. de las distintas variables que se registran en el • Franjas angostas de rendimientos anómalos: monitor de rendimiento (rendimiento, flujo de Estas situaciones se observan en los mapas grano, velocidad de avance, etc.) que se en- como franjas de cosecha con valores de rencuentran fuera del rango de variación normal dimientos altos o bajos que no están relacionade la variable en cuestión (valor promedio más dos con las franjas de cosecha vecinas inmediatas. Normalmente esto se debe a errores en y menos tres desvíos estándar). En el caso del el ancho de cosecha, ocasionados por la confirendimiento del cultivo pueden observarse vaguración incorrecta del ancho de la plataforma lores bajos debidos a fallas de implantación o o del ancho de corte en la trilla. En el primer presencia de malezas. Valores extremos de alto caso, se trata de especificaciones de ancho rendimiento pueden generarse por ejemplo, menores al corte posible en el monitor de rencuando por malas condiciones de tránsito en dimiento que generan franjas con rendimientos el lote se genera patinaje de la cosechadora o mayores que las franjas contiguas y, en el secuando hay cambios bruscos en el flujo de gra- gundo, a trilla con un ancho de corte menor al no que ingresa a la cosechadora por variacio- que tiene la plataforma completa, que genera nes en la velocidad de cosecha, debido a de- franjas con rendimientos menores al observado presiones en el terreno. Ambas situaciones no en las franjas contiguas (Figura 5).

34

### Página 37

Remoción de errores Monitor de rendimiento de caña de azúcar

Los mapas de rendimiento suelen utilizarse El monitor de rendimiento de caña de azúcar para caracterizar la variabilidad del rendimiento de consta de un sistema de pesaje de los trozos los cultivos. Para esto se requieren mapas de ca- de caña de azúcar cosechados que funciona en lidad que se generan utilizando monitores calibra- base a celdas de carga y va instalado en el eledos junto con un adecuado procesamiento de la vador antes que la caña sea descargada sobre información eliminando los datos erróneos. el remolque. El elevador está compuesto por una La remoción de los errores puede tener un base metálica que soporta una serie de cangilones impacto pequeño en la apariencia del mapa pero que transportan la caña troceada. La base metádesde una perspectiva analítica, remover datos erróneos tiene un impacto significativo sobre la uti- lica contiene un sensor de pesaje soportado por lidad de los mapas para mejorar la precisión de las celdas de carga. El sistema incluye un sensor de decisiones de manejo. inclinación que permite corregir el peso, debido a que las lecturas en condiciones de inclinación son inferiores al peso real.

Detalles sobre procedimientos para la remoción

de datos erróneos se especifican en el apartado

2.1.Mapas de manejo con datos espaciales.

Monitor de rendimiento para maní

Al igual que para los cultivos de grano existen

las dos alternativas de monitores, los que miden el

Monitores de rendimiento para cultivos no rendimiento mediante placas de impacto y aquetradicionales llos que lo hacen mediante mediciones volumétricas. Resultados obtenidos en Argentina han deMonitor de rendimiento para el cultivo de mostrado una mejor precisión de los monitores de algodón tipo volumétrico. Este tipo de monitores realiza las El monitor de rendimiento para el cultivo de mediciones de rendimiento a partir de un sensor algodón consta de varias partes, y a diferencia óptico colocado en la noria donde se registran del monitor de rendimiento de cultivos de granos cambios en el volumen de grano transportado por trabaja con tecnología infrarroja, es decir medianlos cangilones. A diferencia de los monitores de te el uso de haces de luz infrarroja para detectar el paso de algodón cosechado por las toberas placa de impacto, en este caso, previo a la calio conductos, previo a la caída en la tolva de la bración se requiere demáquina. La intercepción que el algodón realiza terminar el peso hectolí- En el apartado 3.2. Sistema al pasar por un haz de luz infrarroja determina el trico del maní para con- de guía por satélite, rendimiento que ocurre en un lote. Al igual que vertir el volumen medido automatización agrícola y los monitores de rendimiento de grano, este debe en peso de las vainas controladores electrónicos se ser calibrado adecuadamente para garantizar cosechadas. profundiza sobre los monitores una correcta medición del rendimiento del cultivo de rendimiento. de algodón.

35 PARTE 1

### Página 38

1.4. Adquisición remota y dificultad de detección y registro de ocurrencias de

interés (presencia de enfermedad, plaga, etc.), por

agricultura de precisión la falta de una vista completa del área, e incluso por

Carlos Alberto Vettorazzi y Stanley Best el hecho de que no siempre son detectados visualmente, o por lo menos no antes de que ocasionen pérdidas significativas e irreversibles en la producCarlos Alberto Vettorazzi ción pues, en algunos casos, cuando los síntomas Profesor asociado del Departamento de Ingeniería de se manifiestan visualmente, ya no es posible revertir Biosistemas el problema sin afectar la producción.

ESALQ/USP Así, una de las maneras más eficientes de maPiracicaba, SP, Brasil pear la variabilidad, o determinados sucesos de cavettor@usp.br interés en las áreas cultivadas, es remotamente, por medio de una técnica consagrada denominada adquisición remota.

Stanley Best S.

La adquisición remota puede definirse, de maPhD, Agr. and Bioresources Engineering nera amplia, como un conjunto de técnicas que Director del Programa Agricultura de Precisión INIA, Chile permiten recopilar y registrar datos sobre un desbest@inia.cl terminado objeto, área o fenómeno, por medio de sensores, sin que haya un contacto físico directo.

Introducción Etapas de la adquisición remota

Uno de los principales requisitos en la agricul- La adquisición remota puede dividirse en dos tura de precisión es el mapeo de las variabilidades etapas: adquisición de datos (detección y registro espacial y temporal en las unidades de producción. por medio de sensores) y análisis de datos (proceEse mapeo es fundamental para el tratamiento lo- samiento de datos e interpretación). calizado de los cultivos y puede ser realizado bási- Los principales elementos presentes en la camente de dos maneras: in situ y remotamente. etapa de adquisición de datos son: a) fuente de En el mapeo in situ las variables se detectan, energía; b) energía (radiación electromagnética); c) en general, visualmente, en el campo al recorrer el atmósfera terrestre; d) objeto de interés; y e) plataárea y realizar los debidos registros. Como ejemplo forma/sensor (Figura 1). se puede citar el georreferenciamiento, con recep- La principal fuente de energía en el proceso es tor GPS, de plagas y enfermedades en las plantas el Sol, aunque existen sensores que no dependen de un monte frutal. de esa fuente natural, pues poseen su propia fuenSin embargo, no siempre es posible o viable te de energía, como el caso de los radares. realizar el mapeo directamente en el campo, sea La energía emitida por la fuente puede atrapor la dificultad de locomoción en el área o por la vesar la atmósfera terrestre, interactuar con ella y

36

### Página 39

Figura 1. Elementos de la etapa de adquisición de datos por teledetección (o adquisición remota). Fuente: Florenzano (2011)

alcanzar el objeto de interés, también interactuar Comportamiento espectral de los objetivos con éste, o sea, pude ser reflejada por el objetivo, La adquisición remota se basa en la interacción transmitida o absorbida, y en este último caso es entre la radiación electromagnética (REM) y los obposteriormente emitida en forma de calor. jetivos de interés. Esa interacción será registrada y Esa energía reflejada o emitida por el objetivo analizada de acuerdo con fines específicos y ocuatraviesa nuevamente la capa atmosférica y llega rre de la siguiente manera: del total de radiación al sensor, y allí es detectada y registrada por éste. incidente sobre el objetivo, parte es reflejada por El sensor permanece alojado en una platafor- éste (reflectancia); parte es transmitida (transmima, que puede ser una aeronave, un vehículo aé- tancia), o sea que atraviesa el objetivo; y parte es reo no tripulado (VANT), un satélite artificial, etc. absorbida (absorbancia), para posteriormente ser emitida en forma de calor.

En los sensores a bordo de vehículos no tripulados (principalmente satélites), la energía re- Las proporciones entre reflectancia, transmigistrada es transformada en señales eléctricas tancia y absorbancia varían para cada tipo de obque, posteriormente, son enviadas a estaciones jetivo, fijándose las demás variables en función del terrestres y, en forma de gráficos, tablas y/o imá- tipo de radiación incidente. genes, serán debidamente interpretadas para fi- Los diferentes tipos de REM se clasifican de nalidades específicas. acuerdo con su longitud de onda o frecuencia, y

37 PARTE 1

### Página 40

Figura 2. Comportamiento espectral de vegetación verde y saludable. Fuente: Moreira (2005)

la representación gráfica de la distribución de esos comportamiento espectral, curva de reflectancia e diferentes tipos de REM se denomina espectro incluso firma espectral de determinado objetivo. electromagnético de energía. El principal objeto de interés en la adquisición La agrupación de REM con iguales característi- remota aplicada a la agricultura de precisión es, cas recibe el nombre de banda o segmento. Para evidentemente, el cultivo, seguido de cerca por la adquisición remota las principales bandas de el suelo. interés son la visible, la infrarroja (IR) y las microon- A continuación se presenta el gráfico de comdas. La amplia banda IR puede además dividirse portamiento espectral medio de plantas verdes y en IR cercano (NIR), IR medio (MIR) e IR lejano saludables (fotosintéticamente activas) (Figura 2). (FIR) o térmico7. En la banda visible la radiación es fuertemenEn general, la relación entre objetivo y radiación te absorbida por los pigmentos de la hoja, sobre todo en las longitudes de onda referentes al azul y de las diferentes bandas es representada por el gráal rojo, utilizados en la fotosíntesis. fico de la variación de reflectancia versus longitud de onda o frecuencia. Es el denominado gráfico de En la banda del infrarrojo cercano (NIR) se da una reflexión significativa, siendo la estructura ce-

7 Por siglas en ingles: infrared (IR), instrumentation for near (NIR), mid lular de las hojas la principal responsable de ese infrared (MID), far-infrared (FIR). comportamiento.

38

### Página 41

En el infrarrojo medio (MIR) se dan picos de ferencia de otros objetivos sobre la respuesta del absorción de radiación por el agua presente en el objetivo de interés. Si se estuviera trabajando con tejido vegetal. un cultivo agrícola a nivel de laboratorio (radiomeEsas curvas espectrales se construyen a partir tría) es posible aislar una hoja con las característide mediciones de campo, con equipos denomi- cas deseadas. nados espectroradiómetros y su conocimiento es Con el aumento de la altitud de la plataforma, fundamental para el desarrollo de nuevos senso- otros elementos pueden formar parte de la resres, así como para la selección de las bandas de puesta, como el suelo, partículas presentes en la sensores multi o hiper-espectrales a ser utilizados atmósfera (por ejemplo polvo), otras plantas, etc. en análisis específicos. de modo que la respuesta final será el resultado de la integración de las señales de los diferentes elementos y no más de una señal “pura”.

Niveles de adquisición de datos

En adquisición remota, los datos se obtienen

a partir de sensores instalados en diferentes tipos Sistemas sensores

de plataforma, cada una, móvil o estacionaria, con El sensor remoto es un equipo capaz de rescaracterísticas propias. ponder a la radiación electromagnética en deterLas plataformas pueden clasificarse en tres ni- minadas bandas del espectro electromagnético, veles, de acuerdo con la distancia entre el sensor registrarla y generar productos que –después de y el objetivo de interés: terrestre (campo y labora- una interpretación adecuada– podrán brindar infortorio); aéreo (aviones, helicópteros, VANT, etc.); y mación sobre los objetivos de interés del usuario. orbital (naves espaciales, satélites artificiales, etc.). Los sensores se pueden dividir, primariamente, Cada una de esas plataformas presenta ventajas en formadores de imágenes (cámaras fotográficas, y desventajas. escáneres multiespectrales, etc.) y no formadores Además de las propiedades intrínsecas al ob- de imágenes (espectroradiómetreos, radares altíjetivo y las características del sistema sensor, la metros y otros). intensidad y la calidad de la señal registrada por También pueden clasificarse en activos y pasiel sensor también están influenciadas por la altitud vos. Son pasivos cuando dependen de una fuente de la plataforma. externa de radiación (la principal es el Sol) y aquí Al pasar del nivel terrestre al aéreo y del aé- se encuentra la mayoría de los sensores, como reo para el orbital, la situación se modifica signifi- muchos escáneres multiespectrales instalados a cativamente: la capa atmosférica aumenta y, con bordo de aeronaves y satélites, como el Landsat, ello, aumentan las interferencias sobre la señal SPOT, RapidEye, Ikonos, etc. Son activos cuando registrada. poseen su propia fuente de radiación electromagSi en el nivel de laboratorio se puede aislar nética, como es el caso de los radares formadoparte del material a ser analizado, a medida que res de imágenes y de equipos de campo como la altitud del sensor aumenta, puede haber inter- GreenSeeker, WeedSeeker, etc.

39 PARTE 1

### Página 42

Los sensores formadores de imágenes pueden Una imagen digital de adquisición remota no es producir imágenes de una única banda amplia del nada más que una matriz de valores, denominados espectro, por ejemplo, la banda visible y la banda niveles de gris (NG) que, como ya fue mencionado, NIR, o producir diversas imágenes simultáneas de se refiere a la intensidad de radiación reflejada o la misma escena en diferentes bandas del espec- emitida por el objetivo. Los elementos de la matriz, tro (sensores multi e hiperespectrales), como el que contienen los niveles de gris, se llaman pixeles sensor OLI (Operational Land Manager), a bordo (del inglés: picture elements). del satélite Landsat-8, con nueve bandas espec- El procesamiento digital de imágenes de adquisitrales, de la banda azul a la MIR, incluyendo una ción remota implica modificaciones intencionales en banda pancromática. los NG, que básicamente pueden agruparse en tres Una de las principales características prácticas categorías: pre-procesamiento, realce y clasificación. de los sensores es su poder de resolución. Este término se aplica al sensor, y el término resolución Pre-procesamiento se aplica al producto (imagen). Así, para las imágenes existen las resoluciones espacial, espectral, En la etapa de pre-procesamiento se realizan radiométrica y temporal. correcciones en las imágenes brutas, preparándolas para las etapas siguientes.

La resolución espacial se refiere al tamaño del

píxel en la imagen digital. La resolución espectral Las principales correcciones ejecutadas sobre se relaciona al número y la amplitud de las ban- las imágenes son: la radiométrica, la atmosférica y das espectrales, a las que el sensor es sensible; la geométrica. la resolución radiométrica se refiere a los niveles En la corrección radiométrica se eliminan los de intensidad de la señal de retorno traducidos, posibles ruidos existentes en la imagen. Se entienen general, por el número de niveles de gris (NG) de por ruidos a los pixeles aislados o en grupo en que componen la imagen; y finalmente, la resolu- que el valor del nivel de gris registrado es alterado ción temporal que, como su nombre sugiere, está debido a fallas momentáneas del sensor. Se corelacionada al intervalo de tiempo entre pasadas rrigen por medio de la sustitución de sus valores consecutivas del sensor sobre la misma escena. por otros obtenidos a partir de pixeles cercanos, para lo cual se emplean, en general, filtros digitales Procesamiento digital de las imágenes (ventanas móviles), que también se utilizan para el realce de las imágenes.

La principal finalidad de las imágenes de adquisición remota es brindar información, que es Otra corrección sobre la imagen es la atmosextraída de los datos registrados en la imagen, férica, cuyo objetivo es reducir el efecto de la inpor números digitales que se relacionan al com- teracción entre la radiación atmosférica, principortamiento espectral del objetivo y por medio de palmente dispersión, simulando una condición de la intensidad con que reflejan o emiten radiación atmósfera limpia. electromagnética en bandas específicas de longi- Finalmente, la corrección geométrica busca elitud de onda. minar distorsiones relacionadas al proceso de ob-

40

### Página 43

tención de la imagen y la asociación de la imagen a

un sistema de coordenadas y Datum de referencia.

Realce

Las técnicas de realce tienen como finalidad

mejorar la calidad visual de las imágenes, de modo

de facilitar su análisis. Ya sea que el análisis sea

realizado de forma visual o digital, el proceso siempre comienza con la visualización de la imagen, tanto en la pantalla de la computadora como en copias impresas, si fuera el caso.

Así, la calidad visual de la imagen es bastante

importante, principalmente para una mejor identificación de los elementos presentes en la escena.

Existen varias maneras de realzar imágenes de

adquisición remota, por ejemplo las técnicas que Figura 3. Composición de color de una imagen obtenida por el Satélite implican modificaciones en su histograma, aplica- de Recursos Terrestres Chino-Brasileño (CBERS) ción de filtros digitales, elaboración de composiciones de color en imágenes multi e hiperespectrales (Figura 3), aplicación de análisis de compo- –por ser fuertemente absorbida por la planta para nentes principales, etc. la realización de la fotosíntesis–, y la del infrarroEs preciso destacar, en este punto, una de las jo cercano (IR) que es bastante reflejada por las técnicas más importantes en aplicaciones de adqui- plantas debido a su fuerte relación con la estrucsición remota en vegetación, que es la elaboración tura celular. de imágenes sintéticas denominadas índices de vegetación (IV). Los IV tienen como objetivo reunir Existen innumerables índices de vegetación, la información espectral, al facilitar la discriminación entre los que cabe destacar: razón simple (SR), entre vegetación y no-vegetación en la escena re- diferencia normalizada (NDVI) y ajustado al suelo gistrada, así como visualizar la vitalidad de la cober- (SAVI), etc.8 tura vegetal, siendo útil en el monitoreo de las con- En la Figura 4 se presenta una imagen NDVI de diciones de crecimiento del cultivo, la evaluación de una chacra de trigo, al lado del mapa de productieventos de estrés causados por deficiencias hídrividad de la misma área, obtenido en el campo, en cas y nutricionales, plagas, enfermedades, etc. que fácilmente se puede percibir la relación entre Los índices de vegetación se obtienen a par- ambos. tir de relaciones matemáticas entre valores de reflectancia de diferentes bandas del espectro, 8 Por siglas en inglés: simple ratio (SP), normalized difference vegetation siendo las dos más utilizadas la del rojo (visible) index (NDVI), soil-adjusted vegetation index (SAVI).

41 PARTE 1

### Página 44

píxel de la imagen, una categoría del tema trabajado, y generar así una imagen temática. Esa atribución por medio de algoritmos apropiados, puede ser considerada como la aplicación de un “rótulo” sobre cada píxel, con el número digital y el color relacionados a la debida categoría del tema.

Los métodos de clasificación digital de imágenes pueden dividirse en dos abordajes principales: supervisada y no supervisada.

Clasificación supervisada

Este abordaje de la clasificación digital se denomina supervisada, pues implica una gran interacción entre el proceso y el analista.

Se utiliza cuando existe un conocimiento previo

de las características a ser mapeadas. Ese conocimiento permite que sean obtenidas muestras de pixeles de cada característica/categoría de la leyenda buscada, por medio de polígonos digitalizaFigura 4. Imagen NDVI y mapa de productividad de trigo dos sobre la pantalla. Esas muestras servirán para la formación estadística del algoritmo escogido para el proceso de clasificación. En general, se admite que de 1,5 % a 3,0 % del total de pixeles de la Clasificación imagen sean suficientes para formar el algoritmo.

La clasificación se refiere a la extracción pro- El total de pixeles de las muestras debe dispiamente dicha de información de la imagen. Es la tribuirse de forma proporcional a la superficie de etapa que implica la base de la generación de ma- cobertura (aproximadamente) por cada categoría. pas temáticos a partir de imágenes de adquisición remota, por medio de técnicas de reconocimiento Los pixeles de la muestra van a generar una de padrones. firma espectral para cada categoría, con estadísticas simples sobre sus valores de niveles de gris.

La clasificación puede ser realizada de dos mo- Esas firmas serán empleadas por el algoritmo para dos: digital (o automática) y visual (o manual). clasificar los demás pixeles de la imagen.

Clasificación digital Como ejemplos de métodos de clasificación

Existen varios métodos disponibles para la cla- supervisada pueden citarse: Mínima Distancia y sificación digita de imágenes. El objetivo principal, Máxima Verosimilitud (MaxVer) entre otros. en este tipo de clasificación, es atribuir para cada En resumen, se puede afirmar que el enfoque de la clasificación supervisada se basa en el cono-

42

### Página 45

cimiento a priori de la leyenda buscada y el sumi- Los principales métodos de clasificación no sunistro de muestras de pixeles de cada categoría pervisada se basan en el Análisis de Clusters. de la leyenda para la clasificación por el algoritmo seleccionado. Clasificación visual La clasificación o interpretación visual de las Clasificación no supervisada imágenes de adquisición remota, también denoLa clasificación digital no supervisada de imá- minada clasificación manual, fue utilizada en forma genes de adquisición remota, en realidad debería operativa durante mucho tiempo. La interpretación llamarse “poco supervisada”, pues la supervisión visual de fotografías aéreas, o foto-interpretación por parte del analista existe, aunque es menor que por ejemplo, fue muy utilizada por décadas. La en el caso del enfoque supervisado. interpretación visual ha venido siendo sustituida De modo general, el fundamento de los méto- gradualmente por la clasificación digital, en la medos no-supervisados es el agrupamiento de pixeles dida en que los equipos y sistemas informáticos se con comportamiento espectral semejante, que ge- tornan cada vez más accesibles. neran una imagen con tipos espectrales. Esos tipos Comparativamente con la clasificación digital, son posteriormente asociados a categorías de una puede decirse que la clasificación visual presenta leyenda, por medio de trabajos de campo, consulta un grado mayor de subjetividad. Diferentes analisa mapas existentes, entrevistas, etc. tas, utilizando el mismo material y los mismos proAsí, mientras que en los métodos supervisa- cedimientos, pueden llegar a resultados distintos. dos, la leyenda es establecida a priori, en los mé- De cualquier manera, incluso hoy el análisis vitodos no supervisados es definida a posteriori. sual es importante, pues el contacto del analista El enfoque no supervisado generalmente se con la imagen, incluso aunque sea en la pantalla de utiliza cuando no existe conocimiento previo del la computadora, es puramente visual. Así, a pesar área que será mapeada. Así, la generación de ti- de que no necesariamente se realice clasificación, pos espectrales permitirá la asociación adecuada el entendimiento (lectura) de la imagen siempre es con la situación del campo (Figura 5). necesario. Por ejemplo, ¿cómo podrían extraerse

Figura 5. Cultivo de avena: (a) imagen pancromática colorida; (b) tipos espectrales generados por clasificación no-supervisada

43 PARTE 1

### Página 46

pixeles para componer muestras para la forma- cuando la transpiración desde las hojas excede la ción de una clasificación digital supervisada, si las absorción de agua por las raíces por un tiempo categorías deseadas no pudieran ser visualmente suficientemente prolongado para que ocurra una identificadas? disminución del ensanchamiento celular y disturLa clasificación visual puede ser realizada so- bios en los procesos fisiológicos fundamentales, bre copias en papel de la imagen, para determina- lo que repercute en una disminución de la producdos fines, pero el más común es la digitalización ción y su calidad. directa sobre la pantalla de la computadora, ge- El monitoreo de la condición hídrica en el connerándose un producto ya en formato digital. Es tinuo planta-atmósfera es muy importante. Dentro realizada en base a los denominados elementos de los modernos sistemas, y a la vez prácticos, de análisis de las imágenes, que son: tonalidad, con que actualmente se cuenta para el monitoreo textura, forma y límites, padrón, sombra, localiza- de déficit hídrico cabe mencionar los siguientes. ción y contexto (aspectos asociados).

A. Información de humedad de suelo

La utilización de sensores de humedad de sueEjemplos de aplicación

lo a tiempo real (Figura 6) es una gran herramienSeguidamente se presentan algunos ejemplos ta, que aporta información sobre el contenido de de aplicación de técnicas de adquisición remota humedad en el perfil del suelo. Dicha información en la agricultura. acerca resultados aproximados a la hora de manejar un sistema de riego.

Sistemas de monitoreo de déficit hídrico

Dentro de estos sensores se puede mencioEl agua es uno de los principales factores pro- nar: Reflectometría en el Dominio de la Frecuencia ductivos que afectan el rendimiento de los cultivos, (FDR) y Reflectometría en el Dominio del Tiempo la cual puede ser manipulada agronómicamente (TDR). Actualmente estos sistemas realizan memediante el riego. Las plantas cultivadas requieren diciones a tiempo real y permiten una adecuada de un aporte de agua que reemplace la que se oportunidad de la información para la toma de deevapora, principalmente desde las hojas, para el cisiones de riego, la cual es canalizada por Internet desarrollo de la planta y, finalmente, también para (Web y smart phones) o uso de sistemas de alerta la producción. (sms y emails).

Este requisito se debe a que las hojas están

expuestas a una fuerte demanda evaporativa (flu- B. Estación meteorológica

jos de radiación solar y déficit de vapor ambiental) La información meteorológica es necesaria mientras que la superficie interna está saturada de para una evaluación del desarrollo del cultivo, asovapor de agua. ciado a las condiciones medioambientales que los Así, el estrés hídrico de las plantas es el in- circundan y su demanda evaporativa (cálculo de la dicador más importante para la evolución de los evapotranspiración teórica a partir de data meteorendimientos. El estrés por falta de agua ocurre rológica (Figura 6).

44

### Página 47

Figura 6. Estaciones meteorológicas automáticas y medición termográfica del estrés hídrico, respectivamente

Actualmente, la información meteorológica es bastamente utilizados en países como Estados obtenida desde estaciones meteorológicas auto- Unidos, Canadá, entre otros. máticas, que permiten tener una rápida respuesta a las condiciones ambientales adversas que pue- Tecnologías de automatización y visión artificial dan presentarse, lo que es altamente importante no solo para evaluar déficit hídrico sino también Las personas perciben el mundo a través de un para determinar alertas tempranas de probabilida- pequeño espectro (Visible - RGB o Red-Green-Blue) des de apariciones de enfermedades de cultivos, de lo que realmente existe. Sin embargo, a pesar riesgos de heladas, condiciones de crecimiento de lo limitado del campo de visión del ser humano, adverso, etc. Esta información, asociada a la in- simularlo es un proceso altamente complejo y aún formación espacial vegetativa, podrá evaluar en más tomar acciones sobre el resultado de su análisis. mejor forma las zonas de mayor riesgo, permitien- En la actualidad las escenas reales del mundo do ser la base para el desarrollo de un monitoreo pueden ser vistas a través de un dispositivo digieficiente y efectivo. tal (charge-coupled device o dispositivo de carga C. Uso de termografía infrarroja acoplada en español) conectado a un microprocesador, que puede obtener la información del munLa termografía infrarroja es una metodología do real y procesarla a través de complejos modeque permite la detección remota del estrés hídrico, no detectable visualmente, a partir de la interac- los matemáticos. ción de la radiación con la vegetación. La mayor Automatización parte de la energía absorbida por la hoja es disipada en forma de calor, lo que ha provocado que se Debido a la necesidad de automatizar procesos esté investigando en la transferencia de calor entre en busca de reducir el costo de mano de obra, ha la vegetación y el ambiente y su efecto en el déficit existido un rápido crecimiento de la visión inteligenhídrico en las plantas, con ajustes de esta metodo- te por computadora, la cual mantiene una estrecha logía muy promisoria (Best et al., 2009), tanto a ni- relación con disciplinas como: inteligencia artificial, vel predial (Figura 6) como a mayores escalas con robótica, gráficas por computadora, procesamiento el uso de modelos como METRICS, actualmente de imágenes, fotogrametría, entre otras.

45 PARTE 1

### Página 48

La segmentación de imagen es un proceso dad y clasificación en líneas de procesamiento y digital que consiste en reconocer de forma auto- en general en automatización de procesos. mática los objetos de una escena. Es uno de los Los sistemas de visión artificial proporcionan inelementos más importantes de cualquier sistema formación importante acerca de la naturaleza y los automatizado, proporciona estructuras útiles tales atributos de los objetos presentes en una escena como regiones y bordes. Los algoritmos de seg- y además permiten explorar regiones del especmentación generalmente están basados en dos tro electromagnético donde los ojos humanos no criterios importantes a considerar: uno es la homo- pueden operar, como las regiones del ultravioleta o geneidad de la región y otro es la discontinuidad infrarrojo, los cuales son de alto interés para la deentre regiones disjuntas adyacentes. tección temprana de enfermedades o condiciones Los métodos para llevar a cabo la segmentación fisiológicas de las plantas cuando el ojo humano varían ampliamente dependiendo de la aplicación no es capaz de evaluar (Figura 7). específica, el tipo de la imagen y otros factores. La Así, según los espectros en análisis se pueden clasificación de objetos puede realizarse a través de evaluar: Luz visible, detección de la mayoría de distintas características como son la medición de daños que el ojo humano puede percibir; Infrarrojo objetos, color, forma, tamaño, textura, etc. Cercano, detección de podredumbre, identificación de daños en piel, estimaciones de madurez, Sistemas de segmentación basados en Visión etc.; Ultravioleta, detección de micro fisuras, funArtificial gosis, pudriciones, etc.; Luz estructurada, estimaLa aplicación de visión artificial en la agricultura ciones 3D, detección de formas irregulares, etc.; ha aumentado considerablemente en los últimos Laser, madurez, espesor de piel, etc. años. Hay muchos campos en los que se está in- Finalmente, este tipo de equipamiento está volucrando la visión por computadora: cartografía siendo altamente estudiado para llevar a cabo terrestre y aérea de recursos naturales, monito- equipos de evaluación y monitoreo de tipo portátil, reo de cultivos, agricultura de precisión, robótica, con una práctica aplicación a nivel de campo, que orientación automática, inspección no destructiva se espera que estén disponibles a nivel comercial de las propiedades del producto, control de cali- en no más de cinco años.

Figura 7. Detección de problemas fungosos e virales en vegetación mediante Visión Artificial

46

### Página 49

1.5. Muestreo para mapeo y manejo áreas cultivadas y definir intervenciones de manejo localizado (o sitio-específico), que procura optimide la fertilidad del suelo zar el uso de correctivos y fertilizantes por medio Álvaro V. Resende y Antonio M. Coelho de aplicaciones a dosis variable de acuerdo con la demanda local del cultivo. Tales muestreos también sirven para la adopción de siembra a dosis Álvaro V. Resende variable de los cultivos anuales.

Investigador en Fertilidad del Suelo y Fertilización, En el muestreo tradicional, normalmente, una o Embrapa Maíz y Sorgo pocas muestras son tomadas para representar la alvaro.resende@embrapa.br condición media del suelo en las chacras de cultivos de una propiedad. En el caso del muestreo Antonio M. Coelho georreferenciado, al disponer de información basada en un número mayor de muestras del suelo Investigador en Fertilidad del Suelo y Fertilización, representadas en forma de mapas de fertilidad, Embrapa Maíz y Sorgo ya desde el principio el agricultor se beneficiará antoniomarcos.coelho@embrapa.br de tener un mejor entendimiento sobre las condiciones de su cultivo. Sin embargo, una muestra georreferenciada mal hecha podrá afectar negatiIntroducción vamente no solo el manejo del suelo sino también las demás etapas y aplicaciones de la agricultura Los atributos de fertilidad química, física y biode precisión, pues distorsiones en los mapas de lógica del suelo expresan gran variabilidad espacial atributos del suelo pueden hacer que todas las y temporal e influyen en el potencial productivo en prácticas relacionadas al cultivo realizadas en la los ambientes agrícolas. Paralelamente, el manejo chacra estén desconectadas de la variabilidad real de la fertilización constituye uno de los principales existente en ese ambiente. condicionantes de la productividad de los cultivos.

Una buena caracterización edáfica, con utilización En este apartado se abordan los criterios, asfrecuente de análisis de suelo, es el procedimiento pectos prácticos y procedimientos relativos al proceso de muestreo de suelo para fines de agriculbásico para orientar la toma de decisiones en el tura de precisión, con énfasis en la caracterización gerenciamiento agronómico de los cultivos en la de la variabilidad espacial de la fertilidad de los agricultura moderna. suelos sobre el cultivo de especies anuales.

En ese contexto, la agricultura de precisión

busca un mayor grado de detalle en la información sobre las condiciones del suelo para fomen- Integración entre principios tar decisiones de manejo acertadas. Dentro de geoestadísticos y viabilidad operacional las aplicaciones de agricultura de precisión, los En el manejo de la fertilidad del suelo a través muestreos georreferenciados de suelos permiten de la agricultura de precisión, generalmente el temapear las variaciones de fertilidad dentro de las rreno se subdivide de acuerdo a un muestro en

47 PARTE 1

### Página 50

cuadrículas regular (regular grid) con determinado en la región de El Cerrado en Brasil) podrán contar tamaño de trama, de modo de efectuar un mues- con un número razonable de muestras, incluso treo sistemático con puntos georreferenciados. utilizando muestreos de cuadrículas poco densos, La asociación con las coordenadas geográfi- con tamaño de cuadrícula de área superior a 4 cas posibilita interpolar espacialmente los resulta- hectáreas. Obviamente, manteniendo los 50 pundos de los análisis de suelo del conjunto de mues- tos de muestreo en chacras de menor dimensión, tras extraídas y generar mapas que representen habrá densificación del muestreo en cuadrículas, la variabilidad de los atributos de interés. Una vez lo que repercute positivamente en la calidad de los obtenidos los productos de las interpolaciones – mapas generados y resultará en mayor confiabilipor ejemplo mapas de disponibilidad de potasio dad para los fines agronómicos pretendidos. y de saturación basados en el suelo–, es posible La condición principal que viabiliza el uso de un elaborar otros mapas que contengan la indicación determinado tamaño de cuadrícula es que los da- (prescripción) de las dosis de fertilizantes y correc- tos derivados del muestreo presenten dependentivos necesarios en diferentes partes de la chacra. cia espacial. O sea, que exista correlación entre el Equipos de aplicación disponibles en el mercado valor de un atributo muestreado en un lugar con (fertilizadoras) presentan dispositivos electrónicos los valores de ese atributo en puntos cercanos en que reconocen los mapas de prescripción y me- el muestreo en cuadrículas, de modo de permitir canismos automáticos que ajustan las dosis de los estimar datos para los lugares no muestreados por productos a medida que se aplican en el área a ser medio de la interpolación y, así, generar un mapa manejada a dosis variable. representativo de la variación espacial de dicho Los datos obtenidos con muestreos georrefe- atributo en el campo. Lógicamente, cuanto mayor renciados para el mapeo de la fertilidad del suelo es el tamaño de la cuadrícula, mayor será la disdeben ser procesados y validados según los prin- tancia entre los puntos de muestreo y menor el cipios geoestadísticos, y los mapas deben ser ma- grado de similitud entre nipulados y acabados a través del SIG. Se requiere los valores medidos. A Sobre muestreo de la recolección de cierto número de muestras para partir de cierta distan- cuadrículas también se que los datos puedan ser analizados geoestadís- cia, deja de existir cual- puede ver el apartado 3.1. ticamente de modo de obtener mapas confiables. quier correlación entre Tecnología de precisión para Es importante destacar el nivel de detalle con el ellos, y deja de ser pogestión de nutrientes cual se va a trabajar, que está directamente relacio- sible detectar depennado con la densidad del muestreo. Respetando dencia espacial. los principios de la geoestadística, se pueden ob- Algunas investigaciones realizadas en Brasil tener buenos mapas con cerca de 50 puntos de para la definición del tamaño de la cuadrícula del muestreo georreferenciados en el área a ser ma- muestreo en cuadrículas, han indicado la necepeada. Esa referencia puede ser aplicada a cha- sidad de un gran número de puntos de muescras de diferentes tamaños. Así, chacras con di- treo para poder identificar mejor la variabilidad mensiones superiores a 250 hectáreas (comunes del suelo en los cultivos (Machado et al., 2004,

48

### Página 51

Resende et al., 2006; Gimenez & Zancanaro, potasio (K), calcio (Ca) y magnesio (Mg). La Figura 2012). En un Latossolo de El Cerrado de Goiás, 1 ilustra la situación verificada para el potasio. En Resende et al. (2006) estudiaron cuadrículas el caso del fósforo (P), se obtuvo dependencia de muestreo en una chacra de 97,5 hectáreas, espacial solamente cuando se utilizó el muestreo considerando tamaños de cuadrícula variando más denso, con una cuadrícula de 0,25 hectáde 0,25 a 9,0 hectáreas. Para cuadrículas de reas. La literatura brasilera ha comprobado que, muestreo de hasta 4 hectáreas, la generación por regla general, los atributos de textura, materia de mapas respetando los principios de la geoes- orgánica, pH, potasio, calcio y magnesio presentadística (obteniendo dependencia espacial) fue tan mayor continuidad espacial que el fósforo y posible para los atributos de materia orgánica, los micronutrientes. O sea, para estos últimos hay

Figura 1. Mapas de niveles de potasio (mg dm-3) en el suelo, obtenidos a partir de muestreo en grillas con cuadrículas de 0,25 ha (A); 1 ha (B); 2,25 ha (C); y 4 ha (D). Nótese que la conformación de las regiones de mayor y menor disponibilidad del nutriente se modifica según la densidad del muestreo. (Fuente: Adaptado de Resende et al., 2006)

49 PARTE 1

### Página 52

mayor probabilidad de no encontrar dependencia rreferenciado del suelo debe resultar en mayor efiespacial en muestreos poco densos. ciencia del uso de correctivos y fertilizantes, y así La recomendación del tamaño de la cuadrícu- puede llevar a la reducción en el gasto global de la para muestreo de suelos varía en función de la esos insumos. resolución deseada (“precisión” del mapeo) asociada a costos. Cuadrículas más densas propor- Pre-requisitos para un muestreo cionan mayor confiabilidad de los mapas, pero au- representativo mentan la necesidad de mano de obra y el número La ocurrencia de variaciones de productividad de muestras a ser extraídas, lo cual se refleja en dentro de un área de cultivo es el supuesto básico el gasto de análisis de suelo y en el costo final del que justifica trabajar con agricultura de precisión. manejo con agricultura de precisión.

La cuestión clave es: delimitar la ubicación de esas

Debido a los elevados costos de muestreo y de variaciones e identificar sus causas, para entonanálisis de fertilidad, existe dificultad en armonizar ces definir la mejor estrategia de manejo para cada el rigor geoestadístico con la viabilidad económica lugar. La variabilidad del suelo detectada en una y operacional para la caracterización de la fertili- chacra precisa ser agronómicamente relevante, a dad del suelo en escala comercial. La necesidad fin de que justifique el manejo localizado, evitande compatibilización técnica y económica está do que se realicen intervenciones diferenciadas y siendo considerada y, actualmente, la mayoría de por tanto inocuas o innecesarias. En este sentido, las empresas prestadoras de servicios de agricul- se demandan técnicas que permitan optimizar el tura de precisión en Brasil adoptan muestreos en esfuerzo del muestreo, manteniendo la confiabicuadrículas con tamaños de cuadrícula de 1 a 4 lidad en la recomendación del manejo específico hectáreas. Hasta hace pocos años, aún se traba- del lugar. jaba con cuadrículas con área por encima de las 5 Teniendo en cuenta la eficiencia del proceso de hectáreas y, algunas veces, arriba de 10 hectáreas muestreo del suelo para la agricultura de precisión, en chacras de gran extensión. esta operación no debe limitarse a la determinaSin embargo, esa elección debe ser criteriosa ción de contornos georreferenciados de la chacra y, sin duda, la utilización de muestro en cuadrículas y la sobre posición de un muestreo en cuadrícumás densas, por ejemplo con cuadrícula de 1 hec- las pre-definido por medio de un programa infortárea, es recomendable al iniciarse en la agricultura mático, argumento comúnmente utilizado por los de precisión y también de forma interpolada con proveedores de servicio. Si el objetivo de utilizar muestreos menos densos, mejorando el diagnós- agricultura de precisión es detallar el diagnóstitico de la evolución del cultivo frente a las inter- co de la fertilidad del suelo, se deberían asociar venciones a lo largo del tiempo. Al ponderar los procedimientos adicionales de caracterización de costos, es preciso considerar que, generalmente, chacras para orientar mejor la etapa de muestreo. la información obtenida de los mapas de fertilidad Sobretodo cuando se trata de un área extensa, puede utilizarse por un período de hasta tres años. otros tipos de información georreferenciada pueOtro aspecto importante es que el muestreo geo- den ser importantes para orientar su subdivisión

50

### Página 53

en partes más homogéneas, que deberán ser rendimiento debidamente generado constituye inmuestreadas y mapeadas aisladamente, en caso formación extremadamente detallada y confiable. de que sea conveniente. Una secuencia de datos de productividad obAsí, aspectos normalmente observados par tenida luego de tres o más zafras con diferentes el muestreo tradicional también son válidos para cultivos, puede ser relativizada e integrada en un el muestreo georreferenciado. Las diferencias de único mapa, revelando sub-ambientes estables a color del suelo, de cobertura vegetal, el histórico lo largo del tiempo que presenten potencial prode su uso anterior (incluido el histórico de even- ductivo distinto. Además de ser útil para orientar tual erosión/degradación), de textura, de relieve y el muestreo del suelo y la aplicación a dosis vade drenaje, acostumbran tener implicaciones so- riable, ese tipo de información abre la perspectiva bre la fertilidad del suelo y el potencial productivo de que se apliquen otros enfoques de agricultura a lo largo de las áreas de cultivo, lo cual sugie- de precisión, tales como: fertilización basada en la re la necesidad de una estratificación previa en exportación de nutrientes en la cosecha y siemsub-ambientes. bra a dosis variable. El cultivo de maíz acostumMapas de clasificación de suelos, imágenes bra expresar con mayor claridad las diferencias de satelitales, fotografías aéreas, índices de vegeta- potencial productivo entre chacras. En las mismas ción determinados por medio de sensores especí- condiciones, la soja, más rústica y con capacidad ficos y otras formas de adquisición remota, permi- de compensar limitaciones ambientales, tiende ten identificar patrones contrastantes que pueden a exhibir menor amplitud en las mediciones de utilizarse para identificar sub-ambientes que debe productividad. tener el suelo muestreado y mapeado de manera El conocimiento histórico del uso y de eventuaindividualizada. Sensores de conductividad eléctri- les variaciones en el manejo del suelo y de los insuca, de pH y de materia orgánica han venido sien- mos en diferentes partes del campo es un aspecto do utilizados para la detección de zonas de suelo imprescindible en la estratificación de sub-ambiencontrastante en la agricultura comercial en algunos tes para el muestreo individualizado. Áreas que acpaíses, pero aún requieren estudios para su valida- tualmente forman una única chacra, pueden haber ción y calibración de acuerdo a las condiciones de sido abiertas para el cultivo en distintas épocas. El suelos tropicales. uso de cal y fertilizantes por períodos de tiempo Un aporte de gran relevancia para la delimita- diferentes crea “impresiones digitales” en el sueción de zonas homogéneas para el muestreo di- lo que no pueden ser “ocultadas” por el manejo reccionado del suelo es la identificación de sub- más reciente, induciendo a la formación de zonas áreas de productividad diferenciada dentro de las con fertilidad diferencial. Para identificar ese tipo chacras. El registro de datos de productividad de situación, es fundamental la interacción con el realizado con sensores insertados en las cose- productor o con personas que están directamenchadoras exige su posterior procesamiento pero, te vinculadas al día a día de la conducción de las dada la cantidad de mediciones realizadas –cerca chacras cultivadas. Incluso a partir de observaciode un registro cada dos segundos–, el mapa de nes empíricas, ellos pueden auxiliar mucho en la

51 PARTE 1

### Página 54

interpretación de los mapas de rendimiento y en la

toma de decisiones para el manejo localizado en

diferentes partes del campo.

En definitiva, criterios basados en características topográficas del campo, color del suelo, atributos físicos, profundidad del suelo, espesor del horizonte A, drenaje, datos de adquisición remota, mapas de rendimiento, mapas de conductividad eléctrica, histórico del uso, además de criterios unificados, pueden ser utilizados para orientar la delimitación de sub-ambientes para muestreos de

Figura 2. Esquema ilustrativo de un muestreo en cuadrículas

interés. Esa estrategia debe buscarse siempre con regular. En detalle, lugares de recolección de muestras simples en las cercanías (3 a 6 metros) del punto central de la cuadrícula. el fin de mejorar el manejo de la fertilidad del suelo (Fuente: elaboración Álvaro Resende) a través de la agricultura de precisión.

1 hectárea, y la extracción de suelo solamente en

Procedimientos en el muestreo las cercanías (3 a 6 metros) del punto central, lo georreferenciado que suscita dudas sobre la efectividad del muesUn conjunto de acciones debe ejecutarse en treo así ejecutado. O sea, el status de un deterforma planificada, para obtener un buen muestreo minado atributo del suelo en la cuadrícula puede del suelo para fines de agricultura de precisión. no estar bien representado en la muestra puntual Se pueden utilizar varios métodos para identificar, que generará el valor a ser interpolado en relación caracterizar y entender la variabilidad de los atri- a otros puntos relativamente distantes, localizados butos de los suelos, pero el proceso que ha sido en cuadrículas vecinas. Un intento de revertir esa mayormente utilizado para el muestreo sistemati- posible distorsión consiste en extraer muestras zado y el mapeo intensivo del suelo, consiste en simples a lo largo de una trayectoria de desplael establecimiento de un muestreo en cuadrículas zamiento del muestreo, de modo de distribuir los regularmente distribuidas en el campo (Figura 2), lugares de recolección en un área mayor dentro de lo cual permite el procesamiento geoestadístico e la cuadrícula, en diagonal o en zig-zag, de acuerinterpolar posteriormente los datos de análisis de do con las opciones que se muestran en la Figura suelo para generar los mapas de diagnósticos de 3. Generalmente, esa forma de muestreo ha sido fertilidad. económicamente viable para el manejo de la fertiliEl procedimiento ilustrado en la Figura 2 cum- dad del suelo con aplicación de correctivos y fertiple con los criterios geoestadísticos, pero puede lizantes a dosis variable. cuestionarse en cuanto a la representatividad de Los procedimientos que van desde el mueslas muestras frente a los intereses agronómicos. treo georreferenciado del suelo hasta las aplicacioMuchas veces, cada cuadrícula del muestreo tiene nes de nutrientes a dosis variable representan los una gran área de superficie, comúnmente más de servicios de agricultura de precisión más amplia-

52

### Página 55

Figura 3. Esquema ilustrativo de algunas opciones de desplazamiento utilizadas por proveedores de servicios de agricultura de precisión para la recolección de muestras simples a lo largo de un muestreo en cuadrículas. La identificación de la muestra compuesta está asociada a las coordenadas geográficas del punto central de la cuadrícula. (Fuente: elaboración Álvaro Resende)

mente difundidos entre los agricultores. Empresas

especializadas utilizan muestreadores hidráulicos

de suelo adaptados en cuatriciclos (Figura 4) o

camionetas con GPS para las recolecciones en

el campo, procesan los resultados de análisis por

medio de programas informáticos de geoestadística y utilizan sistemas de información geográfica (SIG) para producir mapas diagnósticos y de prescripción de insumos, siendo estos reconocidos por los equipos distribuidores de correctivos y fertilizantes a dosis variable.

El muestreo de suelo para aplicar agricultura de

precisión normalmente comienza por la obtención,

vía GPS, de los contornos georreferenciados de

la chacra o, si fuese el caso, de los sub-ambientes a ser mapeados de forma independiente, de acuerdo a lo descrito en el apartado anterior. Una Figura 4. Muestreador hidráulico tipo broca (foto pequeña) montado en cuatriciclo, equipo comúnmente utilizado en el muestreo vez definida la densidad de la cuadrícula de mues- georreferenciado del suelo. El GPS es el dispositivo de color blanco acoplado en frente del vehículo, al lado de la caja de almacenamiento treo (la cual se recomienda que sea de cuadrículas de muestras. (Fotos: Álvaro Resende) con área de 1 hectárea o menos para un primer mapeo de fertilidad), la cuadrícula conteniendo los puntos de recolección de suelo es ajustada a los transferidos para el GPS y, a partir de entonces, el contornos de chacra y trazada utilizándose un pro- muestreador puede ir al campo y realizar el muesgrama de navegación y posicionamiento por saté- treo siguiendo las coordenadas geográficas de los lite. En la secuencia, la información de la grilla y de respectivos puntos de recolección de muestras los puntos de recolección georreferenciados son simples.

53 PARTE 1

### Página 56

Cada muestra compuesta, referente a una de origen y de los factores de formación del suelo, cuadrícula, precisa ser adecuadamente identifi- es bien conocida la variabilidad horizontal debida cada por un código para su envío al laboratorio a las diferencias de fertilidad química en las filas de de análisis. A ese código debe estar asociada la cultivos de siembre directa con fertilización en el información, como la identificación de la chacra, la surco (Figura 5). De manera similar, la acumulación profundidad de recolección del suelo y, lógicamen- de nutrientes menos móviles en la capa más sute, las coordenadas geográficas del punto central perficial del perfil del suelo, crea una estratificación de la cuadrícula, las cuales permitirán el procesa- que corresponde a la variabilidad vertical. Así, es miento de los resultados del análisis del suelo en importante buscar una mejor definición de los luprogramas geoestadísticos y SIG. gares exactos y de la profundidad de recolección Para un proceso geoestadístico satisfactorio y de muestras en el campo, de acuerdo con las capara la obtención de mapas más representativos, racterísticas e historia de la chacra. el ideal es que la chacra sea caracterizada con un Cuando la posición de las líneas de fertilización mínimo de 40 a 50 muestras compuestas, que del cultivo anterior son visibles, se debe estandarirepresentarán 40 a 50 datos georreferenciados zar la recolección del suelo solamente en las líneas para determinar modelos de variabilidad espacial o mantener una proporción fija de muestras simde atributos del suelo en el área. Buenos modelos ples recolectadas en las líneas (por ejemplo: 1/3 o matemáticos posibilitarán las intercalaciones y es- 1/4 de las muestras simples en la fila). Ese cuidado timativos más realistas de valores de los atributos pretende prevenir el riesgo de ocurrencia de valoen los lugares muestreados, y generarán mapas res muy dispares en los resultados de los análisis más confiables. Es premisa del número mínimo de (outliers), lo que puede perjudicar la calidad del muestras compuestas puede ser considerada en mapeo a ser realizado. el momento de la definición de la densidad de la La profundidad de la recolección debe ser deficuadrícula de muestreo. Como el procesamiento nida de acuerdo a las mismas premisas considerade datos georreferenciados de manera deseable das en el muestreo tradicional. Lo más común es exige cierto grado de conocimiento técnico, exis- caracterizar la capa de 0 a 20 cm de profundidad. ten programas informáticos que realizan esa tarea Muestreos estratificados (por ejemplo: 0 a 10; 10 a de manera automática, mediante modelos estan- 20; y 20 a 40 cm de profundidad) pueden ser condarizados. En general, esa es una opción más ac- venientes para determinadas situaciones en que cesible para los usuarios pero que puede compro- es necesaria una mejor interpretación de las conmeter la calidad de la información obtenida. diciones de fertilidad a lo largo del perfil del suelo.

Los suelos explorados con cultivos anuales En el muestreo tradicional para análisis de fertipresentan atributos químicos (por ejemplo: pH y lidad, el número de muestras simples recomendadisponibilidad de nutrientes) y físicos (por ejemplo: do para la formación de una muestra compuesta textura y compactación) que varían horizontal y es de 20 a 30, con el objetivo de garantizar una verticalmente. Además de las variaciones pedoge- buena representatividad. En la práctica de muesnéticas por causa de la influencia de los materiales treo para agricultura de precisión, dada la deman-

54

### Página 57

Figura 5. Factores frecuentemente asociados a variaciones puntuales de la fertilidad del suelo y que pueden constituir fuentes de errores o distorsiones en los mapas generados a partir de muestreo georreferenciado: Diferencias del histórico de uso y manejo a corta distancia (A); cambios abruptos de relieve o mineralogía (B); fallas de plantas o focos improductivos donde no existe absorción de nutrientes aplicados en la líneas de siembra (C, D); lugares de depósito de cal en la chacra (E); filas de fertilización que mantienen residuos de fertilizantes (F); bajada de terrazas con exposición de subsuelo (G); aplicación despareja de fertilizantes y correctivos (H); y chacras que promueven la exportación heterogénea de nutrientes (I). (Fotos: A: Marina Vilela; B y I: Luciano Shiratsuchi; C, D, E, F, G y H: Álvaro Resende)

da de mano de obra de mayor intensidad en la Las principales determinaciones analíticas recolección en el área a ser mapeada, el número que posibilitarán identificar el nivel de fertilidad de muestras simples es fijado entre 5 y 10 por cua- del suelo en la chacra y que serán la base para drícula. Incluso, una recomendación más criteriosa las recomendaciones de manejo localizado de indica que ese número no debe ser inferior a 10. correctivos y fertilizantes son: pH; cationes interMientras existan opciones de equipamientos con cambiables (Al, Ca, Mg, K y, eventualmente, Na); mayor grado de automatización en el proceso de P disponible; materia orgánica; y granulometría muestreo, en principio, cualquier tipo de muestrea- (arena, limo y arcilla). La determinación de la disdor de suelo puede ser utilizado para agricultura de ponibilidad de micronutrientes (B, Cu, Fe, Mn y precisión, y es suficiente que sea utilizado justamente Zn) es bastante útil en el diagnóstico de la fercon un GPS. Lo importante es que cada muestra en- tilidad, aunque todavía no sea común el maneviada al laboratorio pueda ser asociada a las coorde- jo de micronutrientes con aplicaciones a dosis nadas geográficas del lugar de recolección. variable.

55 PARTE 1

### Página 58

La frecuencia de muestreo debe ser tanto ma- desparejo (aplicación de cal y fertilizantes) de los yor cuando más intensiva fuera la utilización del cultivos es aleatoria (Figura 5), lo que implica una suelo. Cuando se trabaja con dos o más zafras al discontinuidad en el patrón de variabilidad de los año, con fertilizaciones para cada cultivo, mayor nutrientes. Muestras extraídas en lugares con cones la necesidad de monitorear las alteraciones en diciones muy diferentes dentro de la chacra y ninlas condiciones de fertilidad del suelo en la cha- guna expresión en términos de área (outliers), influcra. Así, los muestreos deben ser realizados en yen en el procedimiento de interpolación y pueden intervalos de 1 a 3 años, condicionados por una distorsionar los mapas de fertilidad. ponderación costo-beneficio. En este aspecto, se En áreas extensas de cultivos anuales en El debe tener presente que el punto fuerte de la agri- Cerrado brasilero, parte de los muestreos para cultura de precisión es el perfeccionamiento del agricultura de precisión aún son realizados en griproceso decisorio en el manejo de la propiedad llas poco densas, siendo frecuente la definición de agrícola como un todo y no apenas en la aplica- tamaños de la cuadrícula por encima de 4 hección de tecnologías disponibles para el suministro táreas. En esta situación, las estimaciones de vade nutrientes. Desde este punto de vista, parte del lores de atributos del suelo para lugares situados retorno de inversión en muestreo del suelo no será entre los puntos de muestreo pueden ser muy inmediato, sino proveniente de las mejoras en las diferentes a la realidad, con perjuicio para la calidecisiones gerenciales a lo largo del tiempo. dad del manejo con agricultura de precisión. Para Los demás procedimientos y cuidados requeri- minimizar este problema, Giménez y Zancanaro dos en el muestreo georreferenciado son los mis- (2012) sugieren que se utilice un muestreo en celmos tradicionalmente preconizados para la reco- das, en el cual cada celda corresponde a una cualección, manipulación y preparación de muestras drícula del muestreo en grillas donde se recopilan de suelo para análisis de fertilidad. 20 muestras simples recorriendo toda el área. El valor así obtenido para un determinado atributo Cabe destacar que la descripción del compor- pasa a constituir el valor medio para el área total tamiento espacial por medio de la geoestadísti- de aquella celda y no se hace interpolación. De ca constituye un enfoque eficiente para atributos este modo, se elimina la posibilidad de que una cuya variabilidad depende esencialmente de pro- muestra problemática afecte la conformación del cesos naturales (ejemplo: aquellos asociados a las mapa diagnóstico, ya que el valor de una celda no característica de formación del suelo, como la tex- está relacionado a los de las celdas vecinas para tura y la mineralogía) y que tienden a permanecer componer ese mapa. estables a lo largo del tiempo. Existen aspectos que tornan más compleja la caracterización de la variabilidad del suelo en áreas agrícolas, espe- Consideraciones finales cialmente en el caso de la fertilidad química (por Con las fertilizaciones (y sus fallas) a cada cultiejemplo: niveles de los nutrientes). La distribución vo, se acumulan interferencias que llevan a modifiespacial de lugares que tuvieran alterados los ni- car los patrones de variabilidad en una misma área veles de nutrientes por fallas o manejo nutricional a lo largo del tiempo. Así, difícilmente los patrones

56

### Página 59

espaciales encontrados para los atributos de ferti- manejables con el uso de correctivos y fertilizanlidad química del suelo en un área sean extrapola- tes constituyen apenas una parte de los condibles para otras o se mantengan inalterados con el cionantes de la productividad final de una chacra. paso del tiempo. De esto se deriva, entonces, que Atributos físicos del suelo, como textura, densila agricultura de precisión en el manejo del sue- dad, porosidad y capacidad de almacenamiento lo debe volcarse para el monitoreo de chacras en de agua, pueden tener gran importancia relativa una perspectiva de ajustes continuos a lo largo del en la determinación de la productividad, así como tiempo, y utilizarse no solo para muestreos periódi- otros abióticos y bióticos que no siempre son cos del suelo, sino también como una herramienta considerados en la agricultura de precisión. Esos que agregue y permita detallar información sobre hechos refuerzan la necesidad de trabajar con un la variabilidad espacial y temporal en las áreas de enfoque transdisciplinario al aplicar agricultura de cultivo. precisión, buscando aprovechar mejor su potencial para obtener mayor eficiencia en el gerenciaComo lo descrito anteriormente, el mapeo que miento de la propiedad agrícola. utiliza muestreo en cuadrículas presenta imperfecciones y los aspectos económicos de este procedimiento podrían inviabilizar la continuidad de la agricultura de precisión en fertilidad del suelo en los modelos actuales, a medida que las ganancias financieras del productor se tornen menos compensadas después de las primeras intervenciones.

Es sabido que la productividad en diferentes partes de una chacra depende de las características del terreno (posición en el relieve, tipo de suelo, textura, capacidad de retención de humedad, etc.) que interactúan o influyen en la fertilidad química del suelo. Por lo tanto, un diagnóstico preliminar de las causas de variación de la productividad posibilita orientar el muestreo, reducir el número de puntos de recolección y optimizar costos, además de mejorar la calidad de la información expresada en los mapas de fertilidad y aumentar la confianza en la toma de decisiones sobre el manejo localizado de fertilización.

Raramente se verifica una alta correlación entre un factor de producción aislado, sea edáfico o no, con la productividad. Así, los factores de producción relacionados con la fertilidad del suelo y

57 PARTE 1

### Página 60

1.6. Técnicas avanzadas de análisis El principal objetivo de la actividad agrícola es la producción final, los primeros captadores que para los cultivos a tiempo real. aparecieron en el mercado fueron sistemas capaRodrigo Quintana ces de determinar las variaciones de rendimiento en el interior de la parcela.

Rodrigo Quintana En este contexto, para enfrentar esos nuevos

Investigador del Instituto Nacional de Investigación desafíos, se necesitan diversas tecnologías que Agropecuaria (INIA) Chile entreguen información desde el suelo, la planta y el rquintana@inia.cl ambiente para detectar y cuantificar la variabilidad natural e inducida de los huertos, para así poder estabilizar y mejorar los rendimientos y la calidad Introducción de los cultivos.

Las nuevas tecnologías puestas al alcance del Para ello se explicarán los diversos equipos inagricultor, ligadas con la agricultura de precisión, tegradores en la cadena de producción y su imestán diseñadas para comportarse como visión portancia de cada uno de ellos. suplementaria (captadores instalados sobre los equipos o sobre los satélites), encargadas de observar los cultivos y generar información para la Medición de las propiedades del suelo elaboración de las bases de datos, herramientas través del uso de equipo de conductividad imprescindibles para ayudar en la toma de decieléctrica siones en el sistema productivo. Además, esta La conductibilidad eléctrica (CE) de los suetecnología actúa como una memoria suplemen- los puede definirse como la aptitud de éstos para taria para el almacenamiento y análisis (Sistemas transmitir la corriente eléctrica. Múltiples factores de Información Geográfica) de la masa de informa- contribuyen a la variabilidad de la CE, tales como: ción generada por los captadores. los que afectan la conectividad de agua en el sueLa utilización de captadores, en su función lo, la agregación del suelo (agentes cementantes principal de multiplicadores de los ojos del agri- como arcillas, materia orgánica y estructura del cultor, debe suponer un sistema de adquisición de suelo), electrolitos en la solución del agua (saliniinformación intrapredial de forma exhaustiva, sin dad, iones, contenido de humedad del suelo, y intervención humana y al menor costo. La infor- temperatura del suelo), y la conductividad de la mación (cualitativa o cuantitativa) generada por los fase mineral (tipo y cantidad de minerales). captadores puede hacer referencia a: Las mediciones espaciales de la CE han sido

• Planta reportadas como un potencial indicador de la variación de la producción de los cultivos, causada

• Suelo

por diferencias en el agua del suelo. En algunos

• Enfermedades casos, la CE puede ser directamente correlacio-

• Clima nada con la propiedad física y la química del suelo

58

### Página 61

so natural) y bien desarrolladas se pueden delimitar

utilizando los estudios de suelos de escala regional

municipal, sin embargo, el estudio de la distribución

de los suelos altamente susceptibles de compactación o al sellamiento (inducido por el hombre) con fines de manejo y recuperación, requiere de estudios detallados y ultra detallados y el empleo de otros métodos e índices para su evaluación ya que estos problemas no son predecibles a través de las

Figura 1. Sistema EM38 y desarrollo de Mapa de Conductividad

Unidades Pedológicas de Suelos. Esto permitirá arEléctrica de Suelo monizar las cualidades del suelo (posibilidades de penetración y circulación de fluidos, retención de humedad, capacidad de enraizamiento, susceptibicomo la localización de un horizonte impermeable, lidad a la degradación física y química, etc.) y práctila textura, la salinidad, el agua, la materia orgáni- cas agronómicas con los requerimientos del cultivo ca, los metales, entre otros. Por ejemplo, existen en función de su variación en el campo para maxisensores que miden esta CE a través del contacto mizar el margen de ganancias evitando los daños directo con el suelo como VERIS 3100, EM38, etc. excesivos. Para ello hay novedosos equipos que Este valor puede ser usado para inferir propie- utilizan diversas técnicas de medición en las cuales dades físicas como la textura, puesto que la CE se detallan a continuación.9 aumenta con el aumento en el contenido de arcilla.

Los resultados de esta medición no son absolutos Equipo de medición mediante resistencia ya que la CE varía, además, con el contenido de mecánica agua, las sales disueltas y la temperatura del sueEl sensor está conformado por un transductor lo. Los datos obtenidos a partir de la medición de octagonal de anillos extendidos (EORT), acoplado CE son útiles para el diseño de sistemas de riego a un órgano de trabajo del tipo escarificador alado. y orientar el muestreo de suelos para análisis físico La resistencia o impedancia mecánica del suelo es y químico. medida por el transductor, para posteriormente correlacionarla con su estado de densificación o Mediciones de compactación espacial de compactación.10 suelo

9 Fuente: Captación y segmentación de suelos. Universidad Nacional de

La compactación excesiva es probablemente Colombia. Junio 2014: http://www.virtual.unal.edu.co/cursos/sedes/palmimás extensiva de lo que se piensa por el incremen- ra/2057/lecciones/subleccion35.html to en el uso de la labranza pesada y cosechadoras 10 Fuente: Revista Ciencias Técnicas Agropecuarias. Desarrollo de un sensor para la medición continúa de la compactación del suelo. pesadas y también por el uso intensivo del suelo. Junio 2014: http://scielo.sld.cu/scielo.

Las áreas de suelos con capas cementadas (proce- php?pid=S2071-00542011000100001&script=sci_arttext

59 PARTE 1

### Página 62

Fundamentación del sensor

El principio de funcionamiento del sensor a desarrollar se basa en el sensoramiento de las tensiones del suelo, es decir se clasifica como un sensor de fuerzas verticales y horizontales. El sensor está conformado por un órgano de trabajo del tipo escarificador alado, y un transductor octagonal de anillos extendidos.

Al interactuar la reja y la parte frontal del brazo o soporte del sensor con el suelo, este último acciona el transductor octagonal deformándolo de

Figura 2. Sensor de compactación desarrollado en el Centro de

Investigaciones Agropecuarias (CEMA), de la Universidad Agraria de forma tal que se puede determinar mediante la exLa Habana (UNAH) tensometría, las fuerzas o resistencia que opone el

Figura 3: Sistema EM38 y desarrollo de Mapa de Compactación de Suelo. Fuente: Proyecto INIA-FIA Agricultura de Precisión en Frutales (2013)

60

### Página 63

suelo al ser cortado, tanto en el eje vertical como Medición espacial de materia orgánica de horizontal, generando mapas de compactación suelos que son muy útiles para mejorar la condición del Actualmente la empresa Veris, generó equipos desarrollo de los cultivos.11 para determinar en forma no destructiva la Materia Orgánica (MO) del suelo, generando planos espaMedición portable de compactación de ciales de ésta información, el equipo es denomisuelo con sensor ultrasónico nado OpticMapper, recoge datos de alta calidad, El equipo ultrasónico de profundidad toma rápida y fácil de procesar. lecturas en incrementos de 2.5 cm mientras El Veris OpticMapper tiene un sensor óptico de que la celda de carga mide la resistencia a la doble longitud de onda montado dentro de una penetración. fila plantadora, configurado especialmente-por de-

• Los datos de compactación se muestran en bajo de los residuos de cultivos y la superficie del PSI o kPA. suelo seco.

• Permite tomar lecturas geo-referenciadas de Las mediciones del suelo se adquieren a tracompactación de suelo. vés de una ventana de zafiro en la parte inferior

• Registra hasta 722 perfiles (579 con la opción del pie de equipo, en el surco. Las lecturas se GPS/DGPS**).12 recogen una vez por segundo y conectados a su ubicación geográfica por un GPS. La profundidad

11 Ídem 10 de medición es ajustada entre 1 a 3 pulgadas

12 Fuente: Junio 2014: http://www.solostocks.com.ar/ (2.5 a 7.6 cm).

Figura 4: Sensor Óptico Veris para determinar materia orgánica de suelos

61 PARTE 1

### Página 64

Mediciones nutricionales

La absorción de nutrientes de cada cultivo

responde a una serie de factores dentro de los

cuales se incluyen, la producción total de materia

seca (crecimiento anual), fenología del crecimiento anual, disponibilidad de nutrientes en el suelo (fracción soluble del suelo), condiciones de manejo que favorecen la sincronía de crecimiento con la sincronía de absorción de los elementos necesarios en las cantidades adecuadas para evitar desequilibrios y problemas fisiológicos y/o de calidad del producto cosechado.

Los métodos tradicionales utilizan muestreos

dirigidos, que son certeros pero ocupan mucho

tiempo y recursos para obtener la información,

a veces esa información llega a destiempo para

cumplir el objetivo que es entregar información

oportuna.

El interés de evaluar la evolución de nutrientes

en el suelo permite conocer por balance de masas la relación del agua en el suelo (acumulación máxima de agua en el suelo-acumulación parcial de agua en cada momento de evaluación) con la concentración de nutrientes (relación de masa de nutrientes en volumen de agua) en cada perfil, los cambios nutricionales generados por Figura 5. Sistema de monitoreo permanente de la solución del suelo la extracción de la planta (extracción fenológi- usando extractómetros ca diferencial) y por los mecanismos de pérdida (principalmente de lixiviación determinadas con extractómetros de solución de suelo). Para ello se busca en cada periodo fenológico, además se instalan extractómetros a diferentes profundi- se pueden analizar en forma espacial generándades según el patrón de localización de raíces dose mapas espaciales de deficiencia de cada en cada zona de evaluación (Figura 5). Así se elemento faltante. puede determinar en forma más aproximada los A través de este sistema, se obtienen planos momentos en los cuales es necesario aumentar espaciales de elementos que puedan estar en déo disminuir la cantidad de aplicación de nutrien- ficit o en exceso, ejemplo de ello se demuestra en tes en función del objetivo de crecimiento que la Figura 6.

62

### Página 65

Figura 6. Distribución espacial de cada elemento, ejemplo en huertos de olivos, Chile

Equipos de medición química foliar

El manejo adecuado de los niveles de nutrientes

es fundamental para asegurar una óptima fertilización

y producción en sus cultivos. Para obtener mediciones in situ, existe un equipo llamado Kit Multi Ión.

El sistema Multi Ión permite conocer los niveles exactos de la mayoría de macro nutrientes a Figura 7. Kit Multi Ión tiempo real con los beneficios a nivel agronómico y técnico que esto supone. Las mediciones a tiempo real permiten el control exhaustivo al agricultor Este sistema no solo permite obtener una rápara actuar en forma rápida y específica sobre su pida información, sino que da la ventaja de hacer cultivo, sin necesidad de enviar muestras al labo- aplicaciones en forma oportuna y diferenciada, ratorio para su análisis. asociada a los planos de vigor.

63 PARTE 1

### Página 66

Sistema de medición continua para pH de poco tiempo un mapa de la variabilidad del pH de Suelo suelo, haciéndolo muy útil para tomar decisiones Para la determinación del pH se emplean sen- precisas para mejorar las condiciones de suelo. sores electroquímicos. Los sensores son pequeños dispositivos que como resultado de una inte- Balance hídrico del suelo racción química, el sensor transforma dicha inforLa humedad del suelo se encuentra siempre en mación química o bioquímica de tipo cuantitativo, constantes cambios producidos por diversos facentrega una señal medible y útil analíticamente. tores. Por ejemplo en un mismo campo con igual La tecnología de sensores electroquímicos suelo e influencia de las condiciones atmosféricas, es especialmente apropiada para abordar de un la humedad del suelo es desigual. Esta diferencia modo económico, rápido y fiable su interpretación. está determinada por el consumo de agua del sueEjemplo de ello es el equipo denominado lo debido a la evapotranspiración de las plantas.

MANAGER (MSP), de la empresa Veris. Existen distintos procedimientos para determinar el contenido de agua en el suelo y poder relacionarlo con las necesidades de agua de las plantas y el riego, que han ido evolucionando al compás del desarrollo científico y tecnológico. En tal sentido existen diversos equipos de determinación de humedad de suelo en tiempo real, en este caso se comentaran los sensores de tipo: Reflectometría en el Dominio de la Frecuencia (FDR) y Reflectometría en el Dominio del Tiempo (TDR).

Equipos basados en las propiedades

Figura 8. Equipo MANAGER (MSP), para determinación del pH en suelo

dieléctricas del suelo

Existen básicamente dos clases de instruEl equipo está constituido por un cilindro hi- mentos que utilizan esta técnica para determinar dráulico que se penetra en el canal del surco re- la humedad volumétrica del suelo (θv), los denocogiendo el suelo que luego es presionado contra minados TDR y los FDR. Ambos se basan en las los electrodos de pH. Después de unos segundos propiedades del suelo como condensador eléctriel pié del equipo se baja nuevamente para recoger co y miden el coeficiente dieléctrico aparente de más suelo. Mientras lo hace, la nueva tierra que éste (ε), el cual es fundamentalmente función de la viene en la muestra mueve el suelo anterior a la humedad, dado que el del aire es ε ≈ 1, el de los parte trasera de las boquillas de pulverización de sólidos del suelo es ε ≈ 2-5 y el del agua es ε ≈ 80. artesa y los pies del arado a limpiar los electrodos El coeficiente dieléctrico del suelo también varía de pH. En resumen éste equipo permite generar en con la temperatura y con la salinidad, pero su in-

64

### Página 67

fluencia suele ser pequeña (temperatura 4 °C) ex- do el generador de pulsos de radiofrecuencia, el cepto en las proximidades a la superficie del suelo, osciloscopio analizador de pulsos y el procesador por lo que no se precisan correcciones en la ma- de datos. Miden la humedad volumétrica del suelo yoría de los casos. con un margen de error del 1-5%.

La zona de medida es la comprendida entre las

varillas de acero (2, 3 ó 4 modelos), tal y como se

Sensores de reflectometría en el dominio aprecia en el esquema (Figura 7) y a lo largo de del tiempo toda su longitud.

Miden el coeficiente dieléctrico del suelo (ε) a Para medidas en superficie no requieren la partir del tiempo de recorrido de un pulso elec- instalación de elementos permanentes en el suetromagnético a lo largo de varillas de acero que lo, pero para medidas en profundidad hay que se introducen en el suelo y que sirven de guía a realizar un acceso e instalar más o menos permalas ondas. nentemente las sondas. Una dificultad práctica Los equipos se componen de una sonda por- importante es que la distancia entre la sonda y ta-varillas que se entierran al suelo, un cable de el instrumento registrador se limita a longitudes conexión y un cuerpo central, donde va instala- inferiores a 25 m.

Figura 9. Distintos tipos de sondas TDR y zona de medida con 2, 3 ó 4 varillas

65 PARTE 1

### Página 68

también genera problemas, principalmente en

las medidas superficiales.

La zona de influencia, sobre la que se realiza la medida (Figura 9), corresponde a unos 10 cm en altura (5 por encima del sensor y 5 por debajo) y aproximadamente 7 cm de radio, si bien es en los primeros 3 cm es donde se mide el 90% de la señal. Por ello, la instalación del tubo de acceso debe ser muy cuidadosa, a fin de que exista un completo contacto de la pared del tubo con el suelo y evitar que queden huecos que darían lecturas falsas, tanto si se llenan de aire o de agua, dadas las diferencias de coeficiente dieléctrico.

Figura 10. Evolución estacional del contenido de humedad del

suelo (%v/v), medido con TDR, a distintas profundidades para los Tanto los sensores TDR como los FDR, retratamientos de riego con kc = 0.45 (izquierda) y secano kc = 0.0 (derecha) quieren transformar la señal medida a valores de humedad volumétrica mediante un calibrado, el cual se realiza internamente en el procesador de Sensores de Reflectometría en el Dominio datos. En la mayoría de suelos es suficiente con de la Frecuencia la calibración estándar (precisión del 5%), aunSon también conocidos como sensores de que dicha ecuación de calibración necesite ajuscapacitancia ya que utilizan esta propiedad para tes específicos para suelos de mucha materia medir el coeficiente dieléctrico (ε) de la matriz del orgánica, muy arcillosos o salinos, pudiéndose suelo. Determinando la capacitancia se obtiene la conseguir entonces precisión en torno al 1-2 %. constante dieléctrica y, en consecuencia, la estiSon resistentes, estables y de respuesta rápida. mación del contenido de agua del suelo.

Necesitan poco mantenimiento pero son de cosEl sistema FDR plantea una serie de incon- te elevado. Tienen poca limitación en cuanto a venientes. El más importante es el escaso de la longitud del cable (400 m) y permiten instalar volumen del suelo al que se refieren las deteren una sola sonda varios sensores a diferentes minaciones de la capacitancia, lo que obliga a profundidades. una perfecta y costosa instalación del tubo de acceso a la sonda, requiere además de que en En la gestión del manejo del riego, la gran vendicha fracción de suelo no haya materiales ex- taja de los instrumentos multisensor es el proportraños como piedras o raíces y que no exista cionar la posibilidad de un registro “casi continuo” separación entre el tubo y el suelo, ya que la de datos a distintas profundidades del suelo y en interferencia del aire influye sobre la calidad de la mayoría de los casos, puede ser suficiente anala medida. La existencia de grietas en el suelo lizar la tendencia que sigue el contenido de agua,

66

### Página 69

para lo cual no se necesita de una calibración procedimiento es necesario definir un límite supeespecífica. rior (paro riego) y un límite inferior (inicio riego) de Muchos de los equipos FDR comerciales llevan contenido de agua para la profundidad de suelo asociados programas gráficos para análisis de los correspondiente a la ubicación del sistema radicudatos, en los que la humedad se puede presen- lar activo, que en el caso de la vid puede llegar a 2 tar sensor a sensor o de forma acumulada en los m, aún cuando en la mayoría de las situaciones en distintos sensores, indicando así el agua almace- regadío una alta proporción de la extracción total nada en una cierta capa de suelo. Mediante estos de agua ocurre en los 50-100 cm. gráficos se puede obtener una idea del consumo diario por parte de las raíces y los intervalos nocturnos, tramos horizontales, en los que apenas Sistema de termografía para detección de hay extracción de agua (Figura 11 A y B). Como estrés hídrico ya se comentó, para el manejo del riego por este Las plantas requieren un aporte continuado de agua que reemplace la que se evapora principalmente desde las hojas. Este requisito se debe a que las hojas están expuestas a una fuerte demanda evaporativa (flujos de radiación solar y térmica y aire caliente y seco) mientras que la superficie interna está saturada de vapor de agua. Para que el dióxido de carbono entre en las hojas los estomas deben de estar abiertos, lo cual permite que el vapor de agua escape libremente desde el interior de la hoja siguiendo el gradiente de presión de vapor. Para mantener el flujo del agua sin que se produzca la deshidratación del tejido, las plantas han desarrollado elaborados sistemas de captación y transporte de agua. La Figura 12 muestra un esquema del sistema suelo-agua- planta y sus interacciones.

Un pequeño desfase en el proceso de transporte en respuesta a las alteraciones en el abastecimiento de agua desde el suelo o en la demanda atmosférica provoca un déficit hídrico en la planta

Figura 11: Monitoreo de Riego a través de sensores de humedad lo cual es dañino para la planta. Es posible caracde suelo. A) Representación de la humedad volumétrica del suelo mediante sensor FDR y B) Decisión de riego en función del nivel de terizar el estado del agua en la planta en términos estrés considerado energéticos, evaluando su potencial hídrico.

67 PARTE 1

### Página 70

Sistema de evaluación hídrica mediante

termografía infrarroja

El potencial hídrico foliar (YL) es una variable comúnmente utilizada para evaluar el estado hídrico de las plantas. El método estándar para realizar esta medición es el de la cámara de presión o Scholander que brinda valores precisos del YL, pero tiene la desventaja de ser destructivo y lento. Por esto resulta poco práctico a la hora de medir grandes superficies como se requiere en la agricultura de precisión. Dada la variabilidad espacial que presentan los cultivos, la estimación remota del potencial hídrico se convierte en una herramienta fundamental para diseñar estrategias de riego sitios-específicos, importantes para optimizar el uso del agua de riego para la obtención de la producción y la calidad.

Figura 12. Esquema del sistema suelo-planta-aire Figura 13. Cámara térmica portátil marca Fluke modelo TI 4

68

### Página 71

Fundamento teórico de la aplicación de ésta

tecnología:

Como indicador del estatus hídrico derivado de

la obtención de imágenes termográficas, se utiliza

el “índice de estrés hídrico de cultivo” o CWSI, según la relación propuesta por Jones (1999), siendo expresado como:

Donde, para una particular condición de déficit Figura 14: Dendrómetros automatizados para medición de crecimiento de presión de vapor, del tronco y de frutos

Temperatura foliar o de canopia promedio.

Temperatura mínima de canopia para el culti- Sensores no destructivos para medir vo (no estresado). calidad en alimentos funcionales En la actualidad, la espectroscopia se utiliza Temperatura máxima de canopia para el culcomo una herramienta no destructiva para detertivo (estresado). minar características organolépticas de la fruta a ser cosechada o en el árbol. Su funcionamiento se Un CWSI con un valor de 0 indica que el cultivo sustenta en el desarrollo de calibraciones entre un no presenta estrés hídrico, mientras que un CWSI de 1, significa un estrés hídrico máximo para cada análisis de referencia del compuesto a ser medido cultivo. en relación a la del sensor que puede ser en el espectro del Infrarrojo Cercano (NIR), Ultravioleta (UV), Ultrasónico, entre otros. Un ejemplo del uso Uso de dendrómetros para monitorear el de este tipo de instrumentos, se encuentra en la diámetro de troncos y frutos industria de vino, en donde se utiliza para la cuanLa medición del diámetro del tronco y del fruto, tificación de distintas variables químicas para dees necesario para dar seguimiento a los cultivos en terminar la calidad de la uva a vinificar. Ejemplo de sus variaciones, tanto diurnas como nocturnas en ello, unas de las variables que se puede determiel contenido de agua. El diámetro del tronco dismi- nar son: °Brix, pH, acidez titulable, contenido fenuye durante el día porque las plantas pierden más nólico y color. La gran ventaja de estos equipos agua por la transpiración que la que ellas pueden es la gran rapidez de medición (2 a 3 segundos absorber. En la noche cuando hay poca perdida aproximadamente) y la posibilidad de evaluar evode agua los troncos aumentan en diámetro debido luciones en campo que permiten realizar gestión a la absorción y al almacenamiento del agua. de manejo.

69 PARTE 1

### Página 72

Figura 15. Equipo de medición de calidad de fruta NIR y sensor de Multiplex UV.

Sin desmedro que existen diferentes tipos de espacial y temporal de predios para llevar a cabo equipos que se utilizan en campo debe estudiar- el manejo del mismo (manejo de sitio-específico) se o validarse las curvas de calibración necesarias acorde al conocimiento integral del predio. Por para su uso masivo en la mayoría de los frutales. otra parte, al hacer uso de instrumental asociado Hoy en día en el contexto internacional se está tra- a sensores y teledetección asociado a los avances bajando en el desarrollo de medición dinámica con de la informática, hace posible el estudio de áreas estos tipos de equipos. extensas, permitiendo la generación de informaFinalmente, el equipamiento asociado a la ción clave para el control y manejo de los huertos agricultura de precisión permite generar solucio- que permitirán maximizar el rendimiento y la calines a los problemas, al tener como uno de sus dad que repercutirán en la mayor rentabilidad de fundamentos de trabajo el considerar la variación sistema productivo.

70

### Página 74

LUN

45

3

122

RO

2

004

322

### Página 75

PARTE 2

INTEGRACIÓN DE

INFORMACIONES Y TOMA

DE DECISIONES

RO

2

004

322

### Página 76

2.1. Creación de mapas de manejo el proceso de gerenciamiento de campo, lo cual

posibilita una adecuada toma de decisiones. con datos espaciales

Los datos muestreados en el campo por los

Elena Charlotte Landau, Ziany Neiva Brandão, Carla

profesionales de diversas áreas del conocimiento

Moreira de Faria frecuentemente presentan diferencias en términos

del nivel de detalle (resolución espacial) y escala,

Elena Charlotte Landau aspectos relacionados con el método de muesEmbrapa Milho e Sorgo. Sete Lagoas-MG, Brasil. treo u obtención de cada tipo de información. El charlotte.landau@embrapa.br profesional del área de SIG es el responsable de efectuar los cambios necesarios para organizar la Ziany Neiva Brandão información sobre un determinado lugar en formaEmbrapa Algodão. Campina Grande-PB, Brasil. to de mapas, para una mejor comprensión y acceziany.brandao@embrapa.br sibilidad de los datos obtenidos. Esto permitirá la posterior integración espacial de esos datos multiCarla Moreira de Faria disciplinarios y la identificación de patrones, lo que Embrapa Milho e Sorgo. Sete Lagoas-MG, Brasil. contribuye a la generación de mapas de manejo carla.faria@embrapa.br del área cultivada.

El acceso a los datos, que incluye los resultados del modelaje, se extiende entonces a un “sisIntroducción tema de decisión” o herramienta de decisión que La agricultura de precisión abarca la combina- utiliza una mezcla de modelos del proceso y de ción de diversas tecnologías e informaciones, e in- datos biofísicos y bioquímicos obtenidos en las cluye: datos recogidos en campo (características evaluaciones. De esta manera, existe la necesidad físicas y químicas del suelo, topografía, datos de de un sistema de modelaje con SIG que sea integral y que permita a los productores agrícolas, en productividad), datos derivados de la interpretatiempo y forma, la comprensión de la variabilidad ción de imágenes satelitales (variabilidad espacial espacial de los atributos evaluados, para mejorar y/o temporal del cultivo) y la generación de mapas el gerenciamiento y para una adecuada toma de con prescripciones de aplicación de insumos. A decisiones en la búsqueda del aumento de la propartir de la integración espacial (geográfica) y/o ductividad y de la rentabilidad. temporal de los distintos datos, se pretende optimizar el rendimiento económico y reducir los impactos ambientales en el área de producción. La Sistemas de información geográfica para integración espacial de información multidiscipli- el mapeo en la agricultura de precisión naria requiere el involucramiento de un profesional La agricultura de precisión se basa en el gecon conocimiento en el área de sistemas de infor- renciamiento localizado de sistemas agrícolas, mación geográfica (SIG), que actúe en contacto utilizando recursos tales como mapeo de factores directo con los otros profesionales necesarios en de producción, herramientas de soporte para las

74

### Página 77

decisiones y de aplicación localizada de insumos. recomienda el uso de filtros, la realización de un Una de las principales herramientas de la agricul- análisis de consistencia, o incluso la exclusión de tura de precisión es el mapa de rendimiento ob- datos erróneos (Sudduth y Drummond, 2007). tenido a partir de datos registrados en el campo. Considerando los factores que influyen en la Este mapa posibilita evaluar el proceso productivo productividad y la importancia de los mapas en y sirve de base para la planificación de las estrate- la toma de decisiones para plantaciones postegias de gestión. riores, muchos autores defienden no sólo la creaEl mapa de rendimiento es la representación ción de un mapa instantáneo sino la necesidad gráfica de un conjunto de puntos distribuidos es- de crearlo dentro de un sistema de gestión que pacialmente en el área cultivada, que indican la almacene una base histórica de algunos años, en productividad obtenida en cada uno de los puntos la que todos los parámetros disponibles sobre el muestreados subsecuentemente. Este conjunto área deben ser considerados. En este sentido, es de puntos puede ser interpolado para la obtención aconsejable la evaluación comparativa de la inforde un mapa de superficie y así representar el mo- mación recopilada en diversas cosechas con el fin mento de la cosecha en una determinada área. de llegar a una conclusión posible respecto a un problema específico. De esa forma, los mapas de La productividad de un cultivo depende de rendimiento también posibilitarían la evaluación de varios factores como: la variedad utilizada, el molos efectos de diferentes prácticas agrícolas en la mento de la siembra, la dosis de siembra, las prácproducción, lo que podría auxiliar en las investigaticas de cultivo adoptadas, el control de plagas uticiones o incluso en los tests de campo realizados lizado, el tipo de suelo, la variación de nutrientes por el propio productor. en el suelo, la disponibilidad de agua, los efectos del clima y los cultivos anteriormente plantados – además del propio objetivo de producción actual Corrección de errores y compromiso con y otras variables relacionadas con la habilidad de la precisión cada productor en particular. Todos estos paráme- A los profesionales de SIG les corresponde la tros influyen en el potencial productivo del cultivo tarea de introducir todos los datos en el sistema y pueden generar discrepancias que necesitan de de gerenciamiento. El mapeo del histórico del área análisis en profundidad, antes de la toma de deci- posee una amplia gama de métodos utilizados en sión para futuras cosechas (Brandão et al., 2014). la captura de los datos. La falta de estandarización Así, el mapa de rendimiento indica la productividad entre los softwares utilizados en equipamientos y resultante y no las causas de las variaciones en la sensores garantiza trabajo extra en esa tarea, lo productividad. cual la vuelve relativamente compleja.

Además de considerar los datos de productivi- Los mapas de rendimiento muestran errores dad registrados inicialmente, es necesario realizar comunes que están bien definidos y descritos en la un análisis criterioso del proceso productivo para literatura, como por ejemplo: errores de posicionaeliminar datos tendenciosos, imprecisos o incohe- miento geográfico, tiempo de llegada de granos al rentes provenientes de cada local, para lo cual se sensor, cambios bruscos de velocidad, etc., lo que

75 PARTE 2

### Página 78

Figura 1. Ejemplos de fuentes de errores en registros de rendimiento de maíz obtenidos en dos áreas experimentales: a) y c) representan errores de posicionamiento y de cambios en la velocidad, lo que resulta en el registro de filas y puntos no paralelos y puntos de una misma fila de siembra no equidistantes; b) y d) representan los efectos de los errores de muestreo en los valores de productividad registrados (Figuras originales. Fuentes de datos: Mantovani et al., 2004 y Coelho et al., 2013)

hace que sea esencial la remoción o minimización En algunos casos, los datos están en formade sus efectos (Figura 1). Actualmente, no existe tos que no son digitales, como mapas en papel, un método estándar para la corrección de datos que es preciso digitalizar. Otras veces, la precide rendimiento, a pesar de que se han sugerido di- sión de los equipos es variable, y se hace neceferentes técnicas de filtrado o detección para tratar sario estandarizar el tamaño de las muestras. Un errores específicos (Sudduth y Drummond, 2007). ejemplo típico es la recolección de datos a través

76

### Página 79

del Sistema Global de Navegación por Satélite compararlos posteriormente con imágenes. La de- (GNSS), ya que existen cuatro sistemas en ope- finición del tamaño de la muestra y de la cantidad ración: GPS (Estados Unidos), GLONASS (Rusia), de submuestras debe ser altamente estudiada Galileo (Unión Europea) y Beidou (China). para garantizar que sea compatible con el tamaAdemás de esto, existen tres categorías de re- ño del respectivo píxel en la imagen. El muestreo ceptores: los de navegación con precisión métrica, inteligente considera la variabilidad de variables los topográficos con precisión centimétrica y los indicativas para alterar la densidad del muestreo geodésicos con precisión milimétrica. Por ejemplo, (como la topografía, color del suelo, pH, Ca); o los receptores RTK instalados en tractores para el sea, lugares de gran variabilidad deben ser muesmapeo de rendimiento o incluso para la aplicación de treados con mayor intensidad. insumos, otorgan precisión en milímetros; mientras Si los errores no fueran corregidos adecuadaque otros equipos portátiles, como clorofilómetros o mente, los usuarios de los mapas podrían llegar a sensores de nitrógeno en las hojas, utilizan recepto- conclusiones erróneas y así poner en riesgo la creres de navegación con errores de entre 3 y 10 m, dibilidad y la validez de los resultados. Por ejemplo dependiendo de la región y de las condiciones at- Thyle’n et al. (2001) describieron que removieron mosféricas en el momento de recopilar los datos. de 10 % a 50 % de las mediciones realizadas en Por su parte, la variación en la precisión del po- un experimento de campo al usar diferentes algosicionamiento geográfico se relaciona con la dife- ritmos y técnicas de filtrado. De esta manera, los rencia de sincronización entre el reloj atómico de errores pueden tener un fuerte efecto sobre la dislos satélites y el reloj digital instalado en los recep- tribución de la productividad resultante, especialtores, al considerar que la señal toma 0,7 s para mente al utilizar métodos de interpolación. viajar del satélite hasta el receptor. Así, un error de Solo después del adecuado procesamiento

1 ns (un nanosegundo) en la sincronización del de los datos y de su georreferenciamiento preciso tiempo, causa un error de 30 cm en términos de será posible obtener varios mapas de un mismo posicionamiento geográfico. local que contengan información sobre diversos El procesamiento adecuado de los datos bus- parámetros relevantes para el análisis agronómico ca garantizar una mayor confiabilidad de los ma- y la toma de decisiones con mayor seguridad. pas resultantes. La interpretación de fotografías Mientras tanto, la identificación y corrección de aéreas, imágenes capturadas por sensores en supuestos errores no siempre es fácil. Registros de aviones, planeadores y VANT (vehículos aéreos rendimiento fuera de las filas de siembra pueden no tripulados), e imágenes satelitales de alta re- obtenerse cuando las cosechadoras realizan masolución (píxel de 1 m o menos), debe ser muy niobras de descarga de granos, resultando en un cuidadosa no solo durante la recolección de datos desplazamiento transversal a las filas de siembra. sino también en la etapa de planificación para la Normalmente, las filas de siembra presentan irregurecolección de las muestras. laridades en el borde del cultivo, lo que puede estar Esto es imprescindible cuando se recogen los relacionado con el cambio en la dirección y la velodatos del suelo o de las plantas con la intención de cidad de la cosechadora en el intervalo entre filas de

77 PARTE 2

### Página 80

siembra muestreadas sucesivamente. En otros ca- en la definición de recomendaciones a ser realisos, ese tipo de irregularidad puede ser el resultado zadas en cultivos posteriores en esas áreas de de problemas fisiológicos que son consecuencia de producción. la influencia de factores abióticos o bióticos sobre el Los mapas de rendimiento pueden presentar borde del cultivo, como mayor exposición al viento los datos en tres formatos básicos: y al sol, crecimiento mayor de plantas espontáneas a. Mapa de puntos: representación gráfica de los en ese ambiente, etc. Así, en diversas situaciones datos en los puntos de recolección; es difícil afirmar si los posibles errores están relacionados con fallas en la recolección o si representan b. Mapa de superficie continua: derivado de interla variabilidad espacial del área. polaciones geoestadísticas; y c. Mapa de isolíneas: indica áreas con productividad semejante, dentro de intervalos Creación de mapas de rendimiento predefinidos.

El mapa de rendimiento es una de las princi- Los procedimientos frecuentemente utilizados pales herramientas de la agricultura de precisión, para el mapeo del rendimiento son: pues sirve para representar claramente las áreas homogéneas en términos de productividad y varia- 1. Organización de los datos de rendimiento conbilidad espacial en diferentes partes de un cultivo siderando las coordenadas geográficas (latitud plantado. Para eso, es necesario que la maquina- y longitud) de los lugares en que fueron efecria agrícola utilizada en la cosecha posea un sis- tuados los registros de rendimiento por los tema de registro de datos calibrado de acuerdo sensores instalados en la maquinaria agrícola al cultivo, con capacidad para almacenar datos utilizada en la cosecha. de rendimiento georreferenciados, que permita la A partir de allí, los datos de rendimiento pueden exportación de esos datos a efectos de corregir ser georreferenciados a través de un SIG y reerrores y realizar su procesamiento utilizando SIG. presentados en forma de un mapa de puntos El mapa de rendimiento presenta información (Figuras 1 y 2a). Se debe tener en cuenta que detallada de la producción en distintas áreas del no será posible representar geográficamente campo sembrado y posibilita la integración es- aquellos registros obtenidos en lugares sin sepacial con la variación de otros parámetros que ñal de GPS. Los datos recogidos en cada punpotencialmente influyen en el desarrollo del cultivo to también pueden ser representados mediante plantado. Esto permite diagnosticar y corregir las un mapa en forma de grilla o de cuadrículas, en causas de baja productividad en algunas partes el cual el valor de cada cuadrícula está relaciodel área plantada. El rendimiento también es un nado con el de los puntos situados en la zona indicador de éxito o fracaso de las operaciones de correspondiente a esa cuadrícula (Figura 2b). gerenciamiento o manejo del cultivo, pues resulta de la interacción de los diversos factores que 2. Realización de un análisis de calidad de los dainfluyen en el desarrollo del cultivo. El nivel de ren- tos mapeados para la corrección de errores y dimiento obtenido en cada lugar será importante eliminación de puntos con datos discordantes.

78

### Página 81

Existen diferentes técnicas para identificar valo- Una vez generado el mapa de rendimiento res potencialmente erróneos. Los métodos más (variable continua) se hace posible definir tipos frecuentes para eliminar errores graves consis- de colores y modificar la leyenda de manera ten en la identificación de valores absurdos o ex- de facilitar la comparación de los valores obtremos de rendimiento (nulos, extremadamente servados con otras características mapeadas altos o extremadamente bajos, muy divergentes en la misma área. de los valores registrados en el entorno, etc.),

4. Creación de los mapas de isolíneas a partir de

sin dejar de considerar conjuntamente caraclos de superficie y de los de puntos, en que terísticas que, eventualmente, pueden justificar son previamente definidos los valores de renla ocurrencia de esas divergencias, como por dimiento a ser considerados en cada tipo de ejemplo variaciones de relieve. leyenda (Figura 2d).

3. Someter datos en bruto obtenidos durante

Los métodos de interpolación por el inverso de

la recolección (después de la identificación y

la distancia (I QD) y por ponderación del inverso de

remoción de errores) a un análisis de depenla distancia (IDW) son estándar en la mayoría de dencia espacial a través de la generación de los softwares de SIG disponibles. Se basan en los mapas de superficie mediante la interpolación valores de un número predefinido de puntos cerde datos específicos de rendimiento. De este canos, considerando con mayor peso los puntos modo se obtiene como resultado la represen- más cercanos. La diferencia entre ambos se da tación de la productividad como variable es- en el cálculo de los pesos asignados a los puntos pacialmente continua al considerar datos de cercanos más próximos. puntos cercanos (Figura 2c). Existen diversos El método de interpolación geoestadística, métodos de interpolación que generan mapas también llamado en inglés kriging, se basa en la resultantes diferentes como por ejemplo: el de dependencia espacial de otra variable y, median- “interpolación por el inverso del cuadrado de te un ajuste por regresión, interpola valores para la distancia” (IQD, por su sigla en inglés), el de lugares no medidos con variancia mínima. Así, el “interpolación por ponderación del inverso de análisis geoestadístico está basado en el concepto la distancia (IDW, por su sigla en inglés) y el de variables espacializadas. Los pesos son deterde “interpolación geoestadística por kriging”. minados a partir de un análisis espacial, basado Por lo tanto, el mapa resultante dependerá en el semivariograma, lo que produce un modelo del método de interpolación definido y de los de superficie de las mediciones realizadas con el parámetros adoptados (Figura 3). Cuando sea proceso de kriging.13 posible, el método más adecuado para la representación gráfica de un área puede ser definido a partir de la comparación entre el mapa 13 Detalles sobre el procedimiento para análisis geoestadístico y creación de rendimiento resultante y la variación de las de mapas kriging utilizando Vesper, estarán disponibles a la brevedad en el Manual de geoestadística en el sitio web de la Red de Agricultura de características identificadas a partir de imáge- Precisión de EMBRAPA, a través del siguiente link: nes satelitales o fotografías aéreas (Figura 4). http://www.macroprograma1.cnptia.embrapa.br/redeap2

79 PARTE 2

### Página 82

Figura 2. Formas de representación del rendimiento registrado en un área cultivada con maíz en el Municipio de Sete Lagoas (Minas Gerais, Brasil) en la zafra 1999/2000: a) mapa de puntos, b) mapa de cuadrículas con 10 m de lado, c) mapa de superficie continua derivado de la interpolación utilizando el método IDW, d) mapa de superficie continua con isolíneas cada 2 000 kg/ha (Mapas originales. Fuente de datos: Mantovani et al., 2004)

El mapa producido tendrá las características recolección asociada a una máquina equipada, de las áreas formadas durante el proceso de inter- con otras sin esos equipamientos (Figura 3). polación y servirá de base para la definición de zo- Brandão et al. (2014) compararon los resultanas de manejo. Shiratsuchi y Machado (2003) uti- dos de la aplicación del método de interpolación lizaron los tres métodos citados más arriba para la geoestadística con los obtenidos considerando el creación de mapas, con el inverso de la distancia índice de Green NDVI a partir de una imagen aéy kriging, y demostraron que es posible distanciar rea de la misma área. El modelo de Green NDVI las líneas de recolección de la cosechadora instruindica variaciones en la biomasa de la vegetación mentada en cosechas posteriores en esa misma relacionadas con la concentración de clorofila en área. La utilidad de esto está en poder realizar una las plantas, lo que puede visualizarse en la imagen

80

### Página 83

aérea a través de la variación de la relación entre

las radiaciones verde e infrarroja absorbidas y reflejadas por el dosel del cultivo. De este modo, los autores demostraron que es posible crear zonas de manejo a partir de imágenes del dosel, y que los mapas generados con el método de kriging entre el rendimiento y el de Green NDVI fueron muy similares (Figura 4). Sin embargo, como resaltaron los mismos autores, lo más importante es la observación constante del área de producción y la delimitación de áreas de manejo considerando las variaciones observadas año a año (Brandão et al.

2014), cuando las interferencias provocadas por el

manejo o la aplicación de fertilizantes van alterando las características morfológicas y nutricionales

Figura 3. Mapas representativos de la variación espacial de un área del suelo en el área plantada. experimental: a) mapa de rendimiento obtenido de la cosechadora.

Interpolaciones con espacios de cuatro pasadas de la máquina; b) por el inverso de la distancia sin promedio de los puntos centrales; c) por kriging sin promedio; d) por kriging con promedio. Fuente: adaptado de Shiratsuchi & Machado (2003) Herramientas para la identificación y el mapeo de zonas de manejo La zona de manejo se define como la subregión del campo que presenta una combinación de factores limitantes de la productividad y de la calidad para la cual se puede aplicar una dosis uniforme de insumos (Doerge, 2013). Uno de los principales problemas de la agricultura de precisión es la necesidad de un muestreo en grillas denso a fin de detectar la variabilidad espacial del atributo a evaluar. Así, la creación de zonas de manejo (ZM) posibilita la creación de mapas que representen – de la manera más próxima a la realidad– el área del cultivo estudiado.

La aplicación en campo de técnicas de agriFigura 4. Utilización del programa Vesper para la obtención de cultura de precisión se facilita con la generación mapas kriging para: a) Green NDVI y b) Productividad mecanizada, recopilados en cultivo comercial de algodón en la Fazenda Pamplona de zonas de manejo, ya que se pueden utilizar / GO, en la zafra 2011. Fuente: adaptado de Brandão et al. (2014) los mismos sistemas de la agricultura convencional para el manejo de los cultivos dentro de una misma zona de manejo. Así, todos los factores

81 PARTE 2

### Página 84

que afectan el rendimiento del cultivo deben dis- los datos sobre la variación espacio-temporal del ponerse en una única base, que incluya factores rendimiento del maíz en 1999-2000, 2000-2001 y cuantitativos estables (como por ejemplo: tipos de 2001-2002, características físicas y químicas del suelo y topografía) y dinámicos (como por ejemplo: suelo (conductividad eléctrica, pH en agua, calcio, la aparición de plantas dañinas, estado nutricional magnesio, fósforo, potasio, saturación de alumidel cultivo en la última zafra, etc.). nio, materia orgánica, saturación de bases, humeEl uso de esta fuente de conocimiento permite dad) y aspectos de relieve. identificar diferentes zonas de manejo de acuer- Al interpretar un mapa de rendimiento a fin de do con el historial de producción, lo cual permitirá realizar un futuro gerenciamiento del campo se detambién identificar los parámetros más relevantes ben tener en cuenta, principalmente, las causas para diagnosticar y corregir las causas de baja o persistentes de variabilidad. La correcta generade menor productividad en determinadas áreas ción e interpretación de datos referentes a la vadel cultivo plantado (Figura 5). Esta constatación riabilidad espacial de los cultivos es la etapa más es fundamental cuando las diferencias en los nive- importante del proceso de implementación de la les de nutrientes del suelo coinciden con variacio- agricultura de precisión. nes de rendimiento del cultivo analizado.

Para la delimitación de zonas de manejo han

sido utilizadas técnicas de análisis estadístico de

agrupamiento de datos para posibilitar la identificación de la variabilidad de los diversos factores que afectan el desarrollo del cultivo estudiado.

Esas técnicas pueden clasificarse en dos métodos

principales: jerárquico y de particionamiento.

Los métodos jerárquicos producen una secuencia anidada de clusters, estableciendo una jerarquía entre los clusters de conjuntos de datos, de acuerdo a sus similitudes. Los métodos de particionamiento posibilitan el uso de un conjunto de atributos directamente relacionados con la variabilidad nutricional del área en estudio. Entre los métodos de agrupamiento utilizados más frecuentemente para la definición de zonas de manejo se encuentran: K-Means y Fuzzy C-Means (Taylor et al., 2007; Santos et al., 2003; Yan et al., 2007). En el ejemplo representado en la Figura 5, las zonas de manejo fueron generadas a partir del análisis de componentes principales (PCA), a partir de

82

### Página 85

Figura 5. Mapeo de zonas de manejo en un área cultivada con maíz en el Municipio de Sete Lagoas (Minas Gerais, Brasil). En este ejemplo están representados espacialmente los datos principales que aportarán para la definición de las zonas de manejo: a) mapas de rendimiento, b) características del suelo y c) zonas de manejo generadas (Mapas originales. Fuente de datos: Mantovani et al., 2004)

83 PARTE 2

### Página 86

2.2. Uso de la geoestadística y los demostró que las varianzas observadas solo podían tener sentido si se consideraba la distancia sistemas de información geográfica entre muestras. Matheron (1963), basándose en en agricultura estas observaciones, desarrolló la teoría de las vaDario E. Fernández y Manel Ribes i Dasi riables regionalizadas, que contiene los principios fundacionales de la geoestadística.

Dario E. Fernández Aplicada esta teoría a las ciencias agronómiINTA Alto Valle, Río Negro, ARGENTINA cas, la geoestadística considera cada valor muesfernandez.dario@inta.gob.ar tral (variable aleatoria z) asociado a una posición (coordenadas x,y) y se vale de esta misma depenManel Ribes i Dasi dencia para hacer inferencias sobre la distribución UdL, Departament de Producció Vegetal i Ciència Forestal, de los datos, lo que ha permitido resolver el proCatalunya, ESPAÑA. blema de dependencia espacial que compromete manelo@eagrof.udl.cat el cálculo de ciertos índices de distribución que no consideran la ubicación espacial de las muestras y generalmente dependen fuertemente de su La geoestadística es una metodología utilizada tamaño. para la evaluación de recursos, a la que se ha recu- En forma sintética se puede afirmar que, harrido por más de cuarenta años en las compañías ciendo uso de la dependencia espacial que tiemineras. Su aplicación a las ciencias biológicas es nen los datos de una muestra, la geoestadística más reciente y se basa fundamentalmente en que emplea un algoritmo para cuantificar una variable en general, los datos colectados en puntos cerca- dada, en lugares no muestreados. Luego, la desnos tienden a ser más similares que los colectados cripción de la distribución espacial de esa variable a mayor distancia. Este hecho lleva a considerar se realiza mediante el uso de mapas con datos un modelo de variación espacial que contiene al interpolados, unidos por isolíneas. menos tres componentes: una estructura general, que puede ser definida como una tendencia; una El método de interpolación más comúnmente segunda estructura superimpuesta, relacionada utilizado es el de la distancia inversa ponderada con la correlación espacial y con una variación gra- (DIP o IDW por su sigla en inglés), debido a la sendual y, finalmente; un tercer componente que con- cillez de los cálculos. Sin embargo, la técnica de siste en una variación al azar causada por errores kriging ordinario (KO) ha probado su utilidad y vende muestreo o variaciones espaciales a escalas taja sobre la mayoría de los métodos de interpomenores que la red de muestras. lación, las cuales derivan de la capacidad de este El desarrollo de la geoestadística comienza a método para proveer el mejor estimador no sespartir de la labor de D. G. Krige en 1951, quien gado. Este método de interpolación se denomina trabajando con datos de concentraciones de oro, kriging, en honor a D.G. Krige.

84

### Página 87

Caso práctico de uso de la geoestadística de ese daño en algunos cultivos forestales y más para el monitoreo de plagas en cultivos frecuentemente en bosques naturales. agrícolas En los cultivos agrícolas utilizados para la proLa necesidad de determinar la densidad pobla- ducción de alimentos, ya sean para consumo frescional de las plagas mediante métodos sencillos, co o procesado, ésta metodología de monitoreo rápidos, fiables y económicos, ha sido siempre de plagas (fotografía espectral, térmica, etc.) no ha uno de los objetivos perseguidos en el manejo in- tenido hasta el momento un desarrollo que permita tegrado de plagas. su utilización en forma práctica.

Para desarrollar una táctica adecuada para el Por tanto, para el desarrollo de un sistema de control de una plaga es necesario, en primer lu- monitoreo económico y eficaz, se deben utilizar gar, conocer el riesgo potencial (daño económico) herramientas que permitan hacer una estimación que una determinada población puede causar al indirecta de las densidades poblacionales (métocultivo y, además, establecer puntos de referencia do de monitoreo relativo) y a partir de unas pocas biológica para predecir ciertos eventos de su ciclo muestras, realizar inferencias sobre el potencial de de vida. daño económico de las plagas.

La relación entre la densidad de una plaga y el Es aquí donde dos herramientas desarrolladas daño que produce, constituye la base del mane- en forma independiente pueden ser usadas en jo integrado de plagas. Esta problemática ha sido conjunto para simplificar tanto el monitoreo como abordada con el desarrollo de métodos de moni- el proceso de toma de decisión en el contexto del toreo absolutos (por ejemplo número de individuos manejo integrado de plagas: la geoestadística y por m2), relativos (por ejemplo, número de indivi- los SIG. duos por trampa) o mediante índices de población (por ejemplo, porcentaje de plantas dañadas). Distribución espacial de los insectos Las tareas de monitoreo necesarias para la El estudio de la dispersión de una población y detección temprana de una plaga –antes de que sus patrones de distribución tiene gran relevancia alcance el nivel de daño económico– requieren de ecológica. Esta información es útil para determinar una adecuada capacitación de los productores y/u los métodos de análisis de los datos, estimar el operarios y consumen excesivo tiempo y esfuerzo. tamaño de la población, evaluar los programas de Esta actividad, por tanto, tiene un elevado costo monitoreo y hacer inferencias sobre la condición de implementación. de la población.

La incorporación en los últimos años de dife- A través del tiempo, han sido propuestos diferentes herramientas de la agricultura de precisión, rentes modelos de distribución para ajustar a dacomo la fotografía aérea o las imágenes satelitales, tos ecológicos. Como modelo teórico se ha sugesolo ha servido para la evaluación de los daños rido la distribución Poisson, en la que se considera causados por las plagas o, en el mejor de los ca- que cada individuo se comporta en forma indesos, para el desarrollo de modelos de predicción pendiente de los demás y que la probabilidad de

85 PARTE 2

### Página 88

encontrar a un individuo en una muestra es la mis- o tres dimensiones que describe la distribución ma para todas las muestras. Esta situación rara espacial de la plaga estudiada. Este análisis puevez se da en la naturaleza, ya que normalmente de proveer información crucial para mejorar el uso los individuos se relacionan con otros de su misma de técnicas sustentables de control de plagas o especie, con otras especies y también interactúan de programas de monitoreo, particularmente en con el ambiente. Por tanto, existe una desviación el contexto del manejo integrado de plagas de de la distribución de una población real, respecto precisión. de la ideal de Poisson. A partir de la década de 1990, la geoestadístiSin embargo, las distribuciones probabilísticas ca ha sido utilizada por diversos investigadores en (por ejemplo Poisson) que permiten calcular me- el desarrollo de programas de monitoreo y control didas de agregación de los individuos, tienen un de varias plagas, tanto de lepidópteros, coleóptelimitado valor para hacer inferencias sobre la es- ros, áfidos y otros insectos, como así también para tructura espacial de los datos. Para esto es nece- realizar mapas de isolíneas de otros aspectos relesario utilizar otros métodos que permitan evaluar la vantes de los cultivos y suelos agrícolas. correlación espacial de los insectos. Debido a que Estos estudios pueden realizarse a escala parestos métodos son difíciles de interpretar, diferencelaria o a una escala mayor. A escala de la partes autores proponen que es necesario redefinir el cela, conocer la distribución espacial de la plaga objetivo del monitoreo hacia el concepto de “mapear” la población en vez de estimar o categorizar permite optimizar la toma de decisiones para su la media, aún a costa de resignar cierta robustez control; a media-gran escala, permite también plaen el cálculo. nificar su muestreo, definir los puntos de muestreo y tomar decisiones en la aplicación de programas La rápida visualización y sencillez de interpretaregionales de control y seguimiento. ción que proporciona un mapa, difícilmente pueda ser superada por ningún índice o dato calculado El objetivo del muestreo de individuos o datos por otros medios. Sin embargo, como se men- discrecionales debe ser redefinido en el sentido de cionó previamente, no es posible fotografiar una “mapear” las poblaciones, al considerar que este población de insectos para describir su disper- enfoque puede reducir notablemente el uso de sión. En cambio, sí se pueden colectar muestras agroquímicos en programas de manejo integrado puntuales y transformar éstas en mapas de iso- de plagas de precisión, en comparación con los líneas con iguales densidades mediante técnicas programas de control tradicionales. de interpolación. El desarrollo del análisis espacial de las poblaLa geoestadística, por su parte, permite resol- ciones de insectos en la Entomología Aplicada, ha ver dos de las principales limitantes de los índices abierto nuevas posibilidades para el estudio y el de dispersión: la dependencia espacial que com- manejo de plagas que, al ser complementado por prometía el cálculo de éstos y además, mediante los SIG, permite el manejo de gran cantidad de dael kriging, permite la generación de datos en zo- tos de manera rápida, sencilla y visualmente muy nas no muestreadas, y producir un mapa en dos práctica.

86

### Página 89

Sistemas de Información Geográfica grafía (pendiente, altitud) en la distribución espacial Los SIG se basan en la utilización de un recep- de la variable. tor de señales satelitales o GPS que permite ubicar Por otra parte, los programas de diseño (por un punto en el espacio en tres dimensiones (longi- ejemplo CAD) poseen una interfase muy sencilla tud, latitud y altura) y de un programa de ordena- con Google Earth, lo que posibilita trabajar desde dor (ArcGis, MapInfo, Geomatics, gvSIG, Q-GIS, el escritorio de la computadora e interrelacionar etc.) que relaciona los datos colectados por el re- esta información con las imágenes del terreno. ceptor GPS, con otros datos de interés. Los SIG, Otros programas como gvSIG y Quantum-GIS por tanto, permiten compilar y manipular una gran están desarrollados en base a software libre, son cantidad de datos espacialmente referenciados de uso gratuito y poseen todas las herramientas (ver mayor detalle en el capítulo 1.2). necesarias para dar un tratamiento integral a los mapas y otros datos relevantes que se quiera Como dato práctico, es muy importante conoanalizar. cer perfectamente el sistema de coordenadas (x,y) de referencia y su unidad de medida. Debido a su En términos generales, se puede concluir que sencillez de cálculo e interpretación se recomien- en la actualidad se dispone de una extensa lista da el uso del sistema UTM ya que se expresa en de programas para el uso de la cartografía digital, lo que permite trabajar con diferentes formatos y metros. Además, cuando se superponen mapas sistemas referenciales, que en la mayoría de los en un SIG, éstos deben tener el mismo sistema casos son compatibles entre sí. de referencia para poder hacer comparaciones y relacionar las capas de datos. En este marco, se presenta como una alternativa válida para programas de grandes áreas, en los Una manera sencilla de mostrar los mapas de que el análisis geoestadístico y su integración en distribución de plagas es su incorporación al pro- los SIG, son complementos necesarios. Se asume grama gratuito Google Earth. Si bien este software que la aplicación de esta metodología permitirá un no constituye un SIG propiamente dicho, permite manejo más eficiente de la gran cantidad de datos la superposición de los mapas en distintos forma- generados en estos programas y una mejora del tos (el más común *.jpg) con imágenes satelitales proceso de toma de decisiones. del terreno y posee además, algunas herramientas rudimentarias de marcación y medición, que son muy sencillas y útiles. Metodología práctica para el análisis Un aspecto interesante que permite analizar geoestadístico y su integración a un SIG el programa Google Earth está relacionado con • Paso 1. Realizar la colecta de datos georrefela posibilidad de superponer una imagen (*.jpg) renciados y su ordenamiento en una planilla de plana, añadiendo el efecto 3D del terreno (Figura cálculo en columnas ajustadas (x,y,z).

3). Esta herramienta ayuda a interpretar algunas • Paso 2. Efectuar un primer análisis estadístico propiedades que pudieran estar ocultas o poco vi- básico, obteniendo la media, la varianza, dessibles, como por ejemplo, la influencia de la topo- viación estándar, etc.

87 PARTE 2

### Página 90

• Paso 3. Realizar una prueba de normalidad de pepita) y el menor valor de la sumatoria de los los datos. En caso de no ser normales, se pro- residuos al cuadrado (RSS). cede a transformarlos. Se recomienda utilizar

• Paso 10. Realizar el kriging ordinario (KO). Se

la función logarítmica. Como regla general se recomienda el kriging puntual ya que el kriging asume que si la desviación estándar es mayor en bloques tiende a dar mapas más suavizados. que la media, se deben transformar los datos.

• Paso 11. Luego del kriging se debe realizar la

• Paso 4. Realizar la transformación inversa de validación cruzada, que consiste en dejar fuera los datos para el posterior proceso de kriging y del kriging un valor por vez y estimarlo con el obtención del mapa. resto de los valores vecinos.

• Paso 5. Detectar la presencia de posibles va- • Paso 12. Se analizan los valores de z (reales) lores atípicos (outliers). Éstos pueden ser dis- y z* (estimados), esperando que el valor medio tribucionales (cuando se alejan del valor medio de z-z* sea cercano a cero y que la varianza de la muestra), o espaciales (cuando son muy normalizada de la diferencia esté próxima a la diferentes del valor de sus vecinos). Se deben unidad. revisar, corregir y en última instancia, remover.

• Paso 13. Con los valores z, apareados a las

• Paso 6. Cuando se tienen suficientes datos coordenadas (x,y) se construye el mapa de iso- (más de 500 o 1 000 puntos) se puede analizar líneas (Figura 2). la anisotropía (análisis de tendencia), es decir,

• Paso 14. Incorporar el mapa obtenido a un

evaluar si existe una mayor correlación en alguSIG. El mapa puede exportarse como una imana dirección en particular. Si no existe evidencia gen o utilizar los datos generados a partir del de anisotropía, o se cuenta con pocos datos, kriging (x,y,z*), para generar el mapa en el prose continúa con el análisis omnidireccional. grama de SIG seleccionado.

• Paso 7. Construcción del variograma (Figura 1).

Dependiendo del software utilizado, se acepta

el modelo obtenido por defecto o, si el programa lo permite, posteriormente se puede realizar un ajuste manual (prueba y error) intentando minimizar la suma de residuos al cuadrado (RSS).

• Paso 8. Chequear que el modelo ajustado

tenga al menos 15 intervalos de distancia y no

menos de 30-50 pares de datos por intervalo.

• Paso 9. Seleccionar el modelo que presenta el

menor valor de k (relación entre la meseta y la

88

### Página 91

Figura 1. Semivariograma construido con datos de capturas anuales de Cydia pomonella en 760 trampas distribuidas en 65 km2. Ajuste de un modelo esférico con 43 intervalos de distancia

Figura 2. Mapa de iso-capturas de Cydia pomonella obtenido mediante el análisis geoestadístico, que muestra áreas con diferentes umbrales de insectos acumulados

89 PARTE 2

### Página 92

Figura 3. Ajuste del mapa de iso-capturas de insectos a la altimetría del terreno, utilizando el programa Google Earth™

Difusión de información agronómico de interés, etc. En los últimos años se

Uno de los mayores problemas que enfrenta observa más frecuentemente la incorporación de la implementación de un programa de colecta y los SIG en sistemas más complejos de soportes difusión de información es el establecimiento de de decisiones (SSD por su sigla en inglés) donde un efectivo sistema de comunicación con los par- se incluyen también datos geofísicos, políticos, soticipantes y/o interesados. En general, los produc- ciales, económicos y de manejo del hábitat. tores, monitoreadores, asistentes y profesionales, En la actualidad las tecnologías de información reciben información de diferentes fuentes como y comunicación (TIC) están teniendo un desarroservicios de extensión públicos y privados, com- llo muy acelerado y es cada vez más frecuente el pañías de servicios, etc., pero es difícil obtener acceso a Internet y el uso de teléfonos celulares información en tiempo real de diferentes variables inteligentes. Estas herramientas pueden ser aproproductivas en el área de influencia de las parcelas vechadas con un costo muy bajo, para poner a de interés o incluso de toda la región. disposición de los usuarios información en tiempo En este contexto es posible implementar un real de la situación productiva de un determinado sistema de vigilancia y monitoreo a nivel regional territorio o área de influencia. que sirva de alerta rápida en casos de detectarse Por tanto, se propone un sistema de vigilancia la presencia de alguna plaga específica, un dato y monitoreo que consta de tres etapas específicas:

90

### Página 93

1. Colecta de datos en el campo mediante mo- 2.3. Interpretación de

nitoreo directo, trampeo, etc. y transmisión de

esos datos a un centro de cómputo. informaciones espacializadas y

definición de unidades de manejo

2. Análisis de los datos mediante el uso de la Ricardo Melchiori, Alejandra Kemerer y Susana geoestadística y confección de los mapas de Albarenque. distribución o de riesgo para la generación de un SIG regional, mediante la superposición de daMelchiori, Ricardo J. M. tos catastrales, ubicación de sitios de muestreo, Grupo Recursos Naturales y Factores Abióticos mapas de isolíneas, imágenes satelitales, etc.

Estación Experimental Agropecuaria Paraná del INTA,

3. Publicación de los mapas en un sitio web ac- Argentina

cesible y de rápida visualización por parte de melchiori.ricardo@inta.gob.ar

los decisores.

Kemerer, Alejandra C.

En definitiva, lo que se pretende con estas he- Grupo Recursos Naturales y Factores Abióticos rramientas es reducir el impacto negativo de la Estación Experimental Agropecuaria Paraná del INTA ocurrencia de ciertos fenómenos que afectan la Argentina producción agrícola, mediante la generación de in- kemerer.alejandra@inta.gob.ar formación que sea útil tanto a los productores, técnicos, profesionales, como a los decisores políticos, Albarenque, Susana M. y así reducir los tiempos de acción y los recursos Grupo Recursos Naturales y Factores Abióticos Estación Experimental Agropecuaria Paraná del INTA, involucrados en las tareas de mitigación.

Argentina

albarenque.susana@inta.gob.ar

Introducción

El estudio de la variabilidad espacial de las propiedades del suelo, la productividad del cultivo o de índices de vegetación derivados de imágenes satelitales permite agrupar áreas de características similares dentro de los lotes de producción. Estas áreas diferenciadas constituyen zonas de manejo donde la combinación de los factores responsables de la variación del rendimiento del cultivo permite adecuar las prácticas de cultivo (Doerge, 1999), como por ejemplo la fertilización o la densidad de siembra.

91 PARTE 2

### Página 94

El reconocimiento de la variabilidad espacial es- Dosis de fertilización (kg N/ha) = (DNZ– NdZ)/EUN tableciendo manejos diferentes entre zonas, permite optimizar el uso de los insumos de acuerdo a Donde: las necesidades del cultivo y así mejorar el beneDNZ = demanda de nitrógeno estimada según ficio económico y disminuir el impacto ambiental.

La posibilidad de ajuste del manejo de los cultivos rendimiento esperado por zona y el requeripor zonas requiere la existencia de diferencias de miento de N (valor de tabla) productividad entre ellas. Habitualmente las va- NdZ= Nitrógeno disponible por zona riaciones en la productividad están asociadas a diferencias en las propiedades físicas y químicas EUN= eficiencia de uso del nitrógeno del suelo y la topografía. Estas diferencias afectan la disponibilidad de recursos entre zonas, lo que puede considerarse al ajustar las prácticas de manejo de los cultivos.

Tabla 1. Requerimientos nutricionales de los cultivos de

trigo, maíz, soja, girasol y alfalfa (adaptado de IPNI) Criterios para el manejo de la fertilización Requerimiento (kg/tn grano) por zonas Cultivo N P K S Maiz 22 4 19 4 Nitrógeno La delimitación de zonas permite estimar las va- Trigo 30 5 19 4.5 riaciones en la demanda de nutrientes de los culti- Soja 80 8 33 7 vos de acuerdo con su productividad. El ajuste de Girasol 40 5 28 11 la fertilización por zonas puede resolverse mediante el empleo de un balance simplificado. Este puede Alfalfa 27 2.5 21 3.5 estimarse utilizando la información existente –como la que ha compilado el International Plant Nutrition Otra alternativa para el cálculo de la dosis de Institute (IPNI) (Tabla 1)– sobre los requerimientos nutricionales de diferentes cultivos, la determina- fertilización nitrogenada por zonas es utilizar nición de la disponibilidad de nitrógeno (Nd = N a la veles críticos de nitrógeno, determinados para siembra + mineralización) y la eficiencia de uso del productividades diferentes. El nivel crítico (NC) renitrógeno (EUN = 50%). La disponibilidad de nitró- presenta la cantidad de nutriente que no limita el geno contempla la determinación del nitrógeno a rendimiento del cultivo. Este método considera la la siembra y una estimación de mineralización que disponibilidad del nutriente en el suelo mediante puede estimarse de manera aproximada como muestreos dirigidos por zonas y el NC acorde a la un porcentaje del contenido de nitrógeno total del productividad media de las zonas consideradas, y suelo (Nt) (valores que oscilan entre 1.5 a 5 %, se- estima la dosis como la diferencia entre el NC y el gún la textura del suelo) (Figura 1). nitrógeno disponible en el suelo (Figura 1).

92

### Página 95

Figura 1. Alternativas de recomendaciones de fertilización nitrogenada según zonas de manejo utilizando un balance simplificado o nivel crítico según productividad

El cálculo de las recomendaciones de fertiliza- Fósforo

ción nitrogenada puede realizarse empleando la En el manejo de la fertilización fosfatada por siguiente relación: zonas pueden emplearse dos criterios para el cálculo de la dosis de fertilización. En un caso la doDosis de fertilización (kg N/ha) = NCnz – Ndz sis de fósforo (P) puede calcularse en función de la extracción de fósforo en los granos del cultivo Donde: anterior y en otro considerando el nivel de fósforo NCZ=Nivel crítico de N determinado para cada disponible en el suelo, un nivel crítico y un modelo zona de acuerdo con su productividad de recomendación (Figura 2).

NdZ=Nitrógeno disponible en el suelo a la siem- En el primer caso, la dosis de fertilización fosbra del cultivo, determinado para cada zona fatada por zonas se calcula como la extracción de

93 PARTE 2

### Página 96

Figura 2. Alternativas de recomendación de fertilización fosfatada según zonas de manejo considerando la extracción de fósforo en los granos del cultivo anterior y considerando el nivel de fósforo disponible en el suelo, nivel crítico y un modelo de recomendación

fósforo por el cultivo anterior empleando el rendi- En el segundo caso se requiere conocer: el nivel miento medio por zonas y el requerimiento de fós- de disponibilidad de fósforo en el suelo mediante foro según el cultivo (Tabla 1) y (Figura 2). muestreos por zonas, un nivel crítico de referencia y un modelo de recomendación de dosis. Como Dosis de fertilización (kg P/ha) = RMz * Rpz modelo de recomendación pueden utilizarse alternativas locales disponibles, como por ejemplo la Donde: del cálculo de dosis considerando el nivel crítico RMz = rendimiento medio del cultivo anterior de fósforo, la disponibilidad de fósforo en el suelo y por zona la dosis equivalente de fósforo. La dosis equivalenRPZ = requerimiento de P (valor de tabla) te de fósforo (DEP) es la cantidad de fósforo de fer-

94

### Página 97

tilizante a agregar para elevar en 1 parte por millón V2z = porcentaje de saturación de bases a al- (ppm) el contenido de fósforo disponible en el sue- canzar con el uso de enmiendas (normalmente lo (este valor puede determinarse en laboratorio o se pretende alcanzar un nivel de saturación con a campo) (Figura 2). La DEP puede variar entre 2 bases de al menos un 80 %) y 6 kgP/ppm (Benavidez et al., 2000) y depende principalmente de la textura y de la composición química del suelo, entre otros factores. Tabla 2. Cálculo de la necesidad de encalado (CO3Ca) por zona en función de la capacidad de intercambio catiónico (CIC) y del porcentaje de saturación con bases (V1 y V2).

Dosis recomendada (kg P/ha)= (NCp – Pdz) * DEP

Necesidad

CIC V1 V2

Donde: Zona de encalado

(meq/100g) (%) (%) (tn/ha) NCp= nivel crítico de P

Zona 1 12 40 80 4.8

Pdz= fósforo disponible en el suelo por zonas

Zona 2 18 52 80 5.0

DEP= dosis equivalente de P

Zona 3 22 70 80 2.2

Enmiendas

La delimitación de zonas permite, al igual que Criterios de manejo de la estructura del para la fertilización de los cultivos, estimar las ne- cultivo por zonas cesidades de enmiendas, como por ejemplo el encalado. El cálculo de las dosis puede resolver- De manera similar a lo planteado para el ajuste se mediante el empleo de modelos de corrección de las prácticas de fertilización de acuerdo con las disponibles que determinen las variables intervi- variaciones en la productividad, es factible y convenientes dentro de cada zona de interés. niente realizar ajustes de las variables que modifican la estructura del cultivo, como el espaciamiento Un modelo factible de emplear se basa en la entre surcos y la densidad de siembra. Los cultivos determinación de la capacidad de intercambio expresan diferentes respuestas a cambios en escatiónico y del porcentaje de saturación de bases paciamiento y densidad, comúnmente asociadas por zona medida en el campo (actual) y el pora las distintas tolerancias a estreses que limitan el centaje de saturación a alcanzar con la enmienda crecimiento durante el período crítico y reducen el (Gambaudo y Micheloud, 2008). rendimiento. La sensibilidad a cambios en la densiNecesidad de encalado (tn/ha) = CIC*(V2z-V1z)/100 dad es decreciente para maíz, girasol, trigo y soja.

El cultivo de maíz es el más sensible a los camDonde: bios en la densidad de siembra cuando factores CIC= capacidad de intercambio catiónico como la disponibilidad hídrica y/o la disponibilidad de V1z = porcentaje de saturación de bases ac- nutrientes limitan el crecimiento. Esto significa que la tual del suelo obtenida por la relación: suma de densidad óptima de siembra se incrementa en funbases*100/CIC ción de la calidad de la zona de manejo (Figura 3).

95 PARTE 2

### Página 98

La validación de las recomendaciones o la generación de nuevas técnicas pueden realizarse mediante ensayos en franjas, una práctica sencilla cuando se dispone de herramientas de agricultura de precisión y los experimentos son adecuadamente planificados.

Para la realización de la validación de prácticas

de manejo por zonas se deben tener en cuenta

aspectos como ubicación y dimensiones de los

tratamientos, condiciones de cosecha del ensayo

y procesamiento de los datos de rendimiento.

Con respecto a la ubicación y dimensiones de

los tratamientos se recomienda orientar las franjas

de manera que incluyan áreas de las distintas zonas de manejo del lote. La longitud de estas debe permitir un suficiente número de datos de rendimiento y su ancho debe exceder el ancho del caFigura 3. Esquema de la respuesta en rendimiento del cultivo de maíz bezal de cosecha. Es prioritaria la calibración del a cambios en la densidad de siembra para zonas de productividad baja (Zona 1), media (Zona 2) y alta (Zona 3) (Adaptado de Kruk y monitor de rendimiento en el lote previo a la coseSatorre, 2003) cha de ensayos y la adecuada identificación de las franjas evaluadas en el mapa de rendimiento. Así mismo, el mapa de rendimiento debe ser aconEl cultivo de soja es menos sensible debido a dicionado como se detalla en el apartado 2.1 de su gran plasticidad. Sin embargo, en condiciones este manual (Creación de mapas de manejo con de crecimiento limitantes normalmente expresa datos espaciales). cambios favorables en rendimiento ante disminuciones del espaciamiento entre hileras, y así compensa caídas en el rendimiento.

Consideraciones generales para el ajuste

de las prácticas de manejo por zonas

La respuesta de los cultivos varía de forma sitio-específico, por lo que se requiere validar los esquemas o las propuestas de recomendación de manera local. Para esto es conveniente realizar experimentos a campo utilizando las herramientas de la agricultura de precisión.

96

### Página 99

2.4. Aspectos económicos: análisis al balance, más que por la reducción de costos en áreas potencialmente cultivables. de viabilidad de adopción de Más allá de los beneficios agronómicos asointervenciones en los sistemas de ciados a los gastos de producción y cultivo, la producción agricultura de precisión mejora el resultado final Marc Vanacht por el uso intensivo que da a los bienes agrícolas (equipamiento, almacenamiento, transporte). Por ejemplo, durante la temporada de cultivo 2013 en Marc Vanacht el Medio Oeste de Estados Unidos las fechas de Consultor de Estratégia de Empresas plantación fueron postergadas por el frío y la huGraduado de la Universidad de Leuven, Bélgica (Economia, medad de la zona. Cuando finalmente las condiBusiness Administration, Ley) ciones fueron aceptables, la mayoría de los granos marc@van8.com de maíz y soja fueron plantados en dos semanas, marcvan8@me.com rendimiento nunca antes logrado. Sin los tractores equipados con dirección automática trabajando día y noche, a alta velocidad y eficiencia, no hubieIntroducción ra sido posible. La agricultura de precisión salvó el cultivo 2013.

Como en todas las decisiones de inversión, el

agricultor desea calcular por adelantado cuánto se Hay otros aspectos donde la agricultura de beneficiará su actividad agrícola con la adopción precisión contribuye a la rentabilidad. Da acceso de la agricultura de precisión. La mayoría de los a dinero (préstamos) y minimiza riesgos (seguros) costos de inversión en hardware, sistemas y per- más fácilmente, y daría acceso preferencial (o exclusivo) a los clientes corrientes, en comparación sonal son conocidos previamente. El rendimiento con los que no adoptan la agricultura de precisión. es a veces más difícil de calcular o de estimar. La experiencia en países que adoptaron la agricultura de precisión hace muchos años muestra que Conceptos básicos generalmente se paga por sí misma, a veces muy Es útil abordar algunos conceptos básicos de rápido en la misma temporada, a veces extendida contabilidad y análisis financiero antes de analizar después de varios años de uso. los específicos de la agricultura de precisión.

Lleva tiempo entender completamente los be- Costos fijos versus costos variables: Los neficios de la agricultura de precisión. Inicialmente costos variables (a menudo fungibles) pueden fála mirada se focalizó en ahorrar en insumos tales cilmente ser asignados a la superficie del cultivo o como fertilizantes, al mejorar el objetivo de la apli- a las cabezas de animales. Ejemplos: fertilizantes, cación. Esta visión puede ser un tanto reducida. químicos, semillas, licencias de biotecnología, etc.

La cosecha aumenta al aumentar los niveles de (o alimentación, farmacia veterinaria). Los costos insumos en lugares adecuados que agregan más fijos (usualmente bienes de capital) son adquiri-

97 PARTE 2

### Página 100

dos en una sola operación de compra y asigna- navegación de precisión o la dirección automátidos a una superficie de unidad animal usando una ca permiten de 22 a 24 horas de trabajo al día. división basada en amortizaciones anuales de la Las operaciones normales están limitadas por la inversión. Ejemplos: tractores, rociadores, cose- luz solar (8 a 16 horas por día dependiendo de la chadoras, etc. La agricultura de precisión a me- estación y la latitud). Duplicar el trabajo por día por nudo supone el uso de costos fijos (equipos de máquina tendría un impacto positivo y reduciría los navegación, muestreo de suelo, computadoras y costos por unidad a la mitad. A menudo los besoftwares) para mejorar la eficacia en los costos neficios operacionales sobrepasan el valor de los de producción. beneficios agronómicos.

Agronomía versus operaciones: Los costos Cálculos de costos: para comparar los difede los cultivos agrícolas (semillas, fertilizantes, quí- rentes tipos de costos, los agricultores utilizan un micos, más o menos agronomía) apuntan al creci- criterio común, usualmente el costo por hectárea. miento rentable del cultivo por el que los ingresos Esto es fácil para bienes fungibles (tasa x costo de (ventas de toneladas de lo producido por precio unidad) pero puede ser más difícil para bienes de del mercado) son más altos que el costo del incre- inversión (amortización anual dividida por el númemento del cultivo. Esto puede parecer obvio, pero ro de hectáreas, más bienes fungibles y costo del se vuelve difícil cuando los precios de los granos personal). Los cálculos de costo por hectárea son son menores como resultado de una sobre ofer- útiles; muestran por ejemplo que para las coseta. La agricultura de precisión sirve para mejorar chas de manzanas en el estado de Washington en el uso de insumos, tanto al reducir costos como Estados Unidos el 70% del total de costos consisal mejorar los rendimientos por unidad de tierra. te en la mano de obra necesaria para su recolecAmbas estrategias (reducir costos, mejorar la ga- ción y que para el maíz en Illinois el mayor costo nancia) son válidas. En la mayoría de los casos, es la tierra. la agricultura de precisión trabaja en ambos as- La agricultura de precisión a menudo apunta a pectos, al optimizar los costos y obtener efectos acrecentar los rendimientos, los agricultores han positivos en los rendimientos. comenzado a usar una nueva regla para calcular Para emplear todos los insumos y lograr elevar el efecto del costo de la agricultura de precisión y el volumen de cosecha en los silos, los agricultores su rentabilidad: costo por tonelada producida. Esta manejan inteligentemente todo tipo de operacio- aproximación tiende a estar más enfocada en la nes, desde la preparación de la tierra, la aplicación rentabilidad que en los costos; permite altos costos de diferentes insumos, la cosecha en los campos, en situaciones de cosechas altas y promete costos el transporte desde el campo hacia el lugar de reducidos en situaciones de cosechas bajas. almacenamiento inicial o procesamiento. Todas Es ideal que se calcule la producción neta: por estas operaciones requieren dinero, tanto en per- ejemplo toneladas de azúcar, no toneladas de sonal o, en muchos casos, en costos asociados materia verde; o jugo en lugar de fruta; o el grano con equipamiento y aquí es donde la agricultura seco en el elevador de la cosechadora en vez del de precisión puede hacer una gran diferencia. La grano verde en el campo.

98

### Página 101

Bienes reales de Operaciones Transformación,

capital: Variable insumos: agrícolas: marketing, ventas,

Tierra, plantaciones, Alimentación y farmacia, Equipamiento,

confinamiento de los animales, semillas y biotecnología, contratación, distribución, líneas ferroviarias, elevadores, químicos, fertilizantes. transporte. trazabilidad. terminales, depósitos, etc.

Figura 1. Servicios financieros: Riesgo de gestión, créditos de temporada e inversión de capital. Fuente: elaboración propia

Efectos internos versus relaciones exter- Se pueden identificar los diferentes líderes del nas: Más allá de los beneficios internos (agrono- mercado en cada uno de los cuadros de esta camía y operaciones) la agricultura de precisión a dena de valor. Es el talentoso trabajo de cada agrimenudo mejora la posición de negociación del cultor lo que hace que estos seis cuadros trabajen agricultor con actores externos. juntos de forma rentable. La tecnología de la agriPara los servicios financieros, los datos acu- cultura de precisión puede contribuir a la rentabimulados a través de la agricultura de precisión lidad de cada uno de los cuadros. La agricultura permiten al agricultor negociar primas de seguro de precisión va más allá de un simple muestreo más bajas así como tasas de interés más bajas de suelos en cuadrícula de una hectárea y de la en préstamos, ya sea para insumos estacionales o aplicación a dosis variable de cal para corregir el para inversión de bienes capitales. pH en el campo. Quizás fue así cuando comenzó a principios de la década de 1980 en la Universidad Los clientes prefieren comprar formularios de de Minnesota en Estados Unidos, pero la agriculagricultores que permiten documentar en detalle la tura de precisión ha cambiado su forma y es ahora historia del cultivo (insumos utilizados, condiciones parte integral de la gestión agrícola moderna. en la cosecha) o, mejor aún, parámetros que permiten mejorar la evaluación de la calidad. En cultivos de alto valor en Europa y Estados Unidos, para Cálculos de rentabilidad en agricultura de la trazabilidad y las certificaciones del producto se precisión usan a menudo elementos recolectados a través Un software personal como es Microsoft Excel de la agricultura de precisión. le da al agricultor la oportunidad de modelar y proEstos conceptos pueden ser colocados en un bar las diferentes hipótesis de rentabilidad de las esquema de cadena de valor, como se muestra en inversiones de agricultura de precisión. la Figura 1. Este tipo de esquema es utilizado por los En el pasado, el software de contabilidad agríeconomistas y los estrategas de negocios para des- cola no era diseñado para posibilitar la ejecución cribir cómo los diferentes aspectos están interconec- de los escenarios de costo-beneficio de las invertados y cómo todos ellos cooperan para crear valor. siones de la agricultura de precisión. El progreso lo

99 PARTE 2

### Página 102

ha hecho, pero muchos agricultores todavía tienen por ejemplo a 65 km de distancia pueden quique resolverlo usando simples hojas de cálculo. tarle rentabilidad a la cosecha. Por otra parte, el Hay varias maneras de calcular la rentabi- control de malezas con un bajo rendimiento por lidad de la agricultura de precisión: bajar todos un mal suelo cuesta lo mismo que un buen rendilos costos sobre una base por hectárea, o por miento de un buen suelo. tonelada de producción, o calcular por campo, El análisis de costo beneficio de los diferenpor cosecha, o por todo el establecimiento. Cada tes aspectos de la agricultura de precisión puede una de estas maneras tiene sus beneficios y su ser calculado usando simples hojas de cálculo. A propia complejidad. Bajar los cálculos de todo continuación, en las Tablas 1, 2 y 3, se presentan por hectárea quizás luce mejor pero asume que algunos ejemplos, inspirados en el libro Precision todas las hectáreas son iguales y no lo son. Los Farming Profitability publicado por la Universidad costos de transporte para un campo que está de Purdue, Indiana, Estados Unidos.

Tabla 1. Ejemplo de hoja de cálculo para equipamiento de la agricultura de precisión Costo/ Año/ Hectárea Costo unitario [A] Años de uso (Est) [B] Costo anual [A] / [B] Monitor de rendimiento 3 Unidad GPS 3 Software 1 Entrenamiento 2 Corrección diferencial EQT /RTK 3 Señal diferencial 1 Contrato de mantenimiento 1 Honorarios del consultor 1 Asignación de costo de oficina 1 TOTAL

* Costo por hectárea: dividir el costo anual por el número de hectáreas en que el equipamiento será utilizado.

100

### Página 103

Tabla 2. Ejemplo de hoja de cálculo de costo de dosis variable de fertilizante

Costo unitario [A] Años de uso (Est) [B] Costo anual [A] / [B] VRT Equipo de aplicación 4 Análisis de suelo 3 or 4 VRT tasa de solicitud 1 Honorarios asesor de cultivos 1 Costo de Cartografía 3 or 4 TOTAL

* Costo por hectárea: dividir el costo anual por el número de hectáreas en que el equipamiento será utilizado.

Tabla 3. Eficacia de los equipos de fumigación/distribución con navegación de GPS Costo de equipamiento Costo de amortización anual (5 años) Costo de capital anual (interés 15%) Costo annual Máximo uso hora / día /semana / mes / año 22 h/d - 132 h/s - 528 h/m - 6600 h/a Costo por hora de trabajo a capacidad máxima anual Velocidad de trabajo km/h 16 Ancho de trabajo (metros) 15 Cobertura máxima por hora / día / semana / mes / año (ha) 24 ha/h - 528 ha/d - 3168 ha/s - 12672 ha/m - 158400 ha/a Costo por hectárea tratada a capacidad máxima

* Los vehículos equipados con GPS de alta precisión automática (RTK) pueden cubrir mayor cantidad de hectáreas que los vehículos manuales. Esto es posible porque pueden trabajar más horas (incluyendo la noche) y pueden operar a mayor velocidad sin perder la precisión (o tener un conductor que se queda dormido).

101 PARTE 2

### Página 104

Importancia de la capacidad de la hacer el trabajo en diez días en primavera y diez maquinaria agrícola días de otoño. Esta diferencia de tiempo supone Como muestran las tablas anteriores, la capa- que los agricultores pueden ahora plantar macidad de las máquinas agrícolas puede ser expre- yores extensiones híbridas y tienen sustancialsada por día, por semana, por mes. Existen so- mente cosechas más altas. El resultado: mayor lamente algunas situaciones agronómicas donde rentabilidad. una máquina puede ser usada continuamente du- En situaciones de cosechas dobles la capacirante un año entero. De todos modos, la capaci- dad semanal es muy importante. Reducir el tiemdad de crecimiento semanal y mensual por el uso po sin cosechas en los campos es mejor. Las de los sistemas de navegación de alta precisión cosechas son solamente productivas si crecen, puede ser de gran importancia para el resultado fi- no cuando las semillas están almacenadas espenal de la rentabilidad. Seguidamente se presentan rando ser plantadas, ni cuando los granos se van algunos ejemplos. secando en los tallos esperando ser cosechados.

En la provincia Heilongjiang, Manchuria, norte En algunas partes de Brasil el pico de capacidad de China, la capacidad necesaria de combinar las (expresado en hectáreas/día o hectáreas/semana) cosechadoras para maíz y soja, es calculada para sería un factor crítico en la rentabilidad de la seque estos cultivos puedan ser cosechados en 10 gunda cosecha. días. La razón es simple: cuando el invierno golpea en Heilongjiang, golpea fuerte, con mucho frío y mucha nieve y una vez que la nieve llega, el trabajo Diferencias en el uso de los mapas de en el campo es imposible; por lo tanto, es nece- variabilidad en agricultura sario cosechar dentro de los 10 días previos a la Hacia mediados de la década de 1990 la llegada de la nieve. Esto significa que la unidad de agricultura de precisión introduce a los agriculcosto por cosecha en el norte de China es más tores en los mapas. Esto fue posible gracias al alta que en el sur de Brasil. software basado en Sistemas de Información En el Medio Oeste de Estados Unidos solía ser Geográfica (SIG) y a los rápidos chips de prouna práctica común plantar el maíz en tres sema- cesamiento de clase Pentium. Los mapas son nas de primavera y cosecharlo en tres semanas magníficas herramientas para sugerir la variabide otoño. El tiempo es determinado por la exten- lidad espacial horizontal entre diferentes partes sión del híbrido, más largo en el sur, más corto en del campo. Se pueden mostrar variaciones esel norte. Ahora el agricultor puede comprar má- paciales de rentabilidad procesando mapas de quinas de más alta capacidad, con mayor poder, rendimiento en mapas de rentabilidad. Sin empero sobretodo que permiten realizar el trabajo bargo, como todas las herramientas de comunien menos días y operan a más velocidad, gracias cación, los mapas pueden ser engañosos, por lo a las herramientas de navegación automática de que a continuación se detallan algunos aspectos alta precisión. Esto significa que actualmente los importantes sobre el uso de los mapas de variaagricultores del núcleo del Medio Oeste, pueden bilidad en agricultura.

102

### Página 105

Interpolación por kriging rendimiento es un mejor indicador de la variabilidad

¿En cuántos puntos de información están ba- del suelo que un mapa de interpolación basado en sados los mapas? Los mapas de rendimiento tien- muestras de suelo de cuadrícula de una hectárea. den a tener muchos puntos de información por Estudios en la Universidad de Wageningen en Los hectárea y probablemente reflejen la realidad. Los Países Bajos han mostrado que los nematodos mapas de suelo tienden a ser interpolaciones entre de suelo en invernaderos pueden tener “efectos datos de muestras de suelo muy distantes entre epidemiológicos”. sí, a menudo un punto de dato por hectárea y a Algunas herramientas como los mapas de conveces menos. Estas interpolaciones tienen esca- ductividad eléctrica son útiles porque están baso significado científico. Aún con mayor frecuen- sados en mediciones de alta densidad y pueden cia, los coloridos mapas de muestreo de suelos mostrar variabilidad sin recurrir a interpolaciones en cuadrículas basados en métodos de kriging, matemáticas. son vendidos a los agricultores como realidad y Las muestras de suelo son útiles si son usadas usados como base para las recomendaciones de correctamente. El muestreo inteligente concentra fertilidad. El muestreo de suelo en cuadrículas e muestras en áreas del campo que son homogéinterpolaciones por kriging fueron herramientas fáneas basadas en información de otras fuentes ciles y mal usadas en los inicios de la agricultura (mapas de rendimiento, mapas de conductividad de precisión. eléctrica, mapas a color, mapas de crecimiento de ¿Qué fue erróneo? La interpolación de datos cosecha, mapas de diferencia infrarrojos IR, made muestras puede ser válida, dado que existen pas de Índice de vegetación de diferencia normalibases lógicas para la interpolación. El kriging es zada (NDVI), etc.). Describe en detalle el promedio con frecuencia legítimamente usado en estudios de valores del suelo de una zona de manejo deterepidemiológicos y tienen sentido (enfermedades minada por otros medios. El muestreo inteligente contagiosas esparcidas por contacto; cuanto más no mide la variabilidad, sólo describe una zona. cerca dos personas están, más alta es la probabilidad de contagio de una persona a otra). Los insectos de rápida reproducción y enfermedades de Categorías: Curvas de frecuencia ácaros de hongos, pueden ser expresados usan- Cuando se expresan datos en un mapa, o un do mapas de kriging. Cuanto más cerca y juntos gráfico o histograma, se tiende a agrupar los datos están los insectos, más alta es la probabilidad de en categorías como por ejemplo pequeño / mereproducción y multiplicación. diano / grande, o <8 ton/ha / 8-10 ton/ha / >10 El suelo no tiene características epidemioló- ton/ha, o un número más alto de categorías. Cada gicas. Los suelos no son contagiosos. Estudios categoría tiene un color en un mapa, o una barra detallados en la Universidad del estado de Iowa en un histograma. (Mallarino) han mostrado una gran variabilidad de Los softwares también pueden sugerir el núsuelos, incluso a 10 cm del nivel de escala, a lo mero de categorías, y/o incluso el valor del interlargo y a través de la línea de cultivo. Un mapa de valo de las diferentes categorías. Dos elementos

103 PARTE 2

### Página 106

Figura 2: Ejemplos de tipos de frecuencia

ayudarían a decidir cómo presentar los datos: los refieren a datos agrupados o segmentados. Si un datos en sí mismos o la experiencia de gestión. segmento bajo o alto es concentrado en un área Los datos en sí mismos tendrían frecuencias geográfica específica del campo, probablemente en diferentes formas: en forma de campana, en sea mejor separarlo de la totalidad del campo y traforma de U, extenderse igualmente, o extenderse tarlo diferenciadamente, con diferente agronomía. desigualmente, tal como se visualiza en la Figura En muchos casos ninguno de los datos estaría

2. Aunque un mapa no mostrase estas diferen- por arriba de la media. Si la frecuencia de los datos tes formas de datos, estos igualmente serían muy es regularmente o irregularmente difundida sobre el importantes. formulario de propagación completo de arriba abaUna forma de campana muestra los datos agru- jo, los datos serían más coloridos a la vista, pero pados alrededor del promedio. Primera pregunta: probablemente no serían operacionales. Esto signi- ¿Qué tan amplio es el promedio: +/- 5 %, +/- 10 %? fica que todo lo que se mide no sería relevante para Las estadísticas usarían desviaciones estándares, la administración del campo, por lo que habría que pero un agricultor debería utilizar algo más práctico mirar otros parámetros, otros conjuntos de datos. y operativo para decidir cuál es el promedio para Un histograma o un mapa son inútiles si ellos no él. La representación visual de los datos sería muy ayudan en el análisis o en la toma de decisiones. simple: entorno a la media aceptable, debajo de la media aceptable, encima de la media.

Esto hace los datos muy gerenciales: ¿Qué se Experiencias del uso de agricultura de puede hacer para corregir “debajo de la media” y precisión en el contexto internacional por “encima de la media”? Quizás si se eligieran A través de los años la justificación económimás categorías. ca de la agricultura de precisión se ha vuelto más La frecuencia de la curva con forma de U mues- fácil. Los GPS y los vehículos con sistemas de tra una situación totalmente diferente. El promedio navegación y corrección diferencial se han vuelto matemático no significa todo, porque muchos da- más baratos. La precisión ha mejorado mucho. A tos son a la vez altos y bajos. Los investigadores se mediados de la década de 1990 el costo básico

104

### Página 107

de los sistemas de GPS en Estados Unidos es- ahorro sustancial de agua, la mejora en el ritmo de taba por encima de los U$S 25 000 por sistema, inundaciones y facilita las operaciones a lo largo con una precisión de medio metro. Hoy está por de la temporada. debajo de los U$$ 10 000 con el valor corriente del La rentabilidad de los sistemas de la agriculdólar. Los vehículos automáticos de navegación tura de precisión es calculada por el agricultor la comenzaron costando U$$ 70 000, ahora han caí- mayor parte del tiempo (con la ayuda de consuldo a U$$ 25 000 con precisiones en 10 cm. Los tores y contadores). Se incluye al establecimiensistemas de tiempo real cinemático (RTK, por su to como un todo y probablemente se da una sigla en inglés) con precisiones en los 2 - 5 cm en mirada individual a los campos y a los cultivos. un vehículo en movimiento, regularmente se pagan Desafortunadamente estos cálculos son privados a sí mismos dentro del primer año de operación. y no están disponibles para otros agricultores. Muy Aunque el costo de muestreo de suelo y de pocos estudios macro, que incluyan a un gran núanálisis de suelo no ha bajado mucho, los siste- mero de agricultores, han sido realizados y publimas de transferencias de datos se han automati- cados. A continuación se presentan tres ejemplos zado más, sus resultados ayudan a que la toma de de estos estudios, que son internos y no estaban decisiones se realice en menor tiempo y los errores destinados a ser publicados, aunque se le ha permitido al autor referirse a los datos. en la transcripción de datos se han eliminado. De manera similar sucedió para la información de satélite de detección remota. Los sensores en tiem- Ejemplos prácticos de rentabilidad de po real para las aplicaciones de nitrógeno son to- agricultura de precisión davía caros, pero han demostrado ser rentables en Una cooperativa agrícola en el Medio Oeste de un medio de alto rendimiento (7-10 toneladas por Estados Unidos hizo un estudio de la rentabilidad hectárea) en situaciones de cultivo de trigo. Las de la agricultura de precisión aplicada a los campos redes de sensores inalámbricos en huertas y viñe- de maíz y soja en Illinois (1997-1998). Sólo se condos en California por ejemplo han sido rentables sideró el beneficio agronómico, no los beneficios (recolección selectiva de alta calidad/ alto precio operacionales o externos que el agricultor poseía. de venta de uvas, vino, fruta o verduras).

En el 10 % de los campos los métodos traLos sistemas de alta precisión RTK han rede- dicionales (tarifa plana) fueron más rentables; en finido el riego. Los cultivos anuales de verduras su mayoría en campos donde la variabilidad fue son ahora regados por líneas de goteo. El cam- muy baja y la tarifa variable de tecnología no agrebio de sistema de riego superior a líneas de goteo gó beneficios, o en campos donde la variabilidad subterráneo ha permitido ahorrar 70 % de agua fue tan extrema que la situación no fue manejay ha reducido los costos en tratamientos con fer- ble y cada tratamiento promedio fue mejor que tilizantes e insecticidas. Asimismo, los sistemas los métodos caros para corregir la situación. En RTK han permitido a los productores de arroz en el 25 % de los campos, la agricultura de preciArkansas, Estados Unidos, desarrollar sistemas sión tuvo la misma rentabilidad que los métodos de campo de grado cero. Lo que ha permitido el tradicionales. En dos tercios de los campos, los

105 PARTE 2

### Página 108

agricultores lograron hacerlos más rentables des- Dependiendo de la situación de los agricultores, pués de la adopción de la agricultura de preci- de las máquinas y de los campos; las máquinas sión, debido a mayores rendimientos por el mejor equipadas con sistemas RTK actualmente plantan uso de los insumos, que por el ahorro de costos entre 3 y 5 % más semillas por hectárea evitando en insumos. Como resultado de este estudio, la saltear espacios. Esto es lo mismo que obtener cooperativa vio a la agricultura tradicional de no de 3 a 5 hectáreas gratis, sin pagar por ellas, por precisión como una excepción, solo siendo re- cada 100 hectáreas plantadas. En áreas montacomendada en casos raros y bien definidos. La ñosas la diferencia de rentabilidad fue aún mayor. agricultura de precisión es ampliamente adopta- Asimismo, los agricultores ahorraron entre 7 y da por los agricultores en Illinois. 10 % en costos de insumos, al evitar tratamientos Los servicios de extensión asociados con la dobles o superposiciones. Resultados similares Universidad estatal en Pensilvania estudiaron el fueron informados desde Iowa. efecto sobre el consumo total de fertilizantes des- La Universidad Agrícola en el Sur de China pués de la adopción de la agricultura de precisión (Guangzhou, China) desarrolló una máquina de (1997-1999). Después de dos años de datos de siembra directa de arroz para pequeños y mecientos de agricultores, muchas cosechas y miles dianos agricultores (2008-2011). La máquina de campos, la conclusión fue: el uso total de ferti- remplazó al transplante tradicional con un sistelizantes no se redujo. Los fertilizantes simplemente ma ingenioso de canales húmedos y secos a lo estaban en mejores condiciones, con mejores ren- largo de la línea de siembra. Las semillas fueron dimientos y resultados positivos en la mayoría de posicionadas a un nivel de precisión centimétrica las situaciones. A pesar de estos resultados posi- y fertilizadas a la misma vez. Las pruebas a través tivos, la adopción de la agricultura de precisión en de los años y varios lugares confirmaron alentaPensilvania es todavía un poco lenta. Los agricul- dores resultados, todos ellos procedentes de la tores son pequeños y a menudo de medio tiem- implementación de la tecnología de la agricultura po, la tierra es montañosa y los suelos son menos de precisión en una nueva área: una máquina remfértiles. Los agricultores son reacios a invertir en plaza 40 trabajadores durante el transplante, por agricultura de precisión, aunque ésta sea rentable, eso el arroz tendría un ciclo de crecimiento más debido a que el nivel de rentabilidad en dinero, no largo; los rendimientos aumentarían un 10 % (proen porcentaje, es menor del que ellos consideran bando ésto la siembra directa puede ser al menos adecuado. De todos modos, como el costo de la tan buena que el transplante de arroz); las tasas de tecnología de la agricultura de precisión ha des- nitrógeno podrían ser reducidas al 30 %, mientras cendido, se ha acelerado el proceso de adopción. se mantienen o aumentan los rendimientos por el En la región del delta del Missisipi (entre posicionamiento preciso “en la parte superior de Memphis y Nueva Orleans), un distribuidor regio- la semilla” y el tiempo ideal, antes de la germinanal quiso confirmar los beneficios operacionales ción, emergencia y crecimiento rápido del cultivo. del sistema RTK con navegación precisa en centí- Esta tecnología está siendo probada en Vietnam, metros de cultivos de algodón y soja (2009-2010). Filipinas y Tailandia. (2010-2012).

106

### Página 109

Una compañía con una plantación de 1 500 tamaño, pero no se estuvo de acuerdo en comhectáreas de durazno en Francia redujo el tamaño partir los detalles del nuevo sistema por razones de la unidad de gestión usada para la exploración, de competividad. el tratamiento y la cosecha del cultivo, de 15 a 1.5 Grandes establecimientos cerealeros en Ucrania hectáreas (2003-2004). Trabajando en unidades sospecharon que perdieron el 30 % de la cosecha más pequeñas, fue posible confinar tratamientos entre el campo y el elevador. Debido al equipade insectos y enfermedades a unas pocas hectá- miento de cada cosechadora y cada camión con reas, ahorrando un tercio en costos de insumos. GPS y telemática, la causa de la pérdida pudo ser En vez de tratamientos completos a grandes uni- identificada y corregida (2007-2008). De manera dades, en el inicio de la infección, ahora se realizan similar, una granja de maíz en el Medio Oeste de tratamientos a pequeñas unidades en las que es Estados Unidos sospechó de ocasionales pero necesario. Esto significa que menos hectáreas son sistemáticos errores en la carga reportada por los tratadas. El seguimiento de maduración del culti- camiones en los muelles de recepción de una insvo en bloques más pequeños con una cosecha talación de fermentación de etanol (2009-2010). selectiva permite un tiempo más largo de cose- Estos fueron pequeños errores impredecibles pero cha, menos fruta demasiado verde o demasiado la mayoría a favor de la planta. Los GPS y los temadura –lo que es altamente apreciado por los lemáticos en los camiones de reparto rápidamensupermercados– y permite un tiempo más flexible te alertaron sobre lo que sucedía. Los errores en de entrega, evitando los precios bajos durante los medición todavía suceden, lo que es normal, pero períodos de pico de suministro. algunos actúan a favor de la planta y otros a favor Todo esto no hubiese sido posible sin el uso de del agricultor. Los costos de los telemáticos fueron las computadoras para la exploración, el monito- devueltos en pocos meses. reo y el seguimiento de la maduración del cultivo El autor ha tenido el privilegio de aprender socon GPS, almacenando cada árbol en una base bre los beneficios de la agricultura de precisión en de datos SIG y cosechando por un bloque de 1.5 varias operaciones en Brasil y Chile. En cada caso hectáreas. Antes de la implementación del nuevo (naranjas, aceitunas, caña de azúcar y soja) las sistema, la compañía había analizado la posibili- técnicas de la agricultura de precisión fueron una dad de ir aún más lejos en la gestión detallada. Se parte fundamental del total de la agronomía y de concluyó que más allá de las unidades de gestión la gestión operacional interna. En cada caso los de 1.5 hectáreas, los mayores beneficios fueron en beneficios se extendieron a las relaciones con los gran medida compensados por el incremento de clientes y al nivel total y predecible de flujo de caja. los costos. Además, se concluyó que las unidades de 1.5 hectáreas fueron óptimas por la estructura existente de huerta (ancho de la hilera, espacio Claves para la toma de decisiones entre los árboles, líneas de riego por goteo). Se La agricultura de precisión comenzó como una aceptó que la nueva huerta es plantada de forma forma de mejorar los aportes de nutrientes en camdiferente y gestionada en unidades de diferente pos de maíz y soja en el Medio Oeste de Estados

107 PARTE 2

### Página 110

Unidos. Es ahora una parte fundamental de cómo 2.5. Monitoreo temporal de los

trabajan los establecimientos profesionales en

todas partes del mundo. La pregunta no es si la

sistemas de producción para la

agricultura de precisión puede ser implementada toma de decisiones y mejora

de una manera rentable, sino cómo implementar Evandro Chartuni Mantovani y Gisela de Avellar la agricultura de precisión de modo de obtener el más rápido y alto retorno de la inversión posible.

Evandro Chartuni Mantovani

Para un agricultor en cualquier parte de Investigador Embrapa Maíz y Sorgo, PhD

Sudamérica la pregunta es: ¿cuál sistema sustitu- Mecanização Agrícola

ye mejor la operación existente, y cómo implemen- Sete Lagoas, MG, Brasil

tar el nuevo sistema? ¿Se entra en un “Big Bang” evandro.mantovani@embrapa.br

con alto nivel de inversión, riesgos más altos pero

también con la posibilidad de mayor rentabilidad? Gisela de Avellar

¿O se va de manera “gradual”, paso a paso, pri- Professora do curso de Cartografia e Geoprocessamento, MSc. mero implementando aquellas áreas donde los re- Centro Universitário de Sete Lagoas – UNIFEMM tornos positivos son muy probables, y más tarde Sete Lagoas, MG, Brasil a mayor escala? gisella@uai.com.br Cada campo, cada establecimiento será diferente. Cada agricultor tiene diferentes niveles de especialidad o especialidades en diferentes Introducción áreas. El punto crítico sería para los consultores escuchar cuidadosamente y orientar a los agri- El uso de metodologías de agricultura de precicultores a través del proceso. La agricultura de sión mejora la eficiencia en el manejo de áreas proprecisión no es una meta en sí misma. Es una ductivas, por la optimización en la aplicación de herramienta. Es un proceso continuo que lleva a insumos, y también en el gerenciamiento eficiente mejorar la gestión agrícola total y, por último, a de las actividades del sistema de producción. Así, mejorar la rentabilidad y la supervivencia del esta- el trabajo con metas productivas para los cultivos blecimiento rural a largo plazo. mediante agricultura de precisión busca reducir las inestabilidades o variabilidades de producción al utilizar equipos de muestreo georreferenciado para el mapeo físico y químico del suelo, lo cual aumenta la capacidad de manejo de las diferentes áreas. Para el seguimiento del ciclo del cultivo se utilizan fotografías aéreas o imágenes satelitales a fin de realizar la toma de decisiones en tiempo real, principalmente para la fertilización nitrogenada en cobertura y para el control fitosanitario, con el monitoreo de insectos, plagas y enfermedades.

108

### Página 111

En la distribución de insumos, el uso de equi- es necesario complementar el análisis de producpos con programas de aplicación a dosis varia- tividad con mapas temporales, de por lo menos 3 ble optimiza el uso de fertilizantes y agroquímicos, años, para conocer los patrones de producción, permite planificar la siembra para obtener un es- complementado con la evaluación económica en tándar deseado en la cosechadora y, como conse- los mapas de rendimiento. cuencia, evita la contaminación del medioambien- Los problemas resultantes de la variabilidad te. Además, el uso del piloto automático permite espacial, incluso en áreas más extensas, pueden aumentar la capacidad operacional de los equipos evitarse con el uso de técnicas de agricultura de del cultivo, aumentando el número de horas traba- precisión para el monitoreo, control, recolección jadas por día durante la implementación del cultivo y uso de datos e informaciones, en el sentido de en áreas extensas. revertir este cuadro, buscando la toma de decisioPor lo tanto, se deben priorizar acciones inte- nes e intervención en el sistema de producción. gradas del sistema de producción por parte de La necesidad de establecer un análisis con el especialistas agronómicos en la utilización de agri- objetivo de una correcta toma de decisiones dencultura de precisión, porque permiten el mapeo tro del proceso de utilización de la agricultura de adecuado de las áreas de producción, con infor- precisión, implica la búsqueda de patrones mínimación del conocimiento del lugar, de los recursos mos para intervenir en el sistema de producción. estables del campo, de los costos de producción Para definir los patrones de productividad en alta, y de las condiciones estacionales, y así estable- media y baja, es necesario establecer criterios cer las recomendaciones necesarias para la toma para la etapa de análisis de datos utilizando inforde decisiones del agricultor. De esta manera, los mación con mapas temporales de rendimiento. La resultados obtenidos en mapas georreferenciados primera etapa se realiza con la indicación de un contribuirán a la modernización de los procesos mapa de tendencias de variabilidad espacial que de producción y de transferencia de tecnología y muestra las áreas de productividad estabilizadas y potenciarán el gerenciamiento económico del sis- releva los costos de producción. tema de producción.

Tendencia de la variabilidad

Monitoreo temporal de los sistemas de Una de las principales ventajas en el tratamiento producción georreferenciado del cultivo es poder presentar los El nivel tecnológico aplicado al sistema de datos en diferentes niveles de detalle, dentro del enproducción de un determinado cultivo varía de foque analítico con el que se estudia la región. Los un establecimiento a otro. Consecuentemente, datos tienen que organizarse en niveles de presenel valor de la productividad, aisladamente, de un tación y de manera que no necesariamente se pase determinado campo de producción, identifica la de un nivel a otro en una secuencia obligatoria. Esta variabilidad espacial, aunque no es eficiente para estrategia posibilita la obtención de una infinidad de determinar el patrón de producción. Para estable- combinaciones de datos y comparaciones entre dicer el gerenciamiento de las áreas de producción ferentes alternativas de acción.

109 PARTE 2

### Página 112

De acuerdo con Santos (1997) en algunas si- soporte de análisis estadísticos complementarios tuaciones se debe considerar el hecho que una fue posible identificar áreas con diferentes patroúnica técnica no es suficiente para todas las si- nes de producción. tuaciones presentadas y tampoco define las li- En la primera etapa del trabajo, se realizó una mitaciones para varios ambientes. Con el mejor uniformización de los mapas de rendimiento. La priconocimiento de la estructura de producción de mera cosecha de soja generó 30 428 muestras, con un campo es posible planificar el proceso de inter- una productividad que varió entre 1,3 y 4,1 t/h. En vención en el mantenimiento de la productividad la segunda cosecha de soja, fueron 40 409 muesy/o mejoras en las áreas de inestabilidad y baja tras y la productividad varió entre 2 y 5,9 t/h. En la productividad, a partir de 3 años de observación. cosecha del maíz, en 2002, se generaron 24 213 En un establecimiento rural, el mapa de rendi- muestras que variaban entre 1,4 y 5,1 t/h, tal como miento le permite al productor realizar una radio- puede visualizarse en la Figura 1. grafía de la variación espacial del campo al dividir Las decisiones gerenciales son más seguel campo en áreas homogéneas y mostrar el por- ras cuando el productor trabaja utilizando una qué de esa variación. combinación de tres o cuatro años de mapas de Como ejemplo, un área piloto de 115 hectá- rendimiento, porque así los factores espaciales y reas de la Fazenda Recanto, en Sidrolândia, MS, temporales pueden ser separados y clasificados.

Brasil, fue trabajada con la metodología de agricul- Para comparar los datos de diferentes cultivos – tura de precisión con datos georreferenciados de por ejemplo maíz y soja– fue preciso transformar dos cosechas de soja y una de maíz de invierno. los mapas de rendimiento en grillas uniformizadas El gran volumen de información generado permitió que permitiesen comparar el comportamiento de diversos análisis y algunas conclusiones. Con el los datos en los mismos puntos de recolección.

Figura 1. Mapas de rendimiento de maíz y soja, del área de 115 ha, de la fazenda Recanto, Sidrolândia, MS, Brasil

110

### Página 113

Figura 2. Uniformización de los mapas de cosecha de maíz y soja, del área de 115 ha, de la fazenda Recanto, Sidrolândia, MS, Brasil

Este procedimiento estandariza los mapas ¿Qué es un área estable? La tendencia a la esgenerados en la cosecha. Estas grillas generan tabilidad en un campo puede ser definida cuando, nuevos mapas estandarizados de cosecha, que en un mismo punto, la variación de la productiviindican las diferencias espaciales. Con la superpo- dad es pequeña a lo largo de las diferentes cosesición de los nuevos mapas es posible generar un chas incluidas en el cálculo. La Figura 4, muestra cuarto mapa y establecer el patrón de producción. los patrones de producción de un área de 115 ha, Una inspección visual de esos mapas indica cuá- con 3 años de cosecha: les áreas de productividad por encima o debajo • Área azul: 12% del área con una producción de la media ocurren normalmente en las mismas alta y estable. áreas, tal como puede visualizarse en la Figura 3. • Área verde: 75% del área con gran estabilidad El mapa de tendencia espacial de las áreas es pero producción media. la base para el trabajo de planificación y programa- • Área amarilla: 13% del área inestable, donde ción de intervención del sistema de producción. hubo una gran variación.

111 PARTE 2

### Página 114

Figura 3. Mapas de cosecha de maíz y soja, del área de 115 ha de la fazenda Recanto, Sidrolândia, MS, Brasil

En un año la producción fue muy alta, en otro Es común identificar mayor inestabilidad en la fue muy baja y en el tercero estuvo dentro de la productividad de las áreas del entorno, debido a la media. Es preciso aclarar que la productividad me- dificultad de operación de máquinas para la aplicadia de un área, cuando se trata de agricultura de ción de insumos, a la deficiencia en la distribución precisión, se refiere a aquélla área. de agua en el riego, a la cosecha, etc.

De acuerdo con esta clasificación, una inves- El análisis económico de los datos se realiza tigación en el lugar de algunas áreas puede ser registrando todos los costos involucrados en el una garantía para identificar los factores limitantes. proceso de la técnica de agricultura de precisión, Un análisis posterior puede mostrar dónde es eco- en un sistema de producción, evaluando todas las nómicamente viable interferir o mantener la inter- etapas del cultivo. Según Matoso (2002), para la vención. En la Figura 4 se presenta un ejemplo de asignación de costos se consideran los costos área con porcentajes de rentabilidad por tipo de fijos y variables, teniendo en consideración los productividad. costos de equipo y software, servicios de geren-

112

### Página 115

Figura 4. Establecimiento de patrones de producción del área de 115 ha de la fazenda Recanto, Sidrolândia, MS, Brasil

ciamiento y costo del dinero. De la misma manera, controlar modificaciones adicionales. El potencial para la implementación de los cambios se calculan de rentabilidad puede ser clasificado en números los costos relacionados con los insumos y su apli- tratados de diferentes tipos y, de este modo, se elicación. Los rendimientos estimados se obtienen minan factores aislados que limitan la producción teniendo en cuenta la productividad con las alter- y se puede cuantificar el potencial de rendimiento nativas analizadas. económico.

A continuación, al conocer el punto de equi- Utilizando los dos tipos de mapas, de rendilibrio en el análisis de costos de producción, en miento y de rentabilidad, la primera y segunda la Figura 5 se establece un mapa de rentabilidad etapa del ciclo de la agricultura de precisión son y en la Figura 6, asumiendo que los factores limi- realizadas para conocer los tipos de producción: tantes han sido erradicados, de forma que la pro- de alta, media y baja productividad/rentabilidad/ ductividad de una determinada área haya llegado perjuicio, que deberán ser analizadas para la ina sus límites naturales y el agricultor ya no puede tervención o el mantenimiento de los niveles de

113 PARTE 2

### Página 116

Items Valores producción. Así, para un análisis temporal de daRendimiento (kg/ha) 1.916,25 tos, los mapas de rendimiento de por lo menos 3 Precio (R$/kg) 0,30 años consecutivos, necesitan ser sistematizados para:

Ingreso bruto (R$) 574,88

Margen bruto (R$) 56,19 • Definir los patrones de producción/tendencias,

Margen líquido (R$) 0,00

en los mapas de rendimiento del maíz.

Punto de equilibrio: costos variables • Establecer los criterios para definir los tipos de 1.728,95 (kg/ha) rendimiento, en función del análisis económico Punto de equilibrio: costos fijos (kg/ha) 1.916,25 de los datos de productividad, con el fin de esTasa de rentabilidad sobre los costos tablecer el mapa de rentabilidad.

1,11

variables

Tasa de rentabilidad sobre los costos fijos 1,00 • Establecer un análisis in situ, con el fin de realizar una intervención diferenciada en las áreas

Figura 5. Análisis económico: punto de equilibrio y tasa de rentabilidad, inestables y de bajo rendimiento. del área de 115 ha de la Fazenda Recanto, Sidrolândia, MS, Brasil La intervención en los lugares de inestabilidad de producción y de bajo rendimiento se caracteriza como la tercera etapa del ciclo, que puede ser desde una fórmula de fertilizante más adecuada, un cambio para un cultivar más adaptado, o incluso una actividad para mejorar las condiciones físicas del suelo y reducir su compactación.

Las recomendaciones de dosis de aplicación

de fertilizantes son imprecisas y generalmente están basadas en una meta de rendimiento para un mapa específico del suelo (Larscheid et al., 1997), ignoran la variabilidad dentro de cada unidad del mapa y asumen datos climáticos promedio. Sin embargo, en esta tercera etapa aún existen problemas para su total implementación por la dificultad de gerenciar el sistema de producción porque, en la mayoría de los casos, ocurren acciones aisladas de parámetros y también por la falta de criterios más eficientes en la definición de parámetros de clasificación de los niveles de productividad en

Figura 6. Mapa de rentabilidad de soja, del área de 115 ha, de la tipos estables de producción. Por lo tanto, esta Fazenda Recanto, Sidrolândia, MS, Brasil clasificación demandaría un plazo mayor para al-

114

### Página 117

canzar la variabilidad temporal de los campos de mo de rendimiento necesario para hacer rentable producción. esta tecnología.

Larscheid et al. (1997) clasifican las decisio- Swinton y Lowenberg-Deboer (1998) muestran nes de gerenciamiento de un establecimiento que el análisis de presupuesto parcial ha sido la agrícola en: 1) decisiones de largo plazo, que herramienta más utilizada para evaluar la rentabiliconsideran adoptar en el establecimiento es- dad en la agricultura de precisión. Este análisis se trategias de rotación de cultivos; 2) decisiones enfoca solo en aquellos ítems de costos y rentabiintermediarias relativas a la próxima época de lidad que promueven el cambio en la utilización de siembra; y 3) decisiones de corto plazo, que una nueva práctica, y normalmente se calcula por consideran la zafra en curso durante el período área o por lote. Un análisis completo de rentabilide crecimiento. Incluso, según los mismos auto- dad debería incluir el efecto del impacto en todo el res, actualmente la principal aplicación de mapas establecimiento, así como el efecto de los riesgos. de rendimiento como herramienta para la toma Incluso así, la técnica de presupuesto parcial es de decisiones sigue siendo más adecuada para una excelente manera de comenzar a analizar la rentabilidad media. decisiones de largo plazo e intermediarias, especialmente cuando un campo se vuelve disponible Así, mapas de por lo menos 3 años consea lo largo de muchos años. cutivos de rendimiento, con análisis para el establecimiento de patrones de producción, permiten Es evidente que al analizar un mapa de rendistinguir los tipos de productividad, en función dimiento de un año, esta clasificación podría ser del análisis económico de los datos y establecer realizada considerando apenas la variabilidad el mapa de rentabilidad. El uso de este procediespacial. La clasificación para la evaluación del miento facilita el análisis in situ de producción más área sería más precisa al considerar el factor va- rápida y de bajo costo, para una intervención diferiabilidad temporal, el cual agregaría los ítems de renciada en las áreas inestables y de baja producestabilidad y caracterización de los lugares de tividad, tal como se muestra en la Figura 7. producción.

Por eso, es preciso establecer los procediAdemás, el nivel tecnológico aplicado al sis- mientos adecuados para la aplicación del contema de producción de un determinado cultivo cepto y de técnicas que viabilicen la optimizavaría de un establecimiento a otro y, consecuen- ción del sistema de producción. Las acciones temente, el valor de un rendimiento aisladamente, aisladas de intervención no siempre producirán no es eficiente para determinar el valor de esos resultados que justifiquen económicamente el tipos. Por ello, se necesita complementar el aná- uso de la agricultura de precisión. Por otro lado, lisis de productividad e introducir la evaluación ya son conocidas las técnicas eficientes para económica en los mapas de rendimiento con el trabajar con el mapeo temporal de los sistemas fin de establecer el costo de producción por área de producción, como se muestra en la Figura y conocer el punto de equilibrio, o sea, el míni- 8, el modelo de Moore (2002) que permite al

115 PARTE 2

### Página 118

Figura 7. Adopción de un enfoque simple para realizar mejoras significativas en la rentabilidad (Fuente: Mark Moore, AGCO, 2002)

Histórico del área de producción

-Variab. temporal: M1+M2+M3+M4

Integración de datos

Conocimiento del área: mapeo

Identificación de las

Mapas Campos Áreas Ensayos Zonas de manejo

Invasoras antiguos anegadas de campo Evaluación de

las decisiones

Recursos estables del campo Establecimiento de las

Tipo de suelo Profundidad del suelo Topografía Zonas de manejo

Mapa de

Condiciones estacionales Modificación de las rendimiento

Clima Cultivo, Nutrientes Plagas y ZM por las condiciones

padrón tipo/variedad del suelo enfermedades estacionales

Decisiones

del agricultor

Recomendaciones y análisis

¿Cuál es el escenario?

Conocimiento del área

Identificación de las

Zonas de manejo

Implementación de las decisiones

Figura 8. Modelo de gerenciamiento del sistema de producción para la toma de decisiones del agricultor (Fuente: Mark Moore, AGCO, 2002)

116

### Página 119

agricultor tomar decisiones durante el cultivo, en

tiempo real y después de la cosecha.

El establecimiento de patrones que identifican

las diferentes áreas de producción dentro de un

mismo campo, permite al agricultor tomar decisiones acertadas y, al mismo tiempo, evaluar si las recomendaciones implementadas tendrán el efecto esperado. De este modo, permite un gerenciamiento económico del sistema de producción, con acciones durante el ciclo del cultivo y después de la cosecha. A partir de la siembra, con los mapas de tendencia, el agricultor puede acompañar el cultivo y, en el caso del maíz, la intervención en tiempo real para la corrección de nitrógeno y agua por ejemplo, permite la recuperación de la productividad, antes de que finalice el ciclo.

117 PARTE 2

### Página 121

PARTE 3

IMPLEMENTACIÓN

DE LA AGRICULTURA

DE PRECISIÓN

### Página 122

3.1. Tecnología de precisión para controladores ha mejorado el uso de gestión en sitios-específicos. gestión de nutrientes Las tecnologías de la agricultura de precisión Harold Reetz están ahora disponibles para agricultores y sus asesores y les brindan nuevas y excitantes posiHarold F. Reetz, Jr. bilidades de mejorar los sistemas de gestión de Consultor de Reetz Agronomics, LLC. producción agrícola. Como muestra la Figura 1, la B.S. in Agricultural Science-Agronomy, University of gestión de nutrientes agrícolas puede usar tecIllinois,1970 nología de precisión en una variedad de maneras para medir las condiciones, las actividades de moM.S. in Crop Physiology and Ecology, Purdue Universitynitoreo y los resultados récords de las prácticas Agronomy Department, 1972 de gestión e insumos. El uso de la tecnología se Ph.D. in Crop Physiology and Ecology, Purdue University- está convirtiendo en una parte importante de la Agronomy Department, 1976 agricultura y hace a los sistemas de producción Monticello, Illinois USA agrícola más productivos, más rentables y más Harold.Reetz@ReetzAgronomics.com sostenibles.

Este capítulo resume como algunas de estas

tecnologías son aplicadas en los modernos sistemas de gestión de nutrientes. De las muchas heIntroducción rramientas disponibles sólo una selección puede Los agricultores y sus asesores ponen a punto ser discutida, pero ésta sirve como ejemplo de los el sistema de gestión de la producción de cultivos modos interesantes en que la tecnología está repara mejorar rendimientos y ganancias, a menudo volucionando los sistemas de producción agrícola encuentran razones para cambiar la tasa de apli- alrededor del mundo. cación para insumos variados (semilla, fertilizante, químicos) con el fin de dar cuenta de la variabilidad del tipo de suelo y de otros factores. Determinación de la variabilidad dentro de La combinación de herramientas y servicios un campo disponibles hacen posible cambios tales como El uso de la agricultura de precisión en sitios lo es la tasa variable de tecnología (VRT14), sien- específicos depende de si existe alguna razón do ésta la parte más importante de la agricultura para cambiar la gestión hacía las diferentes partes de precisión de sitio-específico. La aplicación del campo. Esto usualmente significa que hay alVRT de algunos insumos ha sido practicada guna fuente de variabilidad que puede ser manejadesde la década de 1920, pero la disponibilidad da cambiando prácticas o insumos. La variabilidad de GPS, GIS y el amplio rango de monitores y puede ser determinada por la medición de algunos parámetros que guían la decisión del cambio de gestión. Por ejemplo, un uso común de la agricul-

14 Por sigla en inglés: variable-rate technology (VRT) tura de precisión, es variar la tasa de la aplicación

120

### Página 123

Figura 1. Esta ilustración muestra ejemplos las diferentes tecnologías de la agricultura de precisión que están siendo usadas para la producción de cultivo en sitios específicos. Fuente: Better Crops, 1994, IPNI

de fertilizante de un área del campo a la otra. Ese Muestreo de cuadrícula

cambio en la tasa podría estar basado en el aná- Con poca o ninguna información sobre el camlisis de suelo, el rendimiento de los cultivos ante- po el muestreo de cuadrícula es válido, el primer riores, la capacidad de mantener el agua de los conjunto de muestras de suelo podría ser recogido suelos, u otros factores que pueden ser medidos en una base de cuadrícula uniforme. Recoger una o estimados. muestra por hectárea da una buena base de datos, la cual es recomendada para la aplicación de fertiliMuestreo de suelo zante. Cada muestra es preparada con cinco a diez La forma más común para determinar la varia- muestras de suelo recolectadas dentro del área de bilidad de nutrientes en los suelos es mediante el una hectárea, luego se mezclan y se depositan en muestreo de suelo y el análisis de las muestras en una bolsa o caja pequeña y son enviadas al laboralos laboratorios que determinan el contenido rela- torio. Las muestras deberían ser recogidas en una tivo de nutrientes. superficie uniforme (a menudo alrededor de 20 cm).

121 PARTE 3

### Página 124

Figura 2. Un patrón de cuadrícula uniforme de muestreo de suelos Figura 3. Un patrón de muestreo inteligente para el muestreo de usado cuando es necesario conocer lo más pequeño de las fuentes de suelos donde se conocen las fuentes de variación -en este caso variabilidad en el campo. Fuente: IPNI, 2013 topografía- que afectan los niveles de nutrientes de los suelos. Otros mapas de la variabilidad del campo pueden ser usados para guiar el muestreo inteligente y brindar mejores recomendaciones para la aplicaciones de nutrientes Más información sobre muestreo de cuadriculas en el apartado 1.5. Muestreo para mapeo y manejo de la fertilidad del suelo. mación en la que los mapas son basados, se usan para crear un archivo de datos de aplicación (otro mapa) que sirve al controlador de dosis para ajustar la dosis de la aplicación de fertilizante ya que el Muestreo inteligente - zonas de gestión aplicador se mueve a través del campo.

Sí la indicación de variabilidad es conocida -por

mapas de rendimientos anteriores, mapas de tipo Mapas

de suelos, conductividad eléctrica, etc.- es mejor Algunas zonas de gestión son basadas en mapara definir las zonas de gestión ya que se conoce pas de tipo de suelo, topografía, rendimiento de la fuente de variación y muestra acorde a los lími- cultivos anteriores y otra información. En EEUU los tes de esas zonas. Este método de muestreo inte- mapas de estudios de suelos son usados comúnligente toma ventaja de lo ya conocido acerca del mente. Los estudios digitales georreferenciales campo, para ayudar a definir las tasas adecuadas de suelos están disponibles para casi todos los de fertilizante a ser aplicadas. El muestreo inteli- campos de producción de cultivos, brindando no gente a menudo se basa en mapas de variabilidad, solamente mapas, sino gran cantidad de datos registrados de acuerdo a la ubicación del GPS en de apoyo sobre las características del suelo, de la una base de datos de SIG. Estos mapas o la infor- producción de cultivos y otros usos.

122

### Página 125

Cuando los estudios de suelo no están disponibles, otros mapas pueden ser usados para las zonas definidas de muestreo. Un mapa de conductividad eléctrica del suelo puede ser usado para obtener una idea general sobre la variabilidad del suelo. La conductividad eléctrica del suelo es medida para saber cuánta corriente eléctrica puede conducir el suelo. Las partículas más pequeñas de arcilla conducen más corriente que las partículas más grandes de limo o arena, por eso la conductividad eléctrica puede ayudar a estimar la textura

Figura 5. Un diagrama de corriente eléctrica (líneas de puntos) fluyendo

del suelo. El mapa es generado tirando de un carro entre diferentes discos en el carro de conductividad eléctrica y cómo a través del campo para tomar las lecturas. éste es movido a través del suelo.

El carro es equipado con una serie de discos

que se mueven a través del suelo y recogen lecturas de la corriente eléctrica pasando a través del suelo entre los discos. Varios miles de lecturas son tomadas dentro de cada hectárea. La información recolectada proporciona una estimación de las características de la variabilidad del suelo., especialmente de la textura del suelo (relativo al contenido de arcilla) y factores relacionados. La posición de

Figura 4. Un carro de conductividad eléctrica usado en un campo de Figura 6. Un mapa de medidas de conductividad de los suelos tomadas trigo cosechado para medir la conductividad eléctrica del suelo. con un sistema de carro de conductividad eléctrica que muestra la Sitio web: www.veristech.com variabilidad de la conductividad eléctrica del suelo dentro del campo

123 PARTE 3

### Página 126

cada medida es grabada con las coordenadas del dos, estos sensores pueden ser usados para haGPS para proporcionar un mapa detallado de la cer ajustes instantáneos en la marcha de la tasa variabilidad de la textura del suelo en la zona de de N de fertilizante, ya que el aplicador se mueve enraizamiento del cultivo. Ya que muchos de los a través del campo. factores de productividad en variabilidad de suelos son relacionados a la textura, el mapa de conductividad eléctrica ayuda a estimar la variabilidad en productividad de suelo y así guía las decisiones de gestión de nutrientes.

Teledetección

La teledetección aérea o satelital tiene potencia para identificar las fuentes de variabilidad que probablemente ayudarían a determinar la dosis adecuada de la aplicación de fertilizante. Ellas son a menudo útiles para determinar la variabilidad a mayor escala, para guiar la tasa variable de aplicación de fertilizante. Las imágenes de los Google Maps y los Bing Maps pueden proporcionar algu- Figura 7. Un sensor manual “greenness” (intensidad del verde) usado na indicación de la variabilidad de suelos y quizás para evaluar la salud actual del crecimiento del cultivo. Este sensor utiliza infrarrojo sean suficientes, sí relacionan las observaciones de suelo que identifican los ejemplos de los diferentes tipos de suelo mostrados en las imágenes.

Hay siempre una compensación en la escala de

precisión. Las imágenes satelitales dan una cobertura más amplia a menores costos, pero con menor resolución (detalle). La imagen aérea proporciona más detalle, pero es más cara por hectárea de cobertura.

Monitores y sensores

Recientemente, varios tipos de monitores están disponibles, estos usan sensores para medir la reflexión de la luz desde el follaje del cultivo, el cual puede ser comparado con una franja de referencia Figura 8. Una serie de unidades de sensor montadas sobre cada en el campo para indicar el contenido relativo de fila en un aplicador de fertilizante puede ser usado para estimar las necesidades de N en la marcha y guiar el controlador del aplicador nutrientes del cultivo. Adecuadamente montados para ajustar la dosis de la aplicación de side-dress fertilizante nitrógeno en tiempo real. Foto: Corn & Soybean Digest y calibrados en contra de los estándares conoci-

124

### Página 127

Cuando se usan mapas, sensores u otros, 4R como una guía para las prácticas de manejo se mide la variabilidad y se ajusta la aplicación, de nutrientes que son agronómicamente viables, es más importante pensar sobre lo que se está económicamente sustentables y responsables haciendo, usar las herramientas adecuadas y to- frente al medio ambiente. La Figura 9 muestra los mar mejores decisiones de gestión que si éstas componentes del Programa Administración de tienen sentido. Las herramientas y las máquinas Nutriente 4R, que fue construido usando la fuenson maravillosos bienes pero es necesario seguir te adecuada, a la dosis correcta, en el momento las recomendaciones de la ciencia agronómica y y lugar adecuados para conocer las necesidades de la experiencia. económicas, medioambientales y sociales de un sistema sostenible de toma de decisiones de manejo de nutrientes.

Manejo de nutrientes Los factores ennumerados alrededor del diagrama son varios de los indicadores del rendiAdministración de nutriente 4R miento, usados para determinar la efectividad del La industria de fertilizantes, en cooperación sistema de gestión en el cumplimiento de sus obcon científicos alrededor del mundo han desarro- jetivos. La tecnología de precisión juega un papel llado el Programa de Administración de Nutrientes importante en muchas de estas prácticas.

Figura 9. Diagrama del sistema de gestión de administración de nutrientes 4R

125 PARTE 3

### Página 128

Fuente los materiales fertilizantes, tales como el N que son

El sistema 4R de gestión de nutrientes comien- suceptibles a las pérdidas del campo. El objetivo es za con la fuente adecuada. Diferentes fuentes de hacer que todos los nutrientes del cultivo estén en nutrientes pueden ser seleccionadas de diferentes el momento justo y con la dosis óptima para conocultivos o condiciones del campo o para diferentes cer las necesidades del crecimiento del cultivo. épocas del año. La agricultura de precisión puede Lugar ayudar a los agricultores a reconocer que fuente Otro uso importante de la tecnología de precisión de nutrientes sería mejor para el cultivo y la époes para la colocación del fertilizante. La dirección ca de la aplicación. Las formas pueden ser seco, Tiempo Real Cinemático15 permite precisión en la líquido, suspenciones o gas (amoníaco anhidro). colocación con 2 o 3 cm o a menor variación. Con la Cada uno tiene diferentes características que afecdirección RTK los nutrientes pueden ser colocados tan su utilidad para brindarle nutrición a la planta. exactamente en la banda de fertilizante donde ellos La cantidad necesaria para cada cultivo depende son necesarios y las semillas pueden ser plantadas de la decisión de cuál es la fuente más adecuada. en una ubicación exacta con respecto a la banda de Dosis fertilizante, aún varios meses más tarde.

La dosis en la que el fertilizante es aplicado es

Siembra

una de las aplicaciones más importantes de la tecnología de la agricultura de precisión. Como se des- En la siembra, la tasa variable parecería ser una cribía anteriormente, los mapas y sensores pueden práctica natural para ser usada en la gestión de siser usados para determinar la dosis adecuada para tio-específico. Y está siendo adoptada por algunos agricultores para ajustar la tasa de siembra a los aplicar el fertilizante. Los controles de precisión puemejores y más apropiados tipos de suelo, capaciden ser usados para ajustar la dosis durante la aplidad de agua u otro criterio. Desafortunadamente, cación. Los diferentes sistemas pueden ser usados es mucha la información que se necesita para topara presiembra, side-dress y top-dress. La tecnolo- mar decisiones prácticas y científicamente válidas gía de precisión brinda varias opciones para ayudar a para saber cuál es la tasa de siembra adecuada seleccionar la mejor dosis para cada campo. para las diferentes partes del campo. Cuanto más información sobre los campos individuales este Tiempo disponible y más relaciones agronómicas puedan Las diferentes tecnologías disponibles permi- ser definidas entre los parámetros de los campos ten a los agricultores la aplicación del fertilizante en variables, la siembra de tasa variable se convertirá tiempo para emparejar el desarrollo del cultivo. Los en una práctica más común. Ya que las relaciones monitores y modelos metereológicos pueden ser a menudo son dependientes de la composición de gran ayuda en el seguimiento del desarrollo del genética del híbrido o de la variedad, se complican cultivo para predecir el momento adecuado para las aún más las posibilidades de utilización de la siemaplicaciones de nutrientes. El tiempo de aplicación bra de tasa variable. debería adecuarse a la necesidad de absorción del cultivo tan estrechamente como sea posible para 15 RTK, por su sigla en inglés

126

### Página 129

Manejo de plagas gistros precisos y detallados de las actividades,

La variedad de prácticas en el manejo de pla- los insumos y la producción de todo el campo. El gas es probablemente aún más desafiante. Para monitoreo minucioso es de gran ayuda para idenlos insectos, hay una tendencia a que la infección tificar cambios en el sistema, que son necesarios sea general a través del campo. Sin embargo, los en cada temporada y para hacer un seguimiento ácaros tienden a concentrase en áreas pequeñas de las tendencias de los niveles de nutrientes y de y la tasa variable de tratamiento puede ser más la respuesta en la cosecha. efectiva y económica.

Varios monitores, sensores y modelos pueden Investigación agrícola: una llave de paso ser herramientas útiles. Las herramientas tecnoló- hacia la gestión de sitio-específico gicas pueden ser efectivas para la exploración de La implementación exitosa de la agricultura de los ácaros de cultivos de soja, cítricos y frutas. Las precisión depende de la capacidad para identifienfermedades infecciosas son a menudo pronos- car la variabilidad en los campos y para entender ticadas usando modelos de información del clima como se maneja esta variabilidad. La mejor aproen el lugar o una base más amplia de datos cli- ximación es aprender todo lo que se pueda sobre máticos de fuentes centrales y de internet. Por el las características del campo a través de los mécontrario, las aplicaciones de tecnología de tasa todos como prueba de suelo, mapeo de la variavariable son limitadas, pero la tecnología es toda- bilidad de suelo y monitoreo de la variabilidad de vía importante en la gestión de un campo a escala. rendimiento.

El control de malezas es probablemente la aplicaLa prueba de suelo es una herramienta imporción más importante en el control de las plagas de tante para determinar la variabilidad en los nutrienuna tecnología de tasa variable. tes del suelo. Para desarrollar recomendaciones Los sensores pueden ser usados para detectar que son más específicamente adecuadas para la densidad de la infección y en algunos casos aún una granja o campo individual, los datos de resayudan a identificar las especies de malezas. Los puesta del fertilizante recolectados por el agricultor mapas de infecciones de maleza de años anterio- sobre la gestión de su propio campo puede ser un res, la exploración de sus resultados y sus senso- recurso valioso. Con la tecnología de la agricultura res son usados para definir las áreas dentro de un de precisión es relativamente fácil para un agriculcampo que pueda necesitar aplicaciones de herbi- tor construir su propia base de datos de respuesta cidas especiales – producto o tasa – y para ubicar de nutriente. La investigación agrícola de parcelas un problema particular de maleza. puede ser realizada para establecer las calibraciones de respuesta de fertilizante para las pruebas Implementación de la agricultura de precisión de suelo de este campo.

La implementación del sistema de la agricultura Con la tacnología de precisión, es relativade precisión es un gran compromiso. Para ganar mente fácil para los agricultores hacer sus proel mayor beneficio de la inversión en tecnología, pias investigaciones, usando su equipo agrícola un agriculror y sus asesores deben mantener re- normal y con muy poca o ninguna interrupción de

127 PARTE 3

### Página 130

la actividad normal del campo. De hecho, cada zadas automaticamente, como muestra la Figura campo podría convertirse en un campo de inves- 10. Luego de los tiempos de cosecha, la informatigación para nuevas prácticas de prueba de pro- ción recolectada por el monitor de rendimiento del ductos, insumos o tasas de aplicación. De esta mismo campo puede ser extraída y unida con las forma el agricultor y sus asesores pueden usar parcelas de fertilizante para determinar la relación información de sus propios campos para guiar las entre el fertilizante aplicado y el rendimiento. Esa decisiones de cómo mejorar su sistema de pro- información junto con las pruebas de suelo puede ducción de cultivo. ser usada para guiar recomendaciones para fuEl estudio de la tasa de respuesta puede ser turas aplicaciones en ese campo y otros campos realizado con el controlador de la tarjeta de datos manejados de forma similar. Las parcelas agrícolas en el controlador de la tasa de fertilizante, de ma- también puden ser establecidas para estudiar otras nera que el fertilizante es esparcido a través del prácticas de gestión, por ejemplo los productos de campo, las parcelas con diferentes tasas son tra- insumos, la labranza, el momento adecuado, etc.

Figura 10. Este mapa muestra en donde fue establecido un conjunto de parcelas de tasa de N en un campo de maíz, usando el controlador sobre el aplicador de fertilizante. Tomando en cuenta que esta prueba tiene seis tasas diferentes de N, cada cuatro veces duplicada

128

### Página 131

Esto permite con un análisis simple de estadística ayudar a remover los efectos de la variabilidad en el campo. Las parcelas son cosechadas como lo son las del resto del campo sin interrumpir las operaciones normales del campo. Los datos de la parcela son extraídos más tarde del monitor de rendimiento de la cosechadora.

Las comparaciones agrícolas son una parte importante de los sistemas de mejora de la producción del cultivo. La Figura 12 muestra un ejemplo de cómo tales comparaciones pueden ser hechas, usando un equipamiento normal de campo y con una muy pequeña interrupción de las actividades

Figura 11. La información del estudio de N muestra que la tasa óptima regulares del campo. Para evaluar el valor de la de N fue alrededor de 150 Ib N/A tasa variable de la aplicación de N, el N fue apli-

Figura 12. Ejemplo del plano de un campo de comparación agrícola de tarifa plana y aplicación de tasa variable N en una franja de prueba. Un estudio duplicado separado sobre la tasa de N es incluido en el lado izquierdo para ayudar a definir la tasa de N óptima para el campo. (Fuente: Dan Schaefer, Illinois Council on Best Management Practices, 2013)

129 PARTE 3

### Página 132

cado en franjas usando la tasa variable de N ba- tigación para evaluar nuevos productos y nuevas sada en la variación de tipo de suelo, mostrada prácticas. Las comparaciones agrícolas son vapor la franjas de variable coloreadas de verde. Las liosas porque ellas prueban las nuevas ideas en franjas alternadas (áreas anaranjadas) tuvieron una la gestión del propio agricultor y en sus propios aplicación de N acordes al promedio de N requeri- campos. do por el campo. Comparando el rendimiento total Los sistemas de guía de alta precisión, como (o el beneficio) desde las franjas de VRT con las los RTK, son necesarios para usar alguna de las franjas promedio del campo, se puede determinar aplicaciones específicas de la tasa variable. Esto si la VRT fue justificada y hacer planes de futuro requiere más señales sensibles con puntos de reacordes. ferencia con base en tierra para usar en conjunto Se señala que en este caso un estudio de tasa con las señales satelitales. Pero los ahorros en refue realizado en el lado izquierdo del mismo cam- ducción de superposiciones y saltos en las aplipo, usando parcelas más pequeñas pero mane- caciones del campo pueden pagar por los costos jado con un equipo normal a escala del campo. extra. Menos semillas, químicos y fertilizantes son Tales comparaciones de campos pueden ser im- necesarios sí la dirección es la precisión. Menor plementadas con la tecnología y las herramientas cantidad de combustible es usado. Más granos de dirección en la granja y puede ayudar a cada son cosechados sí la distancia entre surcos es unicampo a convertirse en un sitio valioso de inves- forme y precisa.

Figura 13. Un drone volando sobre un campo de cultivo de trigo. Otro drone usado para la exploración aérea de varias parcelas de trigo. Fuente:

Progressive Farmer, Dan Schaefer & DTN, 2013

130

### Página 133

Tecnología de vehículo aéreo no tripulado 3.2. Sistemas de guía por satélite,

y drones automatización agrícola y

La nueva tecnología que ha llegado al mercado controladores electrónicos

agrícola es el VANT, a veces se refiere a ellos como

drones16. El tamaño y el costo de los VANT y dro- Stanley Best

nes se han vuelto más accesibles en los últimos

dos o tres años. Estas unidades pueden ahora Stanley Best

ser equipadas con varias cargas útiles, como por

Doctor en Ingeniería Agrícola y Recursos

ejemplo cámaras, para ayudar con la exploración

u otras actividades del campo. Biológicos

Existen posibilidades de la utilización de dro- Director Nacional del Programa Agricultura de Precisión INIA nes para la aplicación de reguladores químicos de Quilamapu Chile crecimiento y pesticidas. Los sistemas de control sbest@inia.cl se han vuelto muy sofisticados y precisos. Ellos pueden ser programados para seguir un camino predeterminado y regresar después de completar Introducción su misión. Recientemente drones del tamaño de Una de las tecnologías que es promisoria para una mosca doméstica han sido usados con éxi- el mejoramiento del sector productivo a nivel predial to. ¿Cómo pueden ser usados en agricultura? No es la agricultura de precisión. Esta herramienta asocabe ninguna duda que alguien encontrará una ciada a las tecnologías de la información y basada manera de usarlos. en el posicionamiento satelital, consiste en obtener datos georreferenciados de los predios para un Reflexión mejor conocimiento sobre su variabilidad espacial a nivel de rendimiento y calidad. En general los sitios La producción de cultivo está haciendo uso de más pueden presentar distintos tipos de variabilidad, daherramientas tecnológicas todos los días. Hoy en dos por: topográfica, génesis de suelo, distinto tipo día, las herramientas agrícolas usadas a diario no de manejo, etc. Mientras mayor sean los diferenciaeran ni siquiera soñadas 15 años atrás. No se puede les de rendimiento existente en un sitio, mayor será predecir cuáles serán las tecnologías agrícolas del el éxito de obtener resultados con una estrategia de futuro. Pero es un buen plan continuar evaluando lo aplicación variable de recursos (agua, fertilizantes, que está disponible y sí es lo suficientemente flexible semillas, agroquímicos, etc). para adoptar las nuevas tecnologías que se adapten En la actualidad las tecnologías asociadas a la mejor al cada sistema de producción. aplicación variable de insumos son una realidad y pueden estar al alcance de todos. Estas herramientas de la agricultura de precisión corresponden a máquinas y equipos inteligentes que

16 Drone, del inglés: zángano. ejecutan tareas precisas con el apoyo de la infor-

131 PARTE 3

### Página 134

mática, la electromecánica, el GPS, etc; las cua- monitores miden rendimiento, humedad, flujo, veles integradas a los sistemas comunicacionales locidad, evaluación de superficie, entre otros. En lo permiten una gestión oportuna de las acciones que respecta a calibraciones todos los monitores productivas. deben ser calibrados en peso, humedad (excepto Las máquinas o equipos reciben en su com- AGCO, Figura 1) y distancia (se debe corroborar putadora las órdenes de aplicación variable de en caso de no ser medida por GPS). insumos que están debidamente georreferencia- Los mapas de rendimiento permiten cuantificar das, las cuales hacen que actuadores hidráuli- la variabilidad de rendimiento existente durante la cos o electrónicos realicen la labor de aplicar los cosecha de un cultivo dentro del potrero, quedaninsumos en el lugar y la cantidad correcta (agua, do grabada espacialmente. Los mapas de rendisemilla, fertilizante y pesticidas). Este factor que miento son uno de los principales componentes permite generar registros de las acciones desa- en la agricultura de precisión debido a su utilidad rrolladas como certificación de calidad, sí son tanto en el desarrollo como en las estrategias del integradas a herramientas comunicacionales pue- manejo de precisión. den ser evaluadas a tiempo real. Entre estas heEl contar con información georreferenciada es rramientas electrónicas se encuentran el monitor un paso importante en la aplicación variable de inde rendimiento, el banderillero satelital, el sistema sumos, permite determinar la variabilidad presente autopiloto, entre muchos otros que se explican a en el potrero. Para ello existen diferentes herracontinuación. mientas que pueden llevar a una mejor definición de los ambientes homogéneos presentes en un Monitores de Rendimiento potrero, tales como: carta de suelos, fotografías Los monitores de rendimiento (Figura 1) han aéreas, imágenes satelitales, entre otras. Una de sido diseñados con el objetivo de recolectar da- las herramientas más destacadas es el mapa de tos para su posterior análisis. Los datos almace- rendimiento, debido a que permite saber no sólo nados por hectárea son alrededor de 600 puntos la variabilidad presente en el potrero sino también dependiendo de la frecuencia, los que son gra- cuantificarla, metafóricamente, es una radiografía bados en la tarjeta de memoria. La superficie que del potrero. abarcan los puntos de rendimiento está com- El mapa de rendimiento facilita la cuantifipuesta por el ancho de la plataforma de la cose- cación de la variabilidad natural de un potrero. chadora y la distancia recorrida en el tiempo que Además mediante ensayos debidamente protarda en grabar un dato y otro. Cuando el monitor gramados aporta datos de respuesta variable a de rendimiento de la cosechadora está conecta- la aplicación de insumos. Si esos datos son indo a un GPS, esos datos pueden componen un terpretados correctamente y apoyados con un mapa de rendimiento. muestreo de suelo por sitios homogéneos, guiaLos monitores son muy similares en cuanto a do y posicionado adecuadamente, aportarán clala información que brindan pero tienen una serie ridad en la toma de decisiones para la aplicación de diferencias en cuanto su calibración. Todos los variable de insumos.

132

### Página 135

Figura 1: Monitores de rendimiento más difundidos

Existen en el mercado diversas herramientas otros han sido más pasivos, pero a medida que para medir caracteres específicos, con el objetivo la tecnología se ha convertido en una parte del de dejar de utilizar dosis uniformes y pasar a utilizar procedimiento de operación estándar o más bien dosis variables, sin embargo, es necesario tener dicho en una práctica común, como es el caso en cuenta ciertos parámetros para evitar errores. del banderillero satelital en la pulverizadora. En este caso la adopción ha sido lineal debido a sus La recomendación a realizar en cada zona en ventajas directas, al reemplazar el trabajo insalubre particular, depende de la adecuada prescripción y y rudimentario de los banderilleros humanos y al éxito de la dosis variable asociada. Este es uno de permitir el trabajo nocturno. El banderillero satelilos puntos clave que se debe estudiar para de- tal permitió reemplazar el trabajo insalubre y rudisarrollar una metodología práctica para ser usada mentario de los banderilleros humanos y habilitó el por los productores. trabajo nocturno, lo que ha llevado su instalación Algunos productores han incorporado activa- en gran cantidad de pulverizadoras y en todos los mente esta tecnología a sus sistemas de gestión, aviones aeroaplicadores.

133 PARTE 3

### Página 136

Figura 2. Ejemplo del moderno panel de control de un banderillero Satelital Figura 3. Monitor de aplicación variable de agroquímicos

Es creciente, también, la cantidad de sembra- cultivos, conectados a DGPS permiten obtener doras cuyas funciones son monitoreadas median- mapas precisos de la distribución espacial del prote controladores de siembra. Estos equipos infor- ducto aplicado. man sobre la dosificación de semilla y fertilizante.

También permiten conocer valores entre los que se

destacan la velocidad de avance, la capacidad de Monitoreo de siembra de precisión trabajo y la densidad de siembra. También detec- En la actualidad son muchas las compañías tan anomalías en la entrega de semillas, asociados tanto locales como internacionales que desarrollan a dosificaciones menores o mayores al objetivo y comercializan este tipo de equipos, permitiendo o cuerpos obturados que no entregan semillas. al agricultor y prestador de servicio poder monitoEstas ventajas directas sobre la performance de rear la gestión de siembra. Estos equipos poseen la maquinaria y del operario, han producido la una serie de sensores los que permiten monitorear adopción de este tipo de equipos sea inobjetable, las caídas de fertilizantes y semillas para evitar talogrando un alto incremento de adopción por los ponamientos u mala dosificación de insumos. agricultores de EEUU y de diferentes países de Entre los sistemas de monitoreo de siembra Europa y de América Latina. se destacan por su buena relación precio/calidad los desarrollados por la empresa argentina Control Aplicador variable de agroquímico Agro y Plantium entre otros en la región, como Los sensores de aplicación variable de agro- Precisión Planting en EEUU por nombrar algunos. químicos permiten dosificar en forma eficiente la Por otra parte, este tipo de sensores también cantidad de pesticidas según el área foliar de los pueden ser utilizados en conjunto con cajas reduc-

134

### Página 137

Figura 4. Sistema de monitoreo y de siembra variable montado en una sembradora de la empresa BHV, dinámica presentada en Chile, (derecha) y sistema incorporado en plataforma digital (izquierda)

toras para el control de siembra y fertilización varia- el apoyo de un sistema de posicionamiento del ble. Estas últimas, responden a las variaciones de tipo Tiempo Real Cinemático (RTK, por su sigla diagnóstico agronómico geo-posicionado dentro en inglés) que permiten direccionar al tractor con de un potrero, así como a prescripciones de dife- altísimas precisiones, evitando los errores en las lírentes densidades de siembra (también pueden ser neas de siembra y pulverizaciones. En general este incluidos los fertilizantes asociados), o sea que, una vez cargado el mapa de prescripción del potrero, se pueden establecer en el potrero diferentes sitios de rendimientos potenciales. Ya cargadas las prescripciones de semilla y fertilizantes para cada sitio (mapas) y calibrada la sembradora; la máquina al ser posicionada por señal de GPS o DGPS (GPS Diferencial o sub-métrico) realiza la aplicación variable de acuerdo a la prescripción. En América del Sur ya existe este tipo de máquinas de fabricación local (Brasil y Argentina, Figura 4).

Sistema autopiloto de guía

Un piloto automático (Figura 5) es un sistema

electro-mecánico e hidráulico, utilizado para guiar

un vehículo sin la asistencia de un ser humano. Figura 5. Sistema autopiloto montado en tractor y siembra realizada con autopiloto Actualmente este tipo de equipos es utilizado con

135 PARTE 3

### Página 138

sistema podría ser implementado en los prestado- Por otro lado, los sistemas de navegación y res de servicio de siembra y fumigación quienes guía basados ​​en la visión artificial no son complia través de esta tecnología verían incrementar los cados y sólo utilizan los marcos de imagen capturendimientos de su trabajo y entregarían un servi- rados por una cámara fija del tractor. Este último cio de calidad para el productor de achicoria que sistema ha demostrado tener bajos errores y su se traduciría en mejores rendimientos del cultivo. uso no depende necesariamente de las condiciones climáticas, como ocurre algunas veces con los sistemas satelitales (DGPS, RTK).

Sistema de visión artificial de ópticos de

Los sistemas de guía por visión artificial, se baauto guía

san en realizar el trazado de guía acorde a la orienLos sistemas de guía automática o autopiloto pue- tación de objetos visibles en el terreno (tales como den reducir en gran medida la fatiga de conductores y hilera de siembra, surco, etc., Figura 6). La tecnolotienen como resultado el aumento de la productividad gía de visión artificial de la máquina tiene la ventaja y la seguridad de las operaciones agrícolas. de utilizar las características locales para afinar el Diferentes enfoques se han estudiado para la curso de navegación del vehículo. Así, los sistemas realización del guiado automático de las máquinas de guía por visión artificial poseen características agrícolas. En los sistemas de autopiloto se usan una tecnológicas muy parecidas a las que posee un combinación de soluciones existentes, incluyendo el operador humano, sin que exista la posibilidad de DGPS, RTK y sistemas de visión por computadora. que éste se canse y, por ende, cometa errores.

Figura 6. Ejemplos de sistemas de guía por visión artificial

136

### Página 139

El SmartSteer (Figura 7) es un sistema de au- Sembradoras variables de alta precisión toguiado para las cosechadoras New Holland CX Este tipo de sembradoras a diferencia de las y CR que permite controlar de manera automática expuestas anteriormente, utilizan un sistema RTK la dirección de la cosechadora, aprovechando al de guía en la siembra y un sistema de alta precimáximo la anchura de corte del cabezal. Para ello sión en la localización de la semilla, permitiendo loutiliza un láser de infrarrojo que detecta el borde grar una siembra altamente precisa, útil para el uso del cultivo que está sin cosechar. Los cambios de la señal y en el rastrojo son reflejados en el culti- de maquinaria de control de malezas mecanizadas vo e informan sobre la posición de la cosechadora que se expone más adelante en este capítulo. respecto al borde de la cosecha. El sensor se encuentra situado en el lado izquierdo de la cabina, debajo de la extensión del techo, el cual puede detectar la línea siega (difícil para el operador) a ambos lados de la cosechadora. Se puede cambiar de cabezal, en función del tipo de cultivo sin que sea necesario modificar la posición del sensor de alineación. Se trata de un sistema autónomo e independiente de las señales externas, aunque compatible si se desea con los sistemas de GPS.

Más información sobre sistemas de visión artificial

y automatización agrícola se puede consultar en el

apartado 1.4. Adquisición remota.

Figura 8. Sembradora de alta precisión de la empresa Precision

Planting (EEUU)

Control de malezas de alta precisión

El control integrado mecánico se utiliza para la

eliminación de maleza en cultivos hilerados sembrados con alta precisión. El crecimiento de las malas hierbas dentro de las filas de cultivos es el principal problema para la respuesta en producción (en especial en los primeros estadios de la plata), debido a su alto costo y muchas veces a la imposibilidad

Figura 7. Sistema de auto guiado para cosechadoras: SmartSteer

de utilizar herbicidas. Hoy en día se han desarrolla-

137 PARTE 3

### Página 140

Figura 9. Control de malezas utilizando maquinaria automatizada. http://www.thtechnology.co.uk/

do maquinarias que en conjunto con una siembra Por su parte, las novedades en comunicación, altamente precisa y uso de un sistema de visión por internet y telefonía celular permiten que el produccomputadora, procesan la información que se va tor visualice lo que sucede en su campo, comancaptando en línea y ubican las plantas sembradas de sus equipos a distancia y acceda a mapas de mientras los cortadores se van moviendo para eli- rendimientos, aplicación y siembra en tiempo real. minar malezas (Figura 9). En las pruebas realizadas se han obtenido resultados sorprendentes, como por ejemplo, la eliminación de más del 80% de ma- Reflexión: La tecnología sigue avanzando y existe la leza en el cultivo sin daño al cultivo madre. impresión que ocurre más rápido que su asimilación.

Sistemas de monitoreo y control de Tecnología de riego variable

maquinaria agrícola

La alta variabilidad espacial en las condiciones

Una innovación interesante es el sistema de físicas del suelo se traduce en una des-uniformicontrol de maquinaria agrícola, que posibilita tener dad del agua de riego aplicada en el predio. Este un seguimiento de las labores realizadas por los problema generalmente no es considerado tanvehículos que están en el campo. Estos sistemas to para el diseño de nuevas obras de riego (astambién trabajan bajo plataformas en PC de es- persión, goteo y riego superficial) sino en las ya critorio y Smart Phones, es decir que es posible existentes. Dicha ineficiencia en la aplicación del seguir el funcionamiento del implemento del cam- agua de riego finalmente conlleva a pérdidas de po en tiempo real y a través del teléfono celular fertilizante nitrogenado y posterior contaminación o una tablet (Tracking de Maquinaria). Un ejemplo de los acuíferos subterráneos por lixiviación. El de este sistema es ConnectedFarm, un nuevo pro- conocimiento de áreas uniformes en propiedades ducto de Trimble (Figura 10). físicas y el uso de modelos computacionales, per-

138

### Página 141

Figura 10. Esquema de funcionamiento de Connected Farm

miten un mejor manejo del recurso hídrico, con un do a su poca necesidad de mano de obra y manaumento de la eficiencia de uso, tanto del agua tenimiento, y alta flexibilidad de operación. Bajo un como de fertilizantes nitrogenados, protegiendo adecuado diseño el sistema genera aplicaciones así las aguas subterráneas de contaminantes. de agua de alta eficiencia, conservando tres preInformación de variabilidad sobre la cual se ciados recursos: agua, energía y tiempo. asociarán los cambios en propiedades físicas (tex- Hoy en día, los pivotes son impulsados ​​ por tura, velocidad de infiltración, capacidad de retenmotores eléctricos o de aceite hidráulico situado ción, etc.) es de alta relevancia para la sectorizaen cada torre y guiado por un panel de control. ción de zonas de producción que permitan evaluar Este sistema utiliza bajas presiones de operación o modificar el uso de sistemas de riego. entre 10 a 15 psi (en la línea principal de pivote), las que suelen ser suficientes para el correcto funSistema de aplicación variable de riego cionamiento de pivotes diseñados por LESA (aplipara sistemas presurizados cación de pulverización de baja elevación) y LEPA El Pivote Central es uno de los sistemas más (baja solicitud de precisión y energía), con pivotes usados en la agricultura tradicional de riego, debi- de hasta 400 m de largo en el nivel operativo y

139 PARTE 3

### Página 142

con una moderada inclinación de campos. Poseen o la que incorpora la variabilidad también en la una eficiencia de aplicación de agua de 85 a 98 línea de riego. Ambos incorporan la posibilidad por ciento. de riego variable y son los de mayor precisión Los avances en riego tecnificado han sido un en cuanto a capturar la variabilidad de riego pero importante factor para la agricultura, optimizando poseen la desventaja de poseer un altísimo costo un recurso limitado y dando seguridad de riego (cercano a los US$ 30 000). para la producción de cultivos. Si bien los avan- En el caso del sistema de riego variable por ces en esta área son importantes, es factible apli- zonas existen actualmente dos grandes marcas, car tecnología de avanzada que permita realizar el sistema australiano canlink3000 (figura 13) y el mejoras al sistema. En el caso de la aplicación sistema Valley Zone Control (figura 14). Ambos sisvariable de riego en pivotes, para la cual se iden- temas se basan en la definición de la variabilidad tifica la variabilidad espacial de los requerimien- del suelo, como ya lo hemos descripto, sobre la tos hídricos bajo el área cubierta por el pivote, generación de una segmentación por trazos del ya sea por la existencia de diferentes cultivos o pivote para la aplicación de riego, según tipo de por diferentes condiciones de suelo. En el caso suelo y necesidad de los cultivos. de riego variable en pivotes existen dos grandes El uso de este tipo de tecnología permite un incorporaciones tecnológicas que están asocia- ajuste de las cargas de agua cercanas a la variadas, al riego por zonas angulares (trozos de torta) bilidad existente en el predio. En las imágenes si-

Figura 11. Sistemas de aplicación variable de riego por sectores angulares (izquierda) y por zonas (derecha)

140

### Página 143

Figura 12. Sistema de riego diferencial FarmScan (a) desuniformidad del suelo (b) panel de control, sistema FarmScan (c) vista aérea y subdivisión de áreas de riego (d) mapa de aplicación de cargas de agua

guientes se visualiza un ejemplo de un predio que por ejemplo aplicar agua después de una lluvia, utilizó el sistema Valley, se puede observar una por topografía, por tipo de suelo, pivotes con dos mejora gradual de la cobertura del suelo, que fi- cultivos, o según densidad de siembra (VRT), entre nalmente terminó sin zonas débiles particulares, a otros (figura 16). excepción de las áreas donde el cultivo fue volado por el viento al inicio de la temporada.

Otra forma es la utilización de riego por zonas

angulares, ajustando los ángulos de riego a la

variabilidad del suelo existente (Figura 15).

Este tipo de equipos de control por ángulos

(Figura 15) puede ser utilizado para realizar aplicaciones en función de diferentes parámetros como

141 PARTE 3

### Página 144

Figura 13. Sistema de riego diferencial Valley (a) desuniformidad del

suelo, evaluado con EM38 (superficial y profundidad); (b) panel de

control de la aplicación diferencial Valley

Figura 14. Visualización de imagen multiespectral de un pivote

utilizando el sistema Valley de aplicación variable de riego

Figura 15. Equipos comerciales de manejo diferencial por ángulos AGsense (superior) y Linsey (inferior)

142

### Página 145

Figura 16. Zonificación de riego según: rendimiento (A), posterior a lluvia y tipo de suelo (B), dosificación variable de semillas (C), y topografía (D)

Robotización de la agricultura estado actual y de las ventajas y posibilidades de Actualmente, el sector agroalimentario es ob- robotización de las tareas agrícolas. Los objetivos jeto de especial atención en cuanto a la incorpo- que se plantean con la robotización agrícola son: ración de tecnologías avanzadas, debido a las • Permitir la sustitución de operarios en tareas exigencias cada vez mayores de producción, di- peligrosas para la salud, como la pulverización versidad y calidad de los productos, así como de de productos fitosanitarios. la presentación de los mismos. A lo anterior, se suma el problema creciente de la falta de mano • Abordar la realización de tareas repetitivas y tede obra. Cabe por lo tanto, hacer un análisis del diosas, como la recolección de frutos.

143 PARTE 3

### Página 146

• Realizar tareas en horas nocturnas, lo cual permite el ahorro de tiempo, por ejemplo, en la recolección.

• Mejorar la precisión en algunas de las tareas

agrícolas, como las relacionadas con la biotecnología, y en concreto la multiplicación de plantas a partir de tejido vegetal.

• Optimizar la eficiencia y calidad de algunas de

las tareas como la uniformidad en la realización

de huecos para el trasplante.

• Lograr la disminución de riesgos ambientales

como la reducción de la cantidad de producto

fitosanitario que se emite al aire.

Figura 17. Robocrop, tractor robotizado de la empresa Tillett and

• Reducir costes, ya que se disminuye la canti- Hague Technology Ltd., para eliminar la maleza de forma mecánica sin dañar el cultivo útil dad de combustible y de productos utilizados en algunas tareas.

• Elevar la calidad de los productos como por Robot utilizado para la preparación del ejemplo, la utilización de menos pesticidas. cultivo de viñedos: este robot podador desarrollado por la empresa Vision Robotics Corporation Existen hoy en día claros ejemplos de la ten- (VRC), se especializa en el corte preciso y limpio dencia global en la incursión de la robótica, como de los viñedos. La clave de la robótica aplicada a se detalla a continuación. viñedos, es el uso en el robot de cámaras estereoscópicas de exploración que realizan 15 fotoRobocrop gramas por segundo. El análisis de toda la vid y Es un tractor robotizado con visión por com- del trabajo a realizar se procesa antes de que las putadora basado en un sistema de orientación tijeras del robot comiencen a podar la vid. A bordel control de químicos en malezas, desarrollado do del robot, un equipo procesa y utiliza la superpor la empresa Tillett and Hague Technology Ltd., posición de múltiples fotos para crear un modelo Inglaterra. Este robot usa navegación por guia- 3D de la vid y, a c ontinuación, se aplican normas do a través de las líneas de cultivo y al detectar de poda, que fueron programadas en el software, una mala hierba por medio de la visión artificial, guiados por un experto. Estas normas son proceéste la elimina a través de un corte realizado en sadas, para luego indicarle a los brazos robóticos forma mecánica. Este robot se comercializa como hidráulicos con tijeras, la forma en que deben poRobocrop, ver Figura 17. dar y dónde hacer los cortes (Figura 18).

144

### Página 147

Finalmente, es claro que la necesidad de alimento sano, ambientalmente sustentable y económicamente rentable, está guiando un cambio en el desarrollo de la agricultura. En la cual no solo la genética tendrá un rol importante, sino también se visualiza un rol fundamental de las tecnologías asociadas a la automatización de equipamiento agrícola, relacionadas al mundo globalizado de la información. Las grandes corporaciones internacionales tales como John Deer, CNH, Monsantos, Bayer entre otras, están invirtiendo en estas líneas

Figura 18. Brazos robóticos del Robot podador de viñedos y abriendo espacios a nuevos desarrollos. Por otra parte, se están creando un sin número de pequeñas empresas tecnológicas y de servicios de agricultura de precisión, que están forjando el cambio de paradigma de producción agrícola, gestando un nuevo salto que quizás se mayor al de la revolución verde.

Figura 19. Proyección de la robótica en la agricultura.

Fuente: N. Noguchi, 2013

El avance en el área de la robótica es cada día

más importante, en especial en países avanzados

con un alto costo de mano de obra, tales como

Japón, Corea y EEUU entre otros. En la Figura 19,

se visualizar una proyección en la evolución de la

robótica en la agricultura.

145 PARTE 3

### Página 148

3.3. Sensores de nitrógeno para la de los cultivos, para lo cual es necesario contar con elementos de toma de decisión adicionales. medición y aplicación en el cultivo Cabe mencionar que en el caso de nutrientes taen tiempo real les como el fósforo, cuya disponibilidad no cambia Lorenzo León abruptamente en el tiempo, esta metodología presenta menores errores en cuanto a las prescripciones desarrolladas.

Lorenzo F. León G.

Es en este contexto donde surge una segunda

Ingeniero Agrónomo, Magister en Ciencias Agropecuarias

aproximación o metodología, desarrollada princiINIA – Chile

palmente para la fertilización nitrogenada, la que

lleon@inia.cl

está basada en la detección remota y aplicación

en tiempo real en función del estado actual del culIntroducción tivo. En virtud de esta detección remota, se realiza una prescripción nitrogenada tomando en consiPara la aplicación de prescripciones nitrogena- deración un algoritmo o fórmula de cálculo, la cual das variables espacialmente, existen dos aproxi- puede operar bajo distintos principios agronómimaciones principales. Una primera metodología cos. Para desarrollar la detección remota de cultipara esta aplicación está basada en las propieda- vo requerido en esta metodología, distintos sensodes de los cultivos anteriores, tales como la distri- res han sido puestos a disposición del sector probución de los índices vegetativos y los rendimien- ductivo en los últimos años. Al igual que en el caso tos de las últimas campaña en cada uno de los de los algoritmos de cálculo de prescripción, estos lotes. Estas características pueden ser obtenidas sensores poseen diferentes principios de funciomediante el uso de los monitores de rendimiento namiento, siendo algunos más adecuados para el o sensores de canopia. Adicionalmente, las pro- uso en determinadas condiciones de cultivo. piedades físico hídricas de los suelos y su distribuEn el presente capítulo se desarrollará una breción espacial contribuyen a establecer este tipo de ve reseña de los principios involucrados en la defiprescripciones basadas en información anterior. nición de la aplicación nitrogenada en tiempo real, En este sentido, y tal como lo ha manifestado y una exposición más detallada de los sensores recientemente Hegge (2013), con esta aproxima- disponibles a nivel de mercado para incorporar dición se pueden generar importantes fuentes de cha metodología de medición y aplicación nitrogeerror asociadas a la prescripción nitrogenada a ser nada en tiempo real. desarrollada. Según Hegge(2013), esta desventaja está asociada principalmente a la escala de tiempo entre la captura de los datos de las capas Principios de la metodología de medición correspondientes a propiedades del suelo, al ren- de propiedades del cultivo y aplicación dimiento del cultivo y a la fertilización a desarrollar nitrogenada en tiempo real en la presente temporada. Esta problemática es Esta metodología posee distintos principios de especial cuidado en la fertilización nitrogenada de funcionamiento, que representan al mismo

146

### Página 149

Figura 1. Esquema general del funcionamiento y los principales elementos del sistema de aplicación de dosis variable de N. En el círculo rojo se aprecia la posición del sensor en el sistema de aplicación. Fuente imagen: Taylor y Fulton (2010)

tiempo una activa área de investigación y desa- que se obtienen de este modo dependen de una rrollo para optimizar el sistema. Según Hegge interacción entre las plantas y suelo. (2013), en términos generales la aplicación ideal para este método está asociada con el uso de Esquema general de funcionamiento sensores proximales para la determinación de las Según Taylor y Fulton (2010), un sistema de características del cultivo y en el control en tiempo real. Lo anterior significa que este método se tasa de aplicación variable en tiempo real de N puede adaptar bien a los nutrientes, para los que basado en sensores debería estar constituido por el cambio en el suministro hacia los cultivos es los siguientes elementos principales: sensores de bastante rápido, siendo el N el caso que ha te- planta, un módulo de visualización y control y un nido un mayor número de experiencias exitosas. controlador de velocidad de la aplicación (Figura De la misma forma, se ha considerado como una 1). Los sensores pueden ser utilizados para meventaja muy importante de basar el control sobre dir adicionalmente las propiedades del suelo. Sin las propiedades de los cultivos, que las señales embargo, en el presente capítulo el análisis está

147 PARTE 3

### Página 150

limitado a la función de la detección remota para la Según la descripción de McGrath (2012), los aplicación de la tasa variable de N. principales sensores activos utilizados comercialEl controlador de tasa de aplicación consiste mente emiten luz en las longitudes de onda (1) rojo en los siguientes elementos: una interfase de con- y (2) infrarrojo cercano (NIR, por su sigla en inglés). trol del usuario, un medidor de flujo, una válvula La reflectancia es calculada en función de la luz de control de flujo y un sensor de velocidad. Es que se recibe desde los cultivos, obtenidos los importante destacar que en algunos casos el mó- valores promedios en cada segundo de marcha y dulo de display y control puede ser el mismo para detección remota. A partir de esta información es el sistema de detección remota y el controlador de posible calcular distintos índices vegetativos, que tasa de flujo. Adicionalmente, si existe un módulo inmediatamente alimentarán los algoritmos de cálde GPS (lo que regularmente ocurre en la imple- culo en tiempo real. El índice vegetativo más conomentación actual de estos sistemas), éste es usa- cido y de mayor uso en este tipo de aplicaciones do con finalidades de mapeo de las características corresponde al Índice de Vegetación de Diferencia del cultivo, las dosis prescritas en tiempo real y las Normalizada (NDVI, de su sigla en inglés): velocidades de trabajo.

NDVI= (NIR – Red)/ (NIR + Red) Sensores e índices vegetativos

Donde,

Los sensores que pueden ser utilizados en el

sistema antes descrito, se pueden dividir en dos NIR: reflectancia del cultivo en el infrarrojo tipos principales: pasivos y activos. Aquellos co- cercano rrespondientes al primer tipo, dependen de la luz Red: reflectancia del cultivo en el rojo. ambiental para recibir la reflectancia de los cultivos, necesaria para el cálculo de los índices vegetativos. Por otra parte los sensores activos poseen Las plantas sanas y vigorosas absorben la luz una fuente de luz propia, con lo que la reflectancia roja y reflejan la luz del infrarrojo cercano, y el varecibida depende de estas fuentes de iluminación lor de NDVI se acercará a 1. Contrariamente, un artificial. En términos comerciales, actualmen- cultivo con bajo status de nitrógeno o enfermo, te predominan aquellos sensores de tipo activo, presentará un valor de NDVI más cercano a 0. En dado que sus prestaciones son mayores, en tanto condiciones de campo el rango real observado se que, actúan bajo diferentes condiciones de ilumi- encuentra típicamente entre 0,7 y 0,8 para un culnación, incluyendo la detección remota noctur- tivo sano y con suficiente N, y en el rango entre na, sin necesidad de un ajuste en función de la 0,25 y 0,3 para un cultivo que presenta una defiluz existente al momento de la aplicación. Por su ciencia extrema de N. Cabe mencionar que otros parte, los sensores pasivos necesitan de un sen- colores tales como verde o ámbar también se han sor de radiación para el ajuste de las lecturas y su utilizado en lugar del rojo al calcular el NDVI. En la empleo a nivel comercial no ha resultado ser masi- sección 3 del presente capítulo se mostrará con vo. Consecuentemente, en el presente capítulo se mayor detalle distintos sensores con los que es analizarán únicamente los sensores de tipo activo. posible calcular estos índices vegetativos en tiem-

148

### Página 151

po real como información base para la realización cultivo. De esta forma, esta franja se emplea para de las prescripciones. determinar la contribución del medio ambiente de nitrógeno. En la Figura 2 se puede observar el esAlgoritmos de cálculo para la prescripción tablecimiento de una de las mencionadas franjas nitrogenada en un cultivo de maíz.

Recientemente, Taylor y Fulton (2010), han

señalado que la elaboración de una prescripción

basada en sensores considera dos elementos

principales. En primer lugar, se debe tener claramente establecida la relación entre la propiedad de la planta de interés y su relación a la información entregada por los sensores. Este primer paso es necesario de ser considerado, ya que los sensores disponibles en el mercado pueden no medir en la misma forma o utilizar el mismo principio para el cálculo del índice vegetativo empleado para determinar la tasa de aplicación en tiempo real. Si

Figura 2. Franja de referencia de N para el cálculo de la prescripción

bien en la mayoría de los casos esta relación no en tiempo real. La zona sin limitación de N se muestra entre las líneas amarillas en la figura. Fuente imagen: Shannon et al. 2010 es perfecta, es probable que ella se pueda aplicar en un amplio intervalo de condiciones con algún error aceptable. En este sentido, distintos grupos de investigación de la agricultura de precisión en Consideraciones generales el mundo, actualmente trabajan para optimizar el Es necesario considerar que el requisito de N empleo de dicha información y algoritmos asocia- es complejo, por lo que es recomendable comdos bajo condiciones de alta variabilidad espacial prender los principios de acción de los sensores en las propiedades del suelo y comportamiento activos a ser empleados y, asimismo, la agronomía del cultivo. detrás de los algoritmos de cálculo. Actualmente El segundo paso corresponde a determinar varios de los fabricantes de estos sensores ofrela tasa de aplicación como una función de la in- cen determinados algoritmos robustos de cálcuformación entregada por el sistema de detección lo para facilitar el uso en el terreno. Sin embargo, remota, tal como las diferencias en los niveles de es deseable contar con una o varias experiencias NDVI. Para poder desarrollar dicha tasa de aplica- específicas de prueba de dichos sensores en el ción, uno de los métodos más usado corresponde área agroclimática y el cultivo en donde serán a la aplicación en función de una superficie o franja empleados. de referencia, que es un área donde se aplica su- Lo anterior es una consecuencia del hecho de ficiente nitrógeno para asegurar que este elemen- que el requerimiento de N para alcanzar el máximo to no sea un factor limitante en el crecimiento del rendimiento en un cultivo determinado está defini-

149 PARTE 3

### Página 152

do por distintos factores, tales como la capacidad desde la plantación, el rendimiento esperado a de respuesta de N, su disponibilidad y el potencial ser obtenido y las tasas de N aplicadas con antede rendimiento bajo las condiciones agroclimáti- rioridad. Según Roberson (2013), otros entradas cas específicas. Además, se debe tener en cuenta posibles de ser implementadas corresponden a que estos factores varían espacio-temporalmente la eficiencia del uso del N y la acumulación térmiy que en la mayor parte de los casos son indepen- ca a partir de la fecha de siembra. Por su parte, dientes uno de otro. Otros factores de importancia dentro de las entradas derivadas de los sensores, corresponden a las características físico-hídricas podemos considerar la información de la franja de del suelo, las condiciones del clima y de la gestión referencia de N (ver Figura 2), y el valor actual de predial. Estos últimos influencian notablemente el NDVI en donde la maquinaria se encuentra en un potencial de rendimiento, la disponibilidad de N y momento determinado en el campo. La variación la capacidad de respuesta de la aplicación de N. de este u otro índice a medida que la maquinaria En lo que concierne al momento de aplicación, se mueve a través del campo genera la informaalgunos de los principios básicos que señalan dis- ción necesaria para el desarrollo de la aplicación tintos autores son: en primer lugar la parcialización diferencial de N. de la aplicación nitrogenada en los períodos en La dosis de prescripción en tiempo real es calque el nutriente es más requerido. En segundo lu- culada mediante una fórmula que considera la ingar, es necesario considerar variables ambientales formación de entrada (usuario y sensores) antes tales como la tendencia climática de la tempora- mencionada. Dicha fórmula representa la parte da en curso, es decir, si esta es húmeda o seca central del algoritmo de cálculo. Existen distintos respecto del valor histórico y la relación de esta tipos de fórmula, dependiendo de la información condición ambiental con las variables edáficas del empleada, el equipamiento en uso y el cultivo a campo. Estas consideraciones ayudarán notable- ser fertilizado. En la Figura 3 (a y b) se puede obmente a incrementar la eficiencia del uso de nitró- servar dos relaciones que vinculan el NDVI medigeno aplicado a través de este sistema. do por los sensores y la prescripción finalmente desarrollada en tiempo real. En la Figura 3 (a) se muestra una relación lineal de cálculo en donde la Uso de algoritmos de prescripción en tiempo real dosis a ser prescrita de N, sube linealmente desde Se han generado distintos algoritmos de cál- un cultivo pobre en nitrógeno hasta un cultivo de culo para la prescripción de N en tiempo real. nivel medio (NDVI =0,67) y decae en forma lineal a Estos algoritmos consideran dos tipos principales medida que NDVI sube para los rangos en donde de entrada de información. En primer lugar están se encuentran las plantas que tienen mejores esaquellas realizadas por el usuario y en segundo tatus de nitrógeno (NDVI > 0,67). Por su parte, en lugar, las derivadas del uso de los sensores de la Figura 3(b) se muestra la relación entre NDVI y N que forman parte del equipamiento y que son la tasa prescrita para otro algoritmo de cálculo y motivo de análisis en el presente apartado. cuya relación entre la lectura de NDVI y dicha presSegún McGrath (2012), dentro de las entradas cripción nitrogenada es no lineal. En ambos casos, de usuario se pueden incluir los días transcurridos el método tiene como resultado privilegiar a las

150

### Página 153

Figura 3. Relación entre el índice NDVI medido por sensores y la tasa de aplicación calculada y aplicada en tiempo real para los dos ejemplo de algoritmo de cálculo. Fuente figura: McGrath (2012)

plantas que no han alcanzado un nivel óptimo de quema que siguen bajo evaluación en orden de nitrógeno, pero que tampoco están con un NDVI optimizar esta metodología de cálculo. Así, por demasiado bajo que corresponde a aquellas con ejemplo, Holland y Schepers (2013) han probado un potencial de rendimiento muy reducido. un método para reducir la dependencia del cálculo Es necesario recalcar el hecho que distintos de la prescripción nitrogenada al uso de la franja autores han señalado recientemente que esta me- de referencia. En tanto, otros grupos han visto altodología puede ser optimizada ostensiblemente tamente necesario el indagar sobre nuevos índices a través de la implementación de variables, como vegetativos capaces de evidenciar de mejor forma la conductividad electromagnética de los suelos. la variabilidad espacial del estatus de N en el camEn este sentido, la eficiencia de la nutrición nitro- po (Raper et al. 2013). genada sería un punto central a considerar en los algoritmos de cálculo. Con esto, el uso de mapas Controladores y sus ajustes de conductividad electromagnética así como la Según Taylor y Fulton (2010), un aspecto clave prescripción en tiempo real para la aplicación variable de N corresponde a un Ampliar información basada en las propiedades controlador de la tasa de aplicación correctamenen el apartado 2.4. de los cultivos han sido pro- te calibrado. En general dichas tasas prescritas se Aspectos económicos, puestos como una vía para pueden actualizar a cada segundo. Por esto, la análisis y viabilidad optimizar los algoritmos de calibración del controlador de flujos es de primera de la adopción de cálculo. importancia para seguir con precisión los resultaintervenciones en Finalmente, es necesario dos de esta prescripción basados en sensores y la los sistemas de mencionar que actualmen- aplicación en terreno, sin ningún tipo de desfase producción. te, hay distintos aspectos y temporal. El controlador de dosis debe ajustarse técnicas dentro de este es- para responder lo más rápidamente como sea po-

151 PARTE 3

### Página 154

sible mientras todavía se mantiene cierta estabili- espacial. Esto proporcionaría un mejor promedio a dad en el sistema. través de todo el brazo. Dicho valor medio se envía La capacidad de sintonizar un controlador de a la interfaz de usuario donde se convierte a una velocidad varía entre los fabricantes y modelos, tasa de aplicación, según lo señalado en el punto y puede poseer desde varios ajustes a ninguno. Uso de algoritmos de prescripción en tiempo real.

La mayoría de los sistemas de control de tasa A continuación se mostrará las características usan la velocidad de válvula para ajustar el tiempo correspondientes de varios de los sensores dispode respuesta, mientras que algunos pueden uti- nibles a nivel comercial. lizar otras configuraciones. El manual del operador debe utilizarse como una referencia para los N-Sensor Yara controladores de ajuste. En este sentido, hay que El N-Sensor Yara corresponde a un sensor actener en cuenta que la configuración predetermitivo que opera montado en la maquinaria y que nada para la mayoría de los controladores es para mide la reflectancia del cultivo a medida que esta el mantenimiento de la estabilidad en el sistema. se mueve a través del campo. Dicho sensor cuenProbablemente no son los mejores ajustes para el ta con un ángulo de visión oblicuo (Figura 4), con lo tiempo de respuesta óptimo y algún tipo de afinaque ha sido considerado de especial utilidad para ción o ajuste específico probablemente se requiera los cultivos en sus primeros estadios de desarrollo. para mejorar el rendimiento del controlador para la aplicación de la tasa variable de N. De esta manera, este sensor y su sistema asociado, es capaz de variar la tasa de aplicación de N asegurando la velocidad correcta y la óptima Sensores disponibles a nivel comercial cantidad de N aplicado en cada punto en el camLa mayoría de los sistemas de aplicación varia- po, según la prescripción desarrollada. La expeble de N basados en sensores poseen al menos riencia práctica ha demostrado que su empleo ha cuatro unidades de detección remota. Las inves- permitido aumentar los rendimientos en relación a tigaciones recientes han demostrado que existe las prácticas agrícolas convencionales en los luuna variabilidad de campo a una escala muy pe- gares donde ha sido implementado, minimizanqueña, por lo que, consecuentemente, la informa- do la pérdida y el consecuente impacto sobre el ción utilizada para alimentar el algoritmo de cálculo medio ambiente. Gil y Jiménez (2001), manifestaes mejor, sí se dispone de más sensores en la ma- ron que las ventajas más importantes del sistema quinaria que se encuentra desarrollando la aplica- N-Sensor son: el incremento obtenido del margen ción. Sin embargo, debe considerarse al mismo bruto por hectárea, la posibilidad de aplicación y tiempo un compromiso entre la obtención de más respuesta en tiempo real, la mejora de la calidad, y mejor información adquirida al tener más senso- la cantidad de producto obtenida y una mejor gesres y el coste final del sistema. En términos técni- tión y eficiencia en el uso del nitrógeno. Sin emcos, los aplicadores de un ancho superior a 15 m bargo, también se ha mencionado que el elevado deberían tener por lo menos seis sensores para la coste de adquisición de este equipamiento hace correcta caracterización de dicha microvariabilidad difícil su amortización en muchas explotaciones,

152

### Página 155

Figura 4. N-Sensor de Yara. (a) el sensor para la detección remota de los índices vegetativos va montado en el techo de tractor. (b) Dicho sensor mide en forma oblicua a medida que se realiza el escaneo y la aplicación en tiempo real en el campo. Fuente imagen: Yara Internacional

Figura 5. (a) montaje de sensores GreenSeker al frente de la maquinaria. (b) detalle de sensor, el cual es ubicado en forma perpendicular al cultivo.

Imagen Fuente: Vellidis y Lincopresicion

especialmente en aquellas situadas en zonas con Los sensores utilizan LED para generar luz de producciones reducidas. color rojo y el infrarrojo cercano, siendo posicionados en el frente de la maquinaria y perpendiculares GreenSeeker al cultivo. La luz generada se refleja en el cultivo y El GreenSeeker es producido por NTech se mide para el cálculo del índice NDVI, utilizando Industries, corresponde a un sistema de detección las bandas rojo y NIR. y aplicación, óptico integrado, que mide el estado Las recomendaciones de N se basan en el ponutricional nitrogenado en los cultivos, siendo ca- tencial de rendimiento del cultivo para la tempopaz de aplicar en tiempo real y en tasa variable los rada en curso y la capacidad de respuesta de los fertilizantes según las necesidades de N del cultivo. cultivos a la aplicación de N. El sistema modifica

153 PARTE 3

### Página 156

Figura 6. (a) montaje de sensores CropCircle ASC-210 al frente de la maquinaria. (b) detalle del sensor, el cual es ubicado en forma perpendicular al cultivo. Fuente imagen: Schepers

en cada sector del campo la tasa de aplicación genada. Entre otras utilidades, la información del según su algoritmo de cálculo interno. Este siste- sensor se puede utilizar para cuantificar el impacto ma es compatible con varios tipos de controlado- de los nutrientes, del agua, de las enfermedades u res de aplicación variable y sistemas de entrega. otras condiciones de crecimiento.

Los sensores GreenSeeker se se pueden montar El sensor ACS-210 se puede montar en cualen varias configuraciones en la maquinaria, con- quier tipo de vehículo para detectar de forma residerando una amplia gama de pulverizadores y mota la biomasa de la planta o el cultivo durante la esparcidores. conducción a través del campo, para la ejecución de la prescripción en tiempo real. Su tamaño comCropCircle pacto y su peso permiten a CropCircle adaptarse El CropCircle corresponde a un sistema produ- fácilmente a distintas configuraciones en la maquicido por de Holland Scientific y distribuido por Ag naria. Actualmente, están disponibles dos modeLeader, que incluye sensores de canopia, equipos los de sensores que proporcionan amarillo / NIR o de mano y sistemas de mapeo. El sensor ACS- sensor IR rojo.

210 de CropCircle proporciona los datos del índice Con un rango de medición de 30cm-2m, el de vegetación, junto con la información básica de equipamiento CropCircle ACS-210 tiene otras reflectancia del dosel de las plantas, en función de características; incluye una señal con poco ruido, la cual se puede desarrollar la prescripción nitro- una buena resistencia al polvo y al agua, una rápi-

154

### Página 157

Figura 7. Montaje de sensores OptRx al frente de la maquinaria y detalle de sensor, el cual es ubicado en forma perpendicular al cultivo. Fuente

figura: Holland Scientific y AgLeader

da tasa de salida de datos, bajo consumo de ener- ción de cultivos. OptRx cuenta con una avanzada gía y peso ligero del hardware. tecnología patentada, de detección de luz que no Este sistema se puede utilizar para múltiples depende de la luz ambiente, por lo que el sistema aplicaciones, tales como: estudios de mapeo de se puede utilizar de día o de noche al igual que los césped, nutrientes de respuesta de cultivos a los sensores presentados anteriormente. fertilizantes, efectos de herbicidas, detección de Este sistema genera activamente luz sobre las enfermedades, selección de híbridos y de predic- plantas en crecimiento, leyendo la luz reflejada de ción de biomasa forrajera. nuevo al sensor (Figura 7). Luego, al utilizar una pantalla de Ag Leader compatible, el sistema de OptRx sensores de cultivos OptRx puede generar una prescripción, la que varía a su vez la velocidad de La alianza entre los fabricantes de sensores aplicación de nitrógeno sobre la marcha, según el asociados a la agricultura de precisión, AgLeader algoritmo de cálculo que este posee. En algunas y Holland Scientific, presentaron la primera versión evaluaciones recientes, se ha visto que la tecnolodel sensor OptRx on-the-go, siendo uno de los gía de tasa variable de OptRxes es capaz de promás recientes que apareció en el mercado, y se porcionar una eficiencia de costes de entrada y un podría considerar una completa actualización del menor impacto ambiental. sistema CropCircle antes presentado. Este instrumento corresponde a un sensor de cultivos diseñado para uso en la cartografía y la recopilación CropSpecTM de datos, así como la aplicación de tasa variable El CropSpecTM es un sensor activo de canopia de N en tiempo real, sirviendo además para la fabricado por Topcon. Como fuente de luz utiliza prescripción de productos asociados a la protec- pulsos de diodos láser, lo cual supone una dife-

155 PARTE 3

### Página 158

Figura 8. CropSpecTM de Topcon (a) el sensor va montado en el techo del tractor para el sensoramiento de los índices vegetacionales. Este sensor mide en forma oblicua a medida que se realiza el escaneo y la aplicación en tiempo real en el campo. Fuente imagen: Topcon

rencia sustancial en el tipo de fuente de luz activa Con una tecnología basada en la competencia ópen relación a los sensores antes presentados. Este tica de Topcon, CropSpec utiliza diodos láser para sensor, al igual que el N sensor de Yara, está dise- su detección. El sensor mide la reflectancia de las ñado para observar el cultivo en una vista oblicua plantas para determinar el contenido de clorofila. (Figura 8) desde una altura de hasta 4 metros, lo Los usuarios pueden leer y grabar los datos que permite una gran huella de medición y el aupara analizarlos y crear reglas. La exploración de mento del grado de precisión en el sensoramiento la cosecha crea un mapa que indica los niveles de de diversos cultivos. CropSpecTM ha sido desanitrógeno, incluyendo tanto las áreas ricas como rrollado en colaboración con Yara Internacional. aquellas deficientes en nitrógeno. Esta información Este fue diseñado para su uso con las consolas X20 o X30 de Topcon, CropSpec funciona con el puede ser utilizada para llevar a cabo una prescripprograma VRC (Map LINK) o cualquiera de las apli- ción de flujo variable para ser utilizada inmediatacaciones de controlador de X20 o X30. Permite mente o en una fecha posterior. Con una simple al usuario controlar la variabilidad en el campo y calibración de dos puntos, el usuario puede definir solucionarla sobre la marcha, o guardar los datos puntos altos y bajos, y luego efectuar la aplicación para su análisis futuro o para la aplicación de la real utilizando el promedio del campo. El flujo deprescripción. seado puede ser determinado por el usuario.

Este sistema cuenta con dos sensores ligeros Para la recopilación de información en condiy fáciles de instalar. Los sensores se montan en ciones de campo, este sensor de cultivos se puede el techo de la cabina, para evitar daños al cultivo. montar en distintos tipos de maquinaria agrícola.

156

### Página 159

Además de la prescripción en tiempo real de cisión locales y en conjunto con expertos en el N que puede ser desarrollada con este sensor, área adquiere especial relevancia. es posible utilizar, la información recogida en el • De la misma forma, el hardware asociado a campo, para evaluar el impacto de la aplicación emisores y controladores cuenta con una perde nutrientes, de agua, de enfermedades y otras manente optimización, siendo necesario tamcondiciones de crecimiento de los cultivos. bién las evaluaciones técnico-económicas respectivas antes de su implementación.

Comentarios finales • De lo anterior se desprende, que si bien es

cierto que este capítulo presenta un estado del

• Los sensores activos para la aplicación de N en

arte de los sensores en tiempo real asociados

tiempo real montados en la maquinaria agrícola

a la aplicación nitrogenada, es necesario manrepresentan el estado del arte para las mediciotener la atención sobre los nuevos desarrollos nes de las características de cultivo en condiofrecidos a nivel comercial para su implemenciones de campo. tación en condiciones productivas.

• Existen varios tipos de estos sensores activos,

siendo una de las mayores diferencias entre

ellos, si la medición se realiza en forma oblicua

o perpendicular al cultivo. Los primeros presentarían ventajas en los cultivos en sus primeros estados de desarrollo o en aquellos más espaciados. Los ejemplos de estos sensores corresponden al N-Sensor de Yara y CropSpec de Topcon. Por otra parte, aquellos sensores cuya medición es perpendicular al cultivo (Cropcircle, Greenseeker y OptRx) tendrían mayores ventajas en cultivos establecidos o que presenten una mayor densidad de follaje.

• Los algoritmos de cálculo y principios de sensoramiento son en la actualidad objeto de estudio, con lo que a nivel comercial, es posible la aparición de nuevas versiones o actualizaciones de los sistemas mencionados en este capítulo para las próximas temporadas. La evaluación de dichos algoritmos en condiciones de campo y cultivos locales es un paso a dar para su implementación a nivel productivo.

En este sentido, el trabajo en conjunto de los

servicios de investigación en agricultura de pre-

157 PARTE 3

### Página 160

3.4. Monitoreo de desempeño La rentabilidad de la VRT cambia en relación

con el cultivo y los insumos, sus precios, el costo

y retorno de las prácticas de la de la tecnología de dosis fija (URT) con respecto agricultura de precisión a la VRT, la distribución espacial de las sub-uniAndrés Méndez, Fernando Scaramuzza, Juan Pablo dades en el terreno (zonas de manejo), y las magVélez y Diego Villarroel nitudes de las diferencias de rendimiento entre subunidades.

Andrés Méndez El potencial de mejora de la rentabilidad debido

Fernando Scaramuzza a la aplicación variable de estos insumos depende

Juan Pablo Vélez de 1) la identificación de áreas en el campo en el

Diego Villarroel que los aportes adicionales de insumos aumentará los ingresos en una escala mayor que los cosINTA Manfredi. tos adicionales que genere dicho aporte y / o 2) Proyecto Nacional de Agricultura de Precisión. la identificación de áreas en las que la reducción Manfredi, Córdoba, Argentina. de los insumos disminuirá los costos en un escala Contacto: agprecision@correo.inta.gov.ar que es mayor que la reducción potencial de ingreagriculturadeprecision@yahoo.com.ar sos correlacionados con un menor rendimiento de Página web: www.agriculturadeprecision.org grano (Koch, 2004).

El nitrógeno (N) en gramíneas es el insumo de

mayor impacto en el resultado económico, adeEnsayo de larga duración de manejo de más de ser un nutriente móvil en el suelo y el más insumos en forma variable esencial para optimizar el rendimiento de grano en La tecnología de Dosis Variable permite a los el cultivo de maíz. La aplicación de N en forma uniagricultores, una vez conocido el comportamien- forme, en la mayoría de los casos, resulta en un to del cultivo en cada sector del lote, empezar a exceso de N y de una escasez en diversas partes calcular las necesidades de insumo en cada zona del campo debido a la variabilidad espacial sobre homogénea más pequeña o subunidad del lote, y el terreno (Snyder, 1997). aplicarlos en forma de sitio-específico (Bragachini, Por otra parte la elección de la densidad es un 2004). factor de producción importante, por los que se La pregunta formulada con mayor frecuencia debe definir la relación entre la cantidad de plantas es, si la agricultura de precisión permite a los agri- logradas por unidad de superficie en un cultivo y cultores lograr mayores beneficios económicos re- su rendimiento, para distintas situaciones de oferta sultantes del aumento de la producción y/o de la ambiental de recursos. (Andrade, 1996). reducción del uso de insumos o de la modificación Todas estas técnicas de manejo son necesarias del manejo del ambiente en general, como es el probarlas y ajustarla en cada lote, por ello en INTA caso de la disminución del espacio entre surco en Manfredi se realizan ensayos en el campo para insuelos con limitaciones. crementar el conocimiento de esta tecnología, es

158

### Página 161

así, que desde el año 2003, se vienen realizando mas frío (julio) es de 9.9º C, dando como resultado ensayos en un lote elegido por su variabilidad, una amplitud térmica anual de 13.6º C. y el períoubicado en la zona de Pampayasta. Los ensayos do libre de heladas es de 102 días (carta de suelo planteados consistían en variar la cantidad de insu- 3163-32). mos en maíz (semilla y fertilizante) y variar el espa- Los suelos del lote pertenecen al complejo de ciamiento entre surcos en soja. Además se ensayó series Manfredi (30 %) con capacidad de uso IIIc, sembrando diferentes cultivos como es el caso de Manfredi en fase moderadamente alcalina en prola campaña 2006/2007 en donde se sembró soja fundidad (25 %), Oliva (25 %) y suelos con alcaen áreas de alto potencial de rendimiento y sorgo linidad sódica subsuperficial (20 %) con una caen las de bajo potencial de rendimiento del lote. pacidad de uso: IV ws (limitaciones de drenaje y Para realizar este ensayo de larga duración se sodio) y al complejo indeterminado Pampayasta y definieron tres zonas de mayor contraste y se iden- de suelos fluviales arenosos de albardones y patificaron como: roja, bajo potencial; amarilla, poten- leocauces con una capacidad de uso: VI sc. (limicial medio, y verde, alto potencial. Se mantuvieron taciones del suelo por el sodio y climáticas) en todas las campañas esas zonas y se variaron los insumos de acuerdo a las necesidades y las repuestas de cada una de ellas, el cálculo de los márgenes se realizó mediante las tablas 1, 2 y 3 del ANEXO, para maíz, soja y sorgo respectivamente.

En una segunda parte del estudio se realizó el

mapeo del Margen Neto, que consistió en agregar a cada punto del mapa el cálculo del margen correspondiente a dicho punto que interpolado o generada la zona en base al margen resultante genera una zonificación del resultado económico.

Características del lote

Los ensayos se realizaron en las inmediaciones de la localidad de Pampayasta, Provincia de Córdoba, Argentina, dentro de lo que se considera como la región semiárida central de la Provincia de Córdoba, en donde la precipitación anual media es de 740mm y de las cuales el 75% ocurren en el semestre más caluroso. El régimen térmico es templado con temperatura media anual de 16.6º C. La temperatura media del mes más caluroso (enero) es de 23.5º C y la correspondiente al mes

159 PARTE 3

### Página 162

Descripción de los ensayos y resultados

Soja 2003

El manejo variable consistió en variar la distancia entre surcos de 0.525

m en la zonas de alto y medio potencial de redimiendo a 0.26 m y en las

zonas de bajo potencial de rendimiento manteniendo la densidad constante. En la zona de bajo potencial de rendimiento con la técnica de estrechar el espaciamiento entre surcos se logro 1.06 Tn/ha de granos, esto es 0,7 toneladas superior espaciamiento de 0.525 en donde se obtuvo un rendimiento de 0,38 Tn/ha, en porcentaje, el rendimiento obtenido con dosis variable es 199% superior a la obtenida con dosis fija. Lo que produjo un cambio en el margen neto (MN) en la zona de bajo potencial, no haciéndolo positivo, pero si disminuyendo las pérdidas económicas en un 78 % pasando de un MN de 39.53 a 8.49 U$S/ha, dada la superficie importante que abarcaba esta zona, el cambio de manejo produjo que en todo el lote el MN se incrementara un 599%, en dinero significa U$S 1241.6 más.

Insumo

Rendimiento MN MN total del lote

Tn/ha Urea PDA Semilla U$S/ha U$S/ha

Kg/ha Kg/ha Unidad/ha

AP 6.33 69.69

DF PM 5.17 120 70 76000 25.00 83.73

BP 4.01 -7.96

AP 6.96 190 70 80000 78.23

DV PM 5.17 0 80 60000 48.02 143.62

BP 4.30 0 0 40000 17.37

Maíz 2004

El manejo variable consistió en variar las dosis de Nitrógeno, Fósforo y

semillas en base a los requerimientos del cultivo y lo que ofrecía el suelo,

este cambio en el manejo con Dosis Variable incrementó el MN en todas

las zonas por ahorro o por incremento de la producción en 12.25, 92 y

318.22 % en Alto Potencial, Potencial Medio y Bajo Potencial respectivamente, lo que produjo que en todo el lote el MN se incrementara un 71.53%, en dinero significa U$S 2395.6 más. La zona de Bajo potencial a

160

### Página 163

pesar de no fertilizarse incrementó el rendimiento debido a un mejor comportamiento ante la disminución de la densidad, en Potencial Medio el MN se incrementa pero debido al ahorro de insumos, ya que el rendimiento se mantuvo igual que con la dosis fija a pesar de no fertilizar con Nitrógeno y de disminuir considerablemente la densidad de siembra, mientras que en la agricultura de precisión el MN se incrementó debido a un aumento de la producción ante la repuesta positiva al incremento de la fertilización nitrogenada y al aumento de la densidad de siembra.

Insumo

Rendimiento MN MN total del lote

Tn/ha Urea PDA Semilla U$S/ha U$S/ha

Kg/ha Kg/ha Kg/ha

AP 1.89 90 (0.525) 51.71

DF PM 1.16 0 0 90 (0.525) -7.00 5.18

BP 0.36 90 (0.525) -39.53

AP 1.89 90 (0.525) 51.71

DV PM 1.16 0 0 90 (0.525) -7.00 36.22

BP 1.06 90 (0.26) -8.49

Maíz 2005

El manejo variable consistió en variar las dosis de Nitrógeno, Fósforo y

semillas en base a los requerimientos del cultivo y lo que ofrecía el suelo,

este cambio en el manejo con Dosis Variable incrementó el MN en todas

las zonas por ahorro o por incremento de la producción en 4.26, 23.14

y 75.91 % en alto potencial, potencial medio y bajo potencial respectivamente lo que produjo que en todo el lote el MN se incrementara un 19.35 %, en dinero significa U$S 2247 más.

En la zona de bajo potencial a pesar de no fertilizarse se incrementó el

rendimiento debido a un mejor comportamiento ante la disminución de la

densidad, en potencial medio el MN se incrementa pero debido al ahorro de

insumos, ya que el rendimiento se mantuvo igual que con la dosis fija a pesar de no fertilizar con Nitrógeno y de disminuir considerablemente la densidad de siembra. Mientras que en alto potencial el MN se incremento debido a un aumento de la producción ante la repuesta positiva del incremento de la fertilización nitrogenada y al aumento de la densidad de siembra.

161 PARTE 3

### Página 164

Insumo

Rendimiento MN MN total del lote

Tn/ha Urea PDA Semilla U$S/ha U$S/ha

Kg/ha Kg/ha Unid/ha

AP 8.74 158.36

DF PM 7.44 120 70 76000 98.40 290.42

BP 6.09 33.67

AP 9.36 190 70 80000 166.21

DV PM 7.44 0 80 60000 121.17 346.61

BP 6.09 0 0 40000 59.23

Soja 2007

El manejo variable consistió en variar el tipo de cultivo, con la misma

sembradora se sembraba soja en alto potencial y potencial medio y al

llegar a bajo potencial, se deshabilita la siembra de soja y se habilita la

siembra de sorgo con la misma sembradora y en tiempo real, ambos a

0.525. En este caso se aprovechó la tolerancia del sorgo a la salinidad de

los suelos para incrementar la producción de granos y de biomasa, para

tratar de revertir el nivel de cobertura, mejorar a futuro la siembra, y para

un mejor aprovechamiento de la lluvia. De este modo en la zona en donde

el rendimiento de soja era poco mas de 1 Tn/ha se logró una producción

de sorgo de 3.55 Tn/ha, que sí bien su valor es el 44% del valor de la soja,

la producción del sorgo superó a la de soja en un 267%, logrando mejorar

el MN a niveles positivos, lo que produjo que en todo el lote, el MN se

incrementara un 17.83 %, que en dinero significa U$S 819.6 más.

Insumo

Rendimiento MN MN total del lote

Tn/ha Urea PDA Semilla U$S/ha U$S/ha

Kg/ha Kg/ha Kg/ha

AP 2.42 (SOJA) 93.97

DF PM 1.71 (SOJA) 0 0 90 33.66 114.91

BP 0.97 (SOJA) -12.73

AP 2.42 (SOJA) 0 0 90 93.97

DV PM 1.71 (SOJA) 0 0 90 33.66 135.40

BP 3.55 (SORGO) 0 0 12 (SORGO) 7.76

162

### Página 165

Maíz 2009

El manejo variable consistió en variar las dosis de Fósforo y semillas

en base a los requerimientos del cultivo y lo que ofrecía el suelo. Los

cambios en las dosis se realizaron en potencial medio y bajo potencial, e

incrementó el MN en 23.26 y 285.71 % respectivamente. En alto potencial

no se varió la dosis de insumos, esto produjo que en todo el lote el MN se

incrementara un 23.21 %, que en dinero significa U$S 910.3 más.

Insumo

Rendimiento MN MN total del lote

Tn/ha Urea PDA Semilla U$S/ha U$S/ha

Kg/ha Kg/ha Unid/ha

AP 5.91 57.09

DF PM 5.00 120 0 76000 35.94 98.07

BP 4.31 5.04

AP 5.91 120 0 76000 57.09

DV PM 5.00 120 0 50000 44.30 120.83

BP 4.91 120 40 38000 19.44

Soja 2010

El manejo variable consistió en variar la distancia entre surcos de 0.525

m en la zonas de alto y medio potencial de rendimiento y a 0.26 m en

las zonas de bajo potencial de rendimiento manteniendo la densidad de

siembra constante, esto incrementó el rendimiento en la zona de BP en

un 20 % (0.3 Tn), lo que produjo un aumento en el MN en un 121 % pasando de un MN de 11.1 a 24.61 U$S/ha, dada la superficie importante que abarcaba la zona de bajo potencial, el cambio de manejo produjo que en todo el lote el MN se incrementara un 6.78%, en dinero significa U$S

540.3 más.

163 PARTE 3

### Página 166

Insumo

Rendimiento MN MN total del lote

Tn/ha Urea PDA Semilla U$S/ha U$S/ha

Kg/ha Kg/ha Kg/ha

AP 2.95 138.35

DF PM 1.94 90 (0.52) 49.83 199.28

BP 1.50 11.10

AP 2.95 90 (0.52) 138.35

DV PM 1.94 90 (0.52) 49.83 212.79

BP 1.80 90 (0.26) 24.61

Mapa de Margen Neto según la cantidad de insumos que se apliquen y

Estos resultados son el promedio de toda la el rendimiento que se obtienen a partir de ellos. zona tratada con dosis fija o dosis variable, pero Es decir, si se aplican menos insumo pero el rensi establecemos en cada uno de los puntos del dimiento se mantiene a pesar de esto, el rendimapa de rendimiento los costos y los ingresos miento de indiferencia disminuye, es decir que en base a las Tn/ha que representa ese punto y será necesario menos cantidad de granos para teniendo en cuenta los valores de las tablas 1, 2 cubrir los costos, este es el objetivo del ahorro y 3 del anexo y mapeamos el MN tal como está, de insumos comprenderemos su dinámica y veremos que Amarilla: todos los puntos considerados como dentro de cada zona existen todavía áreas en buenos o normales establecidos por un MN de donde el nivel de rendimiento a pesar de practi- mayor a 0 (cero) hasta 185 U$S/ha es decir a parcarles dosis variable no alcanza a saldar los cos- tir del cual empieza a tener ganancias hasta el MN tos de producción. obtenido de un rendimiento esperable para la zona Para visualizar el comportamiento del MN, se bajo secano de 6.5 Tn/ha y 2.2 Tn/ha para maíz y delimitaron tres zonas caracterizadas con diferen- soja respectivamente y con los costos detallados tes colores. en la tabla 1 del anexo.

Roja: en donde el MN es menor o igual a 0, Verde: todos los puntos considerados como cuando da 0 es decir en donde la ganancia es buenos o altos, establecidos por un MN de más de nula, el rendimiento que lo genera se denomina U$S 185 para maíz y más de U$S 130 para soja. rendimiento de indiferencia, a partir del cual si A continuación se visualizan: el mapa del reel rendimiento es menor se producen pérdidas sultado económico con dosis fija, a la izquierda, que con dosis fija y en las cantidades que se y el logrado con dosis variable, a la derecha, dedetallan en la tabla 1 del anexo es de 4.2 Tn/ha tallando la superficie correspondiente al resultado en maíz y en soja 1.1 Tn/ha y que puede variar negativo, buen margen y muy buen margen.

164

### Página 167

Soja 2003 No hubo una modificación

significativa al cambiar el manejo.

El achicamiento del espaciamiento

entre surcos en la zona de bajo

potencial disminuye 1.3 has

de MN negativo que pasan a

pertenecer la zona amarilla de MN

bueno.

Maíz 2004 Al realizar dosificación variable

se disminuyó 8.85 has de zona

con MN negativo, se incrementó

1.2 has con MN bueno y 7.69

has pasaron a tener MN muy

bueno.

Maíz 2005 Al realizar dosificación variable

todo el lote pasó a tener MN muy

bueno.

165 PARTE 3

### Página 168

Soja 2007 Hubo una modificación

significativa al cambiar el cultivo de

soja a sorgo en la zona de BP. La

zona en donde no se alcanzaba a

cubrir los costos disminuyó 4.39

has que pasaron a pertenecer a la

zona con buen MN.

Maíz 2009 Hubo una modificación

significativa al realizar

dosificación variable. Haciendo

desaparecer prácticamente

la zona con MN negativo y

disminuyendo 2.38 has a la zona

de Buen MN, pasando a formar

parte de la zona de muy buen

MN.

Soja 2010 Hubo una modificación

significativa al realizar dosificación

variable. Haciendo desaparecer

prácticamente la zona con MN

negativo pasando a formar 2.39

has de esta a la zona con buen

MN.

166

### Página 169

Conclusión se a futuro y el precio de los insumos es conocido

En todo el lote y en promedio de todas las al momento de la compra. campañas, independientemente de la tecnología Un punto a destacar es que a lo largo de los de siembra que se utilizó, el mayor beneficio eco- años que se realizaron los ensayos, la variabilidad nómico se obtuvo con el maíz con U$S 147.40/ entre años fue muy alta y a sí mismo el margen de ha para dosis fija y U$S 203.60/ha para dosis va- la dosis variable fue siempre positivo respecto a la riable, con la soja se obtuvo U$S 67.90/ha para la dosis fija. dosis fija y U$S 105.08/ha para la dosis variable. Por otro lado merece la mención de que la única herramienta de dosis variable con la que se Con respecto a la utilización de la dosis variacuenta en este lote es una sembradora con doble ble en todos los años se obtuvieron beneficios a vía de dosis variable (siembra y fertilización), por lo favor de esta tecnología, pero con el cultivo que que todas las decisiones de cambio de insumos más se justifica es con el de maíz, en promedio de se toman en la siembra. Se podría mejorar la ferlas tres campañas de maíz (2004, 2005 y 2009) la tilización en maíz si las aplicaciones se realizarán dosis variable superó a la dosis fija en U$S 46.28/ más tarde. ha mientras que en soja la dosis variable superó a la dosis fija en U$S 37.14/ha.

En todas las campañas en donde se realizaron Resultado a

Superficie Total en

favor de la

ensayos de manejo variable hubo beneficios a fa- Cultivo / Año

Dosis Variable

del Lote el lote

vor de la práctica de esta tecnología. La sumato- (ha) (U$S/ha) (U$S/ha) ria de los beneficios de la aplicación de tecnología Soja 2003 31.04 1241.6 de agricultura de precisión en las 6 campañas es Maíz 2004 56.89 2395.6 de U$S 8155 en un lote de 40 has. Se disminuyó considerablemente la superficie en donde el ren- Maíz 2005 59.19 2247.6 40 dimiento no alcanzaba a saldar los costos de pro- Soja 2007 20.49 819.6 ducción, y especialmente en maíz, se incrementa- Maíz 2009 22.76 910.4 ron las zonas en donde el resultado era bueno, a Soja 2010 13.51 540.3 muy bueno, esto es debido principalmente al ahoTotal Todas las rro o al mejor aprovechamiento de los recursos. 8155.1 campañas La visión actual de la dosis variable para el manejo de este lote es variar los insumos de acuerdo a la variabilidad del suelo (química, física, topográfica, etc.). En este trabajo se observó que manejar el lote por margen Neto está delimitando nuevas áreas o zonas. Una visión a futuro podría ser el manejo, utilizando este criterio. Un beneficio de éste, es que los precios de los granos pueden fijar-

167 PARTE 3

### Página 170

ANEXO

Tabla 1: Costos de producción en Maíz (REVISTA AGROMERCADO, Octubre de 2010)

comisión U$S/q 0.28

impuestos U$S/q 0.16

Seguro c/put (50% produc) U$S/q 0.48

gastos generales U$S/q 0.23

secado U$S/q 3 puntos 0.36

Flete corto U$S/q 20 km 0.52

Flete largo U$S/q 400 km 3.25

Total gastos de comercialización U$S/qq 5.28

cosecha U$S/ha 6.90% 73.66

siembra U$S/ha 1.1 33.00

semillas unidad/ha U$S/ha 76000 unid/ha 57.00

curasemillas U$S/ha 27 cc/ha 3.34

PDA U$S/ha 70 31.5

Glifosato U$S/ha 4 l/ha 9.60

2.4 D 100% U$S/ha 300cc/ha 1.71

Atrazina U$S/ha 4 l/ha 11.13

Cipermetrina U$S/ha 100cc/ha 0.60

Equip WG 30% superficie U$S/ha 120 g 10.26

aplicación de herbicida U$S/ha 0.58 15.18

Urea Graulada U$S/ha 120 kg /ha 55.20

Gastos directos U$S /ha 228.52

gastos de estructura U$S /ha 91.00

168

### Página 171

Tabla 2: Costos de Producción de Soja (REVISTA AGROMERCADO, Octubre de 2010).

comisión U$S/q 0.52

impuestos U$S/q 0.30

Seguro c/put (50% produc) U$S/q 1.20

gastos generales U$S/q 0.23

secado U$S/q 3 puntos 0.36

Flete corto U$S/q 20 km 0.52

Flete largo U$S/q 400 km 2.92

%IB 29.00

Total gastos comercialización

U$S/ha 133.10

cosecha U$S/ha 6.90% 64.55

siembra U$S/ha 1.1 29.04

semilla + inoculantes U$S/ha 90 kg/ha 57.66

en f fin de ciclo U$S/ha 27 cc/ha 15.68

glifosato U$S/ha 2 aplic = 5lt 14.4

cipermetrina U$S/ha 4 l/ha 0.60

insecticida U$S/ha 300cc/ha 3.63

aplicaciones de agroq U$S/ha 4 l/ha 19.80

Gastos directos U$S /ha 140.81

gastos de estructura U$S /ha 45.00

169

### Página 172

Tabla 3: Costo de Producción en Sorgo (REVISTA AGROMERCADO, Octubre de 2010).

comisión U$S/q 0.26

impuestos U$S/q 0.15

gastos generales U$S/q 0.23

secado U$S/q 3 puntos 0.60

Flete corto U$S/q 20 km 0.52

Flete largo U$S/q 400 km 2.01

%IB 29.00

Total gastos comercialización

U$S/ha 143.26

cosecha U$S/ha 6.90% 52.77

siembra U$S/ha 1.1 29.00

semilla U$S/ha 38000 sem/ha 18.00

PDA U$S/ha 70 kg/ha 43.05

Urea Graulada U$S/ha 40 Kg/ha 55

atrazina U$S/ha 4 l/ha 8.35

glifosato U$S/ha 300cc/ha 9.60

2-4 D U$S/ha 4 l/ha 4.56

Cipermetrina U$S/ha 100cc/ha 1.20

insecticida U$S/ha 120 g 3.63

aplicación de herbicida U$S/ha 0.58 30.36

Urea Graulada U$S/ha 120.00 0.00

Gastos directos U$S /ha 202.75

gastos de estructura U$S /ha 91.00

170

### Página 173

BIBLIOGRAFÍA 1.3. Monitores de rendimiento y mapeo

Albarenque S.M. y J.P. Vélez. Técnicas para el procesamiento de mapas de rendimiento. ISBN 978-987-679- 028-4. Ediciones INTA. 28p. 2011.

1.1. Uso del Sistema de Posicionamiento Bragachini M., Mendez A., Scaramuzza F. y F. Proietti.

Global en la caracterización de áreas agrícolas “Capítulo 3: Monitoreo de rendimiento y elaboración de mapas”. En: Agricultura de precisión: Integrando conoHurn, J. Differential GPS Explained. TRIMBLE. 55p. 1993 cimientos para una agricultura moderna y sustentable.

Hurn, J. GPS: A Guide to the Next Utility. TRIMBLE. 76p. Editores: Bongiovanni R., Chartuni Mantovani E., Best

1989. S. y A. Roel. p. 45-54. PROCISUR, 2006.

Molin, J. P. Agricultura de precisão – o gerenciamento Kleinjan J., Clay D., Carlson G. y S. Clay. “Chapter 4: da variabilidade. Piracicaba: o autor, 83p. 2001. Developing productivity zone from multiple years of yield Rocha, c. h. b. GPS de navegação para mapeadores, tril- monitor data”. En: Gis Applications in agriculture. Edited heiros e navegadores. Juiz de Fora: Ed. Autor, 124p. 2003. by Pierce F.J. and D. Clay. p. 65-79. 2007.

Ping J.L. y A. Dobermann. Processing of Yield Map

Data. Precision Agriculture, 6, 193–212, 2005.

1.2. Uso de Sistema de Informaciones

Geográficas para espacialización de datos del

1.4. Adquisición remota y agricultura de

área de producción agrícola

precisión

Esri – Environmental Systems Research Institute Inc.

ArcInfo. The World’s Leading Desktop Geographic Best, S.; G. Gatica; L. León. Development of an assessInformation System. esri Inc., Redlands/ca, 1994. ment model of water stress of vineyard var. Merlot, based on the use of infrared thermography. Proceedings of Fonseca, L.P.S., G.A.B., Alger K. (orgs.) Corredor de the 8th Fruit, Nut and Vegetable Production Engineering Biodiversidade da Mata Atlântica do Sul da Bahia. Publicação Symposium, Chile, 2009. em cd-rom, Ilhéus, iesb / ci / cabs / ufmg / unicamp.

Florenzano, T.G. Iniciação em Sensoriamento Remoto.

Jones, C. B. Geographical Information Systems and São Paulo, Oficina de Textos, Terceira Edição, 2008.

Computer Cartography. Harlow, Longland. 319 p. 1997.

Jensen, J.R. Sensoriamento Remoto do ambiente:

Landau, E. C. Sistemas de Informações Geográficas e Uma perspectiva em recursos terrestres. São José dos Técnicas de Sensoriamento Remoto como Ferramentas Campos, Parêntese Editora, 2009. para o Planejamento de Estratégias de Conservação Liu, H.T.H. Aplicações de Sensoriamento Remoto. da Diversidade Biológica. In: Prado P.I., Landau E.C., Editora UNIDERP, 2006.

Moura R.T., Pinto, 2003.

Moreira, M.A. Fundamentos do Sensoriamento Remoto

Mantovani, E. C.; Matoso, M. J.; Oliveira, A. C. de; Avelar, e Metodologias de Aplicação. Quarta Edição, Editora G. de. Estabelecimento de critérios para intervenção em UFV, Viçosa, 2011. áreas de produção de milho utilizando conceitos de agricultura de precisão. XXXIII Congresso Brasileiro de Engenharia Agrícola. Anais. São Pedro, SP. 5p. 2004. 1.5. Muestreo para mapeo y manejo de la Mapa - Ministério da Agricultura, Pecuária e fertilidad del suelo Abastecimento, Brasil. Secretaria de Desenvolvimento Giménez, L.M.; Zancanaro, L. “Monitoramento da Agropecuário e Cooperativismo. Agricultura de Precisão. fertilidade de solo com a técnica de amostragem em Boletim Técnico. Brasília, 3a ed. 40 p. 2013. <http://www. grade”. Informações Agronômicas, Piracicaba, n.138, agricultura.gov.br/arq_editor/Boletim%20tecnico.pdf> p.19-25, 2012.

171

### Página 174

Machado, P.L.O.A.; Silva, C.A.; Bernardi, A.C.C. et al. Shiratsuchi, L. S.; Machado, A. L. T. “Variação do es- “Variabilidade de atributos de fertilidade e espaciali- paçamento entre faixas de colheita na Geração de zação da recomendação de adubação e calagem para Mapas de Produtividade”. Boletim de Pesquisa de a soja”. En: Machado, P.L.O.A.; Silva, C.A.; Bernardi, Desenvolvimento, 90. Ed. Empresa Brasileira de A.C.C. (Eds.) Agricultura de precisão para o manejo da Pesquisa Agropecuária, 2003. fertilidade do solo em sistema de plantio direto. Rio de Sudduth, K. A.; Drummond, S.T. Yield Editor: “Software Janeiro: EMBRAPA Solos, p.115-129, 2004. for removing errors from crop yield maps”. Agronomy Resende, A.V.; Shiratsuchi, L.S.; Sena, M.C.; Krahl, L.L.; Journal, v. 99, p.1471–1482. 2007.

Oliveira, J.V.F.; Corrêa, R.F.; Oro, T. “Grades amostrais Taylor, J. A.; McBratney, A. B.; Whelan, B. M. para fins de mapeamento da fertilidade do solo em área “Establishing management classes for broad acre agride cerrado”. En: Congresso Brasileiro de Agricultura de cultural production”. Agronomy Journal, v.99, p.1366- Precisão. 2. São Pedro – SP, 2006. Anais. Piracicaba: 1376, 2007.

ESALQ, 2006. (CD-rom).

Thyle´N, L.; Algerbo, P. A.; Giebel, A. “An expert filter removing erroneous yield data”. En P.C. Robert et al. (ed.)

2.1. Creación de mapas de manejo con datos Proceedings: 5th International Conference on Precision espaciales Agriculture, Bloomington, MN.16–19 Julho 2000. ASA, CSSA, and SSSA, Madison, WI. 2001.

Brandão, Z. N.; Oliveira, R. P.; Sana, R. S.; Sofiatti, V.;

Zonta, J. H.; Medeiros, J. C. “Uso de imagens orbitais Yan, L.; Zhou, S.; Feng, L.; Hong-Yi, L. “Delineation e suborbitais na caracterização da variabilidade espacial of site specific management zones using fuzzy clusteda produtividade”. En: Inamasu, R.: Bernardi, A. C. C. ring analysis in a coastal saline land”. Computers and (Eds). Agricultura de Precisão: resultados de um novo Electronics in Agriculture, p.174-186, 2007. olhar. Ed: Embrapa Instrumentação, São Carlos, SP.

588p. 2014. 2.2. Uso de la geoestadística y los sistemas de

Coelho, A. M.; Faria, C. M. de; Cunha, T. F.; Mota Junior, información geográfica en agricultura H. A. Agricultura de Precisão mapeia colheita de grãos.

Fleischer, S.J., P.E. Blom, R. Weisz. Sampling in preciCampo & Negócio, Uberlândia. V. 19, n. 120, p. 36-40, sion IPM: When the objective is a map. Phytopathology fev. 2013.

89: 1112-1118. 1999.

Doerge, T. A. “Management zone concepts”.

Goovaerts, P. Geostatistics for natural resourses evaluaEn: Site-specifics management guideline. 2013. tion. Oxford University Press, Oxford, 1997.

Disponible en: <www.ipni.net/publication/ssmg.nsf/0/

C0D052F04A53E0BF852579E500761AE3/$file/ Isaaks, E.H., R. Mohan Srivastava. Applied Geostatistics.

SSMG-02.pdf>. Fecha de consulta: 10/12/2013. Oxford University Press. New York, Oxford. 561 pp, 1989.

Mantovani, E. C.; Matoso, M. J.; Oliveira, A. C. de; Avelar,

G. de. Estabelecimento de critérios para intervenção em Liebhold, A.M., R.E. Rossi, W.P. Kemp. Geostatistics áreas de produção de milho utilizando conceitos de and geographic information systems in applied insect agricultura de precisão. XXXIII Congresso Brasileiro de ecology. Ann. Rev. Entomol. 38: 303-327, 1993.

Engenharia Agrícola. Anais. São Pedro, SP. 5p. 2004. Matheron, G. Principles of geostatistics. Econ. Geol.

Santos, A. O.; Pallone Filho, W. J.; Ungaro, M. R. G.; 5:1246-1266, 1963.

Lino, A. C. L.; Radin, B. “Prospecção de zonas poten- Ribes-Dasi, M., M. Bascuñana, J. Avilla. “Estudio de la ciais para manejo diferenciado em agricultura de pre- distribución espacial de Cydia pomonella (L.) y Pandemis cisão utilizando-se padrões de solo-planta-clima”. En: hermana (Denis & Schiffermuller)” en Torregrossa (Leida) Revista Brasileira de Engenharia Agrícola e Ambiental, mediante métodos geoestadísticos. Bol. San. Veg. v.7, p.463-468, 2003. Plagas. 24: 935-948, 1998.

172

### Página 175

2.3. Interpretación de informaciones 2.5. Monitoreo temporal de los sistemas de

espacializadas y definición de unidades de producción para la toma de decisiones y manejo mejora Benavidez R., Boschetti N., Quintero C.; Barrera R. y A. Embrapa - Empresa Brasileira de Pesquisa Agropecuária.

González. “Evaluación de la fertilidad fosfatada de los Manual de métodos de análise de solo. Centro Nacional suelos para los principales cultivos extensivos de Entre de Pesquisa de Solos. 2a. ed. Rio de Janeiro, 212 p.

Ríos”. En: Ciencia Docencia y Tecnología, n° 21, año XI. 1997. p221-266. 2000. Larscheid,G. , Blackmore, B.S. and Moore, M.

Doerge, T. A. “Management zone concepts. SSMG-2”. Management Decision Based on Yield Maps. Presented In: Information Agriculture Conference, Stewart Center, on 1st European Conference on Precision Agriculture.

Purdue, IN. 1999. September 8-10, 1997 Warwick University, Warwick,

Gambaudo S. y H. Micheloud. Capítulo 6: “Enmiendas UK Sponsered by The SCI Agriculture and Environment Group. <http://www.silsoe.cranfield.ac.uk/epf/> minerales”. En: Fertilización de cultivos y pasturas.

2° edición. Buenos Aires. Hemisferio Sur. p129-145. Lowenberg-DeBoer, J. Precision Farming Profitability.

2008. Agricultural Research Programs. Purdue University,

West Lafayette, IN, 131 p. 2000.

Ipni. Cálculo de Requerimientos Nutricionales - Versión

2013 <http://lacs.ipni.net/article/LACS-1024> Mattoso, M.J. Subprojeto Custos de Produção da Cultura do Milho no Brasil, in Projeto Sistemas de Kruk B. y E. Satorre. “Capítulo 13: Densidad y arreglo Produção da Agropecuária Brasileira. SEA, Embrapa espacial del cultivo”. En: Producción de granos. Bases Sede. Brasília, DF. 2002. funcionales para su manejo. p277-316. 2003.

Moore, M. Fieldstar – An integrated approach to reducing farm operating costs and increasing profitability.

2.4. Aspectos económicos, análisis de agco Company. 2002. viabilidad de adopción de intervenciones en Santos, R.F.dos. “Planejamento Ambiental e Sistemas de los sistemas de producción Informações Geográficas”. En: Caderno de Informações Ipni - Site Specific Management Guidelines, Published Georreferenciadas - CIG. Vol.1 - Número 2. Artigo 2. by The Fertilizer Institute - International Plant Nutrition 1997.

Institute Swinton, S.W. and Lowenberg-DeBoer, J. Site-Specific

Lowenberg-DeBoer, Jess, Ericson, Kathleen et al., Guidelines. Profitability of Site-Specific Farming. SSMGPrecision Farming Profitability, Agricultural Research 3.<www.ppi-far.org/ssmg> 4p. 1998.

Programs, Purdue University, West Lafayette, Indiana,

usa, 2000. 3.1. Tecnología de precisión para gestión de

Sonka Steven T. et al., Precision Agriculture in the 21st nutrientes

Century - Geospatial and Information Technologies Ctic - Conservation Technology Information Center, in Crop Management, National Research Council, Indian Creek Watershed Project. Annual Report and

1997. website: http://www.ctic.purdue.edu/IndianCreek/,

Srinivasan, Ancha phd et al., Handbook of Precision West Lafayette, Indiana, usa. 2013.

Agriculture - Principles and Applications, Food Products InfoAg Conference Proceedings 2011, 2013, 2014. A Press, 2006 collection of presentations and information from past Zhang, Q., Pierce F. J. et al., Agricultural Automation - and current InfoAg Conferences. Disponible en: <www.

Fundamentals and Practices, crc Press, 2013 infoag.org>

173

### Página 176

Ipni. 4R, Plant Nutrition Manual: A Manual for Improving Roberson, G. T. MapBased vs. Sensor based nitrogen the Management of Plant Nutrition, 1st Rev. Ed., (T.W. application technology. 2013. Disponible en: <http:// Bruulsema, P.E. Fixen, G.D. Sulewski, eds.), International www.infoag.org/abstract_papers/papers/abstract_145.

Plant Nutrition Institute, Norcross, GA, USA. 2013. pdf>

Ipni. Site-Specific Management Guidelines. A collection Shannon, K. Working with Farmers to Advance Sensor of 45 publications on selected topics of site-specific Technology for In-Season N Management. 2010. precision farming. International Plant Nutrition Institute, Disponible en: <http://www.ksre.ksu.edu/waterqualiNorcross, ga, usa. Disponible en: <http://www.ipni.net/ ty/2010/Presentations/Workshop/Shannon.pdf> ssmg> Taylor, R y J. Fulton. Sensor – based variable application Jim, Patricio. June 4, 2013. Choosing Your UAV. DTN- for cotton. 2010. Disponible en: <http://www.cottoninc.

The Progressive Farmer/Agriculture Markets, News and com/fiber/AgriculturalDisciplines/Engineering/PrecisionWeather. On-line newsletter. Crop-Management-for-Cotton/Sensor-Based-VariableReetz, Harold F., Jr. “Precision Farming as an Instrument Rate-App/Sensor-Based-App-Oct-2010.pdf> for Fertilizer Best Management Practices”. En: Boas practicas para uso eficente de fertilizantes. Vol 1. Luis 3.4. Monitoreo de desempeño y retorno de las Ignacio Prochnow, Valter Casarin, Silvia Regina Stipp, eds. International Plant Nutrition Institute (ipni) – Brazil, prácticas de la agricultura de precisión Piracicaba, SP. Brazil. 2010. Andrade, F, Cirilo, A, Uhart S, Otegui M. Ecofisiología del cultivo de maíz. Editoral La Barrosa, pp:264. Balcarse.

Schaefer, Dan. Illinois Council on Best Management

Buenos Aires. 1996.

Practices. Personal communication. 2014.

Bragachini M.; Méndez A.; Scaramuzza F. Agricultura

de Precisión y Siembra Variable de insumos en tiem-

3.3. Sensores de nitrógeno para la medición y po real mediante el uso de GPS. 2004. Disponible en: aplicación en el cultivo en tiempo real <http://www.agriculturadeprecision.org/siembCoseAlGil, E., A. Giménez. N-sensor. Sistema de apli- ma/Sembradora%20IOM%20Inteligente.html>. Fecha cación selectiva de nitrógeno en tiempo real. de consulta 26/05/2009 Disponible en: <http://ocw.upc.edu/download.php?fi- Kay, R.D.; W.M. Edwards. Farm management. 4th ed. le=15013140/28037-3962.pdf%E2%80%8E> The McGraw-Hill Companies, Boston. 1999.

Hegge, H. “Site-specificfertilizing”. En : H.J. Heege Koch B.; Khosla R.; Frasier W. M.; Westfall D. G.; (ed.), Precision in Crop Farming: Site Specific Concepts Inman D. Economic Feasibility of Variable-Rate Nitrogen and Sensing Methods: Applications and Results. Application Utilizing Site-Specific Management Zones.

Springer Science Business Media. Chapter 9. Pp: 193- 2004 . Disponible en: <http://agron.scijournals.org/

272. 2013. cgi/content/abstract/96/6/1572>. Fecha de consulta

Holland, K. y J. Schepers. Use of a virtual –reference 26/05/2009

concept tointerpret active canopy sensor data. Presicion Miguez F.2008. Márgenes de Maíz 2007/2008. Revista Agric. 14: 71-85. 2013. Agromercado, Argentina.

McGrath. “Sensor Guided variable rate nitrogen”. En: Revista Agromercado, Argentina, Octubre 2010.

CCA Conference Presentation. 2012. Disponible en: Snyder, C.; Schroeder T.; Havlin J.; Kluitenberg G. <http://www.indianacca.org/presentation/3/108/> An economic analysis of variable-rate nitrogen maRaper, T., J. Varco and K. Hubbard. Canopy-based nor- nagement. 1997. Dsiponible en: <agron.scijournals. malized difference index sensors for monitoring cotton org/cgi/content/full/96/6/1572>. Fecha de consulta nitrogen status. Agr. Journal. 105: 1345-1354. 2013. 02/03/2008.

174

## Referência original

- Arquivo de origem: `Manualagricultura.pdf`
- Fonte: IICA/PROCISUR, Manual de agricultura de precisión, Montevideo, 2014, ISBN 978-92-9248-545-0.
- Ano: 2014
