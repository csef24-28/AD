package example.javatpoint.com.androidnotification;

import android.app.*;
import android.content.*;
import android.os.Bundle;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        findViewById(R.id.button).setOnClickListener(v -> addNotification());
    }

    private void addNotification() {
        NotificationCompat.Builder b =
                new NotificationCompat.Builder(this)
                        .setSmallIcon(R.drawable.messageicon)
                        .setContentTitle("Notification")
                        .setContentText("Message");

        Intent i = new Intent(this, NotificationView.class);
        PendingIntent p = PendingIntent.getActivity(
                this, 0, i, PendingIntent.FLAG_UPDATE_CURRENT);

        b.setContentIntent(p);

        NotificationManager m =
                (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);

        m.notify(0, b.build());
    }
}
