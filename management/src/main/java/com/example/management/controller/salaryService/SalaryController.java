package com.example.management.controller.salaryService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.management.model.Salary;
import com.example.management.service.SalaryService;

@RestController
@CrossOrigin(origins = "http://localhost:4200")
@RequestMapping("v1/api/salaries")
public class SalaryController {

    @Autowired
    private SalaryService salaryService;

    @GetMapping
    public List<Salary> getAllSalaries() {
        return salaryService.getAllSalaries();
    }

    @GetMapping("/{id}")
    public Salary getSalaryById(@PathVariable Integer id) {
        return salaryService.getSalaryById(id);
    }

    @PostMapping
    public Salary createSalary(@RequestBody Salary salary) {
        return salaryService.createSalary(salary);
    }

    @PutMapping("/{id}")
    public Salary updateSalary(@PathVariable Integer id, @RequestBody Salary salary) {
        return salaryService.updateSalary(id, salary);
    }

    @DeleteMapping("/{id}")
    public void deleteSalary(@PathVariable Integer id) {
        salaryService.deleteSalary(id);
    }
}
