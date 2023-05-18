
document.getElementById("Media_Aluno").innerHTML = 'Média do Aluno';

nome_aluno = window.prompt('Digite o nome do aluno: ');
document.getElementById("Nome_Aluno").innerHTML = 'Nome do Aluno: ' + nome_aluno;

nota_1 = window.prompt('Digite a Primeira nota do aluno: ');
document.getElementById("Nota_1").innerHTML = 'Nota da Primeira Prova: ' + nota_1;

nota_2 = window.prompt('Digite a Segunda nota do aluno: ');
document.getElementById("Nota_2").innerHTML = 'Nota da Segunda Prova: ' + nota_2;

media = parseInt(nota_1) + parseInt(nota_2) / 2;
document.getElementById("Media").innerHTML = 'A Média do aluno ' + nome_aluno + ' é: ' + media;

    if (media < 5) {
        document.getElementById("Msg_1").innerHTML = 'Aluno ' + nome_aluno + ' Está Reprovado!';
    } else {
        document.getElementById("Msg_1").innerHTML = 'Aluno ' + nome_aluno + ' Está Aprovado!'        
    } 
