// script.js

// document = representacion en memoria cache de la estructura de una pagina, este objeto puede manipular todo el contenido de la pagina

// addEventListener = metodo que agrega eventos a un elemento html del DOM (Document Object Model)

// DOMContentLoaded = evento que carga la pagina web

// function () {const navbarToggler = document.querySelector(".navbar-toggler"); = esta funcion busca y selcciona el elemento html que contenga la clase CSS ("navbar-toggler")

// navbarToggler.addEventListener("click", function () {this.classList.toggle("active"); = se agrega un nuevo evento llaado "(click)", es decir cuando se hage click en el button del navbar entonces se ejecuta la funcion como segunda argumento

// this = se refiere al evento actual al cual se disparo el evento en este caso ("click")

// classList = propiedad del eleemto DOM- que permite manipular las clases css

// toggle = el metodo "toggle" de "classList" permite saber si un elemento ya tiene la clase "toggle" ("active") y si no la tiene se la agrega esto permite cambiar la apariencia del boton navbar, agregando o quitando el estilo aplicado en active



document.addEventListener("DOMContentLoaded", function () {
    const navbarToggler = document.querySelector(".navbar-toggler");
  
    navbarToggler.addEventListener("click", function () {
      this.classList.toggle("active");
  
      const navbarCollapse = document.querySelector(".navbar-collapse");
      navbarCollapse.classList.toggle("active");
    });
});