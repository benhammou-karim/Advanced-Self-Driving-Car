/*
This file contains class representing the activity that control the car with buttons and preview the camera pi with detection of the objets.

Author: Karim BENHAMMOU
*/
package com.example.self_driving_car;

import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    OkHttpClient okHttpClient = new OkHttpClient();
    String IP_ADDRESS = "192.168.158.116";
    String port = "5000";

    //making call asynchronously
    private void callServer(Request request){

        // making call asynchronously
        okHttpClient.newCall(request).enqueue(new Callback() {
            @Override
            // called if server is unreachable
            public void onFailure(@NotNull Call call, @NotNull IOException e) {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        Toast.makeText(MainActivity.this, "server down", Toast.LENGTH_SHORT).show();
                    }
                });
            }

            @Override
            // called if we get a
            // response from the server
            public void onResponse(
                    @NotNull Call call,
                    @NotNull Response response)
                    throws IOException {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            Toast.makeText(getApplicationContext(), response.body().string(), Toast.LENGTH_SHORT).show();
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }
                    }

                });
            }
        });
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button Forward = findViewById(R.id.Forward);
        Button Backward = findViewById(R.id.Backward);
        Button Right = findViewById(R.id.Right);
        Button Left = findViewById(R.id.Left);
        Button Stop = findViewById(R.id.Stop);
        Button Start = findViewById(R.id.Start);
        Button slowdown = findViewById(R.id.slowdown);
        Button speedup = findViewById(R.id.speedUp);
        Button shutdown = findViewById(R.id.shutdown);
        Button medium = findViewById(R.id.medium);

        //This line initializes a WebView object in the activity
        WebView webView = findViewById(R.id.webView);

        Forward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                forward();
            }
        });
        Backward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               backward();
            }
        });
        Right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                right();
            }
        });
        Left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                left();
            }
        });
        Stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                stop();
            }
        });
        Start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                start();
            }
        });
        speedup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               speedup();
            }
        });
        shutdown.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                shutdown();
            }
        });
        slowdown.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                slowdown();
            }
        });
        medium.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                medium();
            }
        });
        //This line enables JavaScript in the WebView object
        webView.getSettings().setJavaScriptEnabled(true);
        //This line loads a web page in the WebView object
        webView.loadUrl("http://"+IP_ADDRESS+":"+port+"/apiCar/video_feed");
    }

    private void forward() {
        Toast.makeText(this, "forward!", Toast.LENGTH_SHORT).show();
        // building a request to make the car go forward
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/forward").build();
        callServer(request);
    }

    private void backward() {
        Toast.makeText(this, "backward!", Toast.LENGTH_SHORT).show();
        // building a request to make the car go backward
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/backward").build();
        callServer(request);
    }

    private void right() {
        Toast.makeText(this, "right!", Toast.LENGTH_SHORT).show();
        // building a request to turn the car to right
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/turnRight").build();
        callServer(request);
    }

    private void left() {
        Toast.makeText(this, "left!", Toast.LENGTH_SHORT).show();
        // building a request to turn the car to left
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/turnLeft").build();
        callServer(request);
    }

    private void stop(){
        Toast.makeText(this, "stop!", Toast.LENGTH_SHORT).show();
        // building a request to stop the car
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/stop").build();
        callServer(request);
    }

    private void start(){
        Toast.makeText(this, "start!", Toast.LENGTH_SHORT).show();
        // building a request to start the car
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/run").build();
        callServer(request);
    }

    private void speedup(){
        Toast.makeText(this, "speedup!", Toast.LENGTH_SHORT).show();
        // building a request to speed up the car
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/speedUp").build();
        callServer(request);
    }

    private void shutdown(){
        Toast.makeText(this, "shutdown!", Toast.LENGTH_SHORT).show();
        // building a request to shutdown the car
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/shutDown").build();
        callServer(request);
    }

    private  void slowdown(){
        Toast.makeText(this, "slowdown!", Toast.LENGTH_SHORT).show();
        // building a request to slow down the car
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/slowDown").build();
        callServer(request);
    }

    private void medium(){
        Toast.makeText(this, "medium!", Toast.LENGTH_SHORT).show();
        // building a request to make the car's speed to medium
        Request request = new Request.Builder().url("http://"+IP_ADDRESS+":"+port+"/apiCar/medium").build();
        callServer(request);
    }
}