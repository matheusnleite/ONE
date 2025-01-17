// let titulo = document.querySelector('h1'); //selecionar a tag h1 no documento HTML
// titulo.innerHTML = 'Jogo do número secreto'; //Inserir o texto dentro da tag h1

// let paragrafo = document.querySelector('p');
// paragrafo.innerHTML = 'Escolha um número entre 1 e 10';

function exibirTextoNaTela(tag, texto){ // funcao para otimizar o codigo, resumindo o que as 4 linhas acima faziam
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

exibirTextoNaTela('h1', 'Jogo do número secreto');  //chamando a funcao de exibir texto na tela
exibirTextoNaTela('p', 'Escolha um número entre 1 e 10');

function verificarChute(){ //funcao do botao de CHUTE
    console.log('O botao foi clicado');
}