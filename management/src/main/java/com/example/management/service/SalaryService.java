package com.example.management.service;  

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.management.model.Salary;
import com.example.management.repository.SalaryRepository;

@Service
public class SalaryService {

    @Autowired
    private SalaryRepository salaryRepo;

    public List<Salary> getAllSalaries() {
        return salaryRepo.findAll();
    }

    public Salary getSalaryById(Integer id) {
        return salaryRepo.findById(id).orElse(null);
    }

    public Salary createSalary(Salary salary) {
        return salaryRepo.save(salary);
    }

    public void deleteSalary(Integer id) {
        salaryRepo.deleteById(id);
    }

    public Salary updateSalary(Integer id, Salary updatedSalary) {
        if (salaryRepo.existsById(id)) {
            updatedSalary.setId(id);
            return salaryRepo.save(updatedSalary);
        }
        return null;
    }
}