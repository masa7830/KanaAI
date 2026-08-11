import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.File;
class User
{
    public static void main(String[]args) throws IOException
    {
        //キーボードから入力するための準備
         BufferedReader br =
        new BufferedReader (new InputStreamReader(System.in,"MS932"));
        
        //user.txtという名前保存用ファイルを扱う
        File file = new File("user.txt");

         // ユーザー名を入れておく変数
        String name;

         // user.txtがすでに存在する場合
        // → 以前Kanaを使ったことがあるユーザー
        if(file.exists())
        {
        // user.txtを読み込む準備
        FileReader fr = new FileReader("user.txt");

        BufferedReader userReader =
        new BufferedReader(fr);

         // 保存されている名前を読み込む
        name = userReader.readLine();

        // 読み込みが終わったのでファイルを閉じる
            userReader.close();

    
        System.out.println("Kana:おかえり、" + name + "！");

        userReader.close();
        }

        // user.txtが存在しない場合
        // → Kanaを初めて使うユーザー
        else{

        System.out.println("Kana:おかえりなさい！");
        System.out.println("Kana:名前を教えてね。");
         // 入力された名前をnameに保存
            name = br.readLine();

            // user.txtへ書き込む準備
            FileWriter fw = new FileWriter("user.txt");

            // 入力された名前をuser.txtへ保存
            fw.write(name);

            // 書き込み終了
            fw.close();

            // 初回だけのあいさつ
            System.out.println("Kana:" + name + "、よろしくね！");
        }

       
        
        //今日の気分を聞く
        System.out.println("Kana:今日の気分はどう？");
        System.out.println("Kana:1. 元気！");
        System.out.println("Kana:2. まあまあかな");
        System.out.println("Kana:3. 疲れた");
        //キーボードから入力された文字列を整数に変換してmoodに保存
        int mood = Integer.parseInt(br.readLine());
        //1から3以外が入力されたら正しい数字になるまで聞き返す
        while (mood != 1 && mood != 2 && mood != 3) {

            System.out.println("Kana:ごめん、よく分からなかった");
            System.out.println("Kana:もう一度選んでね！");
            System.out.println("Kana:今日の気分はどう？");
            System.out.println("Kana:1. 元気！");
            System.out.println("Kana:2. まあまあかな");
            System.out.println("Kana:3. 疲れた");

            //moodの値を新しい入力で更新
            mood = Integer.parseInt(br.readLine());
        }
        //気分に応じてKanaの返事を変える
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
     
        //会話を続けるか確認
        System.out.println("Kana:まだ話す？");
        System.out.println("Kana:1.もう少し話をする");
        System.out.println("Kana:2.今日はもう帰る");
        
        int choice = Integer.parseInt(br.readLine());
        

        //1か2以外なら聞き返す
        while (choice != 1 && choice != 2) {
            System.out.println("Kana:ごめん、よく分からなかった");
            System.out.println("Kana:もう一度選んでね！");
            System.out.println("Kana:1.もう少し話をする");
            System.out.println("Kana:2.今日はもう帰る");

        //choiceを新しい入力で更新
        choice = Integer.parseInt(br.readLine());
        }
       
        //帰ろうとしたら一度だけ引き留める
        if (choice ==1){
            System.out.println("Kana:たくさん話そう");
        }
        else if (choice == 2){
            System.out.println("もうかえっちゃうの!?");
            System.out.println("Kana:1.やっぱりもう少し話す");
            System.out.println("Kana:2.うん、今日は帰る");

            //すでにchoice宣言済みなのでintはつけない
            choice = Integer.parseInt(br.readLine());

            //1か2以外ならもう一度確認
            while (choice != 1 && choice != 2) {
                System.out.println("Kana:ごめん、よく分からなかった");
                System.out.println("Kana:もう一度選んでね！");
                System.out.println("Kana:1.やっぱりもう少し話をする");
                System.out.println("Kana:2.うん、今日はもう帰る");
                
                choice = Integer.parseInt(br.readLine());
            }
        }

            //choiceが1の間会話を続ける
            if (choice ==1){
            
                 while (choice == 1) {
          

                    System.out.println("Kana:何を話す？");

                    //会話内容を文字列として受け取る
                    String talk = br.readLine();

                   //「疲れた」「勉強」を含む入力に反応し、それ以外は相槌を返す
                    if (talk.contains("疲れた")) {
                        System.out.println("Kana:お疲れさま。今日はゆっくりしよ？");
                    }
                    else if (talk.contains("勉強")) {
                        System.out.println("Kana:勉強したんだ！何を勉強したの？");
                        talk = br.readLine();
                        System.out.println("Kana:"+talk+"を勉強したんだね！");
                    }
                    else {
   
                         System.out.println("Kana:" + talk + "なんだね");
                    }                                                                                                                                                                                                                                                                                            
                    //会話を続けるか確認
                    System.out.println("Kana:もっと話そう！");
                    System.out.println("Kana:1.もう少し話す");
                    System.out.println("Kana:2.今日は帰る");

                    //1なら会話を続けて、2ならwhileを終了する
                    choice = Integer.parseInt(br.readLine());
            }
     }
    
            //終了時のあいさつ

            System.out.println("行ってらっしゃい！また来てね！！ばいばーい");
        
            
         
          
        }
    }    




