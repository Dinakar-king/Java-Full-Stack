package com.example.newsapp.service;

import java.util.List; 

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.newsapp.model.Summary;
import com.example.newsapp.repository.SummaryRepository;


    // service/SummaryService.java
@Service
public class SummaryService {

    @Autowired
    private SummaryRepository summaryRepo;

    public Summary saveSummary(Summary summary) {
        return summaryRepo.save(summary);
    }

    public List<Summary> getAllSummaries() {
        return summaryRepo.findAll();
    }
}


