# Proyecto Sistema Experto Multiagente IA

## Descripcion del proyecto

Este proyecto consiste en desarrollar un sistema experto multiagente para apoyar la gestion de inventario y recomendacion de productos en una tienda de anime.

La idea principal es que el sistema pueda revisar productos disponibles, detectar bajo stock, recomendar articulos segun los gustos del cliente y apoyar al encargado de la tienda para tomar mejores decisiones sobre ventas y reabastecimiento.

El sistema estara pensado para una tienda que vende productos como mangas, figuras, posters, llaveros, playeras, stickers, peluches y accesorios relacionados con diferentes animes.

## Objetivo

Desarrollar un sistema experto con agentes inteligentes que permita consultar productos, analizar inventario, recomendar articulos al cliente y sugerir reabastecimiento cuando algun producto tenga pocas unidades disponibles.

## Problema que se quiere resolver

En una tienda de anime puede ser dificil llevar el control de todos los productos, ya que existen muchas categorias, precios, personajes, animes y niveles de stock.

Tambien puede pasar que un cliente no sepa exactamente que comprar, pero si tenga una idea general, por ejemplo: quiere algo de Naruto, One Piece, Demon Slayer o Dragon Ball, pero con cierto presupuesto.

Por eso, este sistema busca ayudar tanto al cliente como al encargado de la tienda, usando reglas de inferencia y una base de datos para generar recomendaciones y alertas de inventario.

## Tema elegido

Sistema experto multiagente para gestion de inventario y recomendacion de productos en una tienda de anime.

## Productos que manejara el sistema

El sistema podra trabajar con productos como:

- Mangas
- Figuras
- Posters
- Llaveros
- Playeras
- Stickers
- Peluches
- Accesorios
- Articulos coleccionables

## Arquitectura inicial del sistema

El sistema estara dividido en varios agentes, donde cada uno tendra una funcion especifica.

### Agente 1: Agente de atencion al cliente

Este agente recibira la solicitud del cliente y detectara que tipo de producto esta buscando.

Ejemplo:

El cliente puede escribir:

"Quiero algo de One Piece que no pase de 300 pesos"

El agente debe identificar:

- Anime solicitado
- Presupuesto
- Tipo de producto, si lo menciona
- Preferencias del cliente

### Agente 2: Agente de inventario

Este agente revisara la base de datos para saber si existen productos disponibles relacionados con la solicitud del cliente.

Tambien verificara:

- Nombre del producto
- Categoria
- Anime
- Precio
- Stock disponible
- Nivel de demanda

### Agente 3: Agente recomendador

Este agente se encargara de sugerir productos de acuerdo con los datos encontrados.

La recomendacion se basara en:

- Anime solicitado
- Presupuesto del cliente
- Stock disponible
- Tipo de producto
- Popularidad del articulo

### Agente 4: Agente de reabastecimiento

Este agente analizara el inventario y detectara productos con pocas unidades disponibles.

Si algun producto tiene bajo stock, el sistema podra sugerir comprar mas unidades.

Ejemplo:

Si una figura de Naruto tiene 2 piezas en stock, el sistema puede marcarla como producto que necesita reabastecimiento.

### Agente 5: Agente explicador

Este agente explicara por que el sistema recomendo cierto producto o por que marco un articulo como bajo stock.

La idea es que el usuario pueda entender la decision del sistema y no solo recibir una respuesta automatica.

## Reglas de inferencia

El sistema usara reglas para tomar decisiones.

Ejemplos de reglas:

- Si el stock de un producto es menor a 5, entonces se recomienda reabastecimiento.
- Si el cliente busca un anime especifico, entonces se muestran productos relacionados con ese anime.
- Si el producto supera el presupuesto del cliente, entonces se busca una alternativa mas barata.
- Si un producto tiene alta demanda y bajo stock, entonces se marca como prioridad de compra.
- Si hay varios productos que cumplen con la solicitud, entonces se recomienda el de mejor relacion entre precio, disponibilidad y popularidad.

## Base de datos

El sistema usara una base de datos para guardar la informacion de la tienda.

La base de datos podra incluir:

- ID del producto
- Nombre del producto
- Anime relacionado
- Categoria
- Precio
- Stock disponible
- Nivel de demanda
- Ventas realizadas
- Recomendaciones generadas

## Ejemplo de uso

Entrada del cliente:

"Busco algo de Demon Slayer que cueste menos de 250 pesos"

Respuesta esperada del sistema:

"Se recomienda un llavero de Demon Slayer porque pertenece al anime solicitado, cuesta menos de 250 pesos y hay stock disponible."

Explicacion:

"El sistema reviso el presupuesto, el anime solicitado y la disponibilidad del producto antes de generar la recomendacion."

## Otro ejemplo de uso

Producto:

Figura de Naruto

Stock actual:

2 piezas

Regla aplicada:

Si el stock es menor a 5, entonces se recomienda reabastecimiento.

Resultado:

El sistema recomienda pedir mas figuras de Naruto porque el stock actual es bajo.

## Herramientas tentativas

- Python
- SQLite
- Flask o FastAPI
- Streamlit o Gradio
- GitHub
- Figma
- VS Code
- Librerias de inteligencia artificial

## Funcionamiento general

Primero, el usuario ingresara una solicitud o consulta sobre algun producto.

Despues, el sistema analizara la informacion usando sus agentes inteligentes.

Luego, el sistema consultara la base de datos y aplicara reglas de inferencia para generar una respuesta.

Finalmente, el sistema mostrara una recomendacion, una alerta de inventario o una explicacion de la decision tomada.

## Estado actual del proyecto

Actualmente el proyecto se encuentra en etapa inicial.

Por el momento se creo el repositorio en GitHub y se esta definiendo la idea principal del sistema, el objetivo, la arquitectura inicial, los agentes y las herramientas que se utilizaran durante el desarrollo.

## Proximos avances

- Crear la estructura de carpetas del proyecto
- Diseñar la base de datos inicial
- Agregar productos de ejemplo
- Crear reglas de inferencia
- Programar el agente de atencion al cliente
- Programar el agente de inventario
- Programar el agente recomendador
- Crear una interfaz basica
- Agregar evidencias del avance
- Realizar commits continuos durante el desarrollo

## Autor

Proyecto final de la materia Sistemas Expertos.
