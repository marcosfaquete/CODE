// Código aula 01 Alura 

/*
var notaDoPrimeiroBimestre = 9;
var notaDoSegundoBimestre = 7;
var notaDoTerceiroBimestre = 4;
var notaDoQuartoBimestre = 2;

var notaFinal = (notaDoPrimeiroBimestre + notaDoSegundoBimestre + notaDoTerceiroBimestre + notaDoQuartoBimestre) / 4;

var notaFixada = notaFinal.toFixed(1);

console.log("Bem vindo + Marcos");
console.log(notaFixada);
*/

//===============================================================================

// My Code

console.log('\n<<< Software Média Aluno >>>');

function Nota(nt01, nt02) {

    window.alert("Digite as Notas do Aluno");
    var nt01 = window.prompt("Digite a Primeira Nota do Aluno:> ");
    var nt02 = window.prompt("Digite a Segunda nota do Aluno:> ");

    console.log('\nNota1: ' + nt01);
    console.log('Nota2: ' + nt02);
 
    var ntSoma = parseInt(nt01) + parseInt(nt02);
    console.log('Soma das Notas: ' + ntSoma);

    var mediaFinal = ntSoma / 2;
    console.log('\n Média do Aluno: ' + mediaFinal);

    if (mediaFinal >= 5) {
        console.log("\n<<< Aluno Aprovado! >>>");

    } else {
        console.log("\n<<< Aluno Reprovado! >>>");
    }
}

Nota();