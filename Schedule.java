import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.FileWriter;
import java.io.FileReader;

class Schedule{
    public static void main(String[] args) throws IOException
    {

         BufferedReader br =
        new BufferedReader(new InputStreamReader(System.in,"MS932"));

        
      
        String[] schedule = new String[7];

         String[] week = {
    "月曜日",
    "火曜日",
    "水曜日",
    "木曜日",
    "金曜日",
    "土曜日",
    "日曜日"
};



    
        System.out.println("Kana:1.予定を登録する");
        System.out.println("Kana:2.予定を確認する");
        System.out.println("Kana:3.終了する");


        int choice = 0;//choiceを作る
// 3を選ぶまで繰り返す
while (choice != 3)
{
    System.out.println("Kana:何をしますか？");
    System.out.println("Kana:1.予定を登録する");
    System.out.println("Kana:2.予定を確認する");
    System.out.println("Kana:3.終了する");

     // ↓ 作ったchoiceの中身を入力された数字に変更する
    choice = Integer.parseInt(br.readLine());

         while (choice != 1 && choice != 2 && choice !=3) {
            System.out.println("Kana:ごめん、よく分からなかった");
            System.out.println("Kana:もう一度選んでね！");
            System.out.println("Kana:1.予定を登録する");
            System.out.println("Kana:2.予定を確認する");
            System.out.println("Kana:3.終了する");


              // choiceを新しい入力で更新
            choice = Integer.parseInt(br.readLine());


         }// 入力チェックwhile終了

          if (choice ==1){
    
        System.out.println("曜日を入力してください");
          String talk = br.readLine();

           int i = 0;

        if(talk.contains("月曜日"))
        {
        i = 0;
        }
       else if(talk.contains("火曜日"))
       {
        i = 1;
       }
       else if(talk.contains("水曜日"))
       {
        i = 2;
       }
       else if(talk.contains("木曜日"))
        {
        i = 3;
        }
        else if(talk.contains("金曜日"))
        {
        i = 4;
        }
        else if(talk.contains("土曜日"))
        {   
        i = 5;
        }
        else if(talk.contains("日曜日"))
        {
        i = 6;
        }
   

        System.out.println("予定を入力してください");
       
        String str = br.readLine();

        schedule[i] = str;

        FileWriter fw = new FileWriter("schedule.txt",true);

        fw.write(week[i] + "," + schedule[i]+ System.lineSeparator());

        fw.close();
        
       
    
    

            System.out.println(week[i] + "の予定は" +schedule[i]+"です。" );
    }// choice == 1 予定登録終了

        
else if(choice == 2)
{
    System.out.println("Kana:何曜日の予定を確認しますか？");
    String checkDay = br.readLine();

    // schedule.txtを読み込む準備
    FileReader fr = new FileReader("schedule.txt");

    BufferedReader userReader =
        new BufferedReader(fr);

    // ファイルの中身を1行ずつ読む
    String line;

    while ((line = userReader.readLine()) != null)
    {
        // 入力された曜日を含む行だけ表示
        if (line.contains(checkDay))
        {
                 // 「曜日,予定」を「曜日」と「予定」に分ける
        String[] data = line.split(",");

        System.out.println(
            "Kana:" + data[0] + "の予定は" + data[1] + "です。"
        );
    } // 曜日一致if終了
        }// schedule.txt読み込みwhile終了

    // 全ての行を読み終わってから閉じる
    userReader.close();
}// choice == 2 予定確認終了
    else if(choice == 3)
    {
         User.goodbye();
    } // choice == 3 終了処理終了

} // 3を選ぶまで繰り返すwhile終了

    }// mainメソッド終了

}// Scheduleクラス終了
    
    