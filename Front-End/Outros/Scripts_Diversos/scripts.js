
// Imprimindo Nomes
function nomes() {
    var namelist = [];
    namelist.push('Marcos','Ana','Julia','João');
    for(var i =0; i < namelist.length; i++)
    console.log("Olá " + namelist[i] + " !");
    console.log('Dentro da Array(Lista) temos ' + (namelist.length) + ' Nomes.');
}
nomes(); //Chamando função.

//===========================================================================================

// Semáfaro
console.log('\n')
console.log(' >>> Semáfaro <<<')
console.log('\n')
function Sinal(x) {     
    if (x == 1) {
        console.log('Sinal Vermelho, Pare!');
    }else if (x == 2) {
        console.log('Sinal Amarelo, Atenção!');
    }else if (x == 3) {
        console.log('Sinal Verde, Siga em Frente!');
    }else if (x === 1 && 2 || 3) {
        console.log('Código Inválido!')
    }
 } 
Sinal(1);               // Chamando a Funcão
console.log('\n')       
Sinal(2);               // Chamando a Funcão
console.log('\n')
Sinal(3);               // Chamando a Funcão
console.log('\n')
Sinal();                // Chamando a Funcão


