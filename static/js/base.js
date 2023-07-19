document.addEventListener('DOMContentLoaded', function () {
    const filterButtons = document.querySelectorAll('.filter-link');

    filterButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault();

            const categoria = button.dataset.categoria;

            // Realizar la redirección a la página PropiedadListView con el parámetro de consulta categoria
            window.location.href = "?categoria=" + categoria;
        });
    });
});
