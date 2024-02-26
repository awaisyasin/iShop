const removeIcons = document.querySelectorAll('.fa-circle-xmark')

removeIcons.forEach(icon => {
    icon.addEventListener('click', () => {
        const message = icon.closest('.message')
        message.remove()
    })
})