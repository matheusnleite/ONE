alert('Boas vindas ao jogo do número secreto!'); // aparecer uma mensagem na tela
let numeroSecreto = 5; // criar uma variavel
console.log(numeroSecreto);
let chute = prompt('Escolha um número entre 1 e 10'); //exibi uma caixa de diálogo que solicita uma entrada do usuário

if (chute == numeroSecreto) {
  alert('Isso ai, você descobriu o número secreto(5)'); //imprimir mensagens no console do navegador
} else {
  alert('Você errou :(');
}
