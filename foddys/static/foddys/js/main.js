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

class deleteRecipe {
    constructor() {
        this.button = document.getElementById('deleteButton');

        
        this.button.addEventListener('click', this.deleteAccept)
    }

    deleteAccept() {
        window.location.replace('/my_recipes/')
        console.log('siema')
    }
}
if(window.location.pathname === '/recipe/'){
const siema = new deleteRecipe()
}

if(window.location.pathname === '/'){
    button = new ShortcutButton();
}


