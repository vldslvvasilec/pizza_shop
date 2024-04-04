const openModal = (btnId, fetchUrl) => {
    const openModalBtn = document.querySelector(btnId);
    const wrap = document.querySelector(".loging_wrap");
    const modal = document.querySelector(".registerModal");

    if (openModalBtn && modal) {
        openModalBtn.addEventListener("click", async (event) => {
            event.preventDefault();
            event.stopPropagation(); // Остановить всплытие события

            try {
                // Загрузка содержимого формы из Django представления
                const response = await fetch(fetchUrl);
                
                if (!response.ok) {
                    // Если ответ от сервера не успешный, выбрасываем ошибку с информацией о статусе ответа
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                // Если ответ успешный, получаем текст ответа
                const data = await response.text();
            
                // Вставляем HTML-код формы в модальное окно
                modal.innerHTML = data;
                // Отображаем модальное окно
                wrap.style.display = "flex";
                modal.style.display = "block";
            
                // Переназначаем обработчик клика на кнопке закрытия модального окна
                modal
                    .querySelector(".close_button")
                    .addEventListener("click", close_modal);
            } catch (error) {
                // В случае ошибки выводим сообщение об ошибке в консоль
                console.error("Ошибка при попытке открыть модальное окно: ", error);
                // Можно также предпринять другие действия, например, показать пользователю сообщение об ошибке
            }
        });
    }
};

const close_modal = () => {
    const wrap = document.querySelector(".loging_wrap");
    const modal = document.querySelector(".registerModal");
    wrap.style.display = "none";
    modal.style.display = "none";
};

// Вызов функции для каждой кнопки
// openModal(".log_button_singin", "/registr/");
openModal(".log_button_loging", "/login/");
