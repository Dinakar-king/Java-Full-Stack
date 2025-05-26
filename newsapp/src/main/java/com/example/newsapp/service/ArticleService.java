package com.example.newsapp.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.newsapp.model.Article;
import com.example.newsapp.repository.ArticleRepository;

@Service

public class ArticleService {

    // service/ArticleService.java



    @Autowired
    private ArticleRepository articleRepo;

    public Article saveArticle(Article article) {
        return articleRepo.save(article);
    }

    public List<Article> getAllArticles() {
        return articleRepo.findAll();
    }
    public Optional<Article> getArticleById(Long id) {
        return articleRepo.findById(id);
    }
    public Optional<Article> updateArticle(Long id, Article updatedArticle) {
        return articleRepo.findById(id).map(article -> {
            article.setTitle(updatedArticle.getTitle());
            article.setContent(updatedArticle.getContent());
            article.setAuthor(updatedArticle.getAuthor());
            article.setPublishedDate(updatedArticle.getPublishedDate());
            return articleRepo.save(article);
        });
    }

    public void deleteByTitle(String title) {
    
        throw new UnsupportedOperationException("Unimplemented method 'deleteByTitle'");
    }

    public boolean deleteArticle(Long id) {
    
        throw new UnsupportedOperationException("Unimplemented method 'deleteArticle'");
    }
}


