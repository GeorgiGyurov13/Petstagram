function scrollToSection() {
        var targetSection = document.getElementById("service");

        var offsetTop = targetSection.offsetTop;
        setTimeout(function() {
            window.scrollTo({
                top: offsetTop,
                behavior: "smooth"
            });
        }, 500);
    }