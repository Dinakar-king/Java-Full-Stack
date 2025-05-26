package com.example.management.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.management.model.Employee;
import com.example.management.repository.EmployeeRepository;
@Service
public class EmployeeService {

    @Autowired
    private EmployeeRepository employeeRepo;

    public List<Employee> getAllEmployees() {
        return employeeRepo.findAll();
    }

    public  Employee getEmployeeById(Integer id) {
        return employeeRepo.findById(id).orElse(null);
    }

    public Employee createEmployee(Employee emp) {
        return employeeRepo.save(emp);
    }

    public void deleteEmployee(Integer id) {
        employeeRepo.deleteById(id);
    }

    public Employee updateEmployee(Integer id, Employee updatedEmp) {
        if (employeeRepo.existsById(id)) {
            updatedEmp.setId(id);
            return employeeRepo.save(updatedEmp);
        } else {
            return null;
        }
    }
}


