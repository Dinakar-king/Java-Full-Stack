package com.example.newsapp.dto;



public class SummaryDTO {
    private Long articleId;
    private String summaryText;

    // Constructors
    public SummaryDTO() {}

    public SummaryDTO(Long articleId, String summaryText) {
        this.articleId = articleId;
        this.summaryText = summaryText;
    }

    // Getters
    public Long getArticleId() {
        return articleId;
    }

    public String getSummaryText() {
        return summaryText;
    }

    // Setters
    public void setArticleId(Long articleId) {
        this.articleId = articleId;
    }

    public void setSummaryText(String summaryText) {
        this.summaryText = summaryText;
    }
}
