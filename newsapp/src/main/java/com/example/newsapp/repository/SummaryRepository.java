package com.example.newsapp.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.newsapp.model.Summary;

public interface SummaryRepository extends JpaRepository<Summary, Long> {
    
}


