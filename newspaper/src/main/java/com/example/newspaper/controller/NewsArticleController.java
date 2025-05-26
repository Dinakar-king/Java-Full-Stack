
package com.example.newspaper.controller;

import com.example.newspaper.model.NewsArticle;
import com.example.newspaper.repository.NewsArticleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.*;

@RestController
@CrossOrigin(origins = "*") // Allow Angular to connect
public class NewsArticleController {

    @Autowired
    private NewsArticleRepository repo;

    @SuppressWarnings("null")
    @PostMapping("/analyze")
    public ResponseEntity<NewsArticle> analyzeNews(@RequestBody Map<String, String> body) {
        String article = body.get("article");

        // Call Python AI model
        RestTemplate restTemplate = new RestTemplate();
        Map<String, String> req = new HashMap<>();
        req.put("article", article);

        // Send request to Flask
        ResponseEntity<Map> response = restTemplate.postForEntity("http://localhost:5000/analyze", req, Map.class);

        String summary = response.getBody().get("summary").toString();
        String category = response.getBody().get("category").toString();

        // Save to database
        NewsArticle news = new NewsArticle();
        news.setArticle(article);
        news.setSummary(summary);
        news.setCategory(category);
        repo.save(news);

        return ResponseEntity.ok(news);
    }

    @GetMapping("/articles")
    public List<NewsArticle> getAllArticles() {
        return repo.findAll();
    }
}
