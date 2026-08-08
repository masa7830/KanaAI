package KanaAI;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


class User
{
    public static void main(String[]args) throws IOException
    {
        System.out.println("Kana:おかえりなさい！");
        System.out.println("Kana:名前を教えてね。");

        BufferedReader br =
        new BufferedReader (new InputStreamReader(System.in,"MS932"));
      
    
        String str = br.readLine();

        System.out.println("Kana:" + str + "、よろしくね！");
        System.out.println("Kana:今日の気分はどう？");
        System.out.println("Kana:1. 元気！");
        System.out.println("Kana:2. まあまあかな");
        System.out.println("Kana:3. 疲れた");
        //キーボードから入力された文字列を整数に変換
        int mood = Integer.parseInt(br.readLine());

        while (mood != 1 && mood != 2 && mood != 3) {

            System.out.println("Kana:ごめん、よく分からなかった");
            System.out.println("Kana:もう一度選んでね！");
            System.out.println("Kana:今日の気分はどう？");
            System.out.println("Kana:1. 元気！");
            System.out.println("Kana:2. まあまあかな");
            System.out.println("Kana:3. 疲れた");
            mood = Integer.parseInt(br.readLine());
        }

        if (mood == 1) {
            System.out.println("Kana:元気そうでよかった！");
        }
        else if(mood == 2){
            System.out.println("Kana:まあ、そういう日もあるよ");
        }
        else if(mood ==3){
            System.out.println("Kana:お疲れ様");
        }
        else{
            System.out.println("Kana:うーん、よく分からなかった");
        }
     
        System.out.println("Kana:まだ話す？");
        System.out.println("Kana:1.もう少し話をする");
        System.out.println("Kana:2.今日はもう帰る");
        
        int choice = Integer.parseInt(br.readLine());
        

        while (choice != 1 && choice != 2) {
            System.out.println("Kana:ごめん、よく分からなかった");
            System.out.println("Kana:もう一度選んでね！");
            System.out.println("Kana:1.もう少し話をする");
            System.out.println("Kana:2.今日はもう帰る");

        choice = Integer.parseInt(br.readLine());
        }
       
        if (choice ==1){
            System.out.println("Kana:たくさん話そう");
        }
        else if (choice == 2){
            System.out.println("もうかえっちゃうの!?");
            System.out.println("Kana:1.やっぱりもう少し話す");
            System.out.println("Kana:2.うん、今日は帰る");

            choice = Integer.parseInt(br.readLine());

            while (choice != 1 && choice != 2) {
                System.out.println("Kana:ごめん、よく分からなかった");
                System.out.println("Kana:もう一度選んでね！");
                System.out.println("Kana:1.やっぱりもう少し話をする");
                System.out.println("Kana:2.うん、今日はもう帰る");
                
                choice = Integer.parseInt(br.readLine());
            }
        }
            if (choice ==1){
            
                 while (choice == 1) {
          

                    System.out.println("Kana:何を話す？");

                    String talk = br.readLine();

                    System.out.println("Kana:" + talk + "なんだね");

                    System.out.println("Kana:もっと話そう！");
                    System.out.println("Kana:1.もう少し話す");
                    System.out.println("Kana:2.今日は帰る");

                    choice = Integer.parseInt(br.readLine());
            }
     }
    

            System.out.println("行ってらっしゃい！また来てね！！ばいばーい");
        
            
         
          
        }
    }    




