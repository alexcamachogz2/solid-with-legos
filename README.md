# Aprendiendo SOLID con LEGOs


En el código ejemplo, cada clase cumple con una responsabilidad única (Pedido, ProcesadorDePagos, Notificador). Además, el sistema está diseñado para ser extensible (nuevos métodos de pago o notificación pueden ser añadidos fácilmente). Las clases de pago son intercambiables sin afectar el sistema (Liskov). Las interfaces para los notificadores están segregadas, permitiendo diferentes implementaciones de notificaciones. Y por último, el `GestorDePedidos` depende de abstracciones, no de clases concretas, lo cual facilita el cambio de los componentes del sistema.

Si quieres leer más sobre los principios SOLID te invito a leer [mi newsletter](https://alexcamachogz.substack.com/)https://alexcamachogz.substack.com/.
