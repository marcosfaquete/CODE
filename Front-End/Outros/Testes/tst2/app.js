
let tracert = "======================================================";

console.log(tracert);
process.stdout.write("\n                <<< Software >>> ");
console.log('\n');
console.log(tracert);




const perguntas = [
    "Olá qual é o seu nome? > ",
]


const respostas = [];

process.stdin.on("data", data => {
    answers.push(data.toString().trim());
})