let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function verificaConsole(){
    console.log('O botão foi clicado');
}

function verificaAlerta(){
    alert('Eu amo JS');
}

function verificaPrompt(){
    let cidade = prompt('Digite o nome de uma cidade:');
    alert(`Estive em ${cidade} e lembrei de você.`);
}

function verificaSoma(){
    let n1 = prompt('Digite um número:');
    let n2 = prompt('Digite outro número:');

    // Converte as strings para números inteiros
    n1 = parseInt(n1);
    n2 = parseInt(n2);
    
    let soma = n1 + n2;

    alert(`A soma de ${n1} + ${n2} = ${soma}`);
}