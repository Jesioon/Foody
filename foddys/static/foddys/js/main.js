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

        this.buttonCountry = document.querySelector('.showCountryList');
        this.buttonTime = document.querySelector('.showTimeList');
        this.recipesCountry = document.querySelector('.countryList');
        this.recipesMealTime = document.querySelector('.timeList');

        this.hideCountry = document.querySelector('.hideCountryList');
        this.hideTime = document.querySelector('.hideTimeList');

        this.buttonCountry.addEventListener('click', this.showCountryList.bind(this));
        this.buttonTime.addEventListener('click', this.showTimeList.bind(this));
        this.button.addEventListener('click', this.dropdownMenu.bind(this));    
        this.hideCountry.addEventListener('click', this.hideCountryList.bind(this))
        this.hideTime.addEventListener('click', this.hideTimeList.bind(this))

    }

    dropdownMenu() {
        this.button.classList.toggle('active');

        if(this.button.classList.contains('active')) {
            this.menu.style.transform = 'scale(1)';
        }
        else {
            this.menu.style.transform = 'scale(0)';
            this.recipesCountry.style.transform = 'scale(0)';
            this.recipesMealTime.style.transform = 'scale(0)';
        }
    }

    showCountryList() {
        this.recipesCountry.style.transform = 'scale(1)';
        this.recipesMealTime.style.transform = 'scale(0)';
    }

    showTimeList() {
        this.recipesMealTime.style.transform = 'scale(1)';
        this.recipesCountry.style.transform = 'scale(0)';
    }

    hideCountryList() {
        this.recipesCountry.style.transform = 'scale(0)';
    }

    hideTimeList() {
        this.recipesMealTime.style.transform = 'scale(0)';
    }
}


if(window.location.pathname === '/'){
    const button = new ShortcutButton();
}

const menuRWD = new BurgerButton();


