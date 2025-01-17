let titulo = document.querySelector('h1'); //selecionar a tag h1 no documento HTML
titulo.innerHTML = 'Jogo do número secreto'; //Inserir o texto dentro da tag h1

let paragrafo = document.querySelector('p');
paragrafo.innerHTML = 'Escolha um número entre 1 e 10';

function verificarChute(){ //funcao do botao de CHUTE
    console.log('O botao foi clicado');
}