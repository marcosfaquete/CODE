

console.log(' >>> Calculadora <<<');

window.alert(' >>> Calculadora <<<');


    var opcao = window.prompt('Digite sua Opção: ' + '\n [1] Somar\n [2] Subtração\n [3] Multiplicação\n');


if (opcao == 1){
    Soma();
    
} 
function Soma(){
    var numero_1 = window.prompt('>>> SOMAR <<<\n Digite o Primeiro numero: ');
    var numero_2 = window.prompt('>>> SOMAR <<<\n Digite o Segundo número: ');
    var resul_somar = parseInt(numero_1) + parseInt(numero_2);
    window.alert('O resultado da soma é: ' + resul_somar);
}

if (opcao == 2){
    Subtração();
}
function Subtração(){
    var numero_1 = window.prompt('>>> SUBTRAÇÃO <<<\n Digite o Primeiro Número: ');
    var numero_2 = window.prompt('>>> SUBTRAÇÃO <<<\n Digite o Segundo Número: ');
    var resul_subtracao = parseInt(numero_1) - parseInt(numero_2);
    window.alert('O resultado da Subtração é: ' + resul_subtracao);
}

if (opcao == 3){
    Multiplicacao();
}
function Multiplicacao(){
    var numero_1 = window.prompt('>>> MULTIPLICAÇÃO <<<\n Digite o Primeiro Número: ');
    var numero_2 = window.prompt('>>> MULTIPLICAÇÃO <<<\n Digite o Segundo Número: ');
    var resul_multiplicacao = parseInt(numero_1) * parseInt(numero_2);
    window.alert('O resultado da Multiplicação é: ' + resul_multiplicacao);
}
