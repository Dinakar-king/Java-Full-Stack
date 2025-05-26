package com.example.newsapp.controller;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.example.newsapp.model.Article;
import com.example.newsapp.service.ArticleService;

@RestController
@RequestMapping("/api/articles")
@CrossOrigin(origins = "http://localhost:4200")
public class ArticleController {

    @Autowired
    private ArticleService articleService;

    // Create
    @PostMapping
    public ResponseEntity<Article> createArticle(@RequestBody Article article) {
        return new ResponseEntity<>(articleService.saveArticle(article), HttpStatus.CREATED);
    }

    // Get all
    @GetMapping
    public List<Article> getArticles() {
        return articleService.getAllArticles();
    }

    // 🔹 Get by ID
    @GetMapping("/{id}")
    public ResponseEntity<Article> getArticleById(@PathVariable Long id) {
        Optional<Article> article = articleService.getArticleById(id);
        return article.map(ResponseEntity::ok)
                      .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // 🔹 Update by ID
    @PutMapping("/{id}")
    public ResponseEntity<Article> updateArticle(@PathVariable Long id, @RequestBody Article updatedArticle) {
        Optional<Article> article = articleService.updateArticle(id, updatedArticle);
        return article.map(ResponseEntity::ok)
                      .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // 🔹 Delete by ID
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteArticle(@PathVariable Long id) {
        if (articleService.deleteArticle(id)) {
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    // 🔸 Optional: Delete by Title (custom)
    @DeleteMapping("/by-title")
    public ResponseEntity<Void> deleteByTitle(@RequestParam String title) {
        articleService.deleteByTitle(title);
        return ResponseEntity.noContent().build();
    }
}
