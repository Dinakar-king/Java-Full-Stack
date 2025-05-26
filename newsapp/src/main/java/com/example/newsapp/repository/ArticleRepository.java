package com.example.newsapp.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.newsapp.model.Article;

    
public interface ArticleRepository extends JpaRepository<Article, Long> {
     void deleteByTitle(String title);
}


