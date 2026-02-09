import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Banco2 {
    static Scanner in = new Scanner(System.in);
    static String investi;
    public static void criar_conta(long cpf, String senha, String nome, long tel,String gmail) {
        try {
            String cpfStr = String.valueOf(cpf);
            String telstr = String.valueOf(tel);
            ProcessBuilder pb = new ProcessBuilder(
                    "python3",
                    "criar_conta.py",
                    cpfStr,
                    senha,
                    nome,
                    telstr,
                    gmail
            );

            pb.directory(new File("/home/tutu3/Downloads/java/"));
            pb.redirectErrorStream(true);

            Process process = pb.start();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream())
            );

            String linha;
            StringBuilder saida = new StringBuilder();

            while ((linha = reader.readLine()) != null) {
                System.out.println("[PYTHON] " + linha);
                saida.append(linha);
            }

            process.waitFor();

            System.out.println("Retorno final: " + saida);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void entrar_conta(long cpf, String senha){
        try {
            String cpfStr = String.valueOf(cpf);

            ProcessBuilder pb = new ProcessBuilder(
                    "python3",
                    "ler_json.py",
                    cpfStr,
                    senha
            );

            pb.directory(new File("/home/tutu3/Downloads/java/"));
            pb.redirectErrorStream(true);

            Process process = pb.start();

            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream())
            );

            String linha;
            StringBuilder saida = new StringBuilder();

            while ((linha = reader.readLine()) != null) {
                System.out.println("[PYTHON] " + linha);
                saida.append(linha);
            }

            process.waitFor();
            int exitcode = process.waitFor();
            if(exitcode == 1){
                System.out.println("######Login autorizado#####");
                carregar_informacoes(cpfStr,senha);
            }else{
                System.out.println("#####Login Invalido#####");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void carregar_informacoes(String cpf, String senha){
            while(true){
            
             System.out.println("1.Pressione para prosseguir");
             System.out.println("0.Para sair");
             int escolha = in.nextInt();
             if (escolha == 1){
                System.out.println("1.ver seus investimentos");
                System.out.println("2.ver investimentos possiveis");
                System.out.println("3.Ver seus dados");
                System.out.println("4.Transferencia");
                System.out.println("5.Pra voltar");
                int escolha_3 = in.nextInt();
                if(escolha_3 == 1){
                  investi = "-i"; 
                  carregar_conta_dados(cpf, senha, investi);
                }else if(escolha_3 == 2){
                  investi = "-ip";
                  carregar_conta_dados(cpf, senha, investi);
                  System.out.println("qual investira (numero nao nome): ");
                  int escolha_investi = in.nextInt();
                  in.nextLine();
                  String escolha_valida_investi = String.valueOf(escolha_investi);
                  investimentos_escolha(cpf, "investimento", escolha_valida_investi);
                }else if(escolha_3 ==3){
                  investi ="-d";
                  carregar_conta_dados(cpf, senha, investi);
                }else if(escolha_3 == 4){
                  System.out.println("1.Ver transferencias: ");
                  System.out.println("2.Fazer uma transferencia: ");
                  int escolha_transferencia = in.nextInt();
                  if(escolha_transferencia==1){
                     ver_transferencias(cpf, senha);                    
                  }else if(escolha_transferencia==2){
                    transferir_classe(cpf);
                  }
                }else if(escolha_3==5){
                   break;
                }
             }else if (escolha==0){
                break;
             }
             
            }
        }
    public static void investimentos_escolha(String cpf, String investe, String escolh_invest){
           try {
               ProcessBuilder pb = new ProcessBuilder(
                "python3",
                "escolha_investi.py",
                cpf,
                investe,
                escolh_invest
               );
               pb.directory(new File("/home/tutu3/Downloads/java/"));
               pb.redirectErrorStream(true);
               Process process = pb.start();

                BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream())
                );

                String linha;
                StringBuilder saida = new StringBuilder();

                while ((linha = reader.readLine()) != null) {
                 System.out.println(linha);
                 saida.append(linha);
                }
                process.waitFor();
                int exitcode = process.waitFor();
           } catch (Exception e) {
            e.printStackTrace();
           }
    }

    public static void carregar_conta_dados(String cpf, String senha,String investe){
       try{
           System.out.println("....");
           ProcessBuilder pb = new ProcessBuilder(
              "python3",
              "carregar_conta.py",
              cpf,
              senha,
              investe
           );
           pb.directory(new File("/home/tutu3/Downloads/java/"));
           pb.redirectErrorStream(true);

           Process process = pb.start();

           BufferedReader reader = new BufferedReader(
             new InputStreamReader(process.getInputStream())
           );
           String linha;
           StringBuilder saida = new StringBuilder();
           while((linha = reader.readLine()) != null){
            System.out.println(linha);
            saida.append(linha);
           }
           process.waitFor();
        } catch (Exception e){
          e.printStackTrace();
        }
    }
    public static void transferir_classe(String cpf) {
        while (true){
             System.out.println("senha: ");
             int senha_campo = in.nextInt();
             String senha_campo_valido = String.valueOf(senha_campo);
             in.nextLine();
             System.out.println("Conta a ser feita a transaçao: ");
             String conta_a_pagar = in.nextLine();
             in.nextLine();
             System.out.println("Valor a transferir: ");
             int valor = in.nextInt();
             String valor_valido = String.valueOf(valor);
             in.nextLine();
             try{
              System.out.println("....");
              ProcessBuilder pb = new ProcessBuilder(
                "python3",
                "transferencia.py",
                cpf,
                senha_campo_valido,
                conta_a_pagar,
                valor_valido
              );
              pb.directory(new File("/home/tutu3/Downloads/java/"));
              pb.redirectErrorStream(true);

              Process process = pb.start();
 
              BufferedReader reader = new BufferedReader(
                new InputStreamReader(process.getInputStream())
              );
              String linha;
              StringBuilder saida = new StringBuilder();
              while((linha = reader.readLine()) != null){
               System.out.println(linha);
               saida.append(linha);
              }
             
              process.waitFor();
              int exitcode_2 = process.waitFor();
              if (exitcode_2 == 3){
                System.out.println(linha);
                break;
              }else{
                System.out.println("Deseja tentar novamente? (s/n)");
                String retornar_2 = in.nextLine();
                if(retornar_2.compareToIgnoreCase("s") == 0){
                   System.out.println("Tentando novamente...");
                }else if (retornar_2.compareToIgnoreCase("n") == 0){
                    System.out.println("voltando...");
                    System.out.println();
                    break;
                }else{
                    System.out.println("Escolha invalida");
                } 
              }
            } catch (Exception e){
              e.printStackTrace();
              break;
            }
        }
    }
    public static void ver_transferencias(String cpf,String senha){
        try{ 
              while(true){

              
               System.out.println("....");
               ProcessBuilder pb = new ProcessBuilder(
                 "python3",
                 "transferencia_ler.py",
                 cpf,
                 senha
               );
               pb.directory(new File("/home/tutu3/Downloads/java/"));
               pb.redirectErrorStream(true);

               Process process = pb.start();
 
               BufferedReader reader = new BufferedReader(
                 new InputStreamReader(process.getInputStream())
               );
               String linha;
               StringBuilder saida = new StringBuilder();
               while((linha = reader.readLine()) != null){
                System.out.println(linha);
                saida.append(linha);
               }
             
               process.waitFor();
               int saida_code = process.waitFor();
               if(saida_code == 2){
                 System.out.println("Aperte enter para voltar");
                 in.nextLine();
                 break;
               }else{
                 System.out.println("erro");
                 System.out.println("voltando...");
               }
              }
        }catch(Exception e){
          System.out.println(e);
        }
    }
    // TESTE
    public static void main(String[] args) {
        entrar_conta(0, "140310");
    }
}

    



