#!/bin/bash



True = 1
False = 2

while [$True == 1]
do
    echo "<<< Cadastro >>>"
    sleep 1
done

echo "Qual é o seu nome?"
read nome

echo "Qual é sua idade?"
read idade

echo "Seu nome é: $nome. "
sleep 1

echo "Sua idade é: $idade anos."

echo "Olá"
sleep 1 


