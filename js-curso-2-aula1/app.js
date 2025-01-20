// let titulo = document.querySelector('h1'); //selecionar a tag h1 no documento HTML
// titulo.innerHTML = 'Jogo do número secreto'; //Inserir o texto dentro da tag h1

// let paragrafo = document.querySelector('p');
// paragrafo.innerHTML = 'Escolha um número entre 1 e 10';
let listaDeNumerosSorteados = [];
let numeroLimite = 3;
let numeroSecreto = gerarNumeroAleatorio();
let tentativas = 1;

function exibirTextoNaTela(tag, texto){ // funcao para otimizar o codigo, resumindo o que as 4 linhas acima faziam
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
    responsiveVoice.speak(texto, 'Brazilian Portuguese Female', {rate:1.2}); // script que vai ler e falar um texto na sua pagina
}


function exibirMensagemInicial(){
    exibirTextoNaTela('h1', 'Jogo do número secreto');  //chamando a funcao de exibir texto na tela
    exibirTextoNaTela('p', 'Escolha um número entre 1 e 10');
}
exibirMensagemInicial();

function verificarChute(){ //funcao do botao de CHUTE
    let chute = document.querySelector('input').value; // pegar o valor dentro da tag
    if(chute == numeroSecreto){
        exibirTextoNaTela('h1', 'Acertou!');
        let palavraTentativa = tentativas > 1? 'tentativas':'tentativa';
        let mensagemTentativas = `Você descobriu o número secreto com ${tentativas} ${palavraTentativa}!`;
        exibirTextoNaTela('p', mensagemTentativas);
        document.getElementById('reiniciar').removeAttribute('disabled'); // vai buscar o elemento pelo id (getElementById) e remover o atributo (removeAttribute) que passarmos
    }else{ 
        if(chute > numeroSecreto){
            exibirTextoNaTela('p', 'O número secreto é menor');
            }else{
                exibirTextoNaTela('p', 'O número secreto é maior');
        }
        tentativas++;
        limparCampo();
    }
}

function gerarNumeroAleatorio() {
    let numeroEscolhido = parseInt(Math.random() * numeroLimite + 1);
    let quantidadeDeElementosNaLista = listaDeNumerosSorteados.length;

    if(quantidadeDeElementosNaLista == numeroLimite){
        listaDeNumerosSorteados = [];
    }

    if(listaDeNumerosSorteados.includes(numeroEscolhido)){ // .includes = verifica se um valor ja existe dentro da lista
        return gerarNumeroAleatorio();
    }else{
        listaDeNumerosSorteados.push(numeroEscolhido); // adiciona um elemento na lista
        console.log(listaDeNumerosSorteados);
        return numeroEscolhido;
    }
}

function limparCampo(){
    chute = document.querySelector('input');
    chute.value = ''; //colocando valor vazio no campo input
}

function reiniciarJogo(){
    numeroSecreto = gerarNumeroAleatorio();
    limparCampo();
    tentativas = 1;
    exibirMensagemInicial();
    document.getElementById('reiniciar').setAttribute('disabled', true);// colocando o atributo disabled novamente no botao
}