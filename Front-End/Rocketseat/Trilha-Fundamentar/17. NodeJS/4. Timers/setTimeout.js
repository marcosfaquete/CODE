

// setTimeout rodar uma função depois de X milissegundos
// Assincronismo
// Callback

const timeOut = 3000
const finished = () => console.log('done!')

setTimeout(finished, timeOut)
console.log('Mostrar')
