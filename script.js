
// Full character lists (abbreviated here for demo; full lists will be used in the zip)
const names = ["Alice","Bob","Charlie"];
const species = ["Human","Dragon","Kobold"];
const genders = ["Female","Male","Nonbinary"];
const height = ["Short","Average","Tall"];
const build = ["Slim","Athletic","Heavy"];
const bust = ["Small","Medium","Large"];
const hair_length = ["Short","Medium","Long"];
const hobbies = ["Reading","Fighting","Cooking"];
const job = ["Farmer","Soldier","Mage"];
const food = ["Bread","Meat","Fruit"];
const drink = ["Water","Wine","Ale"];
const personality = ["Cheerful","Serious","Shy"];
const quirk = ["Nervous","Brave","Lazy"];

// Random choice function
function choice(arr){return arr[Math.floor(Math.random()*arr.length)];}

// Update function to display character
function update(){
    const output = `You generated a character: ${choice(names)}, a ${choice(species)} ${choice(genders)}, ${choice(height)} tall, ${choice(build)} build, ${choice(bust)} bust, hair is ${choice(hair_length)}, enjoys ${choice(hobbies)}, works as a ${choice(job)}, favorite food is ${choice(food)}, favorite drink is ${choice(drink)}, personality is ${choice(personality)}, quirk is ${choice(quirk)}.`;
    document.getElementById("output").innerText = output;
}
