
console.log('\n');
console.log('<<< Média Aluno >>>')
console.log('\n')

var nome = window.prompt('Digite o nome do aluno: ');
console.log('Nome do Aluno é: ' + nome);

var nota_1 = window.prompt('Digite a primeira nota de ' + nome + ': ');
console.log('Primeira Nota de ' + nome + ' é: ' + nota_1);

var nota_2 = window.prompt('Digite a segunda nota de ' + nome + ': ');
console.log('Segunda Nota de ' + nome + ' é: ' + nota_2);
console.log('\n');

var soma = parseInt(nota_1) + parseInt(nota_2);
var media = (soma / 2);

console.log('A média do aluno ' + nome + ' é: ' + media);
window.alert('A média do aluno ' + nome + ' é: ' + media);

if (media < 5){
    console.log('Aluno ' + nome + ' <<< Está REPROVADO! >>>');
    window.alert('Aluno ' + nome + ' <<< Está REPROVADO! >>>');

} else {
    console.log('Aluno ' + nome + ' <<< Está APROVADO! >>>');
    window.alert('Aluno ' + nome + ' <<< Está APROVADO! >>>');
}