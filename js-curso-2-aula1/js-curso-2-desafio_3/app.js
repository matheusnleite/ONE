//////////////////////////////Desafio 1
// let altura = 1.75 , peso = 70;
// function calculaIMC(altura,peso){
//     let imc = peso / (altura*altura);
//      return imc;
// }

//////////////////////////////Desafio 2
// let numero = 4;
// function calculaFatorial(numero){
//     if(numero == 0 || numero == 1){
//         return 1;
//     }
//     let fatorial = 1;
//     for(let i=2;i<=numero;i++){
//         fatorial *= i;// fatorial = fatorial * i
//     }
//     return fatorial;
// }

//////////////////////////////Desafio 3
// let valor = 5
// let cotacao = 4.80
// function converteReais(valor, cotacao){
//     valorReal = valor * cotacao;
//     return valorReal.toFixed(2);
// }

//////////////////////////////Desafio 4
// let altura = 8 , largura = 5;
// function calculaAreaEPerimetroRetangulo(altura, largura){
//     area = altura * largura;
//     perimetro = altura + altura + largura + largura;
//     console.log(`Área: ${area}`);
//     console.log(`Perimetro: ${perimetro}`);
    
// }

//////////////////////////////Desafio 5
// let raio = 8;
// function calculaAreaEPerimetroCirculo(raio){
//     area = Math.PI * raio * raio;
//     perimetro = 2 * Math.PI * raio;
//     console.log(`Área: ${area}`);
//     console.log(`Perimetro: ${perimetro}`);
    
// }


//////////////////////////////Desafio 6

let numero = 4;
tabuada(numero);
function tabuada(numero){
    for(let i=1;i<=10;i++){
        console.log(`${i} X ${numero} = ${i*numero}`);
    }
}
