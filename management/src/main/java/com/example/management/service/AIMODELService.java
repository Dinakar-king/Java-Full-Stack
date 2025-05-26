package com.example.management.service;

import com.example.management.model.SentimentResponseList; // import your model

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AIMODELService {

    public SentimentResponseList getSentimentResponse(String input) {
        String url = "http://localhost:8000/sentiment?text" + URLEncoder.encode(input,StandardCharsets.UTF_8);

        // Set headers
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        // Create HTTP request
        HttpEntity<String> entity = new HttpEntity<>(input, headers);

        // Create RestTemplate instance
        RestTemplate restTemplate = new RestTemplate();

        // Make the request
        ResponseEntity<SentimentResponseList> response = restTemplate.exchange(
            url,
            HttpMethod.POST,
            entity,
            SentimentResponseList.class
        );

        return response.getBody(); // Return the actual response
    }
}