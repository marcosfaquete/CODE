void RegistrarBanda()
{
   Console.Clear();
     Console.WriteLine("Registro de bandas");
     Console.Write("Digite o nome da banda que deseja registrar: ")
     string nomeDaBanda = Console.ReadLine()!;
     Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
}

void RegistrarBanda()
{
   Console.Clear();
     Console.WriteLine("Registro de bandas");
     Console.Write("Digite o nome da banda que deseja registrar: ")
     string nomeDaBanda = Console.ReadLine()!;
     Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
     Console.Clear();
     Thread.Sleep(2000);
     ExibirOpcoesDoMenu();
}

void ExibirOpcoesDoMenu()
{
    ExibirLogo();
}
// código omitido