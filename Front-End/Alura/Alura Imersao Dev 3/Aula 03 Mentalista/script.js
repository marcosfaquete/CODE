function Chutar() {
    var numeroSecreto = parseInt(Math.random() * 11);
    var elementoResultado = document.getElementById("resultado");
    var chute = parseInt(document.getElementById("valor").value);
    console.log(chute);

    if (chute == numeroSecreto) {
        elementoResultado.innerHTML = "Você acertou";
        console.log("acertou");

    } else if (chute > 10 || chute < 0) {
        elementoResultado.innerHTML = "Você deve digitar um número de 0 a 10";
        console.log("Você deve digitar um número de 0 a 10");
    
    } else {
        elementoResultado.innerHTML = "Errou, o número secreto era " + numeroSecreto;
        console.log("errou");
    }
}