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

if(window.location.pathname === '/'){
    button = new ShortcutButton();
}


