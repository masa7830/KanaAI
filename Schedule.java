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

         if (choice == 1)
{
    System.out.println("日付を入力してください");
    System.out.println("例：2026-08-12");

    String date = br.readLine();

    System.out.println("予定を入力してください");
    String str = br.readLine();

    FileWriter fw =
        new FileWriter("schedule.txt", true);

    fw.write(
        date + "," + str + System.lineSeparator()
    );

    fw.close();

    System.out.println(
        "Kana:" + date + "の予定として"
        + str + "を登録したよ！"
    );

} // choice == 1 予定登録終了

        
else if(choice == 2)
{
    System.out.println("Kana:何日の予定を確認しますか？");
    String checkDate = br.readLine();

    // schedule.txtを読み込む準備
    FileReader fr = new FileReader("schedule.txt");

    BufferedReader userReader =
        new BufferedReader(fr);

    // ファイルの中身を1行ずつ読む
    String line;

    while ((line = userReader.readLine()) != null)
    {
        // 入力された日付を含む行だけ表示
        if (line.contains(checkDate))
        {
                 // 「日付,予定」を「日付」と「予定」に分ける
        String[] data = line.split(",");

        System.out.println(
            "Kana:" + data[0] + "の予定は" + data[1] + "です。"
        );
    } // 日付一致if終了
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
    
    