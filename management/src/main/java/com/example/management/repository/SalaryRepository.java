package com.example.management.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.management.model.Salary;
public interface SalaryRepository extends JpaRepository<Salary,Integer> {

}
