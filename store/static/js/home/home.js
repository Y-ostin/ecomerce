document.addEventListener("DOMContentLoaded", function () {
    const elements = document.querySelectorAll(".features-area .single-features, .single-product");
  
    // Animación de aparición al hacer scroll
    function fadeInOnScroll() {
      elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
  
        if (elementTop < windowHeight - 100) {
          element.style.opacity = "1";
          element.style.transform = "translateY(0)";
        } else {
          element.style.opacity = "0";
          element.style.transform = "translateY(20px)";
        }
      });
    }
  
    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll(); // Llamada inicial para cargar elementos visibles en pantalla
  
    // Efecto de "clic" en el botón de añadir al carrito
    const cartButtons = document.querySelectorAll(".update-cart");
    cartButtons.forEach(button => {
      button.addEventListener("click", () => {
        button.classList.add("clicked");
        setTimeout(() => {
          button.classList.remove("clicked");
        }, 300);
      });
    });
  });
  