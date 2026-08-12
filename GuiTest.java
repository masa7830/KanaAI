import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;

class GuiTest
{
    public static void main(String[] args)
    {
        JFrame frame = new JFrame("Kana");

        frame.setSize(500, 400);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();

          // Kanaのセリフを表示する
        JLabel message = new JLabel("Kana:おかえりなさい！");

                JButton addButton =
            new JButton("予定を登録する");

        JButton checkButton =
            new JButton("予定を確認する");

        JButton endButton =
            new JButton("終了する");

        panel.add(message);
        panel.add(addButton);
        panel.add(checkButton);
        panel.add(endButton);

        // ウィンドウにセリフを追加する
        frame.add(panel);

        // 予定登録ボタンが押されたときの処理
addButton.addActionListener(e -> {

    String date = JOptionPane.showInputDialog(
        frame,
        "日付を入力してください\n例：2026-08-12"
    );

    String schedule = JOptionPane.showInputDialog(
        frame,
        "予定を入力してください"
    );

     // schedule.txtに予定を保存する
    try
    {
        FileWriter fw = new FileWriter("schedule.txt", true);

        fw.write(
            date + "," + schedule + System.lineSeparator()
        );

        fw.close();

    message.setText(
        "Kana:" + date + "の予定は「" + schedule + "」だね！"
    );
}
 catch (IOException error)
    {
        message.setText(
            "Kana:ごめん、予定を保存できなかった..."
                   );
    }
});
// 予定確認ボタンが押されたときの処理
// 予定確認ボタンが押されたときの処理
checkButton.addActionListener(e -> {

    String checkDate = JOptionPane.showInputDialog(
        frame,
        "何日の予定を確認しますか？\n例：2026-08-12"
    );

    try
    {
        FileReader fr = new FileReader("schedule.txt");

        BufferedReader userReader =
            new BufferedReader(fr);

        String line;

        // 見つかった予定をためておく
        String result = "";

        while ((line = userReader.readLine()) != null)
        {
            if (line.contains(checkDate))
            {
                String[] data = line.split(",");

                // 見つけた予定をresultに追加する
                result = result + "・" + data[1] + "<br>";
            }
        }

        userReader.close();

        // 予定が見つかった場合
        if (!result.equals(""))
        {
            message.setText(
                "<html>Kana:" + checkDate + "の予定だよ！<br>"
                + result
                + "</html>"
            );
        }
        // 予定がなかった場合
        else
        {
            message.setText(
                "Kana:" + checkDate + "は予定がないよ！"
            );
        }
    }
    catch (IOException error)
    {
        message.setText(
            "Kana:ごめん、予定を読み込めなかった..."
        );
    }
});
        // 終了ボタンが押されたときの処理
endButton.addActionListener(e -> {
    System.out.println("Kana:行ってらっしゃい！また来てね！");
    System.exit(0);
});

        frame.setVisible(true);
    }
}
