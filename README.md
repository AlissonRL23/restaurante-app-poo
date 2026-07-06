# Sistema Restaurante - Programación Orientada a Objetos

**Nombre del estudiante:** Crisley Robalino

## Descripción

Este proyecto consiste en un sistema básico para administrar los productos de un restaurante utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite registrar platillos y bebidas aplicando los principios de herencia, encapsulación y polimorfismo.

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Herencia

La clase **Producto** es la clase padre del sistema. De ella heredan las clases **Platillo** y **Bebida**, reutilizando los atributos y métodos comunes mediante el uso de `super()`.

## Encapsulación

El atributo **precio** se encuentra encapsulado mediante `__precio`. Para acceder y modificar este atributo se utilizan los métodos `obtener_precio()` y `cambiar_precio()`, validando que el precio sea mayor que cero.

## Polimorfismo

Las clases **Platillo** y **Bebida** sobrescriben el método `mostrar_informacion()`, permitiendo que cada objeto muestre información diferente según su tipo.

## Reflexión

La Programación Orientada a Objetos facilita el desarrollo de aplicaciones organizadas, reutilizables y fáciles de mantener. La aplicación de herencia, encapsulación y polimorfismo mejora la estructura del código y permite desarrollar sistemas más eficientes y escalables.
