
    // EXEMPLOS 
const user = {
    nome: "Marcos",
    email: "Marcos@gmail.com",
    nascimento: "01/08/23",
    role: "estudante",
    ativo: true,
    exibirInfos: function() {
        console.log(this.nome, this.email)
    }
}

user.exibirInfos()
// const exibir = user.exibirInfos
// exibir()

const exibir = function() {
    console.log(this.nome, this.email)
}

// Bind método que usamos para prender a execução de uma função num contexto específico
const exibirNome = exibir.bind(user)
exibirNome()
exibir()

    // EXEMPLOS 
const main = {
    nome: "Ana",
    email: "Ana@gmail.com",
    role: "admin",
    criarCurso() {
        console.log('Curso Criado!')
    }
}

// Métodos são funções chamadas dentro do contexto de um objeto
    // EXEMPLOS 
const gato1 = {
    nome: "Maga",
    nascimento: "25/11/2020",
    pelagem: "Mesclada",
    status: {
        castrada: true,
        vacinada: true,
        vermifugada: true
    },
}

// Não faz sentido criar um objeto para cada usuario
// Temos que aprender a reaproveitar o código

// O correto é ter um MODELO DE OBJETO
    // EXEMPLOS 
const gato2 = {
    nome: "Ameixa",
    nascimento: "25/11/2021",
    pelagem: "Mesclada",
    status: {
        castrada: true,
        vacinada: true,
        vermifugada: true
    },
}


// MODELO DE OBJETOS
// EXEMPLO:
const modeloObjeto = {
    nome: stringNome,
    nascimento: stringData,
    pelagem: stringPelagem,
    status: {
        castrado: boolCastrado,
        vacinado: boolVacinado,
        vermifugado: boolVermifugado
    },
}