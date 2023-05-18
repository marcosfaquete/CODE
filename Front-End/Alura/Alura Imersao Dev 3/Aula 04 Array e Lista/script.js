/*
var listaFilmes = ["Yesterday","A chegada","Escola de Rock"];
//  elemento            1           2           3
// indice               0           1           2
// Add novos Elementos
listaFilmes.push("Harry Potter 2");
listaFilmes.push("Harry Potter 3");
listaFilmes.push("Harry Potter 4");
listaFilmes.push("Harry Potter 5");
document.write("<p>" + listaFilmes[0] + "</p>");
document.write("<p>" + listaFilmes[1] + "</p>");
document.write("<p>" + listaFilmes[2] + "</p>");
document.write("<p>" + listaFilmes[4] + "</p>");
//for (var indice = 0; indice < 4; indice = indice + 1)
for (var indice = 0; indice < listaFilmes.length; indice++) {
    //document.write("<p>" + indice + "</p>");
    document.write("<p>" + listaFilmes[indice] + "</p>");
}
//var filme1 = "Yesterday";
//var filme2 = "A chegada";
//var filme3 = "Escola de Rock";
//document.write("<p>" + filme1 + "</p>");
//document.write("<p>" + filme2 + "</p>");
//document.write("<p>" + filme3 + "</p>");
*/

var listaFilmes = ["https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg", "https://www.cafecomfilme.com.br/media/k2/items/cache/50f8055cbf99a024c0772160c01fed2b_XL.jpg?t=20210108_154337","https://cineclick-static.flixmedia.cloud/1280/4d0f56b9-dbe6-410e-ad62-ce3e112afafe.jpg"];

for (var x = 0; x < listaFilmes.length; x++) {
    document.write("<img src=" + listaFilmes[x] + ">");
}