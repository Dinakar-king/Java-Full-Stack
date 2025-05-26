package com.example.management.model;

import java.time.LocalDate;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Entity
@Data
@Table(name = "employees")   
public class Employee {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Integer id;
        @Column(nullable = false,length = 100)
       private  String Name;

         @Column(nullable = false,unique = true,length = 100)
      private   String email;
         @Column(length = 50)
        private    String position;
        @Column(name="department_id")
        private Integer departmentid;

            @Column(name = "hire_date")
         private   LocalDate hireDate;
}
