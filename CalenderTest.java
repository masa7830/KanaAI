import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JButton;

import java.awt.GridLayout;
import java.awt.BorderLayout;

import java.time.LocalDate;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import javax.swing.JOptionPane;
import java.io.FileWriter;

class CalendarTest
{
    public static void main(String[] args)
    {
        JFrame frame = new JFrame("Kana Calendar");

        frame.setSize(600, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 今日の日付
        LocalDate today = LocalDate.now();

        // 表示する月の1日
       LocalDate[] firstDay = {
    LocalDate.of(
        today.getYear(),
        today.getMonthValue(),
        1
    )
};

        // 上部


        LocalDate[] selectedDate = { null };

        JPanel topPanel = new JPanel();

        JButton previousButton = new JButton("←");
        JButton nextButton = new JButton("→");

        JLabel monthLabel = new JLabel(
            firstDay[0].getYear() + "年"
            + firstDay[0].getMonthValue() + "月"
        );

        topPanel.add(previousButton);
        topPanel.add(monthLabel);
        topPanel.add(nextButton);

       // カレンダー本体
JPanel panel =
    new JPanel(new GridLayout(0, 7));

// 予定表示エリア
JLabel scheduleLabel =
    new JLabel("Kana:日付を選んでね！");

JButton addScheduleButton =
    new JButton("この日に予定を追加");

JPanel bottomPanel = new JPanel();

bottomPanel.add(scheduleLabel);
bottomPanel.add(addScheduleButton);

addScheduleButton.addActionListener(e -> {

    // まだ日付を選んでいない場合
    if (selectedDate[0] == null)
    {
        JOptionPane.showMessageDialog(
            frame,
            "先に日付を選んでね！"
        );

        return;
    }

    // 予定を入力
    String schedule =
        JOptionPane.showInputDialog(
            frame,
            selectedDate[0]
            + "の予定を入力してね"
        );

    // 毎週繰り返すか確認
    int repeatChoice =
        JOptionPane.showConfirmDialog(
            frame,
            "毎週繰り返しますか？",
            "繰り返し設定",
            JOptionPane.YES_NO_OPTION
        );

    try
    {
        FileWriter fw =
            new FileWriter(
                "schedule.txt",
                true
            );

        // 毎週繰り返す場合
        if (repeatChoice == JOptionPane.YES_OPTION)
        {
            String countText =
                JOptionPane.showInputDialog(
                    frame,
                    "何回登録しますか？"
                );

            int count =
                Integer.parseInt(countText);

            LocalDate repeatDate =
                selectedDate[0];

            for (int i = 0; i < count; i++)
            {
                fw.write(
                    repeatDate
                    + ","
                    + schedule
                    + System.lineSeparator()
                );

                repeatDate =
                    repeatDate.plusWeeks(1);
            }
        }

        // 1回だけの場合
        else
        {
            fw.write(
                selectedDate[0]
                + ","
                + schedule
                + System.lineSeparator()
            );
        }

        fw.close();

        // 保存後、画面を更新
        String result =
            getSchedule(selectedDate[0]);

        scheduleLabel.setText(
            "<html>Kana:"
            + selectedDate[0].getMonthValue()
            + "月"
            + selectedDate[0].getDayOfMonth()
            + "日の予定だよ！<br>"
            + result
            + "</html>"
        );
    }
    catch (IOException error)
    {
        JOptionPane.showMessageDialog(
            frame,
            "予定を保存できなかったよ"
        );
    }

});

// カレンダーを表示
showCalendar(
    panel,
    firstDay[0],
    scheduleLabel,
    selectedDate
);

// 画面に配置
frame.add(topPanel, BorderLayout.NORTH);
frame.add(panel, BorderLayout.CENTER);
frame.add(bottomPanel, BorderLayout.SOUTH);


        // 次の月へ
nextButton.addActionListener(e -> {

    firstDay[0] = firstDay[0].plusMonths(1);

    monthLabel.setText(
        firstDay[0].getYear() + "年"
        + firstDay[0].getMonthValue() + "月"
    );

   showCalendar(
    panel,
    firstDay[0],
    scheduleLabel,
    selectedDate
);
});

// 前の月へ
previousButton.addActionListener(e -> {

    firstDay[0] = firstDay[0].minusMonths(1);

    monthLabel.setText(
        firstDay[0].getYear() + "年"
        + firstDay[0].getMonthValue() + "月"
    );

   showCalendar(
    panel,
    firstDay[0],
    scheduleLabel,
    selectedDate
);
});

        frame.setVisible(true);

    } // main終了


    // 指定された月のカレンダーを表示するメソッド
   static void showCalendar(
    JPanel panel,
    LocalDate firstDay,
    JLabel scheduleLabel,
    LocalDate[] selectedDate
)
    {
        // 以前の表示を全部消す
        panel.removeAll();

        // 曜日を表示
        String[] week = {
            "月", "火", "水", "木", "金", "土", "日"
        };

        for (int i = 0; i < 7; i++)
        {
            JLabel weekLabel =
                new JLabel(week[i]);

            panel.add(weekLabel);
        }
        

        // 月末の日付
        int lastDay =
            firstDay.lengthOfMonth();

        // 1日が何曜日か
        int startDay =
            firstDay.getDayOfWeek().getValue();

        // 1日より前の空白
        for (int i = 1; i < startDay; i++)
        {
            JLabel blank =
                new JLabel("");

            panel.add(blank);
        }

        // 1日から月末まで
        for (int day = 1; day <= lastDay; day++)
        {
            JButton dayButton =
                new JButton(
                    String.valueOf(day)
                );

                 // このボタンの日付を保存
    int selectedDay = day;

 dayButton.addActionListener(e -> {

    selectedDate[0] =
        LocalDate.of(
            firstDay.getYear(),
            firstDay.getMonthValue(),
            selectedDay
        );

    String schedule =
        getSchedule(selectedDate[0]);

    scheduleLabel.setText(
        "<html>Kana:"
        + selectedDate[0].getMonthValue()
        + "月"
        + selectedDate[0].getDayOfMonth()
        + "日の予定だよ！<br>"
        + schedule
        + "</html>"
    );
});      panel.add(dayButton);
        }

        // 画面を更新
        panel.revalidate();
        panel.repaint();

    } // showCalendar終了

    // 指定した日の予定をschedule.txtから探すメソッド
static String getSchedule(LocalDate selectedDate)
{
    String result = "";

    try
    {
        FileReader fr = new FileReader("schedule.txt");

        BufferedReader reader =
            new BufferedReader(fr);

        String line;

        while ((line = reader.readLine()) != null)
        {
            String[] data = line.split(",");

            // data[0] = 日付
            // data[1] = 予定
            if (data[0].equals(selectedDate.toString()))
            {
                result =
                    result + "・" + data[1] + "<br>";
            }
        }

        reader.close();
    }
    catch (IOException error)
    {
        return "予定を読み込めなかったよ";
    }

    // 予定が1件もなかった場合
    if (result.equals(""))
    {
        return "予定はないよ！";
    }

    return result;

} // getSchedule終了


} // CalendarTestクラス終了