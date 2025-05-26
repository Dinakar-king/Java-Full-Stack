package com.example.management.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.management.model.Department;
import com.example.management.repository.DepartmentRepository;

@Service
public class DepartmentService {

    @Autowired
    private DepartmentRepository departmentRepo;

    public List<Department> getAllDepartments() {
        return departmentRepo.findAll();
    }

    public Department getDepartmentById(Integer id) {
        return departmentRepo.findById(id).orElse(null);
    }

    public Department createDepartment(Department department) {
        return departmentRepo.save(department);
    }

    public void deleteDepartment(Integer id) {
        departmentRepo.deleteById(id);
    }

    public Department updateDepartment(Integer id, Department updatedDept) {
        if (departmentRepo.existsById(id)) {
            updatedDept.setId(id);
            return departmentRepo.save(updatedDept);
        } else {
            return null;
        }
    }
}