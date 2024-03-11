# Gestor de Libros para Biblioteca

Este proyecto incluye una plataforma de gestión de libros diseñada para una biblioteca. La aplicación web está construida utilizando el framework Django siguiendo el patrón Modelo-Vista-Templado (MVT).

## 1. Modelos

- **Libro**: Cada libro tiene un título, autor, género, año de publicación, ISBN y una sinopsis.
- **Autor**: Los autores tienen un nombre y una biografía. Pueden estar asociados con uno o más libros.
- **Género**: Los géneros representan las categorías a las que pertenecen los libros, como ficción, no ficción, ciencia ficción, etc.

## 2. Formularios

- **Formulario de ingreso de libros**: Permite a los administradores de la biblioteca agregar nuevos libros a la base de datos ingresando información como título, autor, género, año de publicación, ISBN y sinopsis.
- **Formulario de búsqueda de libros**: Los usuarios pueden buscar libros por título.

## 3. Vistas

- **Página de inicio (index)**: Página de inicio de la biblioteca. Permite acceder a las distintas secciones y formularios.
- **Página de libros**: Muestra información detallada sobre los libros registrados, incluyendo título, autor, género, año de publicación e ISBN.
- **Página de autores**: Muestra una lista de todos los autores en la base de datos.
- **Página de géneros**: Muestra una lista de todos los géneros en la base de datos.
- **Formulario de búsqueda de libros**: Muestra los resultados de la búsqueda de libros basados en los criterios especificados por el usuario.
- **Formulario de ingreso de libros**: Formularios para que los administradores ingresen nuevos libros a la base de datos.
