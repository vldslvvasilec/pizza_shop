document.addEventListener('DOMContentLoaded', function() {
    let numberButtons = document.querySelectorAll('.number_button');
    let orderButtons = document.querySelectorAll('.card-btn');
    let products = {}; // Объект для хранения данных о продуктах

    numberButtons.forEach(function(numberButton) {
        numberButton.addEventListener('click', function() {
            let productTitle = this.dataset.productTitle;
            let numberType = this.classList.contains('number_plus') ? 'plus' : 'minus';
            let numberElement = document.querySelector('.number_number[data-product-title="' + productTitle + '"]');
            let currentValue = parseInt(numberElement.textContent);
            
            // Увеличиваем или уменьшаем значение в зависимости от типа кнопки
            if (numberType === 'plus') {
                numberElement.textContent = currentValue + 1;
            } else {
                numberElement.textContent = Math.max(currentValue - 1, 0);
            }

            // Обновляем количество в объекте продукта
            products[productTitle] = parseInt(numberElement.textContent);
        });
    });

    orderButtons.forEach(function(orderButton) {
        orderButton.addEventListener('click', function() {
            let productTitle = this.dataset.productTitle;
            let quantityElement = document.querySelector('.number_number[data-product-title="' + productTitle + '"]');
            let quantity = parseInt(quantityElement.textContent);
            
            // Добавляем данные о продукте и количестве в объект
            products = {productTitle: productTitle, quantity: quantity};
            
            // Сбрасываем количество в 0
            quantityElement.textContent = 0;

            // Выводим данные о продукте и количестве
            console.log(products);
        });
    });
});
