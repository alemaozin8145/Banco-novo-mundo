import java.util.Scanner;
public class banco{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        Banco2 banco2 = new Banco2();
        while (true){
         System.out.println("Banco Novo Mundo");
         System.out.println("1.Criar conta no banco");
         System.out.println("2.Entrar no banco");
         System.out.println("0.Sair");
        
         int escolha = in.nextInt();
         if (escolha==1){
            while (true) { 
              System.out.println("Seu CPF: ");
              long cpf = in.nextLong();
              in.nextLine();
              System.out.println("Seu nome completo");
              String nome = in.nextLine();
              in.nextLine();
              System.out.println("Seu numero de telefone");
              long tel = in.nextLong();
              in.nextLine();
              System.out.println("Seu gmail");
              String gmail = in.nextLine();
              in.nextLine();
              System.out.println("Sua Senha (quatro digitos): ");
              String senha = in.nextLine();
              in.nextLine();
              int quantidade = String.valueOf(cpf).length();
              int quantidade_senha = String.valueOf(senha).length();

              if(quantidade <=10 || quantidade>=12){
                System.out.println("Cpf invalido(tente novamente)");
              }else if(quantidade_senha<=3){
                System.out.println("A senha deve conter 4 ou mais caracteres");
              }else{
                System.out.println("Criando a conta...");
                banco2.criar_conta(cpf, senha, nome, tel,gmail);
                break;
              }
            }
         }else if(escolha==2){
            System.out.println("Seu CPF: ");
             long cpf = in.nextLong();
             in.nextLine();
             System.out.println("Sua Senha: ");
             String senha = in.nextLine();
             banco2.entrar_conta(cpf, senha);
         }else if(escolha==0){
            System.out.println("saindo...");
            break;
         }
        }
    }
}