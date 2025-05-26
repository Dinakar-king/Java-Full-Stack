package com.example.newsapp.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.newsapp.model.Summary;
import com.example.newsapp.service.SummaryService;

@RestController
@RequestMapping("/api/summaries")
@CrossOrigin(origins = "http://localhost:4200")
public class SummaryController {

    @Autowired
    private SummaryService summaryService;

    @PostMapping
    public ResponseEntity<Summary> createSummary(@RequestBody Summary summary) {
        return new ResponseEntity<>(summaryService.saveSummary(summary), HttpStatus.CREATED);
    }

    @GetMapping
    public List<Summary> getSummaries() {
        return summaryService.getAllSummaries();
    }
    
}
