alert('Boas vindas ao jogo do número secreto!'); // aparecer uma mensagem na tela
let numeroSecreto = 5; // criar uma variavel
console.log(numeroSecreto);
let chute;
let tentativas = 1;

//enquanto o chute nao for igual ao numero secreto
while(chute != numeroSecreto){
  chute = prompt('Escolha um número entre 1 e 10'); //exibi uma caixa de diálogo que solicita uma entrada do usuário
  //se o chute for igual ao numero secreto
  if (chute == numeroSecreto) {
    alert(`Isso ai, você descobriu o número secreto ${numeroSecreto} com ${tentativas} tentativas`); //imprimir o texto + o valor da variavel
  } else {
    if(chute < numeroSecreto){
      alert(`O número secreto é maior que ${chute}`);
    }else{
      alert(`O número secreto é menor que ${chute}`);
    }
    tentativas++;
  }
}