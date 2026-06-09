/*
Exercice 1.10 : Calcul des nombres parfaits 
On souhaite écrire un programme de calcul des N premiers nombres parfaits. 
Un nombre est dit parfait s’il est égal à la somme de ses diviseurs, 1 compris. 
*/

import{createInterface} from 'node:readline/promises';
import{stdin as input, stdout as output} from 'node:process';
async function main(){
const sc = new createInterface({input, output});

let response;
let sum=0;
let i;

response = parseInt(await sc.question('Veuillez écrire un nombre')); 
console.log(response);

for(i=1; response%i==0; i++){

                    if(response % i == 0){
                    sum += i;
                                if(sum==response){
                                console.log(reponse+' est un nombre parfait.')
                                                 }
                                else{console.log(response+' n\'est pas un nombre parfait.')}
                                        }   
                            }   
sc.close();
                    }
await main()
