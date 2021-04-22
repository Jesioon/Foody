class ShortcutButton {
    constructor() {
        this.hour = new Date().getHours();
        this.button = document.getElementById('buttonMealTime');

        this.checkTime(this.hour);
    }

    checkTime(hour) {
        if (hour<=10) {
            this.button.textContent = 'Śniadanie';
            this.button.href = '/recipes/mealTime/Śniadanie/';
        }
        else if(hour<=16) {
            this.button.textContent = 'Obiad';
            this.button.href = '/recipes/mealTime/Obiad/'
        }
        else {
            this.button.textContent = 'Kolacje';
            this.button.href = '/recipes/mealTime/Kolacja/';
        }
    }
}

class BurgerButton {
    constructor() {
        this.button = document.querySelector('.burger');
        this.menu = document.querySelector('.burgerMenu');
        this.button.addEventListener('click', this.dropdownMenu.bind(this));    
    }

    dropdownMenu() {
        this.button.classList.toggle('active');

        if(this.button.classList.contains('active')) {
            this.menu.style.transform = 'scale(1)';
            // this.button.style.backgroundColor = '#ff3800';
            // this.button.style.color = '#fff';
        }
        else {
            this.menu.style.transform = 'scale(0)';
            // this.button.style.backgroundColor = '#fff';
            // this.button.style.color = '#000';
        }
    }
}


if(window.location.pathname === '/'){
    const button = new ShortcutButton();
}

const menuRWD = new BurgerButton();


