// const manage_menu_button_1 = document.querySelector(".manager_closing_menu");
// const manage_menu_menu_1 = document.querySelector(".manage_nav");
// const manage_menu_button_2 = document.querySelector(".nav-link-manage");
// const manage_menu_menu_2 = document.querySelector(".manager_product_list");

// const open_manage_menu = (button, menu) => {
//     button.addEventListener('mouseenter', function() {
//         menu.style.display = "flex";
//     });

//     menu.addEventListener('mouseleave', function() {
//         setTimeout(function() {
//             menu.style.display = "none";
//         }, 1000);
//     });

//     // Скрываем меню при клике на элементы
//     document.addEventListener('click', function(event) {
//         if (!menu.contains(event.target) && event.target !== button) {
//             setTimeout(function() {
//                 menu.style.display = "none";
//             }, 1000);
//         }
//     });
// };

// open_manage_menu(manage_menu_button_1, manage_menu_menu_1);
// open_manage_menu(manage_menu_button_2, manage_menu_menu_2);

// const manage_menu_button_1 = document.querySelector(".manager_closing_menu");
// const manage_menu_menu_1 = document.querySelector(".manage_nav");
// const manage_menu_button_2 = document.querySelector(".nav-link-manage");
// const manage_menu_menu_2 = document.querySelector(".manager_product_list");

// const open_manage_menu = (button, menu) => {
//     // Удаляем существующие обработчики событий
//     button.removeEventListener('mouseenter', showMenu);
//     menu.removeEventListener('mouseleave', hideMenu);
//     document.removeEventListener('click', hideMenuOnClick);

//     // Добавляем новые обработчики событий
//     const showMenu = () => {
//         menu.style.display = "flex";
//     };

//     const hideMenu = () => {
//         setTimeout(function() {
//             menu.style.display = "none";
//         }, 1000);
//     };

//     const hideMenuOnClick = (event) => {
//         if (!menu.contains(event.target) && event.target !== button) {
//             setTimeout(function() {
//                 menu.style.display = "none";
//             }, 1000);
//         }
//     };

//     button.addEventListener('mouseenter', showMenu);
//     menu.addEventListener('mouseleave', hideMenu);
//     document.addEventListener('click', hideMenuOnClick);
// };

// open_manage_menu(manage_menu_button_1, manage_menu_menu_1);
// open_manage_menu(manage_menu_button_2, manage_menu_menu_2);

// const manage_menu_button_1 = document.querySelector(".manager_closing_menu");
// const manage_menu_menu_1 = document.querySelector(".manage_nav");
// const manage_menu_button_2 = document.querySelector(".nav-link-manage");
// const manage_menu_menu_2 = document.querySelector(".manager_product_list");

// const open_manage_menu = (button, menu) => {
//     let isMenuOpen = false;
//     let isCursorInMenu = false;

//     const showMenu = () => {
//         menu.style.display = "flex";
//         isMenuOpen = true;
//     };

//     const hideMenu = () => {
//         if (!isCursorInMenu) {
//             setTimeout(function() {
//                 if (!isCursorInMenu) {
//                     menu.style.display = "none";
//                     isMenuOpen = false;
//                 }
//             }, 1000);
//         }
//     };

//     const hideMenuOnClick = (event) => {
//         if (!menu.contains(event.target) && event.target !== button) {
//             setTimeout(function() {
//                 if (!isCursorInMenu) {
//                     menu.style.display = "none";
//                     isMenuOpen = false;
//                 }
//             }, 1000);
//         }
//     };

//     button.addEventListener('mouseenter', showMenu);
//     button.addEventListener('mouseleave', hideMenu);
//     menu.addEventListener('mouseenter', () => isCursorInMenu = true);
//     menu.addEventListener('mouseleave', () => {
//         isCursorInMenu = false;
//         hideMenu();
//     });
//     document.addEventListener('click', hideMenuOnClick);
// };

// open_manage_menu(manage_menu_button_1, manage_menu_menu_1);
// open_manage_menu(manage_menu_button_2, manage_menu_menu_2);

const manage_menu_button_1 = document.querySelector(".manager_closing_menu");
const manage_menu_menu_1 = document.querySelector(".manage_nav");
const manage_menu_button_2 = document.querySelector(".nav-link-manage");
const manage_menu_menu_2 = document.querySelector(".manager_product_list");

const open_manage_menu = (button, menu) => {
    let hideMenuTimeout;

    const showMenu = () => {
        clearTimeout(hideMenuTimeout);
        menu.style.display = "flex";
    };

    const hideMenu = () => {
        hideMenuTimeout = setTimeout(function() {
            menu.style.display = "none";
        }, 1000);
    };

    const hideMenuOnClick = (event) => {
        if (!menu.contains(event.target) && event.target !== button) {
            hideMenu();
        }
    };

    button.addEventListener('mouseenter', showMenu);
    button.addEventListener('mouseleave', hideMenu);
    menu.addEventListener('mouseenter', showMenu);
    menu.addEventListener('mouseleave', hideMenu);
    document.addEventListener('click', hideMenuOnClick);
};

open_manage_menu(manage_menu_button_1, manage_menu_menu_1);
open_manage_menu(manage_menu_button_2, manage_menu_menu_2);
