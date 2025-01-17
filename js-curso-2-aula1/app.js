// let titulo = document.querySelector('h1'); //selecionar a tag h1 no documento HTML
// titulo.innerHTML = 'Jogo do número secreto'; //Inserir o texto dentro da tag h1

// let paragrafo = document.querySelector('p');
// paragrafo.innerHTML = 'Escolha um número entre 1 e 10';

let numeroSecreto = gerarNumeroAleatorio();
let tentativas = 1;

function exibirTextoNaTela(tag, texto){ // funcao para otimizar o codigo, resumindo o que as 4 linhas acima faziam
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

exibirTextoNaTela('h1', 'Jogo do número secreto');  //chamando a funcao de exibir texto na tela
exibirTextoNaTela('p', 'Escolha um número entre 1 e 10');

function verificarChute(){ //funcao do botao de CHUTE
    let chute = document.querySelector('input').value; // pegar o valor dentro da tag
    if(chute == numeroSecreto){
        exibirTextoNaTela('h1', 'Acertou!');
        let palavraTentativa = tentativas > 1? 'tentativas':'tentativa';
        let mensagemTentativas = `Você descobriu o número secreto com ${tentativas} ${palavraTentativa}!`;
        exibirTextoNaTela('p', mensagemTentativas);
    }else{ 
        if(chute > numeroSecreto){
            exibirTextoNaTela('p', 'O número secreto é menor');
            }else{
                exibirTextoNaTela('p', 'O número secreto é maior');
        }
        tentativas++;
    }
}

function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1);
}