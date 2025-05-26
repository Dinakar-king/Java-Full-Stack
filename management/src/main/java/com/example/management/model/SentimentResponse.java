package com.example.management.model;

import lombok.Data;

@Data
public class SentimentResponse {
        private String text;
        private String label;
        private float score;
}
