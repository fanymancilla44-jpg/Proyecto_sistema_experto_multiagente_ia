# Reglas de inferencia

En esta parte se explican algunas reglas que se usaran dentro del sistema AnimeFull para que pueda tomar decisiones.

Las reglas de inferencia son importantes porque ayudan a que el sistema no solo guarde informacion, sino que tambien pueda analizar datos y dar una respuesta.

Por ejemplo, si un producto tiene poco stock, el sistema podra detectar que necesita reabastecimiento.

Algunas reglas iniciales seran:

- Si el stock de un producto es menor al stock minimo, entonces se marca como bajo stock.
- Si el stock es igual a cero, entonces el producto se marca como agotado.
- Si el cliente busca un anime especifico, entonces se buscan productos relacionados con ese anime.
- Si el producto supera el presupuesto del cliente, entonces se busca otra opcion mas barata.
- Si un producto tiene alta demanda y poco stock, entonces se recomienda comprar mas unidades.
- Si un producto coincide con el anime, presupuesto y disponibilidad, entonces se recomienda al cliente.

Estas reglan mejoraran conforme al avance del proyecto.