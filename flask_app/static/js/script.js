// require('dotenv').config()
// console.log(process.env.FLASK_APP_API_KEY)
var drinkResultDiv = document.querySelector('#drinkResults');
// CocktailDB api Base url --------- this is a development/educational test key
var COCKTAIL_URL = `https://thecocktaildb.com/api/json/v1/1/search.php?s=`

let drink = document.getElementById('drink');
let thumbnail = document.getElementById('thumbnail');
let instructions = document.getElementById('instructions');
let ingredient1 = document.getElementById('ingredient1');
let ingredient2 = document.getElementById('ingredient2');
let ingredient3 = document.getElementById('ingredient3');
let ingredient4 = document.getElementById('ingredient4');
let ingredient5 = document.getElementById('ingredient5');
let measurement1 = document.getElementById('measurement1');
let measurement2 = document.getElementById('measurement2');
let measurement3 = document.getElementById('measurement3');
let measurement4 = document.getElementById('measurement4');
let measurement5 = document.getElementById('measurement5');
let counter = 0;

function getDrink(event) {
    event.preventDefault();

    var drinkName = document.querySelector('#drinkName').value;

    fetch(COCKTAIL_URL + drinkName)
        .then(function(someServerResponse) {
            return someServerResponse.json()
        })
        .then(function(data) {
            allDrinks = [];
            // if searched word is not in the results
            if(data.drinks === null) {
                document.getElementById('notFound').innerText = "Oops! We couldn't find what you're looking for.";
            } else if (data.drinks !== null) {
                document.getElementById('notFound').innerText = "";
                for (let i = 0; i < data.drinks.length; i++) {
                    allDrinks.push(data.drinks[i]);
                }
                document.querySelector('.drinkcard').style.opacity=1
                drink.innerText = allDrinks[counter].strDrink;
                thumbnail.src = allDrinks[counter].strDrinkThumb;
                instructions.innerText = allDrinks[counter].strInstructions;
                ingredient1.innerText = allDrinks[counter].strIngredient1;
                ingredient2.innerText = allDrinks[counter].strIngredient2;
                ingredient3.innerText = allDrinks[counter].strIngredient3;
                ingredient4.innerText = allDrinks[counter].strIngredient4;
                ingredient5.innerText = allDrinks[counter].strIngredient5;
                measurement1.innerText = allDrinks[counter].strMeasure1;
                measurement2.innerText = allDrinks[counter].strMeasure2;
                measurement3.innerText = allDrinks[counter].strMeasure3;
                measurement4.innerText = allDrinks[counter].strMeasure4;
                measurement5.innerText = allDrinks[counter].strMeasure5;
            } 
        })
        .catch(error => {
            // Handle the error here
            console.log('Something went wrong...', error)
        })
};

document.getElementById('next').addEventListener('click', nextButton);
function nextButton() {
    counter++;
    
    if (counter > allDrinks.length - 1) {
        counter = 0;
        drink.innerText = allDrinks[counter].strDrink;
        thumbnail.src = allDrinks[counter].strDrinkThumb;
        instructions.innerText = allDrinks[counter].strInstructions;
        ingredient1.innerText = allDrinks[counter].strIngredient1;
        ingredient2.innerText = allDrinks[counter].strIngredient2;
        ingredient3.innerText = allDrinks[counter].strIngredient3;
        ingredient4.innerText = allDrinks[counter].strIngredient4;
        ingredient5.innerText = allDrinks[counter].strIngredient5;
        measurement1.innerText = allDrinks[counter].strMeasure1;
        measurement2.innerText = allDrinks[counter].strMeasure2;
        measurement3.innerText = allDrinks[counter].strMeasure3;
        measurement4.innerText = allDrinks[counter].strMeasure4;
        measurement5.innerText = allDrinks[counter].strMeasure5;
    }
    else {
        drink.innerText = allDrinks[counter].strDrink;
        thumbnail.src = allDrinks[counter].strDrinkThumb;
        instructions.innerText = allDrinks[counter].strInstructions;
        ingredient1.innerText = allDrinks[counter].strIngredient1;
        ingredient2.innerText = allDrinks[counter].strIngredient2;
        ingredient3.innerText = allDrinks[counter].strIngredient3;
        ingredient4.innerText = allDrinks[counter].strIngredient4;
        ingredient5.innerText = allDrinks[counter].strIngredient5;
        measurement1.innerText = allDrinks[counter].strMeasure1;
        measurement2.innerText = allDrinks[counter].strMeasure2;
        measurement3.innerText = allDrinks[counter].strMeasure3;
        measurement4.innerText = allDrinks[counter].strMeasure4;
        measurement5.innerText = allDrinks[counter].strMeasure5;
    }
};

document.getElementById('previous').addEventListener('click', previousButton);
function previousButton() {
    counter--;
    
    if (counter < 0) {
        counter = allDrinks.length - 1;
        drink.innerText = allDrinks[counter].strDrink;
        thumbnail.src = allDrinks[counter].strDrinkThumb;
        instructions.innerText = allDrinks[counter].strInstructions;
        ingredient1.innerText = allDrinks[counter].strIngredient1;
        ingredient2.innerText = allDrinks[counter].strIngredient2;
        ingredient3.innerText = allDrinks[counter].strIngredient3;
        ingredient4.innerText = allDrinks[counter].strIngredient4;
        ingredient5.innerText = allDrinks[counter].strIngredient5;
        measurement1.innerText = allDrinks[counter].strMeasure1;
        measurement2.innerText = allDrinks[counter].strMeasure2;
        measurement3.innerText = allDrinks[counter].strMeasure3;
        measurement4.innerText = allDrinks[counter].strMeasure4;
        measurement5.innerText = allDrinks[counter].strMeasure5;
    }
    else {
        drink.innerText = allDrinks[counter].strDrink;
        thumbnail.src = allDrinks[counter].strDrinkThumb;
        instructions.innerText = allDrinks[counter].strInstructions;
        ingredient1.innerText = allDrinks[counter].strIngredient1;
        ingredient2.innerText = allDrinks[counter].strIngredient2;
        ingredient3.innerText = allDrinks[counter].strIngredient3;
        ingredient4.innerText = allDrinks[counter].strIngredient4;
        ingredient5.innerText = allDrinks[counter].strIngredient5;
        measurement1.innerText = allDrinks[counter].strMeasure1;
        measurement2.innerText = allDrinks[counter].strMeasure2;
        measurement3.innerText = allDrinks[counter].strMeasure3;
        measurement4.innerText = allDrinks[counter].strMeasure4;
        measurement5.innerText = allDrinks[counter].strMeasure5;
    }
};

let savedDrink = document.getElementById('save-drink').addEventListener('click', function(event) {
    document.getElementById('save-drink').innerText = 'Coming Soon!';

});
