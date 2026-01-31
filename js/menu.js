const burgerButton = document.querySelector('.humburger-menu')
const menu = document.querySelector('.menu')
const menuLinks = menu.querySelectorAll('.menu-list__item')

burgerButton.addEventListener('click', () => {
    menu.classList.add('menu-active')

})

menuLinks.forEach((links) => {
    links.addEventListener('click', () => {
        menu.classList.remove('menu-active')
    })
})

document.addEventListener('click', (event) => {
    if (!(event.target.closest('.menu') || event.target.closest('.humburger-menu'))) {
        menu.classList.remove('menu-active')
    }

})