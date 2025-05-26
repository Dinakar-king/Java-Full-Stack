package com.example.management.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.management.model.Department;
public interface DepartmentRepository extends JpaRepository<Department,Integer> {

}
