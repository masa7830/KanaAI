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
        System.out.println("Kana:今日も頑張ろう！");
    }

}