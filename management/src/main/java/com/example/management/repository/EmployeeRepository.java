package com.example.management.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.management.model.Employee;
public interface EmployeeRepository extends JpaRepository<Employee,Integer>{
    
}
