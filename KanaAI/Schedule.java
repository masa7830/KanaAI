import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Schedule{
    public static void main(String[] args) throws IOException
    {

         BufferedReader br =
        new BufferedReader(new InputStreamReader(System.in,"MS932"));

        System.out.println("曜日を入力してください");

        String talk = br.readLine();

        String[] schedule = new String[7];

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
        
        String[] week = {
    "月曜日",
    "火曜日",
    "水曜日",
    "木曜日",
    "金曜日",
    "土曜日",
    "日曜日"
};
    
    

            System.out.println(week[i] + "の予定は" +schedule[i]+"です。" );

        }


    }
