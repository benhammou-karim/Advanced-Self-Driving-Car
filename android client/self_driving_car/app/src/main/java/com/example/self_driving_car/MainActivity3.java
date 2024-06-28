/*
This file contains class representing the activity that control the car with voice and with buttons and preview the camera pi with detection of the objets.

Author: Karim BENHAMMOU and assia al faiz
*/
package com.example.self_driving_car;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.view.View;
import android.webkit.WebView;
import android.widget.ImageButton;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;
import java.util.ArrayList;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity3 extends AppCompatActivity implements RecognitionListener {
    OkHttpClient okHttpClient = new OkHttpClient();
    String IP_ADDRESS = "192.168.158.116";
    String port = "5000";
    private SpeechRecognizer speechRecognizer;

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
                        Toast.makeText(MainActivity3.this, "server down", Toast.LENGTH_SHORT).show();
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
        setContentView(R.layout.activity_main3);

        // Request necessary permissions
        ActivityCompat.requestPermissions(this,
                new String[]{Manifest.permission.RECORD_AUDIO},
                PackageManager.PERMISSION_GRANTED);

        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) ImageButton audio1 = findViewById(R.id.imageButton);
        //controlle the rc car with voice
        audio1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Create SpeechRecognizer instance
                speechRecognizer = SpeechRecognizer.createSpeechRecognizer(MainActivity3.this);
                speechRecognizer.setRecognitionListener(MainActivity3.this);

                // Start listening for speech input
                Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "en-US");
                speechRecognizer.startListening(intent);
            }
        });

        //This line initializes a WebView object in the activity
        WebView webView = findViewById(R.id.webView);
        //This line enables JavaScript in the WebView object
        webView.getSettings().setJavaScriptEnabled(true);
        //This line loads a web page in the WebView object
        webView.loadUrl("http://"+IP_ADDRESS+":"+port+"/apiCar/video_feed");
    }



    @Override
    public void onReadyForSpeech(Bundle params) {
        // Called when the speech recognition engine is ready to receive speech
    }

    @Override
    public void onBeginningOfSpeech() {
        // Called when the user starts speaking
    }

    @Override
    public void onRmsChanged(float rmsdB) {
        // Called when the RMS (Root Mean Square) of the input audio has changed
    }

    @Override
    public void onBufferReceived(byte[] buffer) {
        // Called when partial recognition results are available
    }

    @Override
    public void onEndOfSpeech() {
        // Called when the user stops speaking
    }

    @Override
    public void onError(int error) {
        // Called when an error occurs during speech recognition
        Toast.makeText(this, "Error: " + error, Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onResults(Bundle results) {
        // Called when speech recognition results are available

        // Retrieve the recognized speech as an ArrayList
        ArrayList<String> speechResults = results.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);

        if (speechResults != null && !speechResults.isEmpty()) {
            String recognizedText = speechResults.get(0);

            // Call the forward function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("forward")) {
                // Call of forward function here
                forward();
            }
            // Call the backward function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("backward")) {
                // Call of backward function here
                backward();
            }
            // Call the right function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("right")) {
                // Call of right function here
                right();
            }
            // Call the left function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("left")) {
                // Call of left function here
                left();
            }
            // Call the stop function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("stop")) {
                // Call of stop function here
                stop();
            }
            // Call the start function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("start")) {
                // Call of start function here
                start();
            }
            // Call the speedup function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("speedup")) {
                // Call of start function here
                speedup();
            }
            // Call the shutdown function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("shutdown")) {
                // Call of start function here
                shutdown();
            }
            // Call the slowdown function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("slowdown")) {
                // Call of start function here
                slowdown();
            }
            // Call the medium function based on the recognized speech
            if (recognizedText.equalsIgnoreCase("medium")) {
                // Call of start function here
                medium();
            }
        }
    }

    @Override
    public void onPartialResults(Bundle partialResults) {
        // Called when partial recognition results are available
    }

    @Override
    public void onEvent(int eventType, Bundle params) {
        // Called when a recognition event occurs
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